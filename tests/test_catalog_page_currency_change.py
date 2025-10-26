from framework import wait_element
from selenium.webdriver.common.by import By


def test_currency_change_on_catalog(browser):
    browser.get(f'{browser.base_url}/2-home')
    price_element = wait_element(".product-miniature:first-child .price", browser)
    price_eur = price_element.text.strip()
    wait_element(".hidden-sm-down.btn-unstyle", browser).click()
    wait_element("a[title='US Dollar']", browser).click()
    price_element = wait_element(".product-miniature:first-child .price", browser)
    price_usd = price_element.text.strip()
    assert price_eur != price_usd, \
        "Цены не изменились после переключения валюты!"
    assert "€" in price_eur, "Цена не содержит символ EUR (€)"
    assert "€" not in price_usd, "Символ валюты не изменился на USD."

