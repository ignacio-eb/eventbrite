from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class homePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _signInbutton = ".eds-global-header__minor .eds-show-up-md:nth-of-type(2) .eds-show-up-md"
    _createEventBtn = "[data-automation='global-nav-create']" #css
    _searchEventBtn = "//section[@id='home-experiment__moods-section']//button[text()='Events!']" #xpath
    _locationTxtBox = "//input[@id='locationPicker']" #xpath


    def clickSignInButton(self):
        self.elementClick(self._signInbutton,"css")

    def clickCreateEventBtn(self):
        self.elementClick(self._createEventBtn,"css")

    def clickSearchEventBtn(self):
        self.elementClick(self._searchEventBtn,"xpath")


    #Actions

    def getLocationText(self):
        return self.getTextElement(self._locationTxtBox, "xpath")

    def verifySearchEventBtnIsPresent(self):
        return self.isElementPresent(self._searchEventBtn,"xpath")

    def createEvent(self):
        self.clickSignInButton()

    def createFlow(self):
        self.clickCreateEventBtn()