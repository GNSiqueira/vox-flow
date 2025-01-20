from app import app
from app.objects.models import CustomizacaoPermitida
from app.controllers.Generic.GenericController import *

@app.route("/customizacaopermitida", methods=["GET"])
def get_customizacaopermitida():
    return GenericController(CustomizacaoPermitida).get()

@app.route("/customizacaopermitida/<int:id>", methods=["GET"])
def get_customizacaopermitida_id(id):
    return GenericController(CustomizacaoPermitida).get_by_id(id)

@app.route("/customizacaopermitida", methods=["POST"])
def create_customizacaopermitida():
    return GenericController(CustomizacaoPermitida).post()

@app.route("/customizacaopermitida", methods=["PUT"])
@app.route("/customizacaopermitida/<int:id>", methods=["PUT"])
def update_customizacaopermitida(id):
    return GenericController(CustomizacaoPermitida).put(id)

@app.route("/customizacaopermitida/<int:id>", methods=["DELETE"])
def delete_customizacaopermitida(id):
    return GenericController(CustomizacaoPermitida).delete(id)

