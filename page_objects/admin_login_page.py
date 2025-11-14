from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminLoginPage(BasePage):
    PAGE_URL = "/administration"
    TITLE = "PrestaShop"
    PAGE_CSS_ELEMENTS = [
        "#login_form",
        "#email",
        "#passwd",
        "#submit_login",
        "#forgot-password-link",
    ]
    LOGIN_STAY_CHECKBOX = (By.XPATH, "//*[normalize-space()='Stay logged in']")


    def open_admin_login(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    def check_admin_login_title(self):
        self.wait_title(self.TITLE)

    def check_login_stay_checkbox(self):
        by, selector = self.LOGIN_STAY_CHECKBOX
        self.wait_element(selector, by=by)

    def check_page_css_elements(self):
        for selector in self.PAGE_CSS_ELEMENTS:
            self.wait_element(selector)

    def fill_email_form(self, email):
        email_input = self.wait_element("#email")
        email_input.send_keys(email)

    def fill_passwd_form(self,password):
        password_input = self.wait_element("#passwd")
        password_input.send_keys(password)

    def click_email_filed(self):
        self.wait_element("#email").click()

    def click_passwd_filed(self):
        self.wait_element("#passwd").click()

    def click_login(self):
        self.wait_element("#submit_login").click()
