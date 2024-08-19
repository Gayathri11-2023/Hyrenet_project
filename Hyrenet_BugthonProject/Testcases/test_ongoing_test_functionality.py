"""
In this project, we will simulate and automate a ongoing test scenario from an HyreNet- Website with Selenium & Python.
Testcase-ID : TC_ongoing_test_01,

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
class Testongoing:
    dashboard_url = "https://app.hyrenet.in/dashboard"

    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window and close the browser
        :return:None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data1.WebData().ongoingtestUrl)
        self.driver.maximize_window()

        yield
        # using yield keyword this block of code execute after function block of code executed
        self.driver.quit()
    def test_ongoingTest(self, boot):
        """
                        This method navigate to login page
                        :param boot:
                        :return:
        """
        try:
            self.driver.get(data1.WebData().ongoingtestUrl)
            self.driver.maximize_window()
            sleep(5)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().createnew_button_locator)
            sleep(3)

            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().fullnameLocator, data1.WebData().fullname)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().Email_locator, data1.WebData().Email)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().mobilenumberLocator, data1.WebData().mobilenumber)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().password_locator_test, data1.WebData().password_test)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().retype_password_locator, data1.WebData().retype_password)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().createNew_account_locator)
            sleep(3)
        except NoSuchElementException as e:
            print("Elements are not in present")


