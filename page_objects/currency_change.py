from page_objects.base_page import BasePage


class CurrencyChange(BasePage):
    PRICE_ELEMENT = ".product-miniature:first-child .price"
    CURRENCY_ELEMENT = ".hidden-sm-down.btn-unstyle"
    PRICE_EUR = "a[title='Euro]"
    PRICE_DOLLAR = "a[title='US Dollar']"

    def get_price_text(self):
        price = self.wait_element(self.PRICE_ELEMENT)
        return price.text.strip()

    def click_currency_dropdown(self):
        self.wait_element(self.CURRENCY_ELEMENT).click()

    def select_euro(self):
        self.wait_element(self.PRICE_EUR).click()

    def select_dollar(self):
        self.wait_element(self.PRICE_DOLLAR).click()
