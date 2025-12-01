from ...ui.utils.responses import success_response
from ..service.reference_service import ReferenceService
from ..domain.models import Bank, Currency, PaymentType, Recipient, Card, LoginHistory


def bank_to_dto(b: Bank) -> dict:
    return {"bank_id": b.bank_id, "bank_name": b.bank_name, "mfo": b.mfo}


def currency_to_dto(c: Currency) -> dict:
    return {"currency_id": c.currency_id, "code": c.code, "name": c.name}


def payment_type_to_dto(t: PaymentType) -> dict:
    return {"type_id": t.type_id, "type_name": t.type_name}


def recipient_to_dto(r: Recipient) -> dict:
    return {
        "recipient_id": r.recipient_id,
        "name": r.name,
        "iban": r.iban,
        "bank_id": r.bank_id,
    }


def card_to_dto(c: Card) -> dict:
    return {
        "card_id": c.card_id,
        "account_id": c.account_id,
        "card_number": c.card_number,
        "expiry_date": c.expiry_date.isoformat() if c.expiry_date else None,
        "cvv": c.cvv,
    }


def login_to_dto(l: LoginHistory) -> dict:
    return {
        "log_id": l.log_id,
        "client_id": l.client_id,
        "login_time": l.login_time.isoformat() if l.login_time else None,
        "ip_address": l.ip_address,
    }


def get_banks():
    banks = ReferenceService.list_banks()
    return success_response([bank_to_dto(b) for b in banks])


def get_currencies():
    currs = ReferenceService.list_currencies()
    return success_response([currency_to_dto(c) for c in currs])


def get_payment_types():
    types = ReferenceService.list_payment_types()
    return success_response([payment_type_to_dto(t) for t in types])


def get_recipients():
    recs = ReferenceService.list_recipients()
    return success_response([recipient_to_dto(r) for r in recs])


def get_cards():
    cards = ReferenceService.list_cards()
    return success_response([card_to_dto(c) for c in cards])


def get_cards_by_account(account_id: int):
    cards = ReferenceService.list_cards_by_account(account_id)
    return success_response([card_to_dto(c) for c in cards])


def get_logins():
    logs = ReferenceService.list_login_history()
    return success_response([login_to_dto(l) for l in logs])


def get_logins_by_client(client_id: int):
    logs = ReferenceService.list_login_history_by_client(client_id)
    return success_response([login_to_dto(l) for l in logs])

from ..domain.models import Client, Account, Payment  # якщо ще не імпортовано


def clients_with_accounts():
    result = []
    for c in Client.query.all():
        result.append({
            "client_id": c.client_id,
            "full_name": c.full_name,
            "accounts": [
                {
                    "account_id": a.account_id,
                    "account_number": a.account_number,
                    "balance": float(a.balance) if a.balance is not None else None
                }
                for a in c.accounts
            ]
        })
    return success_response(result)


def accounts_with_payments():
    result = []
    from ..domain.models import Account  # якщо не імпортовано нагорі, можна тут

    for acc in Account.query.all():
        payments = set()
        # вихідні і вхідні транзакції
        for tr in acc.outgoing_transactions + acc.incoming_transactions:
            if tr.payment:
                payments.add(tr.payment)

        result.append({
            "account_id": acc.account_id,
            "account_number": acc.account_number,
            "payments": [
                {
                    "payment_id": p.payment_id,
                    "amount": float(p.amount) if p.amount is not None else None,
                    "description": p.description
                }
                for p in payments
            ]
        })

    return success_response(result)
