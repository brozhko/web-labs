from typing import List, Optional
from ..dao.client_dao import ClientDAO
from ..domain.models import Client


class ClientService:
    @staticmethod
    def list_clients() -> List[Client]:
        return ClientDAO.get_all()

    @staticmethod
    def get_client(client_id: int) -> Optional[Client]:
        return ClientDAO.get_by_id(client_id)

    @staticmethod
    def create_client(dto: dict) -> Client:
        return ClientDAO.create(dto)

    @staticmethod
    def update_client(client_id: int, dto: dict) -> Optional[Client]:
        client = ClientDAO.get_by_id(client_id)
        if not client:
            return None
        return ClientDAO.update(client, dto)

    @staticmethod
    def delete_client(client_id: int) -> bool:
        client = ClientDAO.get_by_id(client_id)
        if not client:
            return False
        ClientDAO.delete(client)
        return True
