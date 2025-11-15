from page_objects.add_to_cart import AddToCart
from page_objects.main_page import MainPage


def test_product_add_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open_main()

    add_to_cart = AddToCart(browser)
    add_to_cart.click_product()
    product_in_card = add_to_cart.get_product_name_in_card()
    add_to_cart.click_add_to_cart()
    add_to_cart.check_modal_element_title()
    assert "successfully added" in add_to_cart.check_modal_element_title().text, "Товар не был добавлен."
    product_in_cart = add_to_cart.get_product_name_in_cart()
    assert product_in_card == product_in_cart, \
        (f"Товар не совпадают! На карточке:'{product_in_card}', "
        f"В корзине: '{product_in_cart}'")

