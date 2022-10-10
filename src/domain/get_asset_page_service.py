import os
from typing import Final
from selenium import webdriver
from .asset_page import AssetPage
from .credential import Credential
from .login_page import LoginPage


class GetAssetPageService:
    __asset_page: Final[AssetPage]
    def __init__(self, driver: webdriver):
        self.__asset_page = self.__get_asset_page(driver)

    def asset_page(self):
        return self.__asset_page
    
    def __get_asset_page(self, driver: webdriver):
        try:
            return AssetPage(driver=driver)
        except ValueError:
            account_id = os.environ.get('SBI_ID')
            account_pass = os.environ.get('SBI_PASS')
            LoginPage(driver=driver).login(Credential(account_id, account_pass))
            return AssetPage(driver=driver)
