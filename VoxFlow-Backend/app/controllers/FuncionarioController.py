from app.objects.models import Funcionario
from app.controllers.Generic.GenericController import *

@app.route("/funcionario", methods=["GET"])
def get_funcionario():
    return GenericController(Funcionario).get()

@app.route("/funcionario/<int:id>", methods=["GET"])
def get_funcionario_id(id):
    return GenericController(Funcionario).get_by_id(id)

@app.route("/funcionario", methods=["POST"])
def create_funcionario():
    return GenericController(Funcionario).post()

@app.route("/funcionario/<int:id>", methods=["PUT"])
def update_funcionario(id):
    return GenericController(Funcionario).put(id)

@app.route("/funcionario/<int:id>", methods=["DELETE"])
def delete_funcionario(id):
    return GenericController(Funcionario).delete(id)

