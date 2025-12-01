from typing import List
from ..domain.models import Recipient


class RecipientDAO:
    @staticmethod
    def get_all() -> List[Recipient]:
        return Recipient.query.all()
