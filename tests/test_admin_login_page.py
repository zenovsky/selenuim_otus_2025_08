import allure

from page_objects.login_admin_page import AdminLoginPage


@allure.epic("Страница логина администратора")
@allure.feature("Загрузка страницы логина администратора")
@allure.story("Проверка заголовка страницы логина администратора")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login_title(browser):
    admin_login = AdminLoginPage(browser)
    admin_login.open_admin_login()
    admin_login.check_admin_login_title()


@allure.epic("Страница логина администратора")
@allure.feature("Загрузка страницы логина администратора")
@allure.story("Проверка отображения кнопки 'Оставаться в системе'")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_stay_login(browser):
    admin_login = AdminLoginPage(browser)
    admin_login.open_admin_login()
    admin_login.check_login_stay_checkbox()


@allure.epic("Страница логина администратора")
@allure.feature("Загрузка страницы логина администратора")
@allure.story("Проверка отображения веб-элементов страницы логина администратора")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_css_elements(browser):
    admin_login = AdminLoginPage(browser)
    admin_login.open_admin_login()
    admin_login.check_page_css_elements()
