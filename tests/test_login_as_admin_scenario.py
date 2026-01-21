import allure

from config import ADMIN_EMAIL, ADMIN_PASSWORD
from page_objects.admin_page import AdminPage
from page_objects.login_admin_page import AdminLoginPage


@allure.epic("Страница логина администратора")
@allure.feature("Логин под УЗ адмнистратора")
@allure.story("Сценарий логина по УЗ адмнистратора")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login_logout_cycle(browser):
    admin_login = AdminLoginPage(browser)
    admin_login.open_admin_login()
    admin_login.fill_login_forms("#email", ADMIN_EMAIL)
    admin_login.fill_login_forms("#passwd", ADMIN_PASSWORD)
    admin_login.click_login()

    admin_page = AdminPage(browser)
    admin_page.check_admin_page_title()
    admin_page.click_admin_dropdown_toggle()
    admin_page.click_admin_logout_button()

    admin_login = AdminLoginPage(browser)
    admin_login.check_admin_login_title()
