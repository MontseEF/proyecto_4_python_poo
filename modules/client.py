class Client:
    """
    Base class para todos los clientes (propietarios).
    Identificadores únicos:
    - client_id (interna)
    - email (externa)
    """

    def __init__(self, client_id: str, name: str, email: str, phone: str, address: str):
        self._client_id = str(client_id).strip()
        self._name = name.strip()
        self._email = email.strip().lower()
        self._phone = phone.strip()
        self._address = address.strip()

    # --- Getters / Setters (encapsulamiento) ---
    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value.strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        # Validation Será agregado más adelante en validation.py
        self._email = value.strip().lower()

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        # Validation will be added later
        self._phone = value.strip()

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value.strip()

    # --- Polimorfismo ---
    def get_type(self) -> str:
        return "Regular"  

    def get_summary(self) -> str:
        return (
            f"[{self.get_type()}] "
            f"ID={self.client_id} | Name={self.name} | Email={self.email} | Phone={self.phone}"
        )

    def to_dict(self) -> dict:
        """
        Util para exportar a CSV.
        """
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
