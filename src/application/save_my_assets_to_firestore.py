from typing import Final
from selenium import webdriver

from src.domain.credential import CredentialSbi
from src.domain.get_asset_page_service import GetAssetPageService
from src.repository.firestore_credential import CredentialFirestore
from src.repository.firestore import Firestore


class SaveMyAssetsToFirestore:
    driver: webdriver
    cred_sbi: Final[CredentialSbi]
    cred_firestore: Final[CredentialFirestore]

    def __init__(self, driver, credential_sbi: CredentialSbi, credential_firestore: CredentialFirestore) -> None:
        self.driver = driver
        self.cred_sbi = credential_sbi
        self.cred_firestore = credential_firestore

    def exec(self):
        assets = GetAssetPageService(
            driver=self.driver,
            credential=self.cred_sbi
        ).asset_page().products()
        print(assets)

        datastore = Firestore(self.cred_firestore)
        for asset in assets:
            datastore.save(asset=asset)
