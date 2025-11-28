import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.edge.options import Options as EdgeOption
from selenium.webdriver.firefox.options import Options as FFOption

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test.log")
    ]
)

def pytest_addoption(parser):
    parser.addoption("--browser", default='ch')
    parser.addoption("--headless", action='store_true')
    parser.addoption("--url", default='http://localhost:8081')

@pytest.fixture(scope="module", autouse=True)
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")

    if browser_name == "ch":
        options = ChromeOption()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "ff":
        options = FFOption()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        else:
            options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    elif browser_name == 'edge':
        options = EdgeOption()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Driver for {browser_name} not supported")

    driver.base_url = base_url

    yield driver

    driver.quit()
