from typing import Final

import firebase_admin
from firebase_admin import firestore, credentials
from google.cloud.firestore import Client

from src.domain.asset import Asset
from .firestore_credential import CredentialFirestore
from .interface_datastore import IDataStore

class Firestore(IDataStore):
    db: Final[Client]
    def __init__(self, credential: CredentialFirestore) -> None:
        self.__init_firestore(credential)
        super().__init__()

    def save(self, asset: Asset) -> None:
        dec_ref = self.db.collection(u'assets').document()
        dec_ref.set({
            u'time': str(asset.time),
            u'name': asset.name,
            u'value': asset.value
        })

    def __init_firestore(self, credential: CredentialFirestore):
        cred = credentials.Certificate(credential.toDict())
        app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    