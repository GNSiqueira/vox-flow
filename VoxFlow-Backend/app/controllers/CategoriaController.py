from app import app
from app.objects.models.Categoria import Categoria
from app. controllers.Generic.GenericController import *

@app.route("/categoria", methods=["GET"])
def get_categoria():
    return GenericController(Categoria).get()

@app.route("/categoria/<int:id>", methods=["GET"])
def get_categoria_id(id):
    return GenericController(Categoria).get_by_id(id)

@app.route("/categoria", methods=["POST"])
def create_categoria():
    return GenericController(Categoria).post()

@app.route("/categoria/<int:id>", methods=["PUT"])
def update_categoria(id):
    return GenericController(Categoria).put(id)

@app.route("/categoria/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    return GenericController(Categoria).delete(id)

