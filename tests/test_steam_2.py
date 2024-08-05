import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.store_page import StorePage


@pytest.mark.parametrize(
    "param",
    [
        pytest.param(("The Witcher", 10), id="The Witcher"),
        pytest.param(("Fallout", 20), id="Fallout")
    ]
)
def test_steam_search_game(driver, param):
    name_game, qty = param

    steam = BasePage(driver)
    steam.open()

    home_page = HomePage(driver)
    store_page = StorePage(driver)

    assert home_page.is_home_page_opened, "Home page not opened"

    home_page.search_enter(name_game)
    home_page.click_search()

    assert store_page.is_store_page_opened, "Store page not opened"

    store_page.click_filter()
    store_page.click_highest_price()

    store_page.loading()
    store_page.not_loading()

    assert store_page.sort_check(qty), "The filter doesn't work correctly"
