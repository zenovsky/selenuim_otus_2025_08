from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    PAGE_URL = "/13-brown-bear-vector-graphics.html"
    TITLE = "Brown bear - Vector graphics"
    PRODUCT_IMAGE = "[src$='/brown-bear-vector-graphics.jpg']"
    PAGE_CSS_ELEMENTS = [
        ".current-price-value",
        ".btn.btn-primary.add-to-cart",
        "#quantity_wanted",
        ".wishlist-button-add",
    ]
    PAGE_XPATH_ELEMENTS = [
        (By.XPATH, "//*[normalize-space()='Description']"),
        (By.XPATH, "//*[normalize-space()='Product Details']"),
    ]

    def open_card(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    def check_product_card_image(self):
        self.wait_element(self.PRODUCT_IMAGE)

    def check_css_elements(self):
        for selector in self.PAGE_CSS_ELEMENTS:
            self.wait_element(selector)

    def check_xpath_elements(self):
        for by, selector in self.PAGE_XPATH_ELEMENTS:
            self.wait_element(selector, by=by)
