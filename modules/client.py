from modules.validations import validate_client_id, validate_name,  validate_email, validate_phone


class Client:
    """
    Base class para todos los clientes (propietarios).
    Identificadores únicos:
    - client_id (interno)
    - email (externo)
    """

    def __init__(self, client_id: str, name: str, email: str, phone: str, address: str):
        # Validar ID y asignar 
        self.client_id = client_id

        # Usar setters para que pasen por limpieza/validación
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    # --- Getters / Setters (encapsulamiento) ---
    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        validate_client_id(value)
        self._client_id = str(value).strip()

    @property
    def name(self) -> str:
        return self._name

   

    @name.setter
    def name(self, value: str) -> None:
        validate_name(value)
        self._name = value.strip()


    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        validate_email(value)
        self._email = str(value).strip().lower()

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        validate_phone(value)
        self._phone = str(value).strip()

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = str(value).strip()

    # --- Polimorfismo ---
    def get_type(self) -> str:
        return "Regular"

    def get_summary(self) -> str:
        return (
            f"[{self.get_type()}] "
            f"ID={self.client_id} | Nombre={self.name} | Email={self.email} | Teléfono={self.phone}"
        )

    def to_dict(self) -> dict:
        """Útil para exportar a CSV."""
        return {
            "type": self.get_type(),
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
        }

    def __str__(self) -> str:
        return self.get_summary()
