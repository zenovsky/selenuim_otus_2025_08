from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


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

    @allure_attach_on_fail
    @log_action
    @allure_step("Открыть карточку товара")
    def open_card(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить заголовок страницы карточки товара")
    def check_title_product_card(self):
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("проверить наличие изображения товара")
    def check_product_card_image(self):
        self.wait_element(self.PRODUCT_IMAGE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить основные элементы страницы карточки товара")
    def check_css_elements(self):
        for selector in self.PAGE_CSS_ELEMENTS:
            self.wait_element(selector)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить основные элементы страницы карточки товара")
    def check_xpath_elements(self):
        for by, selector in self.PAGE_XPATH_ELEMENTS:
            self.wait_element(selector, by=by)
