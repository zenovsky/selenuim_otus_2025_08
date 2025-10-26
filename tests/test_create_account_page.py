import pytest

from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_create_account_title(browser):
    browser.get(f'{browser.base_url}/registration')
    wait_title("Registration", browser)


def test_create_account_login_link(browser):
    browser.get(f'{browser.base_url}/registration')
    wait_element(f"a[href$='/login']", browser)


@pytest.mark.parametrize("gender", [
    ("label[for='field-id_gender-1']"),
    ("label[for='field-id_gender-2']"),
])
def test_create_account_gender_radio(browser, gender):
    browser.get(f'{browser.base_url}/registration')
    wait_element(gender, browser)


@pytest.mark.parametrize("field", [
    ("#field-firstname"),
    ("#field-lastname"),
    ("#field-email"),
    ("#field-password"),
    ("#field-birthday"),
])
def test_create_account_regestry_fields(browser, field):
    browser.get(f'{browser.base_url}/registration')
    wait_element(field, browser)


def test_create_account_save_button(browser):
    browser.get(f'{browser.base_url}/registration')
    wait_element("button[data-link-action='save-customer']", browser)

