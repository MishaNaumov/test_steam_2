from utils import JsonUtils
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(JsonUtils.get_attribute("url_steam"))

    @property
    def wait(self):
        return WebDriverWait(self.driver, JsonUtils.get_attribute("timeout"))

    def visibility(self, selector):
        return self.wait.until(EC.visibility_of_element_located(selector))

    def clickable(self, selector):
        return self.wait.until(EC.element_to_be_clickable(selector))

    def presence(self, selector):
        return self.wait.until(EC.presence_of_element_located(selector))

    def is_page_opened(self, selector):
        try:
            self.wait.until(
                EC.presence_of_element_located(selector))
            return True
        except selenium.common.TimeoutException:
            return False
