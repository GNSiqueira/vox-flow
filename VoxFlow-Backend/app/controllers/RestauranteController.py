from app.objects.models.Restaurante import Restaurante
from app.controllers.Generic.GenericController import *

@app.route("/restaurante", methods=["GET"])
def get_restaurante():
    return GenericController(Restaurante).get()

@app.route("/restaurante/<int:id>", methods=["GET"])
def get_restaurante_id(id):
    return GenericController(Restaurante).get_by_id(id)

@app.route("/restaurante", methods=["POST"])
def create_restaurante():
    return GenericController(Restaurante).post()

@app.route("/restaurante/<int:id>", methods=["PUT"])
def update_restaurante(id):
    return GenericController(Restaurante).put(request, id)

@app.route("/restaurante/<int:id>", methods=["DELETE"])
def delete_restaurante(id):
    return GenericController(Restaurante).delete(id)
