import os
from typing import Final
from selenium import webdriver
from .asset_page import AssetPage
from .credential import CredentialSbi
from .login_page import LoginPage


class GetAssetPageService:
    __asset_page: Final[AssetPage]
    def __init__(self, driver: webdriver, credential: CredentialSbi):
        self.__asset_page = self.__get_asset_page(driver, credential)

    def asset_page(self):
        return self.__asset_page
    
    def __get_asset_page(self, driver: webdriver, credential: CredentialSbi):
        try:
            return AssetPage(driver=driver)
        except ValueError:
            LoginPage(driver=driver).login(CredentialSbi(credential.id, credential.password))
            return AssetPage(driver=driver)
