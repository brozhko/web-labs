from typing import List
from ..domain.models import Currency


class CurrencyDAO:
    @staticmethod
    def get_all() -> List[Currency]:
        return Currency.query.all()
