from flask import request
from ..service.account_service import AccountService
from ...ui.utils.responses import success_response, error_response
from ..domain.models import Account


def account_to_dto(acc: Account) -> dict:
    return {
        "account_id": acc.account_id,
        "client_id": acc.client_id,
        "bank_id": acc.bank_id,
        "currency_id": acc.currency_id,
        "account_number": acc.account_number,
        "balance": float(acc.balance) if acc.balance is not None else None,
        "opened_at": acc.opened_at.isoformat() if acc.opened_at else None,
    }


def get_all_accounts():
    accounts = AccountService.list_accounts()
    return success_response([account_to_dto(a) for a in accounts])


def get_account_by_id(account_id: int):
    acc = AccountService.get_account(account_id)
    if not acc:
        return error_response("Account not found", 404)
    return success_response(account_to_dto(acc))


def create_account():
    data = request.get_json() or {}
    acc = AccountService.create_account(data)
    return success_response(account_to_dto(acc), 201)


def update_account(account_id: int):
    data = request.get_json() or {}
    acc = AccountService.update_account(account_id, data)
    if not acc:
        return error_response("Account not found", 404)
    return success_response(account_to_dto(acc))


def delete_account(account_id: int):
    ok = AccountService.delete_account(account_id)
    if not ok:
        return error_response("Account not found", 404)
    return success_response({"deleted": True})
