from selenium import webdriver
import unittest
from pages.home import homePage
import os
import csv

class homePageTests(unittest.TestCase):

    csvPath = 'ip_urls.csv'

    def test_validIPs(self):

        with open(self.csvPath) as csvFile:
            urlReader = csv.reader(csvFile)

            for row in urlReader:
                baseURL = str(row[0])
                print("Testing URL: ",baseURL, "--> ",str(row[1]))
                driverLocation = "/Users/ignacio/PycharmProjects/udemy_python3x_selenium/lib/chromedriver"
                os.environ["webdriver.chrome.driver"] = driverLocation
                # Instantiate Chrome Browser Command
                driver = webdriver.Chrome(driverLocation)
                driver.get(baseURL)
                driver.implicitly_wait(3)

                try:
                    hp = homePage(driver)
                    print("Location got from the page --> ", hp.getLocationText())
                    result = hp.verifySearchEventBtnIsPresent()
                    if (result):
                        print("Event Button Found - FAILED")
                        hp.clickSearchEventBtn()
                        print("*" * 100)
                    else:
                        print("Event Button NOT FOUND - OK")
                        print("*" * 100)
                except:
                    print("Something went wrong")
                    print("Continue with next URL")
                    print("*" * 100)
                    driver.close()
                    continue

                driver.close()