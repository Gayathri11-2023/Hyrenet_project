"""
In this project, we will simulate and automate a create test scenario from an HyreNet- Website with Selenium & Python.
Testcase-ID : TC_createTest_01,

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

class Testcreate:
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
    def test_createTest(self, boot):
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
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().passwordLocator,
                                             data1.WebData().password)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().signinLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().testLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().createTestLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().selectthis_locator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().saveandconLocator)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().testname_locator,
                                             data1.WebData().testnameLocator)
            sleep(2)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().testPeriod_locator)
            sleep(2)
            #locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().testPeriod_datechoosen_locator)
            #sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().applybutton_Locator)
            sleep(2)
            locator1.WebLocators().entertext_by_xpath(self.driver, locator1.WebLocators().jobdescription_locator,
                                             data1.WebData().testdescription)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().saveandsubmit_Locator)
            sleep(2)

        except NoSuchElementException as e:
            print("Elements are not in present")
