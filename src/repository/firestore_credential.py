from typing import Final


class CredentialFirestore:
    project_id: Final[str]
    project_key_id: Final[str]
    private_key : Final[str]
    client_email: Final[str]
    client_id: Final[str]
    client_x509_cert_url: Final[str]

    def __init__(self, project_id: str, project_key_id: str, private_key: str, client_email: str, client_id: str, client_x509_cert_url: str) -> None:
        if (len(project_id) < 0):
            raise ValueError('project_id must not be empty')
        if (len(project_key_id) < 0):
            raise ValueError('project_key_id must not be empty')
        if (len(private_key) < 0):
            raise ValueError('private_key must not be empty')
        if (len(client_email) < 0):
            raise ValueError('private_key must not be empty')
        if (len(client_id) < 0):
            raise ValueError('private_key must not be empty')
        if (len(client_x509_cert_url) < 0):
            raise ValueError('auth_uri must not be empty')

        self.project_id = project_id
        self.project_key_id = project_key_id
        self.private_key = private_key
        self.client_email = client_email
        self.client_id = client_id
        self.client_x509_cert_url = client_x509_cert_url

    def toDict(self):
        return {
            "type": "service_account",
            "project_id": self.project_id,
            "private_key_id": self.project_key_id,
            "private_key": self.private_key,
            "client_email": self.client_email,
            "client_id": self.client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": self.client_x509_cert_url
        }
