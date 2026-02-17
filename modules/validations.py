import re
from modules.exceptions import InvalidNameError, InvalidClientIdError, InvalidEmailError, InvalidPhoneError


# Email: algo@algo.dominio 
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$"

# Teléfono: solo dígitos, 8 a 12 caracteres 
PHONE_REGEX = r"^\d{8,12}$"

# Client ID: alfanumérico y guiones, 1 a 20 chars (evita espacios y texto raro)
CLIENT_ID_REGEX = r"^[A-Za-z0-9_-]{1,20}$"


def validate_name(name: str) -> None:
    name = name.strip()

    if not name:
        raise InvalidNameError("El nombre no puede estar vacío.")

    # Solo letras y espacios (incluye acentos y ñ)
    pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$"

    if not re.match(pattern, name):
        raise InvalidNameError(
            "El nombre solo puede contener letras y espacios."
        )


def validate_client_id(client_id: str) -> None:
    value = str(client_id).strip()
    if not re.match(CLIENT_ID_REGEX, value):
        raise InvalidClientIdError(
            "ID inválido. Use solo letras/números y opcionalmente '-' o '_', sin espacios "
            "(ej: 001, cli_01, A-100)."
        )


def validate_email(email: str) -> None:
    value = str(email).strip()
    if not re.match(EMAIL_REGEX, value):
        raise InvalidEmailError(f"Email inválido: {email}")


def validate_phone(phone: str) -> None:
    value = str(phone).strip()
    if not re.match(PHONE_REGEX, value):
        raise InvalidPhoneError(
            f"Teléfono inválido: {phone}. Debe tener solo dígitos (8 a 12)."
        )
