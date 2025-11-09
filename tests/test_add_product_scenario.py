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
    admin_products_page.click_add_new_product_button()
    admin_products_page.switch_to_modal_iframe()
    admin_products_page.click_modal_add_new_product_button()
    admin_products_page.switch_back_to_default_content()
    admin_products_page.click_product_header_name()
    admin_products_page.fill_product_name("TEST PRODUCT")
    admin_products_page.click_product_pricing()
    admin_products_page.click_retail_price_input()
    admin_products_page.clear_retail_price_input()
    admin_products_page.fill_retail_price_input("42")
    admin_products_page.click_save_button()
    admin_products_page.check_success_alert()
    assert "Successful update" in admin_products_page.check_success_alert().text, "Продукт не был создан."
