from page_objects.currency_change import CurrencyChange
from page_objects.main_page import MainPage


def test_currency_change_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    currency_change = CurrencyChange(browser)
    price_euro = currency_change.get_price_text()
    currency_change.click_currency_dropdown()
    currency_change.select_dollar()
    price_dollar = currency_change.get_price_text()
    assert price_euro != price_dollar, \
        "Цены не изменились после переключения валюты!"
    assert "€" in price_euro, "Цена не содержит символ EUR (€)"
    assert "€" not in price_dollar, "Символ валюты не изменился на USD."