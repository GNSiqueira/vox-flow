from app import app
from app.objects.models import Combo
from app.controllers.Generic.GenericController import *

@app.route("/combo", methods=["GET"])
def get_combo():
    return GenericController(Combo).get()

@app.route("/combo/<int:id>", methods=["GET"])
def get_combo_id(id):
    return GenericController(Combo).get_by_id(id)

@app.route("/combo", methods=["POST"])
def create_combo():
    return GenericController(Combo).post()

@app.route("/combo/<int:id>", methods=["PUT"])
def update_combo(id):
    return GenericController(Combo).put(id)

@app.route("/combo/<int:id>", methods=["DELETE"])
def delete_combo(id):
    return GenericController(Combo).delete(id)

