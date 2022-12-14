from datetime import datetime
from typing import Final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from .obtained_time import ObtainedTime

from .asset import Asset

class AssetPage:
    __products: Final[list]

    def __init__(self, driver: webdriver):
        driver.get('https://site.sbisec.co.jp/account/assets')
        if not self.__is_asset_page(driver):
            raise ValueError('current page is not asset page.')
        
        obtainedTime = ObtainedTime(datetime.now())
        driver.find_element(by=By.ID, value='balance')

        product_table: WebElement = driver.find_element(by=By.XPATH, value='//*[@id="balance"]/ul')
        product_rows: WebElement = product_table.find_elements(By.CLASS_NAME, value='table-row')
        products = []
        for row in product_rows:
            try:
                asset: WebElement = row.find_element(By.CLASS_NAME, value='item-content').find_element(By.CLASS_NAME, value='link')
                product_box: WebElement = row.find_element(By.XPATH, value='div[2]')
                product: WebElement = product_box.find_element(By.TAG_NAME, value='p')
                products.append(Asset(asset.text, self.__parse_price(product.text), obtainedTime))
            except NoSuchElementException:
                continue
        self.__products = products

    def products(self):
        return self.__products.copy()
    
    def __is_asset_page(self, driver: webdriver):
        try:
            WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(by=By.ID, value="balance"))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
    
    def __parse_price(self, priceStr: str):
        unit_removed = priceStr.replace('円', '')
        unit_comma_removed = unit_removed.replace(',', '')
        return int(unit_comma_removed)
