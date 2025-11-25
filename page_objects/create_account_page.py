from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class CreateAccountPage(BasePage):
    PAGE_URL = "/registration"
    TITLE = "Registration"
    LOGIN_LINK = "a[href$='/login']"
    GENDERS_RADIO_BUTTON = [
        "label[for='field-id_gender-1']",
        "label[for='field-id_gender-2']",
    ]
    GENDER_IDS = {
        "mr": 1,
        "mrs": 2
    }
    GENDER_LABEL_TEMPLATE = "label[for='field-id_gender-{gender_id}']"
    FIELDS_MAP = {
        "firstname": "#field-firstname",
        "lastname": "#field-lastname",
        "email": "#field-email",
        "password": "#field-password",
        "birthday": "#field-birthday",
    }
    REGISTRATION_CHECKBOX_OFFERS = (By.XPATH, "//input[@name='optin']/ancestor::label[1]")
    REGISTRATION_CHECKBOX_TERMS = (By.XPATH, "//input[@name='psgdpr']/ancestor::label[1]")
    REGISTRATION_CHECKBOX_NEWS = (By.XPATH, "//input[@name='newsletter']/ancestor::label[1]")
    REGISTRATION_CHECKBOX_PRIVACY = (By.XPATH, "//input[@name='customer_privacy']/ancestor::label[1]")
    SAVE_ACCOUNT_BUTTON = "button[data-link-action='save-customer']"

    @allure_attach_on_fail
    @log_action
    @allure_step("Открыть страницу создания аккаунта")
    def open_create_account(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить заголовок страницы создания аккаунта")
    def check_create_account_page_title(self):
        self.open(self.PAGE_URL)
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие сслыки для входа в аккаунт")
    def check_login_link(self):
        self.wait_element(self.LOGIN_LINK)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие чек-бокса выбора пола")
    def check_genders_radio(self):
        for selector in self.GENDERS_RADIO_BUTTON:
            self.wait_element(selector)

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие полей регистрации")
    def check_registration_fields(self):
        for field_name, selector in self.FIELDS_MAP.items():
            try:
                self.wait_element(selector)
            except Exception:
                raise AssertionError(f"Поле регистрации '{field_name}' "
                                     f"с селектором '{selector}' не найдено или не видимо!")

    @allure_attach_on_fail
    @log_action
    @allure_step("Проверить наличие кнопки сохранения созданного аккаунта")
    def check_save_button(self):
        self.wait_element(self.SAVE_ACCOUNT_BUTTON)

    @allure_attach_on_fail
    @log_action
    @allure_step("Выбрать пол пользователя установив чек-бокс")
    def choose_gender(self, gender_name: str):
        try:
            gender_id = self.GENDER_IDS[gender_name.lower()]
        except KeyError:
            raise ValueError(f"Неверное имя гендера: '{gender_name}'. Используйте 'Mr' или 'Mrs'.")
        final_selector = self.GENDER_LABEL_TEMPLATE.format(gender_id=gender_id)
        gender_label = self.wait_element(final_selector)
        gender_label.click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Заполнить поля регистрации пользователя")
    def fill_customer_form(self, field_name: str, value: str):
        selector = self.FIELDS_MAP[field_name.lower()]
        field_element = self.wait_element(selector)
        field_element.clear()
        field_element.send_keys(value)

    @allure_attach_on_fail
    @log_action
    @allure_step("Установить чек-бокс 'Получайте предложения от наших партнеров'")
    def click_checkbox_offers(self):
        by, selector = self.REGISTRATION_CHECKBOX_OFFERS
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Установить чек-бокс 'Принять условия и  политику конфиденциальности'")
    def click_checkbox_terms(self):
        by, selector = self.REGISTRATION_CHECKBOX_TERMS
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Установить чек-бокс 'Подпишитесь на нашу рассылку'")
    def click_checkbox_news(self):
        by, selector = self.REGISTRATION_CHECKBOX_NEWS
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Установить чек-бокс 'Конфиденциальность данных клиентов'")
    def click_checkbox_privacy(self):
        by, selector = self.REGISTRATION_CHECKBOX_PRIVACY
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Нажать кнопку сохранить и создать аккаунт")
    def click_save_button(self, click=True, scroll=True):
        save_button = self.wait_element(self.SAVE_ACCOUNT_BUTTON)
        if scroll:
            self.scroll_to_element(save_button)
        if click:
            save_button.click()
