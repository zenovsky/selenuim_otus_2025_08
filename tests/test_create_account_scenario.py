from data_generator import default_generator

from page_objects.account_info_page import AccountInfoPage
from page_objects.create_account_page import CreateAccountPage
from page_objects.main_page import MainPage


def test_create_account_scenario(browser):
    create_account_page = CreateAccountPage(browser)
    create_account_page.open_create_account()
    create_account_page.choose_gender("Mr")
    user_data = default_generator.generate_user_data()
    create_account_page.fill_customer_form("firstname", user_data["firstname"])
    create_account_page.fill_customer_form("lastname", user_data["lastname"])
    create_account_page.fill_customer_form("email", user_data["email"])
    create_account_page.fill_customer_form("password", user_data["password"])
    create_account_page.fill_customer_form("birthday", user_data["birthday"])
    create_account_page.click_checkbox_offers()
    create_account_page.click_checkbox_terms()
    create_account_page.click_checkbox_news()
    create_account_page.click_checkbox_privacy()
    save_button = create_account_page.scroll_to_save_button()
    save_button.click()
    main_page = MainPage(browser)
    main_page.click_user_info()
    account_info_page = AccountInfoPage(browser)
    account_info_page.click_information_link()
    account_info_page.verify_field_value("firstname", user_data["firstname"])
    account_info_page.verify_field_value("lastname", user_data["lastname"])
    account_info_page.verify_field_value("email", user_data["email"])



