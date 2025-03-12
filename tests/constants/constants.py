from allure_commons.types import AttachmentType
import allure


class constants:

    def __init__(self):
        print("constants loaded")

    @staticmethod
    def app_url(): #TODO-3.Polymorphism(method overloading)same name with different argument
        return "https://app.vwo.com"
    def app_url(name):
        return "https://app.vwo.com"

    @staticmethod
    def take_screenshot(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)