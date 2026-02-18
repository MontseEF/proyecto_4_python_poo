from modules.client import Client

class CorporateClient(Client):
    def __init__(self, client_id: str, name: str, email: str, phone: str, address: str, company_name: str):
        super().__init__(client_id, name, email, phone, address)
        self._company_name = company_name.strip()

    @property
    def company_name(self) -> str:
        return self._company_name

    @company_name.setter
    def company_name(self, value: str) -> None:
        self._company_name = value.strip()

    def get_type(self) -> str:
        return "Corporativo"

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} | Company={self.company_name}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["company_name"] = self.company_name
        return data
