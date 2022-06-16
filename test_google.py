from selene.support.shared import browser
from selene import be, have
import pytest

search_query = 'selene'
valid_search = 'yashaka/selene: User-oriented Web UI browser tests in Python'
invalid_search = 'yashaka/selenium: User-oriented Web UI browser tests in Python'
query_selector = browser.element('[name="q"]')
id_selector = browser.element('[id="search"]')


@pytest.fixture()
def init_browser():
    browser.open('https://google.com').driver.set_window_size(1920, 1080)


def test_search_selene(init_browser):
    query_selector.should(be.blank).type(search_query).press_enter()
    id_selector .should(have.text(valid_search))


def test_search_invalid_selene(init_browser):
    query_selector.should(be.blank).type(search_query).press_enter()
    id_selector .should(have.text(invalid_search))


