from pages.base_page import BasePage
from selenium.webdriver.common.by import By

UNIQUE_HOME_PAGE_SELECTOR = \
    (By.XPATH, "//*[@id='foryou_tab']//a[@class='pulldown_desktop']")
SEARCH_FIELD_SELECTOR = (By.ID, "store_nav_search_term")
BUTTON_SEARCH_SELECTOR = (By.XPATH, "//a[@id='store_search_link']//img")


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_enter(self, name_game):
        self.visibility(SEARCH_FIELD_SELECTOR).send_keys(name_game)

    def click_search(self):
        self.clickable(BUTTON_SEARCH_SELECTOR).click()

    def is_home_page_opened(self):
        self.is_page_opened(UNIQUE_HOME_PAGE_SELECTOR)
