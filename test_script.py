import pytest
import json
from selenium import webdriver

def data_te():
    # test_data = load_data()
    with open("test_data.json") as f:
        test_data = json.load(f)
        return test_data


@pytest.mark.parametrize("data",data_te())
def test_invoking(driver_make,data):

    print("After assigning the values")
    print(data)
    # driver = webdriver.Chrome()
    # print("Opening Browser")
    # driver.implicitly_wait(30)
    # driver.maximize_window()
    # driver.get("http://google.com")
    driver = driver_make
    driver.get("http://google.com")

    assert "Google" in driver.title
    print("test_Invoking")
    # Access parameters from the 'test_case' dictionary
    username = data['username']
    password = data['password']
    print("username " + username)
    print("password " + password)


def test_invoking123(driver_make):

    driver = driver_make #webdriver.Chrome()
    print("Opening Browser")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://google.com")
    assert "Google" in driver.title


