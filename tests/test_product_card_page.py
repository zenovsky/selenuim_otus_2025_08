import pytest

from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_product_title(browser):
    browser.get(f'{browser.base_url}/13-brown-bear-vector-graphics.html')
    wait_title("Brown bear - Vector graphics", browser)


def test_product_card_image(browser):
    browser.get(f'{browser.base_url}/13-brown-bear-vector-graphics.html')
    wait_element("[src$='/brown-bear-vector-graphics.jpg']", browser)    


@pytest.mark.parametrize("css_element", [
    (".current-price-value"), 
    (".btn.btn-primary.add-to-cart"), 
    ("#quantity_wanted"), 
    (".wishlist-button-add"), 
])
def test_product_card_css_elements_present(browser, css_element):
    browser.get(f'{browser.base_url}/13-brown-bear-vector-graphics.html')
    wait_element(css_element, browser)


@pytest.mark.parametrize("xpath_element", [
    ("//*[normalize-space()='Description']"), 
    ("//*[normalize-space()='Product Details']"), 
])
def test_product_card_xpath_elements_present(browser, xpath_element):
    browser.get(f'{browser.base_url}/13-brown-bear-vector-graphics.html')
    wait_element(xpath_element, browser, by=By.XPATH)    