import pytest
import BaseClass

class TestLoginPage():

    def test_login_page(self,setup_browsers):
        driver = setup_browsers
        driver.get("http://localhost/litecart/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("<PASSWORD>")
        driver.find_element_by_name("login").click()







