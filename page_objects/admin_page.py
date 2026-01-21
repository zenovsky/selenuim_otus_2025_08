from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class AdminPage(BasePage):
    TITLE = "Dashboard • PrestaShop"
    ADMIN_ICON = ".employee_name.dropdown-toggle"
    ADMIN_LOGOUT = "#header_logout"
    ADMIN_HEADER_SEARCH = "#bo_query"
    ADMIN_HEADER_SEARCH_DROPDOWN = (By.XPATH, "//button[contains(text(), 'Everywhere')]")
    ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG = 'a[data-item="Catalog"]'
    ADMIN_CATALOG_SUBMENU = "#subtab-AdminCatalog"
    ADMIN_CATALOG_PRODUCTS = "#subtab-AdminProducts"

    @allure_attach_on_fail
    @log_action
    @allure_step("Открылась страница администратора")
    def check_admin_page_title(self):
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие иконки администратора")
    def check_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие кнопки выхода из страницы администратора")
    def check_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT)

    @allure_attach_on_fail
    @log_action
    @allure_step("Нажать на иконку администратора")
    def click_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Выйти из страницы администратора")
    def click_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT).click()

    allure_attach_on_fail

    @log_action
    @allure_step("Проверить наличие сабменю каталога")
    def check_admin_catalog_submenu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU)

    @allure_attach_on_fail
    @log_action
    @allure_step("Перейти в сабменю каталога")
    def click_admin_catalog_submemu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Перейти в раздел товары")
    def click_admin_catalog_products(self):
        self.wait_element(self.ADMIN_CATALOG_PRODUCTS).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие поля поиска в хэдере страницы администратора")
    def check_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH)

    @allure_attach_on_fail
    @log_action
    @allure_step("Нажать на поле поиска в хэдере страницы администратора")
    def click_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Заполнить поле поиска в хэдере страницы администратора")
    def fill_admin_header_search(self, search):
        search_input = self.wait_element(self.ADMIN_HEADER_SEARCH)
        search_input.send_keys(search)

    @allure_attach_on_fail
    @log_action
    @allure_step("Начать поиск из хэдера страницы администратора")
    def click_admin_header_search_dropdown(self):
        by, selector = self.ADMIN_HEADER_SEARCH_DROPDOWN
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("В выпадающем списке поиска в хэдере выбрать 'Товары'")
    def click_admin_header_search_dropdown_catalog(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG)
