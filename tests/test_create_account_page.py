from page_objects.create_account_page import CreateAccountPage


def test_create_account_title(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()

def test_create_account_login_link(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()
    create_account_page.check_login_link()

def test_create_account_gender_radio(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()
    create_account_page.check_genders_radio()

def test_create_account_regestry_fields(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()
    create_account_page.check_registration_fields()

def test_create_account_save_button(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()
    create_account_page.check_save_button()
