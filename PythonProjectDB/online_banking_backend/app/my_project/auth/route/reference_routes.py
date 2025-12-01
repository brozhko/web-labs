from flask import Blueprint
from ..controller import reference_controller as controller

reference_bp = Blueprint("reference", __name__)


@reference_bp.get("/banks")
def banks():
    return controller.get_banks()


@reference_bp.get("/currencies")
def currencies():
    return controller.get_currencies()


@reference_bp.get("/payment-types")
def payment_types():
    return controller.get_payment_types()


@reference_bp.get("/recipients")
def recipients():
    return controller.get_recipients()


@reference_bp.get("/cards")
def cards():
    return controller.get_cards()


@reference_bp.get("/cards/by-account/<int:account_id>")
def cards_by_account(account_id):
    return controller.get_cards_by_account(account_id)


@reference_bp.get("/login-history")
def login_history():
    return controller.get_logins()


@reference_bp.get("/login-history/by-client/<int:client_id>")
def login_history_by_client(client_id):
    return controller.get_logins_by_client(client_id)

@reference_bp.get("/report/clients-with-accounts")
def report_clients_with_accounts():
    return controller.clients_with_accounts()

@reference_bp.get("/report/accounts-with-payments")
def report_accounts_with_payments():
    return controller.accounts_with_payments()
