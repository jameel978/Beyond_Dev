from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures

import time
import unittest


class test_login(unittest.TestCase):
    HUB_URL = "http://192.168.112.221:4444/wd/hub"
    cookies_button = '//button[@id="didomi-notice-agree-button"]'
    seach_input = "//input[@class='main-header-module-desktop-search-input']"
    setting_icon = "//button[@class='main-header-module-settings-button']"
    hokey_section_button = "//div[@class='main-header-module-desktop-item '][contains(text(),'הוקי')]"
    fottbal_section_button = "//div[@class='main-header-module-desktop-item '][contains(text(),'כדורגל')]"
    follow_button = "//div[@class='mega-header-module-entity-follow-container']/div/div"

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = "Windows 11"
        self.firefox_cap = webdriver.FirefoxOptions()
        self.firefox_cap.capabilities['platformName'] = "Windows 11"
        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] =  "Windows 11" 
        self.caps_list = [self.chrome_cap,self.firefox_cap,self.edge_cap] 
        #self.caps_list = [self.chrome_cap] 

        #return super().setUp()
    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_run_grid, self.caps_list)

    
    def test_run_grid(self):
        for caps in self.caps_list:
            self.search_test(caps)
            
    def wait_and_get_element_by_xpath(driver,xpath,sec=2):
        return WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)) )

    
    def search_test(self,cap):
        driver = webdriver.Remote(command_executor=self.HUB_URL,options=cap)
        driver.get("https://www.365scores.com/he")
        cookies_button_element = self.wait_and_get_element_by_xpath(driver,self.cookies_button,sec=4)
        cookies_button_element.click()
        search_input_element = self.wait_and_get_element_by_xpath(driver,self.seach_input)
        search_input_element.send_keys("fc barcelona")
        time.sleep(1)
        search_input_element.send_keys(Keys.RETURN)
        time.sleep(1)
        current_title = self.driver.title
        self.assertIn("ברצלונה",current_title)
        driver.close()




if __name__ == "__main__":
    unittest.main()