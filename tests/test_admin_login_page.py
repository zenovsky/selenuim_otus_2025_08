from page_objects.admin_login_page import AdminLoginPage


def test_admin_login_title(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.open_admin_login()

def test_admin_stay_login(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.open_admin_login()
    admin_login_page.check_login_stay_checkbox()

def test_admin_css_elements(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.open_admin_login()
    admin_login_page.check_page_css_elements()
