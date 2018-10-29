from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class managePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    _addToFacebookLbl = "///div[@innertext='Add to Facebook']" #rxpath
    _privacyChkBox = "[data-automation='publish-agreement-check']" #css
    _AddToFacebookBtn = "[data-automation='publish-button-value']" #css

    def clickAddToFBLbl(self):
        self.elementClick(self._addToFacebookLbl, "css")

    def clickAddToFBBtn(self):
        self.elementClick(self._addToFacebookLbl,"css")

    def clickPrivacyChkBox(self):
        self.elementClick(self._privacyChkBox,"css")

    def publishToFacebook(self):
        self.clickAddToFBLbl()
        self.clickPrivacyChkBox()
        self.clickAddToFBBtn()

