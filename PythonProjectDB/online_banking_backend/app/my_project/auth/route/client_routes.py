from flask import Blueprint
from ..controller import client_controller as controller

client_bp = Blueprint("clients", __name__)


@client_bp.get("/")
def list_clients():
    return controller.get_all_clients()


@client_bp.get("/<int:client_id>")
def get_client(client_id):
    return controller.get_client_by_id(client_id)


@client_bp.post("/")
def create_client():
    return controller.create_client()


@client_bp.put("/<int:client_id>")
def update_client(client_id):
    return controller.update_client(client_id)


@client_bp.delete("/<int:client_id>")
def delete_client(client_id):
    return controller.delete_client(client_id)
