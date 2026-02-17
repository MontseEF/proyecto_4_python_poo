# modules/exceptions.py

class ClientError(Exception):
    """Error base para el sistema de clientes."""
    pass


class ClientAlreadyExistsError(ClientError):
    pass


class ClientNotFoundError(ClientError):
    pass


class InvalidClientIdError(ClientError):
    pass


class InvalidEmailError(ClientError):
    pass


class InvalidPhoneError(ClientError):
    pass
