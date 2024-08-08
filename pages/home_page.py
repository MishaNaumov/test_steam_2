from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    UNIQUE_LOC = \
        (By.XPATH, "//*[@id='foryou_tab']//a[@class='pulldown_desktop']")
    SEARCH_FIELD_SELECTOR = (By.ID, "store_nav_search_term")
    BUTTON_SEARCH_SELECTOR = (By.XPATH, "//*[@id='store_search_link']//img")

    def search_enter(self, name_game):
        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_FIELD_SELECTOR))\
            .send_keys(name_game)

    def click_search(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_SEARCH_SELECTOR)).click()
