from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Browser_instance:
    def __init__(self, HUB,cap,website):
        self.start_driver(HUB,cap,website)
        
    def start_driver(self,HUB,cap,website):
        self.driver = webdriver.Remote(command_executor=HUB,options=cap)
        self.driver.get(website)
        
    def get_page_title(self):
        return self.driver.title
        
    def close_page(self):
        self.driver.close()
        
    def get_element_by_xpath(self,xpath):
        return self.driver.find_element(By.XPATH,xpath)

    def wait_and_get_element_by_xpath(self,xpath,sec=5):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)) )

    def wait_and_get_elements_by_xpath(self,xpath,sec=5):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)) )


