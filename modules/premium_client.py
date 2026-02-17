from modules.client import Client


class PremiumClient(Client):
    def get_type(self) -> str:
        return "Premium"
