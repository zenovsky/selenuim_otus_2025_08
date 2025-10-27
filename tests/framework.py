from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))


def wait_element(selector, driver, timeout=3, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, selector)))
    except TimeoutException:
        raise AssertionError("Не дождался видимости элемента: {}".format(selector)) 