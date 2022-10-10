from typing import Final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from .asset import Asset

class AssetPage:
    __products: Final[list]

    def __init__(self, driver: webdriver):
        driver.get('https://site.sbisec.co.jp/account/assets')
        if not self.__is_asset_page(driver):
            raise ValueError('current page is not asset page.')
        
        driver.find_element(by=By.ID, value='balance')

        product_table: WebElement = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/section[2]/ul[1]')
        product_rows: WebElement = product_table.find_elements(By.CLASS_NAME, value='table-row')
        products = []
        for row in product_rows:
            asset: WebElement = row.find_element(By.CLASS_NAME, value='css-1cg2qv2').find_element(By.TAG_NAME, value='a')
            product: WebElement = row.find_element(By.CLASS_NAME, value='css-kthg1q')
            products.append(Asset(asset.text, self.__parse_price(product.text)))
        self.__products = products

    def products(self):
        return self.__products.copy()
    
    def __is_asset_page(self, driver: webdriver):
        try:
            driver.find_element(by=By.ID, value='balance')
            return True
        except NoSuchElementException:
            return False
    
    def __parse_price(self, priceStr: str):
        unit_removed = priceStr.replace('円', '')
        unit_comma_removed = unit_removed.replace(',', '')
        return int(unit_comma_removed)
