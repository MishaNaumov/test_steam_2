from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import JsonUtils

UNIQUE_SEARCH_PAGE_SELECTOR = (By.XPATH, "//a[@id='sort_by_trigger']")
FILTER_SELECTOR = (By.XPATH, "//a[@id='sort_by_trigger']")
HIGHEST_PRICE_SELECTOR = (By.ID, "Price_DESC")
LOADING_SELECTOR = (By.XPATH, "//*[@id='search_result_container' and @style]")

NAME_GAME_LOCATOR = \
    "//*[@id='search_resultsRows']//a[{}]//span[@class='title']"
PRICE_GAME_LOCATOR = \
    "//*[@id='search_resultsRows']//a[{}]//div[contains(text(),'уб') " \
    "and not(@class='discount_original_price')]"


class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_filter(self):
        self.clickable(FILTER_SELECTOR).click()

    def click_highest_price(self):
        self.clickable(HIGHEST_PRICE_SELECTOR).click()

    @property
    def wait_special(self):
        return WebDriverWait\
            (self.driver, timeout=JsonUtils.get_attribute("timeout")
             , poll_frequency=0.07)

    def loading(self):
        self.wait_special.until\
            (EC.presence_of_element_located(LOADING_SELECTOR))

    def not_loading(self):
        self.wait.until_not(EC.presence_of_element_located(LOADING_SELECTOR))

    def is_store_page_opened(self):
        self.is_page_opened(UNIQUE_SEARCH_PAGE_SELECTOR)

    def presence_for_dict(self, locator):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, locator)))

    def create_dict(self, qty):
        dict_game = {}
        n = 1

        for game in range(qty):
            dict_game[
                self.presence_for_dict(NAME_GAME_LOCATOR.format(n)).text
            ] = self.presence_for_dict(PRICE_GAME_LOCATOR.format(n)).text
            n += 1

        return dict_game

    def create_special_dict(self, qty):
        special_dict_game = {}
        for game, price in self.create_dict(qty).items():
            special_dict_game[game] = float(price[:-4].replace(",", "."))
        return special_dict_game

    def sort_check(self, qty):
        temp_price = 1000000000000000000000

        for price in self.create_special_dict(qty).values():
            if price <= temp_price:
                temp_price = price
            else:
                return False
        return True
