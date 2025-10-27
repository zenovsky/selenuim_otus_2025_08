import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FFOption
from selenium.webdriver.edge.options import Options as EdgeOption


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
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "ff":
        options = FFOption()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    elif browser_name == 'edge':
        options = EdgeOption()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options) 
    else:
        raise ValueError(f"Driver for {browser_name} not supported")
    
    driver.base_url = base_url

    yield driver

    driver.quit()