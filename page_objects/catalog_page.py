from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class CatalogPage(BasePage):
    PAGE_URL = "/2-home"
    TITLE = "Home"
    CATEGORIES_LINKS = [
        (By.CSS_SELECTOR, "a[href$='/3-clothes']"),
        (By.CSS_SELECTOR, "a[href$='/6-accessories']"),
        (By.CSS_SELECTOR, "a[href$='/9-art']"),
    ]
    FILTER_SUPPLIERS_LINKS = [
        (By.CSS_SELECTOR, "a[href$='/supplier/2-accessories-supplier']"),
        (By.CSS_SELECTOR, "a[href$='/supplier/1-fashion-supplier']"),
    ]
    FILTER_BRANDS_LINKS = [
        (By.CSS_SELECTOR, "a[href$='/brands']"),
        (By.CSS_SELECTOR, "a[href$='/brand/2-graphic-corner']"),
        (By.CSS_SELECTOR, "a[href$='/brand/1-studio-design']"),
    ]
    PRODUCT_LIST_CONTENT = [
        ".btn-unstyle.select-title",
        ".wishlist-button-add",
        ".next.js-search-link",
    ]
    FILTER_BRANDS = "#search_filters_brands"
    FILTER_SUPPLIERS = "#search_filters_suppliers"
    SEARCH_FILTERS = "#search_filters"
    SUBCATEGORIES = "#subcategories"
    PRODUCT_LIST = ".products.row"

    @allure_attach_on_fail
    @log_action
    @allure_step("Открыть страницу каталога")
    def open_catalog(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить заголовок страницы каталога")
    def check_catalog_title(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    allure_attach_on_fail

    @log_action
    @allure_step("Проверить наличие выбора категорий каталога")
    def check_categories_links(self):
        for by, selector in self.CATEGORIES_LINKS:
            self.wait_element(selector, by=by)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие фильтра по поставщикам")
    def check_filters_suppliers(self):
        self.wait_element(self.FILTER_SUPPLIERS)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие выбора поставщиков")
    def check_filters_suppliers_links(self):
        for by, selector in self.FILTER_SUPPLIERS_LINKS:
            self.wait_element(selector, by=by)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие фильтра по брендам")
    def check_filters_brands(self):
        self.wait_element(self.FILTER_BRANDS)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие выбора брендов")
    def check_filters_brands_links(self):
        for by, selector in self.FILTER_BRANDS_LINKS:
            self.wait_element(selector, by=by)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие фильтров поиска")
    def check_search_filters(self):
        self.wait_element(self.SEARCH_FILTERS)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие подкатегорий")
    def check_subcategories(self):
        self.wait_element(self.SUBCATEGORIES)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие списка товаров")
    def check_products_list(self):
        self.wait_element(self.PRODUCT_LIST)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие основного контента на странице")
    def check_products_list_content(self):
        for selector in self.PRODUCT_LIST_CONTENT:
            self.wait_element(selector)
