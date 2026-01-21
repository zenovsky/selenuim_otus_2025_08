import allure

from page_objects.add_to_cart import AddToCart
from page_objects.main_page import MainPage


@allure.epic("Главная страница")
@allure.feature("Покупка товара")
@allure.story("Сценарий добавления товара в корзину")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_add_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open_main()

    add_to_cart = AddToCart(browser)
    add_to_cart.click_product()
    product_in_card = AddToCart(browser).get_product_name_in_card()
    add_to_cart.click_add_to_cart()
    modal_title = add_to_cart.check_modal_element_title()
    assert "successfully added" in modal_title.text, "Товар не был добавлен."
    product_in_cart = add_to_cart.get_product_name_in_cart()
    assert product_in_card == product_in_cart, (
        f"Товар не совпадают! На карточке:'{product_in_card}', В корзине: '{product_in_cart}'"
    )
