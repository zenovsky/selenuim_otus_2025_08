import allure

from page_objects.account_page import AccountInfoPage
from page_objects.create_account_page import CreateAccountPage
from page_objects.main_page import MainPage
from utils.data_generator import default_generator


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Регистрация пользователя")
@allure.story("Сценарий создания пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_scenario(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.choose_gender("Mr")
    user_data = default_generator.generate_user_data()
    create_account.fill_customer_form("firstname", user_data["firstname"])
    create_account.fill_customer_form("lastname", user_data["lastname"])
    create_account.fill_customer_form("email", user_data["email"])
    create_account.fill_customer_form("password", user_data["password"])
    create_account.fill_customer_form("birthday", user_data["birthday"])
    create_account.click_checkbox_offers()
    create_account.click_checkbox_terms()
    create_account.click_checkbox_news()
    create_account.click_checkbox_privacy()
    create_account.click_save_button()

    main_page = MainPage(browser)
    main_page.click_user_info()

    account_info = AccountInfoPage(browser)
    account_info.click_information_link()
    account_info.verify_field_value("firstname", user_data["firstname"])
    account_info.verify_field_value("lastname", user_data["lastname"])
    account_info.verify_field_value("email", user_data["email"])
