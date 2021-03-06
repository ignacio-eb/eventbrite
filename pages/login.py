from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class loginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _signInBtn = "Sign In"
    #"//header[@id='global-header']/div/div/div/a[data-spec='global-header-quick-link'][class='eds-global-header__quick-link eds-show-up-md']/span[class='eds-show-up-md'][text()='Sign In']"

    _emailTxtBox = "[name='email']"
    _submitBtn = "[data-automation='signup-submit-button']"
    _user = "ignacio+test@evbqa.com"
    _passTxtBox = "[data-automation='signup-password-field']"
    _pass = "Eventbrite21!"
    _loginBtn = "[data-automation='signup-submit-button']"

    def clickSignInButton(self):
        self.elementClick(self._signInBtn, "link")

    def enterEmail(self, email):
        self.sendKeys(email, self._emailTxtBox, "css")

    def enterPassword(self, password):
        self.sendKeys(password, self._passTxtBox, "css")

    def clickSubmitButton(self):
        self.elementClick(self._submitBtn, "css")

    def clickLoginButton(self):
        self.elementClick(self._loginBtn, "css")

    def login(self, email, password):
        self.clickSignInButton()
        self.enterEmail(email)
        self.clickSubmitButton()
        self.enterPassword(password)
        self.clickLoginButton()

