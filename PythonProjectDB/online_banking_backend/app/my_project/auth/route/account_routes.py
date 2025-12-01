from flask import Blueprint
from ..controller import account_controller as controller

account_bp = Blueprint("accounts", __name__)


@account_bp.get("/")
def list_accounts():
    return controller.get_all_accounts()


@account_bp.get("/<int:account_id>")
def get_account(account_id):
    return controller.get_account_by_id(account_id)


@account_bp.post("/")
def create_account():
    return controller.create_account()


@account_bp.put("/<int:account_id>")
def update_account(account_id):
    return controller.update_account(account_id)


@account_bp.delete("/<int:account_id>")
def delete_account(account_id):
    return controller.delete_account(account_id)
