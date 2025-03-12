import time
import pytest
import selenium
from selenium import webdriver

from tests.pageObjects.page_factory.dashboardPage_pf import DashboardPage
from tests.pageObjects.page_factory.loginPage_pf import LoginPage
# from tests.pageObjects.page_factory.dashboardPage_pf import DashboardPage
import allure
from allure_commons.types import AttachmentType
from tests.constants.constants import constants
import logging
from tests.constants.constants import constants

@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")#usefixtures->will always try to find the function name in conftest(setup)
    @pytest.mark.qa
    def test_vwologin_negative(self,setup):
        try:
            driver=setup#this will get driver from setup
            driver.get(constants.app_url())
            loginPage= LoginPage(driver)
            loginPage.login_to_vwo(user=self.username, pwd="123")
        # time.sleep(5)
            error_msg_element = loginPage.error_message_text()
            assert error_msg_element == "Your email, password, IP address or location did not match"

            if "Dashboard" not in driver.title:
                constants.take_screenshot(driver,"test_vwologin_negative_tc0")
            time.sleep(10)
        except Exception as e:
            print(e)
    @pytest.mark.usefixtures("setup")  # usefixtures->will always try to find the function name in conftest(setup)
    @pytest.mark.qa
    def test_vwologin_positive(self, setup):
        driver = setup  # this will get driver from setup
        driver.get(constants.app_url())
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        # time.sleep(5)
        dashboardPage=DashboardPage(driver)
        username=dashboardPage.user_logged_in_text()
        assert "Dashboard" in driver.title
        assert username=="Web Automation"
        time.sleep(5)

    # @pytest.mark.usefixtures("setup")  # usefixtures->will always try to find the function name in conftest(setup)
    # @pytest.mark.qa
    # def test_vwologin_negative_tc3(self, setup):
    #     pass
    #
    # @pytest.mark.usefixtures("setup")  # usefixtures->will always try to find the function name in conftest(setup)
    # @pytest.mark.qa
    # def test_vwologin_negative_tc4(self, setup):
    #     pass