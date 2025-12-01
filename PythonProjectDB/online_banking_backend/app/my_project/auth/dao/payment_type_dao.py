from typing import List
from ..domain.models import PaymentType


class PaymentTypeDAO:
    @staticmethod
    def get_all() -> List[PaymentType]:
        return PaymentType.query.all()
