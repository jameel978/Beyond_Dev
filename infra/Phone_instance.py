
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

capabilities = dict(
    platformName= "Android",
    deviceName= "emulator-5554",
    platformVersion= "14.0",
    automationName= "UiAutomator2",
    appPackage= "com.claudivan.taskagenda",
    appActivity= ".Activities.MainActivity"
)

appium_server_url = 'http://localhost:4723'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
options=capabilities_options
        
class Phoneinstance:
    def __init__(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def find_elem_by_ID(self,elem,sec = 3):
        #return self.driver.find_element(by=AppiumBy.ID, value=elem)
        print(elem)
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((AppiumBy.ID, elem)))

    def find_elem_by_XPATH(self,elem,sec = 3):
        #return self.driver.find_element(by=AppiumBy.ID, value=elem)
        print(elem)
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((AppiumBy.XPATH, elem)))
