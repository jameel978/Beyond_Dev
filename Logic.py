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
    cookies_button_xpath = '//button[@id="didomi-notice-agree-button"]'
    seach_input_xpath = "//input[@class='main-header-module-desktop-search-input']"
    setting_icon_xpath = "//button[@class='main-header-module-settings-button']"
    hokey_section_button_xpath = "//div[@class='main-header-module-desktop-item '][contains(text(),'הוקי')]"
    fottbal_section_button_xpath = "//div[@class='main-header-module-desktop-item '][contains(text(),'כדורגל')]"
    follow_button_xpath = "//div[@class='mega-header-module-entity-follow-container']/div/div"
    leumi_leage_star_xpath = "//a[@class='all-scores-widget-competition_all_scores_widget_competition_info_name__8bE-h'][contains(text(),'ליגה לאומית')]//preceding-sibling::div"
    Change_theme_switch_xpath = "//div[@class='settings-module-row-container '][contains(text(),'הגדר רקע כהה')]/div/div"

    def __init__(self, HUB, cap, website):        
        super().__init__(HUB,cap,website)
        self.current_title = None

    def init_coockies_button_element(self):
        self.cookies_button_element = self.wait_and_get_element_by_xpath(self.cookies_button_xpath)

    def init_search_element(self):
        self.search_input = self.wait_and_get_element_by_xpath(self.seach_input_xpath)

    def init_follow_button(self):
        self.follow_button_element = self.wait_and_get_element_by_xpath(self.follow_button_xpath)

    def init_hokey_section_button(self):
        self.hokey_section_button_element = self.wait_and_get_element_by_xpath(self.hokey_section_button_xpath)

    def init_leumi_leage_star_button(self):
        self.leumi_leage_star_button_element = self.wait_and_get_element_by_xpath(self.leumi_leage_star_xpath)

    def init_setting_button(self):
        self.setting_button_element = self.wait_and_get_element_by_xpath(self.setting_icon_xpath)

    def init_Change_theme_switch(self):
        self.Change_theme_switch_element = self.wait_and_get_element_by_xpath(self.Change_theme_switch_xpath)


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

    def click_follow_button(self):
        self.follow_button_element.click()
        print(self.follow_button_element.get_attribute('class'))


    def click_leumi_leage_star_button(self):
        self.leumi_leage_star_button_element.click()

    def click_setting_button(self):
        self.setting_button_element.click()

    def click_Change_theme_switch_element(self):
        self.Change_theme_switch_element.click()

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


    def follow_team_flow(self,txt):
        self.search_flow(txt)
        self.init_follow_button()
        self.click_follow_button()
        time.sleep(0.5)


    def get_follow_status(self):
        self.init_follow_button()
        return self.follow_button_element.text
    

    def change_to_kochkey_section_flow(self):
        self.init_hokey_section_button()
        old_title = self.get_page_title()
        self.hokey_section_button_element.click()
        self.wait_until_title_change(old_title)

    def follow_leumi_leage_from_homepage(self):
        time.sleep(2)
        self.init_leumi_leage_star_button()
        self.click_leumi_leage_star_button()
        time.sleep(0.5)

    def change_theme_flow(self):
        time.sleep(1)
        self.init_setting_button()
        self.click_setting_button()
        self.init_Change_theme_switch()
        time.sleep(1)
        current_settings = self.get_theme_status()
        self.click_Change_theme_switch_element()
        time.sleep(1)
        return (current_settings,self.get_theme_status())

    def get_theme_status(self):
        return self.Change_theme_switch_element.get_attribute("class")



if __name__ == "__main__":
    unittest.main()