import pytest
import BaseClass

class TestLoginPage():

    def test_login_page(self,driver):
        self.driver = driver
        self.driver.get("http://localhost/litecart/")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("<PASSWORD>")
        self.driver.find_element_by_name("login").click()







