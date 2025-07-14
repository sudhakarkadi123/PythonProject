import pytest
from selenium.webdriver.chrome import webdriver


class BaseClass:

    def __init__(self,driver):
        self.driver = driver

    @pytest.fixture(scope="function")
    def getdriver(self):
        return self.driver

