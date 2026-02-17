from modules.client import Client

class PremiumClient(Client):
    def get_type(self) -> str:
        return "Premium"


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
