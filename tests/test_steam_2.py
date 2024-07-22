import time

import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import JsonUtils

UNIQUE_HOME_PAGE = "//a[@class='pulldown_desktop' and text() = 'Your Store']"
WINDOW_SEARCH_ID = "store_nav_search_term"
BUTTON_SEARCH = "//a[@id='store_search_link']//img"
UNIQUE_SEARCH_PAGE = "//a[@id='sort_by_trigger']"
HIGHEST_PRICE_ID = "Price_DESC"
FIRST_GAME = "//div[@id='search_result_container']//a"
NAME_GAME = "//span[@class='title']"
PRICE_GAME = "//div[@class='discount_final_price']"


def test_steam_search_game(driver):
    wait = WebDriverWait(driver, JsonUtils.get_attribute("timeout"))

    def is_page_opened(locator):
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except selenium.common.TimeoutException:
            return False

    assert is_page_opened(UNIQUE_HOME_PAGE), "Home page not opened"

    for item in JsonUtils.get_attribute("game"):
        wait.until(EC.visibility_of_element_located
                   ((By.ID, WINDOW_SEARCH_ID))).send_keys(item)
        wait.until(EC.element_to_be_clickable
                   ((By.XPATH, BUTTON_SEARCH))).click()

        assert is_page_opened(UNIQUE_SEARCH_PAGE), "Store page not opened"

        filter = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, UNIQUE_SEARCH_PAGE))).click()
        wait.until(EC.element_to_be_clickable
                   ((By.ID, HIGHEST_PRICE_ID))).click()

        assert filter.text == "Highest Price"
        wait.until(EC.presence_of_element_located
                   ((By.XPATH, FIRST_GAME))).click()
        time.sleep(10)
