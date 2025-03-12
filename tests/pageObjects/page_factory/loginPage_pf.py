# Page Class
#
#
# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here ( They are not Test cases)
#concept between them remains same but a minor change in syntax will see

from seleniumpagefactory.Pagefactory import PageFactory
from tests.utils.common_utils import webdriver_wait

# TODO-5.Class and Object
class LoginPage(PageFactory): # TODO-4.Encapsulation(private class and locators become private)
    #1.first we do web driver initialization by using constructor
    def __init__(self,driver): # TODO-6.Constructor
        self.driver=driver
        self.highlight=True

        # Page Locators

    locators={
        'username':('css',"#login-username"),
        # 'username' : ('ID', "login-username"),
        'password': ('NAME', 'password'),
        # 'error_message': ('CSS', '#js-notification-box-msg'),
        'error_message' :('ID', "js-notification-box-msg"),
        'submit_button': ('XPATH', '//button[@id="js-login-btn"]')#its like dictionary key:tuple
    }
    #the advantage of this is,when you call the login page ,automatically all the above elements if we are able to find them in the page they will be loaded in your RAM
    #so if they are already loaded in the RAM to access them it will be very easy

    # Page Actions

    def login_to_vwo(self,user,pwd):
        self.username.set_text(user)
        self.password.set_text(pwd)
        self.submit_button.click_button()
        #from where these functions are coming,they are inbuilt functions,they are already added
        #what is the advantage of using this?they are super fast functions
    def error_message_text(self):
        return self.error_message.get_text()#dont have to use webdriverwait because get.text()automatically waits
