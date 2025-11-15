from config import ADMIN_EMAIL, ADMIN_PASSWORD

from page_objects.admin_dashboard_page import AdminPage
from page_objects.admin_login_page import AdminLoginPage


def test_admin_login_logout_cycle(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.open_admin_login()
    admin_login_page.click_email_filed()
    admin_login_page.fill_email_form(ADMIN_EMAIL)
    admin_login_page.click_passwd_filed()
    admin_login_page.fill_passwd_form(ADMIN_PASSWORD)
    admin_login_page.click_login()

    admin_page = AdminPage(browser)
    admin_page.check_admin_page_title()
    admin_page.click_admin_dropdown_toggle()
    admin_page.click_admin_logout_button()
    admin_login_page.check_admin_login_title()


