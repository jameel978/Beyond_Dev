from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import time
import unittest
from infra import Browser_instance



class Website_instance(Browser_instance):
    HUB_URL = "http://192.168.112.221:4444/wd/hub"
    cookies_button = '//button[@id="didomi-notice-agree-button"]'
    seach_input = "//input[@class='main-header-module-desktop-search-input']"
    setting_icon = "//button[@class='main-header-module-settings-button']"
    hokey_section_button = "//div[@class='main-header-module-desktop-item '][contains(text(),'הוקי')]"
    fottbal_section_button = "//div[@class='main-header-module-desktop-item '][contains(text(),'כדורגל')]"
    follow_button = "//div[@class='mega-header-module-entity-follow-container']/div/div"

    def __init__(self, HUB, cap, website):        
        super().__init__(HUB,cap,website)
        self.current_title = None

    def init_coockies_button_element(self):
        self.cookies_button_element = self.wait_and_get_element_by_xpath(self.cookies_button)

    def init_search_element(self):
        self.search_input = self.wait_and_get_element_by_xpath(self.seach_input)

    def wait_until_title_change(self,old_title,sec = 3.0,steps = 0.25):
        current_title = self.get_page_title()
        c_sec = sec
        while((current_title == old_title) & (c_sec > 0.0)):
            time.sleep(steps)
            c_sec -= steps
            current_title = self.get_page_title()
            #print(current_title,old_title,c_sec)
    
    def add_text_search_input_one_by_one(self,txt):
        for i in txt:
            self.search_input.send_keys(i)
            time.sleep(0.1)


    def click_coockies_button(self):
        self.cookies_button_element.click()

    def skip_cookies_popup_flow(self):
        self.init_coockies_button_element()
        self.click_coockies_button()
        time.sleep(0.5)

    def search_flow(self,txt):
        self.init_search_element()
        self.add_text_search_input_one_by_one(txt)
        old_title = self.get_page_title()
        time.sleep(1)
        self.send_return_key_to_search_input()
        self.wait_until_title_change(old_title)

    def send_return_key_to_search_input(self):
        self.search_input.send_keys(Keys.RETURN)


if __name__ == "__main__":
    unittest.main()