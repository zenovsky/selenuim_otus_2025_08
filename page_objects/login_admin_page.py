from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


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

    @allure_attach_on_fail
    @log_action
    @allure_step("Открыть страницу логина администратора")
    def open_admin_login(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверка заголовка страницы логина администратора")
    def check_admin_login_title(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить чек-бокс 'Не выходить из системы'")
    def check_login_stay_checkbox(self):
        by, selector = self.LOGIN_STAY_CHECKBOX
        self.wait_element(selector, by=by)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить основные элементы страницы")
    def check_page_css_elements(self):
        for selector in self.PAGE_CSS_ELEMENTS:
            self.wait_element(selector)

    @allure_attach_on_fail
    @log_action
    @allure_step("Ввести логин и пароль администратора")
    def fill_login_forms(self, selector, value=None):
        element = self.wait_element(selector)
        element.click()
        if value is not None:
            element.send_keys(value)

    @allure_attach_on_fail
    @log_action
    @allure_step("Нажать кнопку войти")
    def click_login(self):
        self.wait_element("#submit_login").click()
