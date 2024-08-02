import pytest
import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import JsonUtils

UNIQUE_HOME_PAGE = "//*[@id='foryou_tab']//a[@class='pulldown_desktop']"
WINDOW_SEARCH_ID = "store_nav_search_term"
BUTTON_SEARCH = "//a[@id='store_search_link']//img"
UNIQUE_SEARCH_PAGE = "//a[@id='sort_by_trigger']"
FILTER = "//a[@id='sort_by_trigger']"
HIGHEST_PRICE_ID = "Price_DESC"
LOADING = "//*[@id='search_result_container' and @style]"
NAME_GAME = "//*[@id='search_resultsRows']//a[{}]//span[@class='title']"
PRICE_GAME = \
    "//*[@id='search_resultsRows']//a[{}]//div[contains(text(),'уб') " \
    "and not(@class='discount_original_price')]"


@pytest.mark.parametrize(
    "param",
    [
        pytest.param(("The Witcher", 10), id="The Witcher"),
        pytest.param(("Fallout", 20), id="Fallout")
    ]
)
def test_steam_search_game(driver, param):
    name_game, qty = param
    wait = WebDriverWait(driver, JsonUtils.get_attribute("timeout"))

    def is_page_opened(locator):
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except selenium.common.TimeoutException:
            return False

    assert is_page_opened(UNIQUE_HOME_PAGE), "Home page not opened"

    wait.until(EC.visibility_of_element_located((By.ID, WINDOW_SEARCH_ID)))\
        .send_keys(name_game)

    wait.until(EC.element_to_be_clickable((By.XPATH, BUTTON_SEARCH))).click()

    assert is_page_opened(UNIQUE_SEARCH_PAGE), "Store page not opened"

    wait.until(EC.element_to_be_clickable((By.XPATH, FILTER))).click()

    wait.until(EC.element_to_be_clickable((By.ID, HIGHEST_PRICE_ID))).click()

    WebDriverWait(driver, timeout=JsonUtils.get_attribute("timeout"),
                  poll_frequency=0.07)\
        .until(EC.presence_of_element_located((By.XPATH, LOADING)))

    wait.until_not(EC.presence_of_element_located((By.XPATH, LOADING)))

    def create_dict():
        dict_game = {}
        n = 1

        for game in range(qty):
            dict_game[wait.until(EC.presence_of_element_located
                                 ((By.XPATH, NAME_GAME.format(n)))).text] = \
                wait.until(EC.presence_of_element_located
                           ((By.XPATH, PRICE_GAME.format(n)))).text
            n += 1

        for game, price in dict_game.items():
            dict_game[game] = float(price[:-4].replace(",", "."))
        return dict_game

    def sort_check():
        temp_price = 1000000000000000000000

        for price in create_dict().values():
            if price <= temp_price:
                temp_price = price
            else:
                return False
        return True

    assert sort_check(), "The filter doesn't work correctly"
