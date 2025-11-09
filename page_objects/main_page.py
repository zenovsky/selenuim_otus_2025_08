from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    TITLE = "PrestaShop"

    HEADER_ELEMENTS = [
        "#contact-link",
        "#_desktop_currency_selector",
        "#_desktop_user_info",
        "#category-3",
        "#category-6",
        "#category-9",
        "#search_widget",
    ]

    USER_INFO_LINK = "a[href$='/my-account']"


    PRODUCT_BLOCKS = [
        (By.XPATH, "//*[normalize-space()='Popular Products']"),
        (By.XPATH, "//*[normalize-space()='On sale']"),
        (By.XPATH, "//*[normalize-space()='New products']"),
    ]

    KEY_BLOCKS = [
        "#carousel",
        ".banner",
        "#custom-text",
        "#blockEmailSubscription_displayFooterBefore",
    ]

    FOOTER_ELEMENTS = [
        (By.XPATH, "//*[normalize-space()='Products']"),
        (By.XPATH, "//*[normalize-space()='Our company']"),
        (By.XPATH, "//*[normalize-space()='Your account']"),
        (By.XPATH, "//p[normalize-space()='Store information']"),
    ]


    def open_main(self):
        self.open("")
        self.wait_title(self.TITLE)

    def check_header_elements(self):
        for selector in self.HEADER_ELEMENTS:
            self.wait_element(selector)

    def check_product_blocks(self):
        for by, selector in self.PRODUCT_BLOCKS:
            self.wait_element(selector, by=by)

    def check_key_blocks(self):
        for selector in self.KEY_BLOCKS:
            self.wait_element(selector)

    def check_footer_elements(self):
        for by, selector in self.FOOTER_ELEMENTS:
            self.wait_element(selector, by=by)

    def click_user_info(self):
        self.wait_element(self.USER_INFO_LINK).click()




