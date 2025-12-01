from typing import List
from ..domain.models import LoginHistory


class LoginHistoryDAO:
    @staticmethod
    def get_all() -> List[LoginHistory]:
        return LoginHistory.query.all()

    @staticmethod
    def get_by_client(client_id: int) -> List[LoginHistory]:
        return LoginHistory.query.filter_by(client_id=client_id).all()
