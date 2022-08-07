import logging
from appium.webdriver.common.appiumby import AppiumBy
from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).click()
        if str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()
        if str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking an Element " + str(locator))

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(AppiumBy.XPATH, configReader.readConfig("locators", locator))[index].click()
        if str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator))[index].click()
        if str(locator).endswith("_ID"):
            self.driver.find_elements(AppiumBy.ID, configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking an Element " + str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        if str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(value)
        if str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element : " + str(locator) + "And Entered Value is : " + str(value))

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).text
        if str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).text
        if str(locator).endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).text
        log.logger.info("Typing in an element : " + str(locator) + "And return Value is : " + str(text))
        return text
