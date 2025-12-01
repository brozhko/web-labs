from typing import List, Optional
from ..domain.models import db, Account


class AccountDAO:
    @staticmethod
    def get_all() -> List[Account]:
        return Account.query.all()

    @staticmethod
    def get_by_id(account_id: int) -> Optional[Account]:
        return Account.query.get(account_id)

    @staticmethod
    def create(data: dict) -> Account:
        acc = Account(**data)
        db.session.add(acc)
        db.session.commit()
        return acc

    @staticmethod
    def update(acc: Account, data: dict) -> Account:
        for key, value in data.items():
            setattr(acc, key, value)
        db.session.commit()
        return acc

    @staticmethod
    def delete(acc: Account) -> None:
        db.session.delete(acc)
        db.session.commit()
