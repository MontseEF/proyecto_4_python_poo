from typing import Dict, List

from modules.client import Client
from modules.exceptions import (
    ClientAlreadyExistsError,
    ClientNotFoundError
)


class ClientManager:
    def __init__(self):
        # key: client_id | valor: Cliente objeto
        self._clients: Dict[str, Client] = {}

    # -------- CREATE --------
    def add_client(self, client: Client) -> None:
        # Duplicado client_id
        if client.client_id in self._clients:
            raise ClientAlreadyExistsError(
                f"Ya existe un cliente con ID {client.client_id}"
            )

        # Email duplicado
        if self._email_exists(client.email):
            raise ClientAlreadyExistsError(
                f"Ya existe un cliente con email {client.email}"
            )

        self._clients[client.client_id] = client

    # -------- READ --------
    def list_clients(self) -> List[Client]:
        return list(self._clients.values())

    def get_client_by_id(self, client_id: str) -> Client:
        if client_id not in self._clients:
            raise ClientNotFoundError(
                f"No se encontró un cliente con ese ID {client_id}"
            )
        return self._clients[client_id]

    def get_client_by_email(self, email: str) -> Client:
        for client in self._clients.values():
            if client.email == email:
                return client

        raise ClientNotFoundError(
            f"No se encontró un cliente con ese email {email}"
        )

    # -------- UPDATE --------
    def update_client(self, client_id: str, **fields) -> None:
        client = self.get_client_by_id(client_id)

        for field, value in fields.items():
            if hasattr(client, field):
                setattr(client, field, value)

    # -------- DELETE --------
    def remove_client(self, client_id: str) -> None:
        if client_id not in self._clients:
            raise ClientNotFoundError(
                f"No se encontró un cliente con ese ID {client_id}"
            )

        del self._clients[client_id]

    # -------- HELPERS --------
    def _email_exists(self, email: str) -> bool:
        for client in self._clients.values():
            if client.email == email:
                return True
        return False
    
    def id_exists(self, client_id: str) -> bool:
        return client_id in self._clients

