from typing import Dict, List

from modules.client import Client
from modules.exceptions import ClientAlreadyExistsError, ClientNotFoundError
from modules.file_handler import load_clients_from_csv, save_clients_to_csv
from modules.logger import log_info, log_error


class ClientManager:
    def __init__(self):
        # key: client_id | value: Cliente objeto
        self._clients: Dict[str, Client] = {}

        # Cargar clientes desde CSV si existe
        for client in load_clients_from_csv():
            self._clients[client.client_id] = client

    # -------- CREATE --------
    def add_client(self, client: Client) -> None:
        # Duplicado client_id
        if client.client_id in self._clients:
            log_error(f"Intento de ID duplicado: {client.client_id}")
            raise ClientAlreadyExistsError(f"Ya existe un cliente con ID {client.client_id}")

        # Email duplicado
        if self._email_exists(client.email):
            log_error(f"Intento de email duplicado: {client.email}")
            raise ClientAlreadyExistsError(f"Ya existe un cliente con email {client.email}")

        self._clients[client.client_id] = client

        # Persistencia + log
        save_clients_to_csv(self.list_clients())
        log_info(f"Cliente agregado: ID={client.client_id} Email={client.email} Type={client.get_type()}")

    # -------- READ --------
    def list_clients(self) -> List[Client]:
        return list(self._clients.values())

    def get_client_by_id(self, client_id: str) -> Client:
        if client_id not in self._clients:
            log_error(f"Cliente no encontrado por ID: {client_id}")
            raise ClientNotFoundError(f"No se encontró un cliente con ese ID {client_id}")
        return self._clients[client_id]

    def get_client_by_email(self, email: str) -> Client:
        for client in self._clients.values():
            if client.email == email:
                return client

        log_error(f"Cliente no encontrado por email: {email}")
        raise ClientNotFoundError(f"No se encontró un cliente con ese email {email}")

    # -------- UPDATE --------
    def update_client(self, client_id: str, **fields) -> None:
        client = self.get_client_by_id(client_id)

        # Si se intenta cambiar el email, validar duplicado (excepto el mismo cliente)
        if "email" in fields:
            new_email = str(fields["email"]).strip().lower()
            if new_email != client.email and self._email_exists(new_email):
                log_error(f"Intento de actualizar a email duplicado: {new_email} (ID={client_id})")
                raise ClientAlreadyExistsError(f"Ya existe un cliente con email {new_email}")
            fields["email"] = new_email  # normalización

        # Actualizar campos existentes
        for field, value in fields.items():
            if hasattr(client, field):
                setattr(client, field, value)

        # Persistencia + log
        save_clients_to_csv(self.list_clients())
        log_info(f"Cliente actualizado: ID={client_id} Campos={list(fields.keys())}")

    # -------- DELETE --------
    def remove_client(self, client_id: str) -> None:
        if client_id not in self._clients:
            log_error(f"Intento de eliminar ID inexistente: {client_id}")
            raise ClientNotFoundError(f"No se encontró un cliente con ese ID {client_id}")

        removed = self._clients[client_id]
        del self._clients[client_id]

        # Persistencia + log
        save_clients_to_csv(self.list_clients())
        log_info(f"Cliente eliminado: ID={client_id} Email={removed.email} Type={removed.get_type()}")

    # -------- HELPERS --------
    def _email_exists(self, email: str) -> bool:
        for client in self._clients.values():
            if client.email == email:
                return True
        return False

    def id_exists(self, client_id: str) -> bool:
        return client_id in self._clients
