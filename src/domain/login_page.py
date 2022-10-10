from typing import Final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from .credential import Credential


class LoginPage:
    input_user: Final[WebElement]
    input_pass: Final[WebElement]
    button_login: Final[WebElement]

    def __init__(self, driver: webdriver):
        try:
            self.input_user = driver.find_element(by=By.ID, value='user_input').find_element(by=By.NAME, value="user_id")
            self.input_pass = driver.find_element(by=By.ID, value='password_input').find_element(by=By.NAME,value="user_password")
            self.button_login = driver.find_element(by=By.NAME, value='ACT_login')
        except NoSuchElementException:
            raise ValueError('current page is not login page.')

    def login(self, cred: Credential):
        self.input_user.send_keys(cred.id)
        self.input_pass.send_keys(cred.password)
        self.button_login.click()
