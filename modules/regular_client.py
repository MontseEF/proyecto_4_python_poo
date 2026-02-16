from modules.client import Client

class RegularClient(Client):
    def get_type(self) -> str:
        return "Regular"
