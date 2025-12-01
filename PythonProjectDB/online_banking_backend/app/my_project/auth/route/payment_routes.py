from flask import Blueprint
from ..controller import payment_controller as controller

payment_bp = Blueprint("payments", __name__)


@payment_bp.get("/")
def list_payments():
    return controller.get_all_payments()


@payment_bp.get("/<int:payment_id>")
def get_payment(payment_id):
    return controller.get_payment_by_id(payment_id)


@payment_bp.post("/")
def create_payment():
    return controller.create_payment()


@payment_bp.put("/<int:payment_id>")
def update_payment(payment_id):
    return controller.update_payment(payment_id)


@payment_bp.delete("/<int:payment_id>")
def delete_payment(payment_id):
    return controller.delete_payment(payment_id)
