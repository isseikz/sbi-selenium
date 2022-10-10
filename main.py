from selenium import webdriver
import chromedriver_binary
from src.domain.get_asset_price_service import GetAssetPriceService

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()

print(GetAssetPriceService(driver=driver).asset_page().products())
# TODO Send asset to server
