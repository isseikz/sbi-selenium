from typing import Final
class CredentialSbi:
    id: Final[str]
    password: Final[str]

    def __init__(self, id: str, password: str):
        if len(id) <= 0:
            raise ValueError("id must not be null or empty.")
        if len(password) <= 0:
            raise ValueError("password must not be null or empty.")
        self.id = id
        self.password = password
