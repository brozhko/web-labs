from typing import List, Optional
from ..domain.models import db, Client


class ClientDAO:
    @staticmethod
    def get_all() -> List[Client]:
        return Client.query.all()

    @staticmethod
    def get_by_id(client_id: int) -> Optional[Client]:
        return Client.query.get(client_id)

    @staticmethod
    def create(data: dict) -> Client:
        client = Client(**data)
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def update(client: Client, data: dict) -> Client:
        for key, value in data.items():
            setattr(client, key, value)
        db.session.commit()
        return client

    @staticmethod
    def delete(client: Client) -> None:
        db.session.delete(client)
        db.session.commit()
