from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class CurrencyChange(BasePage):
    PRICE_ELEMENT = ".product-miniature:first-child .price"
    CURRENCY_ELEMENT = ".hidden-sm-down.btn-unstyle"
    PRICE_EUR = "a[title='Euro]"
    PRICE_DOLLAR = "a[title='US Dollar']"

    @allure_attach_on_fail
    @log_action
    @allure_step("Получить текущую установленную валюту")
    def get_price_text(self):
        price = self.wait_element(self.PRICE_ELEMENT)
        return price.text.strip()

    @allure_attach_on_fail
    @log_action
    @allure_step("Вызвать выпадающий список для смены валюты")
    def click_currency_dropdown(self):
        self.wait_element(self.CURRENCY_ELEMENT).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Сменить валюту")
    def select_currency(self, currency_selector):
        self.wait_element(currency_selector).click()
