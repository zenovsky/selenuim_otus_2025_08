from page_objects.base_page import BasePage


class AddToCart(BasePage):
    PRODUCT = ".thumbnail.product-thumbnail"

    PRODUCT_NAME_IN_CARD = ".h1"

    ADD_TO_CART_BUTTON = ".btn.btn-primary.add-to-cart"

    MODAL_WINDOW_TITLE = ".modal-title.h6.text-sm-center"

    PRODUCT_NAME_IN_CART = ".h6.product-name"

    def click_product(self):
        self.wait_element(self.PRODUCT).click()

    def get_product_name_in_card(self):
        product_on_card = self.wait_element(self.PRODUCT_NAME_IN_CARD)
        return product_on_card.text.strip().lower()

    def click_add_to_cart(self):
        self.wait_element(self.ADD_TO_CART_BUTTON).click()

    def check_modal_element_title(self):
        return self.wait_element(self.MODAL_WINDOW_TITLE)

    def get_product_name_in_cart(self):
        product_in_cart = self.wait_element(self.PRODUCT_NAME_IN_CART)
        return product_in_cart.text.strip().lower()








