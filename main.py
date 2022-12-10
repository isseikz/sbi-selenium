import os
from selenium import webdriver
import chromedriver_binary
from src.application.save_my_assets_to_firestore import SaveMyAssetsToFirestore
from src.domain.credential import CredentialSbi
from src.repository.firestore_credential import CredentialFirestore

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

cred_sbi = CredentialSbi(
    os.environ.get('SBI_ID'),
    os.environ.get('SBI_PASS')
)

cred_firestore = CredentialFirestore(
    os.environ.get('FIRESTORE_PROJECT_ID'),
    os.environ.get('FIRESTORE_PROJECT_KEY_ID'),
    os.environ.get('FIRESTORE_PRIVATE_KEY').replace('\\n', '\n'),
    os.environ.get('FIRESTORE_CLIENT_EMAIL'),
    os.environ.get('FIRESTORE_CLIENT_ID'),
    os.environ.get('FIRESTORE_CLIENT_X509_CERT_URL'),
)

driver = driver_init()

SaveMyAssetsToFirestore(driver, cred_sbi, cred_firestore).exec()
