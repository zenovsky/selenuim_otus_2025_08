import pytest

from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_admin_login_title(browser):
    browser.get(f'{browser.base_url}/administration')
    wait_title("PrestaShop", browser)


@pytest.mark.parametrize("element_selector", [
    ("#login_form"),
    ("#email"),
    ("#passwd"),
    ("#submit_login"),
    ("#forgot-password-link"),
])
def test_admin_login_page_css_elements_present(browser, element_selector):
    browser.get(f'{browser.base_url}/administration')
    wait_element(element_selector, browser)


def test_admin_login_stay_checkbox(browser):
    browser.get(f'{browser.base_url}/administration')
    wait_element("//*[normalize-space()='Stay logged in']", browser, by=By.XPATH)
