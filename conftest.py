from selenium.webdriver.chrome.options import Options
from utils import JsonUtils
from singleton import WebDriver
import pytest


@pytest.fixture()
def driver():
    options = Options()
    for item in JsonUtils.get_attribute("options"):
        options.add_argument(item)
    web_chrome = WebDriver.get_driver(options)
    return web_chrome
