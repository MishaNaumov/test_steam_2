from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.json_utils import JsonUtils


class StorePage(BasePage):
    UNIQUE_SEARCH_PAGE_SELECTOR = (By.XPATH, "//a[@id='sort_by_trigger']")
    FILTER_SELECTOR = (By.XPATH, "//a[@id='sort_by_trigger']")
    HIGHEST_PRICE_SELECTOR = (By.ID, "Price_DESC")
    LOADING_SELECTOR = (
    By.XPATH, "//*[@id='search_result_container' and @style]")

    NAME_GAME_LOCATOR = \
        "//*[@id='search_resultsRows']//a[{}]//span[@class='title']"
    PRICE_GAME_LOCATOR = \
        "//*[@id='search_resultsRows']//a[{}]//div[contains(text(),'уб') " \
        "and not(@class='discount_original_price')]"

    def click_filter(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FILTER_SELECTOR)).click()

    def click_highest_price(self):
        self.wait.until(
            EC.element_to_be_clickable(self.HIGHEST_PRICE_SELECTOR)).click()

    def loading(self):
        WebDriverWait(
            self.driver, timeout=JsonUtils.get_attribute("timeout"),
            poll_frequency=0.07)\
            .until(EC.presence_of_element_located(self.LOADING_SELECTOR))

    def not_loading(self):
        self.wait.until_not(EC.presence_of_element_located
                            (self.LOADING_SELECTOR))

    def is_store_page_opened(self):
        self.is_page_opened(self.UNIQUE_SEARCH_PAGE_SELECTOR)

    def presence_for_dict(self, locator):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, locator)))

    def create_dict_games(self, qty):
        dict_game = {}
        n = 1

        for game in range(qty):
            dict_game[
                self.presence_for_dict(self.NAME_GAME_LOCATOR.format(n)).text
            ] = self.presence_for_dict(self.PRICE_GAME_LOCATOR.format(n)).text
            n += 1

        return dict_game
