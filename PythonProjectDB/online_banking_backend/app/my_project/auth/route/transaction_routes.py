from flask import Blueprint
from ..controller import transaction_controller as controller

transaction_bp = Blueprint("transactions", __name__)


@transaction_bp.get("/")
def list_transactions():
    return controller.get_all_transactions()


@transaction_bp.get("/<int:transaction_id>")
def get_transaction(transaction_id):
    return controller.get_transaction_by_id(transaction_id)


@transaction_bp.post("/")
def create_transaction():
    return controller.create_transaction()


@transaction_bp.put("/<int:transaction_id>")
def update_transaction(transaction_id):
    return controller.update_transaction(transaction_id)


@transaction_bp.delete("/<int:transaction_id>")
def delete_transaction(transaction_id):
    return controller.delete_transaction(transaction_id)
