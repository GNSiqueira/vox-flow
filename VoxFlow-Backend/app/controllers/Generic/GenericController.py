from app.config.imports.flask import *

class GenericController(): 
    def __init__(self, model):
        self.model = model
        self.name_table = self.model.__tablename__

    def get(self):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            itens = session.query(self.model).all()
            itens_json = [item.to_json() for item in itens]
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
        session = conexao.session
        try:
            # Checando tipo de conteúdo
            if request.is_json:
                form = request.get_json()
            else:
                form = request.form.to_dict()

            data = {}
            for key, value in form.items():
                if key == "id":
                    continue
                data[key] = value
            item = self.model(**data)  
            print(item)
            session.add(item)
            session.commit()
            session.close()      
            return created(f"{self.name_table}", [], f"{self.name_table} criado")
        except ValueError as e:
            return bad_request(f"{self.name_table}", [], f"Erro de validação: {str(e)}")
        except Exception as e:
            return internal_server_error(f"{self.name_table}", [], f"Erro ao criar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()

    def put(self, request, id):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            item = session.get(self.model, id)
            if not item:
                return not_found(f"{self.name_table}", [], f"{self.name_table} com ID {id} não encontrado")
            item.from_json(request.json)  # Assumindo que o método from_json existe
            session.commit()
            return ok(f"{self.name_table}", item.to_json(), f"{self.name_table} atualizado")
        except Exception as e:
            return internal_server_error(f"{self.name_table}", [], f"Erro ao atualizar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()

    def delete(self, id):
        conexao = Connection().conectar()
        try:
            session = conexao.session
            item = session.get(self.model, id)
            if not item:
                return not_found(f"{self.name_table}", [], f"{self.name_table} com ID {id} não encontrado")
            session.delete(item)
            session.commit()
            return ok(f"{self.name_table}", item.to_json(), f"{self.name_table} deletado")
        except Exception as e:
            return internal_server_error(f"{self.name_table}", [], f"Erro ao deletar {self.name_table}: {str(e)}")
        finally:
            session.close()
            conexao.desconectar()
