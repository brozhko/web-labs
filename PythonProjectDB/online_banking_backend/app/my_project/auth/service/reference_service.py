from ..dao.bank_dao import BankDAO
from ..dao.currency_dao import CurrencyDAO
from ..dao.payment_type_dao import PaymentTypeDAO
from ..dao.recipient_dao import RecipientDAO
from ..dao.card_dao import CardDAO
from ..dao.login_history_dao import LoginHistoryDAO


class ReferenceService:
    @staticmethod
    def list_banks():
        return BankDAO.get_all()

    @staticmethod
    def list_currencies():
        return CurrencyDAO.get_all()

    @staticmethod
    def list_payment_types():
        return PaymentTypeDAO.get_all()

    @staticmethod
    def list_recipients():
        return RecipientDAO.get_all()

    @staticmethod
    def list_cards():
        return CardDAO.get_all()

    @staticmethod
    def list_cards_by_account(account_id: int):
        return CardDAO.get_by_account(account_id)

    @staticmethod
    def list_login_history():
        return LoginHistoryDAO.get_all()

    @staticmethod
    def list_login_history_by_client(client_id: int):
        return LoginHistoryDAO.get_by_client(client_id)
