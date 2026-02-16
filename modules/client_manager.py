from typing import Dict, List
from modules.client import Client

class ClientManager:
    def __init__(self):
        # key: client_id | valor: Client object
        self._clients: Dict[str, Client] = {}

    # -------- CREATE --------
    def add_client(self, client: Client) -> None:
        # Verificar duplicado a través de client_id
        if client.client_id in self._clients:
            raise ValueError(f"El ID de Cliente ingresado ya existe: {client.client_id}")

        # Verificar duplicado a través de email
        if self._email_exists(client.email):
            raise ValueError(f"El email ingresado ya existe: {client.email}")

        self._clients[client.client_id] = client

    # -------- READ --------
    def list_clients(self) -> List[Client]:
        return list(self._clients.values())

    def get_client_by_id(self, client_id: str) -> Client:
        if client_id not in self._clients:
            raise ValueError(f"Cliente no encontrado: {client_id}")
        return self._clients[client_id]

    def get_client_by_email(self, email: str) -> Client:
        for client in self._clients.values():
            if client.email == email:
                return client
        raise ValueError(f"Cliente no encontrado con email: {email}")

    # -------- UPDATE --------
    def update_client(self, client_id: str, **fields) -> None:
        client = self.get_client_by_id(client_id)

        for field, value in fields.items():
            if hasattr(client, field):
                setattr(client, field, value)

    # -------- DELETE --------
    def remove_client(self, client_id: str) -> None:
        if client_id not in self._clients:
            raise ValueError(f"Cliente no encontrado: {client_id}")
        del self._clients[client_id]

    # -------- HELPERS --------
    def _email_exists(self, email: str) -> bool:
        for client in self._clients.values():
            if client.email == email:
                return True
        return False
