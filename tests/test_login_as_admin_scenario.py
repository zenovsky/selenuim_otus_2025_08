from framework import wait_title, wait_element
from selenium.webdriver.common.by import By
from config import ADMIN_EMAIL, ADMIN_PASSWORD


def test_admin_login_logout_cycle(browser):
    browser.get(f'{browser.base_url}/administration')
    wait_title("PrestaShop", browser)
    email_input = wait_element("#email", browser) 
    email_input.send_keys(ADMIN_EMAIL)
    password_input = wait_element("#passwd", browser) 
    password_input.send_keys(ADMIN_PASSWORD) 
    wait_element("#submit_login", browser).click()
    wait_title("Dashboard • PrestaShop", browser)
    wait_element(".employee_name.dropdown-toggle", browser).click()
    wait_element("#header_logout", browser).click()
    wait_title("PrestaShop", browser)
    

