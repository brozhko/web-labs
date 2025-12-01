from typing import List, Optional
from ..dao.transaction_dao import TransactionDAO
from ..domain.models import Transaction, Account, db


class TransactionService:
    @staticmethod
    def list_transactions() -> List[Transaction]:
        return TransactionDAO.get_all()

    @staticmethod
    def get_transaction(transaction_id: int) -> Optional[Transaction]:
        return TransactionDAO.get_by_id(transaction_id)

    @staticmethod
    def create_transaction(dto: dict) -> Transaction:
        """
        Бізнес-логіка:
        - перевірити, що є from_account, to_account, payment_id, amount
        - перевірити, що акаунти існують
        - перевірити, що на from_account вистачає грошей
        - зменшити баланс на from_account
        - збільшити баланс на to_account
        - створити запис у таблиці transactions
        """

        from_id = dto.get("from_account")
        to_id = dto.get("to_account")
        payment_id = dto.get("payment_id")
        amount = dto.get("amount")

        if from_id is None or to_id is None or payment_id is None or amount is None:
            raise ValueError("from_account, to_account, payment_id, amount є обов'язковими полями")

        from_acc = Account.query.get(from_id)
        to_acc = Account.query.get(to_id)

        if not from_acc or not to_acc:
            raise LookupError("Один з акаунтів не знайдено")

        # на всяк випадок, якщо в БД null
        from_balance = float(from_acc.balance or 0)
        to_balance = float(to_acc.balance or 0)
        amount = float(amount)

        if from_balance < amount:
            # можна також створити транзакцію зі статусом failed,
            # але для простоти просто кидаємо помилку
            raise RuntimeError("Недостатньо коштів на рахунку відправника")

        # оновлюємо баланси
        from_acc.balance = from_balance - amount
        to_acc.balance = to_balance + amount

        tr = Transaction(
            from_account=from_id,
            to_account=to_id,
            payment_id=payment_id,
            amount=amount,
            status="completed",
        )

        db.session.add(tr)
        db.session.commit()

        return tr

    @staticmethod
    def update_transaction(transaction_id: int, dto: dict) -> Optional[Transaction]:
        tr = TransactionDAO.get_by_id(transaction_id)
        if not tr:
            return None
        # просте оновлення статусу / суми, без зміни балансів
        for key, value in dto.items():
            setattr(tr, key, value)
        db.session.commit()
        return tr

    @staticmethod
    def delete_transaction(transaction_id: int) -> bool:
        tr = TransactionDAO.get_by_id(transaction_id)
        if not tr:
            return False
        TransactionDAO.delete(tr)
        return True
