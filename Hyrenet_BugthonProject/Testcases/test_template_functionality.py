"""
In this project, we will simulate and automate a template scenario from an HyreNet- Website with Selenium & Python.
Testcase-ID : TC_template_01,

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


class Test_template:
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

    def test_template_functionality(self, boot):
        """
            This method navigate to login page
            :param boot:
            :return:
        """
        try:
            self.driver.get(data1.WebData().url)
            self.driver.maximize_window()
            sleep(20)
            # getting from  input from the user
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().emailLocator, data1.WebData().email)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().passwordLocator, data1.WebData().password)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().signinLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().templateLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().createLocator)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().selectrole_inputLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().testengineerLocator)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().templateNameLocator)
            sleep(3)
            locator1.WebLocators().entertext(self.driver,locator1.WebLocators().templateNameLocator, data1.WebData().templateName)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().templateplanLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().templateplanchooseLocator)
            sleep(3)
            locator1.WebLocators().entertext(self.driver, locator1.WebLocators().objDurationLocator, data1.WebData().objDuration)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().saveandcontinue_Locator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().addQuestionLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().sourceLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().difficultLocator)
            sleep(3)
            locator1.WebLocators().clickbutton(self.driver, locator1.WebLocators().categoryLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().category_choosenLocator)
            sleep(3)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().one_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().two_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().three_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().four_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().five_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().six_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().seven_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().eight_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().nine_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver,
                                                        locator1.WebLocators().ten_question_addbutton_locator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().closeLocator)
            sleep(2)
            locator1.WebLocators().clickbutton_by_xpath(self.driver, locator1.WebLocators().saveandsubmitLocator)
            sleep(2)

        except NoSuchElementException as e:
            print("Error:Element is not present in the webpage")






