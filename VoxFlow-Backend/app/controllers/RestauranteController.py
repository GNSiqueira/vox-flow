from app.objects.models.Restaurante import Restaurante
from app.config.imports.flask import *

@app.route('/restaurante', methods=['GET'])
def get_restaurante():
    conexao = Connection().conectar()
    session = conexao.session
    restaurantes = session.query(Restaurante).all()
    restaurante_json = [restaurante.to_json() for restaurante in restaurantes]

    return ok("restaurantes", restaurante_json, "Lista de restaurantes")