import time
import pytest
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="function")
def load_data():
    with open("test_data.json") as f:
        jsondata = json.load(f)
        yield jsondata

@pytest.fixture(scope="function")
def setup_module():
    driver = webdriver.Chrome()
    print("Opening Browser")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://google.com")
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify browser: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run browser in headless mode"
    )
@pytest.fixture(scope="function")
def driver_make(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless") # Get the boolean value of the --headless flag

    print(f"\n[Fixture] Initializing {browser_name} browser (headless: {headless_mode})...")

    driver_instance = None
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        if headless_mode:
            chrome_options.add_argument("--headless=new") # For newer Chrome versions
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
        driver_instance = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        if headless_mode:
            firefox_options.add_argument("-headless") # Firefox uses a different headless flag syntax
        driver_instance = webdriver.Firefox(options=firefox_options)
    elif browser_name == "edge":
        edge_options = EdgeOptions()
        if headless_mode:
            edge_options.add_argument("--headless=new")
            edge_options.add_argument("--disable-gpu")
        driver_instance = webdriver.Edge(options=edge_options)
    else:
        pytest.fail(f"Unsupported browser: {browser_name}")

    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)

    yield driver_instance

    print(f"\n[Fixture] Quitting {browser_name} browser...")
    driver_instance.quit()

@pytest.fixture(scope="function", params=["chrome", "firefox", "edge"])
def setup_browsers(request):
    """
    Parameterized WebDriver fixture that sets up and tears down a browser instance
    for each test function, for each browser specified in params.
    """
    browser_name = request.param # Get the current browser name from the parametrize list

    print(f"\n[Fixture] Setting up {browser_name} browser...")

    if browser_name == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser_name == "firefox":
        driver_instance = webdriver.Firefox()
    elif browser_name == "edge":
        driver_instance = webdriver.Edge()
    else:
        print("Exception")
        raise ValueError(f"Unsupported browser: {browser_name}")



    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10) # Implicit wait for elements
    driver_instance.get("http://google.com")
    yield driver_instance # Yield the driver instance to the test function

    print(f"\n[Fixture] Quitting {browser_name} browser...")
    driver_instance.quit()








