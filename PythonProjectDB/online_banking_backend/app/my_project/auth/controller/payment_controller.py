from flask import request
from ..service.payment_service import PaymentService
from ...ui.utils.responses import success_response, error_response
from ..domain.models import Payment


def payment_to_dto(p: Payment) -> dict:
    return {
        "payment_id": p.payment_id,
        "type_id": p.type_id,
        "recipient_id": p.recipient_id,
        "amount": float(p.amount) if p.amount is not None else None,
        "description": p.description,
        "created_at": p.created_at.isoformat() if p.created_at else None,
    }


def get_all_payments():
    pays = PaymentService.list_payments()
    return success_response([payment_to_dto(p) for p in pays])


def get_payment_by_id(payment_id: int):
    p = PaymentService.get_payment(payment_id)
    if not p:
        return error_response("Payment not found", 404)
    return success_response(payment_to_dto(p))


def create_payment():
    data = request.get_json() or {}
    p = PaymentService.create_payment(data)
    return success_response(payment_to_dto(p), 201)


def update_payment(payment_id: int):
    data = request.get_json() or {}
    p = PaymentService.update_payment(payment_id, data)
    if not p:
        return error_response("Payment not found", 404)
    return success_response(payment_to_dto(p))


def delete_payment(payment_id: int):
    ok = PaymentService.delete_payment(payment_id)
    if not ok:
        return error_response("Payment not found", 404)
    return success_response({"deleted": True})
