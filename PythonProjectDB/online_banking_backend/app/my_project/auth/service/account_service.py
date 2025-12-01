from typing import List, Optional
from ..dao.account_dao import AccountDAO
from ..domain.models import Account


class AccountService:
    @staticmethod
    def list_accounts() -> List[Account]:
        return AccountDAO.get_all()

    @staticmethod
    def get_account(account_id: int) -> Optional[Account]:
        return AccountDAO.get_by_id(account_id)

    @staticmethod
    def create_account(dto: dict) -> Account:
        return AccountDAO.create(dto)

    @staticmethod
    def update_account(account_id: int, dto: dict) -> Optional[Account]:
        acc = AccountDAO.get_by_id(account_id)
        if not acc:
            return None
        return AccountDAO.update(acc, dto)

    @staticmethod
    def delete_account(account_id: int) -> bool:
        acc = AccountDAO.get_by_id(account_id)
        if not acc:
            return False
        AccountDAO.delete(acc)
        return True
