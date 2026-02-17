def __init__(self, client_id: str, name: str, email: str, phone: str, address: str):
    self._client_id = str(client_id).strip()

    self.name = name
    self.email = email      
    self.phone = phone      
    self.address = address
