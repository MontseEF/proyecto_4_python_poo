from modules.validations import (
    validate_client_id,
    validate_name,
    validate_email,
    validate_phone,
)


class Client:
    """
    Clase base para todos los clientes.
    Identificadores únicos:
    - client_id (interno)
    - email (externo)
    """

    def __init__(
        self,
        client_id: str,
        name: str,
        email: str,
        phone: str,
        address: str,
    ):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    # ---------- client_id ----------
    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        validate_client_id(value)
        self._client_id = value.strip()

    # ---------- name ----------
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        validate_name(value)
        self._name = value.strip()

    # ---------- email ----------
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        validate_email(value)
        self._email = value.strip().lower()

    # ---------- phone ----------
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        validate_phone(value)
        self._phone = value.strip()

    # ---------- address ----------
    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value.strip()

    # ---------- Polimorfismo ----------
    def get_type(self) -> str:
        return "Regular"

    def get_summary(self) -> str:
        return (
            f"[{self.get_type()}] "
            f"ID={self.client_id} | "
            f"Nombre={self.name} | "
            f"Email={self.email} | "
            f"Teléfono={self.phone} | "
            f"Dirección={self.address}"
        )

    # ---------- Persistencia ----------
    def to_dict(self) -> dict:
        """
        Diccionario alineado EXACTAMENTE con el CSV
        """
        return {
            "tipo": self.get_type(),
            "id_cliente": self.client_id,
            "nombre": self.name,
            "email": self.email,
            "teléfono": self.phone,
            "dirección": self.address,
            "nombre_empresa": "",
        }

    def __str__(self) -> str:
        return self.get_summary()
