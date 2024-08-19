from selenium.webdriver.common.by import By


class WebLocators:
    """
        this class contains all the locators that are required to testing login credentials
    """
    emailLocator = "email"
    passwordLocator = "password"
    signinLocator = "submit"
    settingLocator = '//*[@id="link-manage"]/a'
    logoutLocator = 'logout'
    templateLocator = '//*[@id="link-template"]/a'
    createLocator = '//*[@id="test-page"]/div[2]/div[2]/div/div[1]/div[1]/div/a'
    selectrole_inputLocator ='custom-select-role-selectized'
    testengineerLocator = '//*[@id="custom-based-form"]/div[1]/div[1]/div/div[2]/div/div[6]'
    templateNameLocator ='custom-test-name'
    templateplanLocator = 'custom-test-plan-selectized'
    templateplanchooseLocator = '//*[@id="custom-based-form"]/div[1]/div[3]/div/div[2]/div/div[1]'
    objDurationLocator = 'custom-obj-duration'
    saveandcontinue_Locator = 'step1-submit'
    addQuestionLocator = '//*[@id="test-page-two"]/div/div[2]/div/div/form/div[2]/button'
    sourceLocator = '//*[@id="select-library"]/label[2]'
    difficultLocator = '//*[@id="select-difficulty"]/label[2]'
    categoryLocator = 'library-search-selectized'
    category_choosenLocator = '//*[@id="library-content-wrap"]/div[1]/div[2]/div/div/div[2]/div/div[1]'
    one_question_addbutton_locator = '//*[@id="objectLibQuestion0"]/button[2]'
    two_question_addbutton_locator = '//*[@id="objectLibQuestion1"]/button[2]'
    three_question_addbutton_locator = '//*[@id="objectLibQuestion2"]/button[2]'
    four_question_addbutton_locator = '//*[@id="objectLibQuestion3"]/button[2]'
    five_question_addbutton_locator = '//*[@id="objectLibQuestion4"]/button[2]'
    six_question_addbutton_locator = '//*[@id="objectLibQuestion5"]/button[2]'
    seven_question_addbutton_locator = '//*[@id="objectLibQuestion6"]/button[2]'
    eight_question_addbutton_locator = '//*[@id="objectLibQuestion7"]/button[2]'
    nine_question_addbutton_locator = ' //*[@id="objectLibQuestion8"]/button[2]'
    ten_question_addbutton_locator = '//*[@id="objectLibQuestion9"]/button[2]'
    closeLocator = '//*[@id="modal-question-library"]/div/div/div/div/div[1]/div[2]/button[1]'
    saveandsubmitLocator = '//*[@id="test-page-two"]/div/div[2]/div/div/form/div[6]/div/a[2]'
    detailLocator = '//*[@id="tests-card-container"]/div[7]/div/div/div[3]/a[1]'
    testLocator = '//*[@id="link-test"]/a'
    createTestLocator = '//*[@id="test-page"]/div/div[2]/div/div/div[1]/div/a'
    testname_locator = 'drive-name'
    testPeriod_locator = 'drive-dates'
    usethistocreateLocator = '//*[@id="use-this-to-drive"]'
    testPeriod_datechoosen_locator = '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    applybutton_Locator = '/html/body/div[2]/div[4]/button[2]'
    jobdescription_locator = '//*[@id="create-drive-page-two"]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/p'
    saveandsubmit_Locator = ' //*[@id="create-drive-page-two"]/div/div[2]/div/div/div[7]/button'
    saveandconLocator ='//*[@id="selected-test"]/div/div[2]/div/a[2]'
    selectthis_locator = '//*[@id="test-6094"]/div/div/div/button'
    fullnameLocator = "registerName"
    Email_locator = "registerEmail"
    mobilenumberLocator = "registerMobile"
    password_locator_test = "registerPassword"
    retype_password_locator = "registerRetypePassword"
    createNew_account_locator ="register"
    createnew_button_locator = '//*[@id="app"]/nav/div/form/div/button'

    def entertext(self, driver, locator, textValue):
        driver.find_element(by=By.ID, value=locator).send_keys(textValue)

    def entertext_by_xpath(self, driver, locator, textValue):
        driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)


    def clickbutton(self, driver, locator):
        driver.find_element(by=By.ID, value=locator).click()

    def clickbutton_by_xpath(self, driver, locator):
        driver.find_element(by=By.XPATH, value=locator).click()

