from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import JsonUtils
import pytest


@pytest.fixture()
def driver():
    options = Options()
    for item in JsonUtils.get_attribute("options"):
        options.add_argument(item)
    web_chrome = webdriver.Chrome(options=options)
    web_chrome.get(JsonUtils.get_attribute("url_steam"))
    return web_chrome
