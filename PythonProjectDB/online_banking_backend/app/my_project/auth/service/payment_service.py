from typing import List, Optional
from ..dao.payment_dao import PaymentDAO
from ..domain.models import Payment


class PaymentService:
    @staticmethod
    def list_payments() -> List[Payment]:
        return PaymentDAO.get_all()

    @staticmethod
    def get_payment(payment_id: int) -> Optional[Payment]:
        return PaymentDAO.get_by_id(payment_id)

    @staticmethod
    def create_payment(dto: dict) -> Payment:
        return PaymentDAO.create(dto)

    @staticmethod
    def update_payment(payment_id: int, dto: dict) -> Optional[Payment]:
        pay = PaymentDAO.get_by_id(payment_id)
        if not pay:
            return None
        return PaymentDAO.update(pay, dto)

    @staticmethod
    def delete_payment(payment_id: int) -> bool:
        pay = PaymentDAO.get_by_id(payment_id)
        if not pay:
            return False
        PaymentDAO.delete(pay)
        return True
