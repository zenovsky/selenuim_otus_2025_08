from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url or getattr(driver, "base_url", "")
        self.wait = WebDriverWait(self.driver, 6)

    def open(self, url=""):
        self.driver.get(f"{self.base_url}{url}")

    def wait_title(self, title, timeout=6):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(f"Ждал title '{title}', но был '{self.driver.title}'")

    def wait_element(self, selector, timeout=10, by=By.CSS_SELECTOR):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, selector))
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {selector}")

    def switch_to_frame(self, locator_tuple):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator_tuple))
        except TimeoutException:
            raise AssertionError(f"Не дождался iframe и не смог переключиться: {locator_tuple}")

    def switch_back_to_default_content(self):
        self.driver.switch_to.default_content()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
