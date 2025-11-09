from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


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


    def open_catalog(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    def check_categories_links(self):
        for by, selector in self.CATEGORIES_LINKS:
            self.wait_element(selector, by=by)

    def check_filters_suppliers(self):
        self.wait_element(self.FILTER_SUPPLIERS)

    def check_filters_suppliers_links(self):
        for by, selector in self.FILTER_SUPPLIERS_LINKS:
            self.wait_element(selector, by=by)

    def check_filters_brands(self):
        self.wait_element(self.FILTER_BRANDS)

    def check_filters_brands_links(self):
        for by, selector in self.FILTER_BRANDS_LINKS:
            self.wait_element(selector, by=by)

    def check_search_filters(self):
        self.wait_element(self.SEARCH_FILTERS)

    def check_subcategories(self):
        self.wait_element(self.SUBCATEGORIES)

    def check_products_list(self):
        self.wait_element(self.PRODUCT_LIST)

    def check_products_list_content(self):
        for selector in self.PRODUCT_LIST_CONTENT:
            self.wait_element(selector)
