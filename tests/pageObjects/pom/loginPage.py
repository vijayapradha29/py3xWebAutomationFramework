#To create Page Object Class we need Page Locator and Page Action
# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)
# get email and send keys - email
# get password and send keys - password
# case 1 - click the submit button and navigate to dashboard Page
# case 2 - invalid -> error message

from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.common_utils import webdriver_wait

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    #page locators
    username=(By.ID,"login-username")
    password=(By.ID,"login-password")
    submit=(By.ID,"js-login-btn")
    # forgot_password=(By.XPATH,"//button[text()='Forgot Password?']")
    error_message=(By.ID,"js-notification-box-msg")
    #remove them if u dont use the commented locators

    # free_trial=(By.XPATH,"//a[@data-qa='bericafeqo']")
    # remember_me=(By.XPATH,"//input[@id='checkbox-remember']")
    # sso_button=(By.XPATH,"//button[@class='btn btn--link btn--primary Td(u)']")
    #for valid and invalid test cases we are not going to use forgot password and free trial locators so we will comment it out

    #page actions:
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit(self):
        return self.driver.find_element(*LoginPage.submit)

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username,timeout=5)
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit().click()

    def get_error_message_text(self):
        return self.get_error_message().text