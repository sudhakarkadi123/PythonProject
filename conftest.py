import time
import pytest
from selenium import webdriver
import json

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
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10) # Implicit wait for elements
    driver_instance.get("http://google.com")
    yield driver_instance # Yield the driver instance to the test function

    print(f"\n[Fixture] Quitting {browser_name} browser...")
    driver_instance.quit()








