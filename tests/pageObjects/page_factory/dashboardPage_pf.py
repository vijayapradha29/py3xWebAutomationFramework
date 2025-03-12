from seleniumpagefactory.Pagefactory import PageFactory
from tests.utils.common_utils import webdriver_wait

class DashboardPage(PageFactory):    #TODO - 1.Single Inheritance
    #1.first we do web driver initialization by using constructor
    def __init__(self,driver):
        self.driver=driver
        self.highlight=True

    locators={
        'user_logged_in':('XPATH', "//span[@data-qa='lufexuloga']")
    }

    def user_logged_in_text(self):
        return self.user_logged_in.get_text()