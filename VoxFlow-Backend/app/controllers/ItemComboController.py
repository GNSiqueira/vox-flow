from app import app
from app.objects.models.ItemCombo import ItemCombo
from app. controllers.Generic.GenericController import *

@app.route("/itemcombo", methods=["GET"])
def get_itemcombo():
    return GenericController(ItemCombo).get()

@app.route("/itemcombo/<int:id>", methods=["GET"])
def get_itemcombo_id(id):
    return GenericController(ItemCombo).get_by_id(id)

@app.route("/itemcombo", methods=["POST"])
def create_itemcombo():
    return GenericController(ItemCombo).post()

@app.route("/itemcombo/<int:id>", methods=["PUT"])
def update_itemcombo(id):
    return GenericController(ItemCombo).put(id)

@app.route("/itemcombo/<int:id>", methods=["DELETE"])
def delete_itemcombo(id):
    return GenericController(ItemCombo).delete(id)