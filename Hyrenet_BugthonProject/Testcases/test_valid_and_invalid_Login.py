"""
In this project, we will simulate and automate a valid login scenario from an HyreNet- Website with Selenium & Python.
Testcase-ID : TC_Valid_and_Invalid_Login_01
Successful user login into HyreNet Portal and
Unsuccessful user login into HyreNet portal
"""
# own package
from Data import data1
from Locator import locator1
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Exception
from selenium.common.exceptions import NoSuchElementException
# sleep
from time import sleep
# pytest
import pytest

# Defining a test cases
class Test_01:
    dashboard_url = "https://app.hyrenet.in/dashboard"
    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window and close the browser
        :return:None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data1.WebData().url)
        self.driver.maximize_window()
        yield
        # using yield keyword this block of code execute after function block of code executed
        self.driver.quit()

    def test_login(self, boot):
        """
            This method navigate to login page
            :param boot:
            :return:
        """
        try:
            self.driver.get(data1.WebData().url)
            self.driver.maximize_window()
            sleep(5)
            # getting from  input from the user
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().emailLocator, data1.WebData().email)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().passwordLocator, data1.WebData().password)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().signinLocator)
            sleep(3)
            assert (self.driver.current_url == self.dashboard_url)
            print("valid credentials")
            print("Testcase 1 : The user can logged in by use of valid email and valid password")
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().settingLocator)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().logoutLocator)
            sleep(5)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().emailLocator,
                                             data1.WebData().email)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().passwordLocator,
                                             data1.WebData().invalidpwd)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().signinLocator)
            sleep(3)
            assert (self.driver.current_url != self.dashboard_url)
            print("Invalid credentials")
            print("Testcase 2 : The user can't logged in by use of valid email  and Invalid password")
        except NoSuchElementException as e:
            print("Error:Element is not present in the webpage")



















