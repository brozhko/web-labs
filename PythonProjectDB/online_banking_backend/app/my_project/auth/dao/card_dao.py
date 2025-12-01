from typing import List
from ..domain.models import Card


class CardDAO:
    @staticmethod
    def get_all() -> List[Card]:
        return Card.query.all()

    @staticmethod
    def get_by_account(account_id: int) -> List[Card]:
        return Card.query.filter_by(account_id=account_id).all()
