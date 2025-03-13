from selenium import webdriver
# from tests.constants.constants import constants
from selenium.webdriver import Edge
import pytest

import os
from dotenv import  load_dotenv
load_dotenv()
# we called the load_dotenv() function->this will load the .env file
@pytest.fixture(scope='class')
#marking scope='class'->means it will be available to all the classes
def setup(request):
    driver=webdriver.Edge()
    driver.maximize_window()
    username=os.getenv("USERNAME1")
    # print(username)
    password=os.getenv("PASSWORD1")
    # print(password)
    # driver.get(constants.app_url())
    request.cls.driver=driver#this is used to send the driver to test case,cls is just a variable
    request.cls.username=username#this is used to send the username to test case
    request.cls.password=password#this is used to send the password to test case
    yield driver#return the webdriver when it  is not null
    driver.quit()#the moment when its null,it will run this line
    #we need to pass username,password,driver to test case so we are using return driver
#but if we use return then we need to carete another function to stop thr driver
#as def teardown(request):driver.quit()
#there is a famous function in python known as yield(when you want to call another function)
# yield driver->this is same as return driver
