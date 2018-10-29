from selenium import webdriver
from pages.login import loginPage
import unittest
from pages.home import homePage
from pages.create_event import createPage
import os

class publish2FBTests(unittest.TestCase):

    def test_validLogin(self):
        driverLocation = "/Users/ignacio/PycharmProjects/udemy_python3x_selenium/lib/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate FF Browser Command
        driver = webdriver.Chrome(driverLocation)
        baseURL= "https://www.evbqa.com/"
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        hp = homePage(driver)
        hp.createEvent()

        lp = loginPage(driver)
        lp.login("ignacio+test@evbqa.com", "test123123")

        hp.clickCreateEventBtn()

        cp = createPage(driver)
        cp.createEvent("test","Rock hostel, Collins Avenue, Miami Beach, FL, USA","this is a description","paid")


        # userIcon = driver.find_element(By.XPATH, "//*[@id='navbar']//span[text()='Test User']")
        # if userIcon is not None:
        #     print("login Successful")
        # else:
        #     print("login failed")