import allure

from page_objects.create_account_page import CreateAccountPage


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Загрузка страницы создания аккаунта пользователя")
@allure.story("Проверка отображения загаловка страницы создания аккаунта")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_title(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.check_create_account_page_title()


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Загрузка страницы создания аккаунта пользователя")
@allure.story("Проверка отображения сслыки на вход если аккаунт уже есть")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_login_link(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.check_login_link()


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Загрузка страницы создания аккаунта пользователя")
@allure.story("Проверка отображения кнопки выбора пола пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_gender_radio(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.check_genders_radio()


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Загрузка страницы создания аккаунта пользователя")
@allure.story("Проверка отображения полей ввода информации о пользователе")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_regestry_fields(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.check_registration_fields()


@allure.epic("Страница создания аккаунта пользователя")
@allure.feature("Загрузка страницы создания аккаунта пользователя")
@allure.story("Проверка отображения кнопки создания аккаунта пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account_save_button(browser):
    create_account = CreateAccountPage(browser)
    create_account.open_create_account()
    create_account.check_save_button()
