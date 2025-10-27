from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_product_add_to_cart(browser):
    browser.get(f'{browser.base_url}')
    wait_title("PrestaShop", browser)
    wait_element(".thumbnail.product-thumbnail", browser).click()
    product = wait_element(".h1", browser)
    product_name_on_card = product.text.strip().lower()
    wait_element(".btn.btn-primary.add-to-cart", browser).click()
    modal_title_element = wait_element(".modal-title.h6.text-sm-center", browser)
    assert "successfully added" in modal_title_element.text, "Товар не был добавлен."
    cart_product_title_element = wait_element(".h6.product-name", browser)
    product_name_in_cart = cart_product_title_element.text.strip().lower()
    assert product_name_on_card == product_name_in_cart, \
        (f"Товар не совпадают! На карточке: '{product_name_on_card}', "
         f"В корзине: '{product_name_in_cart}'")

