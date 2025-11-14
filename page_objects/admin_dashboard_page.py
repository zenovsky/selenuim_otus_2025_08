from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    TITLE = "Dashboard • PrestaShop"
    ADMIN_ICON = ".employee_name.dropdown-toggle"
    ADMIN_LOGOUT = "#header_logout"
    ADMIN_HEADER_SEARCH = "#bo_query"
    ADMIN_HEADER_SEARCH_DROPDOWN = (By.XPATH, "//button[contains(text(), 'Everywhere')]")
    ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG = 'a[data-item="Catalog"]'
    ADMIN_CATALOG_SUBMENU = "#subtab-AdminCatalog"
    ADMIN_CATALOG_PRODUCTS = "#subtab-AdminProducts"

    def open_admin_page(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    def check_admin_page_title(self):
        self.wait_title(self.TITLE)

    def check_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON)

    def check_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT)

    def click_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON).click()

    def click_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT).click()

    def check_admin_catalog_submenu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU)

    def click_admin_catalog_submemu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU).click()

    def click_admin_catalog_products(self):
        self.wait_element(self.ADMIN_CATALOG_PRODUCTS).click()

    def check_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH)

    def click_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH).click()

    def fill_admin_header_search(self, search):
        search_input = self.wait_element(self.ADMIN_HEADER_SEARCH)
        search_input.send_keys(search)

    def click_admin_header_search_dropdown(self):
        by, selector = self.ADMIN_HEADER_SEARCH_DROPDOWN
        self.wait_element(selector, by=by).click()

    def click_admin_header_search_dropdown_catalog(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG)
