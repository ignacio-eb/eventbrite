from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class createPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _eventTittleTxtBox = "/html//input[@id='id_group-details-name']" #xpath
    _locationTxtBox = "/html//input[@id='location-name-input']" #xpath
    _descriptionTxtBox = "/html//iframe[@id='id_group-details-description_ifr']" #xpath
    _freeTicketBtn = "//a[#'create-ticket-free-button']" #rxpath
    _paidTicketBtn = "//a[#'create-ticket-paid-button']" #rxpath
    _ticketNameTxtBox = "/html//input[@id='id_group-tickets-0-ticket_type']" #xpath
    _quantityTxtBox = "/html//input[@id='id_group-tickets-0-quantity_total']" #xpath
    _ticketPriceTxtBox = "///input[@name='group-tickets-1-cost']" #rxpath
    _makeYourEventLiveBtn = "/html//a[@id='make-event-live-button-almost-done']" #xpath
    _publishBtn = "/html//button[@id='make-event-live-button-header']/span[@class='eds-btn__children']" #xpath


    def enterEventTittle(self, tittle):
        self.sendKeys(tittle,self._eventTittleTxtBox, locatorType="xpath")

    def enterLocation(self, location):
        self.sendKeys(location, self._locationTxtBox, locatorType="xpath")

    def enterDescription(self, description):
        self.sendKeys(description, self._descriptionTxtBox, locatorType="xpath")

    def clickFreeTicketBtn(self):
        self.elementClick(self._freeTicketBtn, locatorType="xpath")

    def clickPaidTicketBtn(self):
        self.elementClick(self._paidTicketBtn, locatorType="xpath")

    def enterTicketName(self, ticketName):
        self.sendKeys(ticketName,self._ticketNameTxtBox, locatorType="xpath")

    def enterTicketQty(self, ticketQty):
        self.sendKeys(ticketQty,self._quantityTxtBox, locatorType="xpath")

    def enterTicketPrice(self, ticketPrice):
        self.sendKeys(ticketPrice,self._ticketPriceTxtBox, locatorType="xpath")

    def clickMakeYourEventLiveBtn(self):
        self.elementClick(self._makeYourEventLiveBtn, locatorType="xpath")

    def clickPublishBtn(self):
        self.elementClick(self._publishBtn, locatorType="xpath")


    def createEvent(self, tittle, location, description, ticketName, ticketQuantity=1, ticketPrice=10):
        self.enterEventTittle(tittle)
        self.enterLocation(location)
        self.enterDescription(description)
        self.clickPaidTicketBtn()
        self.enterTicketName(ticketName)
        self.enterTicketQty(ticketQuantity)
        self.enterTicketPrice(ticketPrice)

