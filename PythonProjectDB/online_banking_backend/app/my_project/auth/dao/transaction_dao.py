from typing import List, Optional
from ..domain.models import db, Transaction


class TransactionDAO:
    @staticmethod
    def get_all() -> List[Transaction]:
        return Transaction.query.all()

    @staticmethod
    def get_by_id(transaction_id: int) -> Optional[Transaction]:
        return Transaction.query.get(transaction_id)

    @staticmethod
    def create(data: dict) -> Transaction:
        tr = Transaction(**data)
        db.session.add(tr)
        db.session.commit()
        return tr

    @staticmethod
    def update(tr: Transaction, data: dict) -> Transaction:
        for key, value in data.items():
            setattr(tr, key, value)
        db.session.commit()
        return tr

    @staticmethod
    def delete(tr: Transaction) -> None:
        db.session.delete(tr)
        db.session.commit()
