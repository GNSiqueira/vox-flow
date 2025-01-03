from app.config.imports.flask import *

class GenericController(): 
    def __init__(self, model):
        self.model = model
        self.name_table = self.model.__tablename__
        if 'enums' in model.__dict__: 
            self.enums = model.enums
        else:
            self.enums = None

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
        

    def get(self):
        conexao = Connection().conectar()
        try:
            session = conexao.session
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

    def put(self, id):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            item = session.query(self.model).get(id)

            if not item:
                return not_found(
                    f"{self.name_table}", [], f"{self.name_table} com ID {id} não encontrado"
                )

            # Lida com JSON ou form-data
            if request.is_json:
                form = request.get_json()
            else:
                form = request.form.to_dict()

            print("Antes da atualização:", item.to_json())

            # Atualiza os atributos dinamicamente
            for key, value in form.items():
                if key == "id":
                    continue  # Evita atualizar o ID
                if hasattr(item, key):
                    setattr(item, key, value)
                else:
                    print(f"Atributo '{key}' não existe em {self.name_table}, ignorado.")

            print("Depois da atualização:", item.to_json())

            # Adiciona e confirma no banco
            session.add(item)
            session.commit()
            item = self.model(**item.to_json())
            self.validate_enums('str', item)
            return ok(f"{self.name_table}", item.to_json(), f"{self.name_table} atualizado")
        except Exception as e:
            # Log detalhado para debug
            print(f"Erro ao atualizar {self.name_table}: {e}")
            session.rollback()
            return internal_server_error(
                f"{self.name_table}", [], f"Erro ao atualizar {self.name_table}: {str(e)}"
            )
        finally:
            # Fecha a sessão e a conexão
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
