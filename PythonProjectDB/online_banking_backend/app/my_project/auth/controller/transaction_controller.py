from flask import request
from ..service.transaction_service import TransactionService
from ...ui.utils.responses import success_response, error_response
from ..domain.models import Transaction


def transaction_to_dto(t: Transaction) -> dict:
    return {
        "transaction_id": t.transaction_id,
        "from_account": t.from_account,
        "to_account": t.to_account,
        "payment_id": t.payment_id,
        "amount": float(t.amount) if t.amount is not None else None,
        "date_time": t.date_time.isoformat() if t.date_time else None,
        "status": t.status,
    }


def get_all_transactions():
    trs = TransactionService.list_transactions()
    return success_response([transaction_to_dto(t) for t in trs])


def get_transaction_by_id(transaction_id: int):
    t = TransactionService.get_transaction(transaction_id)
    if not t:
        return error_response("Transaction not found", 404)
    return success_response(transaction_to_dto(t))


from flask import request
from ..service.transaction_service import TransactionService
from ...ui.utils.responses import success_response, error_response
from ..domain.models import Transaction


def transaction_to_dto(t: Transaction) -> dict:
    return {
        "transaction_id": t.transaction_id,
        "from_account": t.from_account,
        "to_account": t.to_account,
        "payment_id": t.payment_id,
        "amount": float(t.amount) if t.amount is not None else None,
        "date_time": t.date_time.isoformat() if t.date_time else None,
        "status": t.status,
    }


def get_all_transactions():
    trs = TransactionService.list_transactions()
    return success_response([transaction_to_dto(t) for t in trs])


def get_transaction_by_id(transaction_id: int):
    t = TransactionService.get_transaction(transaction_id)
    if not t:
        return error_response("Transaction not found", 404)
    return success_response(transaction_to_dto(t))


def create_transaction():
    data = request.get_json() or {}
    try:
        t = TransactionService.create_transaction(data)
    except ValueError as e:
        return error_response(str(e), 400)
    except LookupError as e:
        return error_response(str(e), 404)
    except RuntimeError as e:
        return error_response(str(e), 400)

    return success_response(transaction_to_dto(t), 201)


def update_transaction(transaction_id: int):
    data = request.get_json() or {}
    t = TransactionService.update_transaction(transaction_id, data)
    if not t:
        return error_response("Transaction not found", 404)
    return success_response(transaction_to_dto(t))


def delete_transaction(transaction_id: int):
    ok = TransactionService.delete_transaction(transaction_id)
    if not ok:
        return error_response("Transaction not found", 404)
    return success_response({"deleted": True})



def update_transaction(transaction_id: int):
    data = request.get_json() or {}
    t = TransactionService.update_transaction(transaction_id, data)
    if not t:
        return error_response("Transaction not found", 404)
    return success_response(transaction_to_dto(t))


def delete_transaction(transaction_id: int):
    ok = TransactionService.delete_transaction(transaction_id)
    if not ok:
        return error_response("Transaction not found", 404)
    return success_response({"deleted": True})
