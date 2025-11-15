from page_objects.base_page import BasePage


class AccountInfoPage(BasePage):
    ACCOUNT_INFORMATION_LINK = "#identity-link"
    FIELDS_MAP = {
        "firstname": "#field-firstname",
        "lastname": "#field-lastname",
        "email": "#field-email",
        "password": "#field-password",
        "birthday": "#field-birthday",
    }

    def click_information_link(self):
        self.wait_element(self.ACCOUNT_INFORMATION_LINK).click()

    def verify_field_value(self, field_name: str, expected_value: str):
        try:
            selector = self.FIELDS_MAP[field_name.lower()]
        except KeyError:
            raise ValueError(f"Неизвестное поле: '{field_name}'")

        FIELD_LOCATOR = (selector)

        field_element = self.wait_element(FIELD_LOCATOR)

        actual_value = field_element.get_attribute("value")

        if actual_value == expected_value:
            print(f"Проверка успешна: Поле '{field_name}' содержит ожидаемое значение '{expected_value}'.")
        else:
            raise AssertionError(
                f"Ошибка проверки поля '{field_name}'. "
                f"Ожидалось: '{expected_value}', Фактическое: '{actual_value}'"
            )



