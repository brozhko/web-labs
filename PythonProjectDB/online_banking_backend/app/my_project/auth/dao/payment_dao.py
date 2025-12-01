from typing import List, Optional
from ..domain.models import db, Payment


class PaymentDAO:
    @staticmethod
    def get_all() -> List[Payment]:
        return Payment.query.all()

    @staticmethod
    def get_by_id(payment_id: int) -> Optional[Payment]:
        return Payment.query.get(payment_id)

    @staticmethod
    def create(data: dict) -> Payment:
        pay = Payment(**data)
        db.session.add(pay)
        db.session.commit()
        return pay

    @staticmethod
    def update(pay: Payment, data: dict) -> Payment:
        for key, value in data.items():
            setattr(pay, key, value)
        db.session.commit()
        return pay

    @staticmethod
    def delete(pay: Payment) -> None:
        db.session.delete(pay)
        db.session.commit()
