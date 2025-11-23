import allure

from config import ADMIN_EMAIL, ADMIN_PASSWORD
from page_objects.admin_catalog_products_page import AdminCatalogProductsPage
from page_objects.admin_page import AdminPage
from page_objects.login_admin_page import AdminLoginPage


@allure.epic("Страница администратора")
@allure.feature("Редактирование каталога товаров")
@allure.story("Сценарий добавления нового товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_scenario(browser):
    admin_login = AdminLoginPage(browser)
    admin_login.open_admin_login()
    admin_login.fill_login_forms("#email", ADMIN_EMAIL)
    admin_login.fill_login_forms("#passwd", ADMIN_PASSWORD)
    admin_login.click_login()

    admin_page = AdminPage(browser)
    admin_page.check_admin_page_title()
    admin_page.click_admin_catalog_submemu()
    admin_page.click_admin_catalog_products()

    admin_page_catalog = AdminCatalogProductsPage(browser)
    admin_page_catalog.click_add_new_product_button()
    admin_page_catalog.switch_to_modal_iframe()
    admin_page_catalog.click_modal_add_new_product_button()
    admin_page_catalog.switch_back_to_default_content()
    admin_page_catalog.click_product_header_name()
    admin_page_catalog.fill_product_name("TEST PRODUCT")
    admin_page_catalog.click_product_pricing()
    admin_page_catalog.set_retail_price("42")
    admin_page_catalog.click_save_button()
    alert = admin_page_catalog.check_success_alert()
    assert "Successful update" in alert.text, "Продукт не был создан."
