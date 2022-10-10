from selenium import webdriver
import chromedriver_binary
from domain.get_asset_page_service import GetAssetPageService

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()

print(GetAssetPageService(driver=driver).asset_page().products())
# TODO Send asset to server
