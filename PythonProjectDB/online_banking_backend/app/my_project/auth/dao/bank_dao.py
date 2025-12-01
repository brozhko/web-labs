from typing import List
from ..domain.models import Bank


class BankDAO:
    @staticmethod
    def get_all() -> List[Bank]:
        return Bank.query.all()
