from selenium.webdriver.chrome.options import Options
from utils.json_utils import JsonUtils
from singleton import WebDriver
import pytest


@pytest.fixture()
def driver():
    options = Options()
    for item in JsonUtils.get_attribute("options"):
        options.add_argument(item)
    web_chrome = WebDriver(options)
    web_chrome.get(JsonUtils.get_attribute("url_steam"))

    yield web_chrome
    WebDriver.quit()
