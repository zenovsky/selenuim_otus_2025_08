from config import ADMIN_EMAIL, ADMIN_PASSWORD

from page_objects.admin_catalog_products_page import AdminCatalogProductsPage
from page_objects.admin_dashboard_page import AdminPage
from page_objects.admin_login_page import AdminLoginPage


def test_add_product_scenario(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.open_admin_login()
    admin_login_page.click_email_filed()
    admin_login_page.fill_email_form(ADMIN_EMAIL)
    admin_login_page.click_passwd_filed()
    admin_login_page.fill_passwd_form(ADMIN_PASSWORD)
    admin_login_page.click_login()

    admin_page = AdminPage(browser)
    admin_page.check_admin_page_title()
    admin_page.click_admin_catalog_submemu()
    admin_page.click_admin_catalog_products()

    admin_products_page = AdminCatalogProductsPage(browser)
    admin_products_page.click_product_filter_search_input()
    admin_products_page.clear_product_filter_search_input()
    admin_products_page.fill_product_filter_search_input("TEST PRODUCT")
    admin_products_page.click_product_filter_search_button()
    admin_products_page.click_product_bulk_checkbox()
    admin_products_page.click_product_bulk_dropdown()
    admin_products_page.click_product_action_delete()
    admin_products_page.click_product_delete()
    admin_products_page.click_close_action_modale()
    assert "Successful deletion" in admin_products_page.check_delete_success_alert().text, "Продукт не был удалён."
