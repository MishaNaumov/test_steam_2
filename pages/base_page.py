from utils.json_utils import JsonUtils
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver, JsonUtils.get_attribute("timeout")
        )

    def is_page_opened(self, selector):
        try:
            self.wait.until(
                EC.presence_of_element_located(selector))
            return True
        except selenium.common.TimeoutException:
            return False
