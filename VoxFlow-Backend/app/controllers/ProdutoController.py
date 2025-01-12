from app import app
from app.objects.models.Produto import Produto
from app. controllers.Generic.GenericController import *

@app.route("/produto", methods=["GET"])
def get_produto():
    return GenericController(Produto).get()

@app.route("/produto/<int:id>", methods=["GET"])
def get_produto_id(id):
    return GenericController(Produto).get_by_id(id)

@app.route("/produto", methods=["POST"])
def create_produto():
    return GenericController(Produto).post()

@app.route("/produto/<int:id>", methods=["PUT"])
def update_produto(id):
    return GenericController(Produto).put(id)

@app.route("/produto/<int:id>", methods=["DELETE"])
def delete_produto(id):
    return GenericController(Produto).delete(id)

