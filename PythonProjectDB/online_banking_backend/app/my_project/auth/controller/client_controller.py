from flask import request
from ..service.client_service import ClientService
from ...ui.utils.responses import success_response, error_response
from ..domain.models import Client


def client_to_dto(client: Client) -> dict:
    return {
        "client_id": client.client_id,
        "full_name": client.full_name,
        "phone": client.phone,
        "email": client.email,
        "passport": client.passport,
        "address": client.address,
        "created_at": client.created_at.isoformat() if client.created_at else None,
    }


def get_all_clients():
    clients = ClientService.list_clients()
    return success_response([client_to_dto(c) for c in clients])


def get_client_by_id(client_id: int):
    client = ClientService.get_client(client_id)
    if not client:
        return error_response("Client not found", 404)
    return success_response(client_to_dto(client))


def create_client():
    data = request.get_json() or {}
    client = ClientService.create_client(data)
    return success_response(client_to_dto(client), 201)


def update_client(client_id: int):
    data = request.get_json() or {}
    client = ClientService.update_client(client_id, data)
    if not client:
        return error_response("Client not found", 404)
    return success_response(client_to_dto(client))


def delete_client(client_id: int):
    ok = ClientService.delete_client(client_id)
    if not ok:
        return error_response("Client not found", 404)
    return success_response({"deleted": True})
