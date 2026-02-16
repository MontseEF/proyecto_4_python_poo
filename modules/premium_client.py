from modules.client import Client

class PremiumClient(Client):
    def __init__(self, client_id: str, name: str, email: str, phone: str, address: str, level: str = "Gold"):
        super().__init__(client_id, name, email, phone, address)
        self._level = level.strip()

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, value: str) -> None:
        self._level = value.strip()

    def get_type(self) -> str:
        return "Premium"

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} | Level={self.level}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["level"] = self.level
        return data
