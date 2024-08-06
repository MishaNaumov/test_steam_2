import pytest
from pages.home_page import HomePage
from pages.store_page import StorePage
from utils.dict_games_utils import DictGamesUtils


@pytest.mark.parametrize(
    "param",
    [
        pytest.param(("The Witcher", 10), id="The Witcher"),
        pytest.param(("Fallout", 20), id="Fallout")
    ]
)
def test_steam_search_game(driver, param):
    name_game, qty = param

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

    dict_games = store_page.create_dict_games(qty)

    assert DictGamesUtils.sort_check(dict_games), \
        "The filter doesn't work correctly"
