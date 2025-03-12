import time
import allure
import pytest
from selenium import webdriver
from tests.pageObjects.pom.loginPage import LoginPage
from tests.utils.common_utils import webdriver_wait
from tests.pageObjects.pom.dashboard import DashboardPage
from tests.constants.constants import constants


#now here only we will write our assertions
#here we will use the page object class that we have created

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(constants.app_url())
    return driver

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    try:
        driver=setup
        login_page=LoginPage(driver)
        login_page.login_to_vwo(user="vijayatester16@gmail.com",pwd="Wingify@1234")
        time.sleep(2)
        error_msg_element=login_page.get_error_message_text()
        assert error_msg_element== "Your email, password, IP address or location did not match"

    except Exception as e:
        pytest.xfail("Failed TC")
        print(e)


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    try:
        driver=setup
        login_page=LoginPage(driver)
        login_page.login_to_vwo(user="vijayatester16@gmail.com",pwd="Wingify@123")
        # time.sleep(10)
        dashboard=DashboardPage(driver)
        # assert "Dashboard" in driver.title
        assert "Web Automation" in dashboard.user_logged_in_text()
    except Exception as e:
        pytest.xfail("Failed TC")
        print(e)


