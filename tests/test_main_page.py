import pytest

from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_main_title(browser):
    browser.get(f'{browser.base_url}')
    wait_title("PrestaShop", browser)


@pytest.mark.parametrize("header_element", [
    ("#contact-link"),
    ("#_desktop_currency_selector"),
    ("#_desktop_user_info"),
    ("#category-3"),
    ("#category-6"),
    ("#category-9"),
    ("#search_widget"),
])
def test_main_header_top(browser, header_element):
    browser.get(f'{browser.base_url}')
    wait_element(header_element, browser)


@pytest.mark.parametrize("products", [
    ("//*[normalize-space()='Popular Products']"),
    ("//*[normalize-space()='On sale']"),
    ("//*[normalize-space()='New products']"),
])
def test_main_products(browser, products):
    browser.get(f'{browser.base_url}')
    wait_element(products, browser, by=By.XPATH)


@pytest.mark.parametrize("block_id", [
    ("#carousel"),                                   
    (".banner"),                                      
    ("#custom-text"),                               
    ("#blockEmailSubscription_displayFooterBefore"),
])
def test_main_page_key_blocks(browser, block_id):
    browser.get(f'{browser.base_url}')
    wait_element(block_id, browser)    


@pytest.mark.parametrize("footer_element", [
    ("//*[normalize-space()='Products']"),
    ("//*[normalize-space()='Our company']"),
    ("//*[normalize-space()='Your account']"),
    ("//p[normalize-space()='Store information']"),
])
def test_main_footer(browser, footer_element):
    browser.get(f'{browser.base_url}')
    wait_element(footer_element, browser, by=By.XPATH)