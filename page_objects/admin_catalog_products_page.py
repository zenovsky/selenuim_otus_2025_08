from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_objects.base_page import BasePage


class AdminCatalogProductsPage(BasePage):
    ADD_NEW_PRODUCT_BUTTON = "#page-header-desc-configuration-add"
    MODAL_ADD_PRODUCT_IFRAME = (By.NAME, "modal-create-product-iframe")
    MODAL_ADD_NEW_PRODUCT_BUTTON = "#create_product_create"
    PRODUCT_FILTER_SEARCH_INPUT = "#product_name"
    PRODUCT_FILTER_SEARCH_BUTTON = ".btn.btn-primary.grid-search-button"
    PRODUCT_BULK_CHECKBOX = ".bulk_action-type.column-bulk"
    PRODUCT_BULK_ACTION_DROPDOWN = ".btn.btn-outline-secondary.dropdown-toggle.js-bulk-actions-btn"
    PRODUCT_BULK_ACTION_DELETE = "#product_grid_bulk_action_bulk_delete_ajax"
    MODAL_BULK_ACTION_DELETE_BUTTON = ".btn.btn-primary.btn-lg.btn-confirm-submit"
    MODAL_BULK_ACTION_CLOSE_BUTTON = ".btn.btn-primary.btn-lg.close-modal-button"
    PRODUCT_DELETE_SUCCESS_ALERT = (By.XPATH, "//div[@class='alert-text']/p[contains(text(), 'Successful deletion')]")
    PRODUCT_HEADER_NAME = "#product_header_name_1"
    PRODUCT_PRICING_TAB= "#product_pricing-tab-nav"
    RETAIL_PRICE_INPUT = "#product_pricing_retail_price_price_tax_excluded"
    PRODUCT_SAVE_BUTTON = "#product_footer_save"
    PRODUCT_ADD_SUCCESS_ALERT = (By.XPATH, "//div[@class='alert-text']/p[contains(text(), 'Successful update')]")

    def click_add_new_product_button(self):
        self.wait_element(self.ADD_NEW_PRODUCT_BUTTON).click()

    def click_product_filter_search_input(self):
        self.wait_element(self.PRODUCT_FILTER_SEARCH_INPUT).click()

    def clear_product_filter_search_input(self):
        self.wait_element(self.PRODUCT_FILTER_SEARCH_INPUT).clear()

    def fill_product_filter_search_input(self, product_name):
        product_name_input = self.wait_element(self.PRODUCT_FILTER_SEARCH_INPUT)
        product_name_input.send_keys(product_name)

    def click_product_filter_search_button(self):
        self.wait_element(self.PRODUCT_FILTER_SEARCH_BUTTON).click()

    def click_product_bulk_checkbox(self):
        self.wait_element(self.PRODUCT_BULK_CHECKBOX).click()

    def click_product_bulk_dropdown(self):
        self.wait_element(self.PRODUCT_BULK_ACTION_DROPDOWN).click()

    def click_product_action_delete(self):
        self.wait_element(self.PRODUCT_BULK_ACTION_DELETE).click()

    def click_product_delete(self):
        self.wait_element(self.MODAL_BULK_ACTION_DELETE_BUTTON).click()

    def click_close_action_modale(self):
        self.wait_element(self.MODAL_BULK_ACTION_CLOSE_BUTTON).click()

    def check_delete_success_alert(self):
        by, selector = self.PRODUCT_DELETE_SUCCESS_ALERT
        return self.wait_element(selector, by=by)

    def switch_to_modal_iframe(self):
        self.switch_to_frame(self.MODAL_ADD_PRODUCT_IFRAME)

    def click_modal_add_new_product_button(self):
        self.wait_element(self.MODAL_ADD_NEW_PRODUCT_BUTTON).click()

    def click_product_header_name(self):
        self.wait_element(self.PRODUCT_HEADER_NAME).click()

    def fill_product_name(self, product_name):
        product_name_input = self.wait_element(self.PRODUCT_HEADER_NAME)
        product_name_input.send_keys(product_name)

    def click_product_pricing(self):
        self.wait_element(self.PRODUCT_PRICING_TAB).click()

    def click_retail_price_input(self):
        self.wait_element(self.RETAIL_PRICE_INPUT).click()

    def clear_retail_price_input(self):
        price_input = self.wait_element(self.RETAIL_PRICE_INPUT)
        price_input.send_keys(Keys.CONTROL + "a")
        price_input.send_keys(Keys.DELETE)

    def fill_retail_price_input(self, retail_price):
        retail_price_input = self.wait_element(self.RETAIL_PRICE_INPUT)
        retail_price_input.send_keys(retail_price)

    def click_save_button(self):
        self.wait_element(self.PRODUCT_SAVE_BUTTON).click()

    def check_success_alert(self):
        by, selector = self.PRODUCT_ADD_SUCCESS_ALERT
        return self.wait_element(selector, by=by)





