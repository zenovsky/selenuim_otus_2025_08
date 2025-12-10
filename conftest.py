import logging
import allure

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
    parser.addoption("--executor", default= 'local')
    parser.addoption("--vnc", action='store_true', default=True)
    parser.addoption("--video", action='store_true', default=False)
    parser.addoption("--browser_version", default=None)

@pytest.fixture(scope="module", autouse=True)
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    version = request.config.getoption("--browser_version")

    if executor != 'local':
        host = "localhost" if executor == 'selenoid' else executor
        executor_url = f"http://{host}/wd/hub"

        driver = _selenoid_driver(
            browser_name=browser_name, 
            executor_url=executor_url, 
            vnc=vnc, 
            video=video,
            version=version
        )        
    else:
        driver = _local_driver(browser_name, headless)

    driver.base_url = base_url

    yield driver

    driver.quit()

def _local_driver(browser_name, headless):         
    if browser_name == "ch":
        options = ChromeOption()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    elif browser_name == "ff":
        options = FFOption()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        else:
            options.add_argument("--start-maximized")
        return webdriver.Firefox(options=options)
    elif browser_name == 'edge':
        options = EdgeOption()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Driver for {browser_name} not supported")
    
def _selenoid_driver(browser_name, executor_url, vnc=True, video=False, version=None):
    options = None
    if browser_name == "ch":
        options = ChromeOption()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
    elif browser_name == "ff":
        options = FFOption()
        options.add_argument("--start-maximized")
    elif browser_name == "edge":
        options = EdgeOption()
        options.add_argument("--start-maximized")
    else:
        raise ValueError(f"Driver for {browser_name} not supported in Selenoid configuration")
    
    selenoid_capabilities = {
        "enableVNC": vnc,
        "enableVideo": video 
    }

    options.set_capability("selenoid:options", selenoid_capabilities)

    if version:
        options.set_capability("browserVersion", version)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )
    
    return driver

def pytest_runtest_call(item):
    browser_name = item.config.getoption("--browser")
    allure.dynamic.title(f"{item.name} [{browser_name}]")  
