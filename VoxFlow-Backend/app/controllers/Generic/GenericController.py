from sqlalchemy import Column
from app.config.imports.flask import *

class GenericController(): 
    def __init__(self, model):
        self.model = model
        self.name_table = self.model.__tablename__
        if 'enums' in model.__dict__: 
            self.enums = model.enums
        else:
            self.enums = None

    #region Métodos internos
    def __values_get(self):
        primary_key = []
                
        values_return = {}
        
        for key in self.model.__dict__:
            if str(key)[-3:] == '_id':
                primary_key.append(str(key))
        
        for key, value in request.args.to_dict().items():
            count = len(primary_key)
            for primary in primary_key: 
                if primary == key: 
                    values_return[key] = value 
                    break                 
                count -= 1
                if count == 0: 
                    raise ValueError("Erro ao buscar registro - verificar se todos os IDs estão corretos")
        return values_return, primary_key
    
    def __filters(self, value_get):
        filters = []
        for key, value in value_get.items():
            if value is not None:
                filters.append(getattr(self.model, key) == value) 
        return filters

    def __validate_atributes(self, input = None):
        for key, value in input.items():
            count = len(self.model.__dict__)
            for key2 in self.model.__dict__: 
                if key == key2:
                    break
                count -= 1
                if count == 0:
                    raise ValueError(f"Erro ao buscar registro - atributo {key} não encontrado na tabela")
        return True
    
    def validate_enums(self, retorno, model = None):
        if not model:
            model = self.model 
        if self.enums:
            for key, value in self.enums.items():
                check = False
                for enum, value_enum in value.__dict__.items():
                    if model.__dict__[key] == value_enum:
                        if retorno == 'str':
                            model.__dict__[key] = enum
                        check = True
                        break
                    elif model.__dict__[key] == enum:
                        if retorno == 'int':
                            model.__dict__[key] = value_enum
                        check = True
                        break
                if check == False:
                    raise ValueError("Enum inválido - verificar valor de: " + key)
            return True
        return True
    
    #endregion    

    def get(self):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            
            value_get, primary_key = self.__values_get()
            
            if len(primary_key) < len(value_get): 
                raise ValueError("Erro ao buscar registro - verificar se todos os IDs estão corretos")
            elif len(primary_key) > 1 and len(value_get) > 1 or len(primary_key) > len(value_get):
                filters = self.__filters(value_get)
                itens = session.query(self.model).filter(*filters).all()
            elif len(primary_key) == len(value_get):
                filters = self.__filters(value_get)
                itens = session.query(self.model).filter(*filters).all()
            else: 
                itens = session.query(self.model).all()

            itens_json = []
            for item in itens:
                self.validate_enums('str', item)
                itens_json.append(item.to_json())

            return ok(f"{self.name_table}s", itens_json, f"lista de {self.name_table}s encontrada")
        except Exception as e:
            return internal_server_error(f"{self.name_table}s", [], f"Erro ao buscar {self.name_table}s: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()

    def get_by_id(self, id):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            item = session.get(self.model, id)
            self.validate_enums('str', item)
            if not item:
                return not_found(f"{self.name_table}", [], f"{self.name_table} com ID {id} não encontrado")
            return ok(f"{self.name_table}", item.to_json(), f"{self.name_table} encontrado")
        except Exception as e:
            return internal_server_error(f"{self.name_table}", [], f"Erro ao buscar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()

    def post(self):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            if request.is_json:
                form = request.get_json()
            else:
                form = request.form.to_dict()

            data = {}
            for key, value in form.items():
                if key == "id":
                    continue
                data[key] = value
            self.model = self.model(**data)
            
            self.validate_enums('int')

            item = self.model
            
            session.add(item)
            session.commit()

            item = item.to_json()

            self.validate_enums('str')

            return created(f"{self.name_table}", self.model.to_json(), f"{self.name_table} criado")
        except ValueError as e:
            session.rollback()
            return bad_request(f"{self.name_table}", [], f"Erro de validação: {str(e)}")
        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                return conflict(f"{self.name_table}", [], f"Erro de validação: Cadastro ja existente")
            return internal_server_error(f"{self.name_table}", [], f"Erro ao criar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()

    def put(self, id = None):
        conexao = Connection().conectar()
        
        try:
            session = conexao.session               

            if id is None:
                value_get, primary_key = self.__values_get()
                if len(value_get) != len(primary_key):
                    raise ValueError("Campos para a busca do objeto estão faltando, verifique todos os campos!")
                filters = self.__filters(value_get)
                item = session.query(self.model).filter(*filters).all()
                if len(item) == 1: 
                    item = item[0]
                    if request.is_json:
                        form = request.get_json()
                    elif request.form.to_dict():
                        form = request.form.to_dict()
                    else: 
                        raise ValueError("Formulario vazio")
                    
                    self.__validate_atributes(form)

                    for key, value in form.items(): 
                        if key == "id": 
                            continue
                        setattr(item, key, value)

            elif id is not None:
                item = session.query(self.model).get(id)
                if request.is_json:
                    form = request.get_json()
                elif request.form.to_dict():
                    form = request.form.to_dict()
                else: 
                    raise ValueError("Formulario vazio")
                
                self.__validate_atributes(form)

                for key, value in form.items(): 
                    if key == "id": 
                        continue
                    setattr(item, key, value)

            session.add(item)
            session.commit()

            return ok(f"{self.name_table}", item.to_json(), f"{self.name_table} atualizado")
        except Exception as e:
            print(f"Erro ao atualizar {self.name_table}: {e}")
            session.rollback()
            return internal_server_error(
                f"{self.name_table}", [], f"Erro ao atualizar {self.name_table}: {str(e)}"
            )
        finally:
            session.close()
            conexao.desconectar()

    def delete(self, id):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            self.model = session.query(self.model).get(id)
            if not self.model:
                return not_found(f"{self.name_table}", [], f"{self.name_table} com ID {id} não encontrado")
            session.delete(self.model)
            session.commit()
            self.validate_enums('str')
            return ok(f"{self.name_table}", self.model.to_json(), f"{self.name_table} deletado")
        except Exception as e:
            session.rollback()
            return internal_server_error(f"{self.name_table}", [], f"Erro ao deletar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()
