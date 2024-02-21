from selenium.webdriver.common.keys import Keys
from infra import start_chrome_browser
import random
import time


class Youtube_page(start_chrome_browser):
    def __init__(self, website):        
        super().__init__(website)
        self.init_elements()

    def init_elements(self):
        self.search_input = self.get_element_by_xpath("//input[@id='search']")
        self.search_div = self.get_element_by_xpath("//div[@class='ytd-searchbox-spt']") 
        self.init_setting_bar()
        
    def init_setting_bar(self):
        self.setting_bar = self.wait_and_get_element_by_xpath("//button[@class='style-scope yt-icon-button'][@aria-label='Settings']")
    
    def init_setting_items(self):
        self.theme_toggle_button = self.wait_and_get_element_by_xpath("//div[@class='style-scope ytd-toggle-theme-compact-link-renderer']")
       
    def init_theme_elements(self):
        self.ligh_theme_button = self.wait_and_get_element_by_xpath("//yt-formatted-string[contains(text(),'Light theme')][@id='label']")
        self.Dark_theme_button = self.wait_and_get_element_by_xpath("//yt-formatted-string[contains(text(),'Dark theme')][@id='label']")
        
    def init_video_elemetns(self):
        self.all_video_elements = self.wait_and_get_elements_by_xpath("//ytd-video-renderer",sec = 3)
        
    def init_ads_video_skip_button(self):
        self.ads_video_skip_button = self.wait_and_get_element_by_xpath("//button[@class='ytp-ad-skip-button-modern ytp-button']",sec = 0.5)
        
    def init_ads_video_element_overlay(self):
        self.ads_video_element = self.wait_and_get_element_by_xpath("//div[@class='ytp-ad-player-overlay']",sec = 2)

    def init_ads_video_text_elementy(self):
        self.ads_video_text_element = self.wait_and_get_element_by_xpath("//div[@class='ytp-ad-text ytp-ad-preview-text-modern']")
        
    def init_video_setting_button(self):
        self.video_setting_button_element = self.wait_and_get_element_by_xpath("//button[@class='ytp-button ytp-settings-button']")
    
    def init_video_resolution_setting(self):
        self.video_resolution_setting_element = self.wait_and_get_element_by_xpath("//div[@class='ytp-menuitem-label'][contains(text(),'Quality')]")
        
    def init_video_resolution_360p_button(self):
        self.video_resolution_360p_button = self.wait_and_get_element_by_xpath("//div[@class='ytp-panel-menu']/div[@class='ytp-menuitem']/div/div/span[contains(text(),'360p')]")
    
    def init_video_resolution_setting_text(self):
        self.video_resolution_setting_text = self.wait_and_get_element_by_xpath("//div[@class='ytp-menuitem-content']/div/span")
    
    def check_for_ads(self):
        try:
            self.init_ads_video_element_overlay()
            return True
        except:
            return False
        
    def check_if_ad_is_skippable(self):
        try:
            self.init_ads_video_text_elementy()
            return True
        except:
            return False
            
        
    def wait_for_skip_button_and_press_skip(self):
        wait_time = int(self.ads_video_text_element.text)
        time.sleep(wait_time)
        self.init_ads_video_skip_button()
        self.ads_video_skip_button.click()
        
    def init_random_video_elemet(self):
        self.current_video_elemn = self.all_video_elements[0]
        #self.current_video_elemn = random.choice(self.all_video_elements)
        
    def add_text_search_input_one_by_one(self,txt):
        for i in txt:
            self.search_input.send_keys(i)
            time.sleep(0.1)
            
    def add_text_search_input(self,txt):
        self.search_input.send_keys(txt)
    
    def send_return_key_search_input(self):
        self.search_input.send_keys(Keys.RETURN)
        
    def send_down_key_search_input(self):
        self.search_input.send_keys(Keys.DOWN)
                
    def search_flow(self,txt):
        self.add_text_search_input_one_by_one(txt)
        old_title = self.get_page_title()
        self.send_return_key_search_input()
        self.wait_until_title_change(old_title)

    def search_autocomplete_flow(self,txt):
        self.add_text_search_input_one_by_one(txt)
        time.sleep(1)
        old_title = self.get_page_title()
        self.send_down_key_search_input()
        self.send_return_key_search_input()
        self.wait_until_title_change(old_title)
            
    def play_random_video_flow(self):
        self.init_video_elemetns()
        self.init_random_video_elemet()
        self.click_on_video_element()
        
    def wait_until_title_change(self,old_title,sec = 3.0,steps = 0.25):
        current_title = self.get_page_title()
        c_sec = sec
        while((current_title == old_title) & (c_sec > 0.0)):
            time.sleep(steps)
            c_sec -= steps
            current_title = self.get_page_title()
            #print(current_title,old_title,c_sec)
            
    
    def click_on_settings(self):
        self.setting_bar.click()
        self.init_setting_items()
        
    def click_on_toggle_theme(self):
        self.theme_toggle_button.click()
        self.init_theme_elements()
    
    def toggle_light_theme(self):
        self.ligh_theme_button.click()
        
    
    def get_current_page_theme(self):
        self.init_setting_bar()
        self.click_on_settings()
        return self.theme_toggle_button.text
    
    def click_on_video_element(self):
        self.current_video_elemn.click()
        
        
    def skip_ad_flow(self):
        if self.check_for_ads():
            if self.check_if_ad_is_skippable():
                self.wait_for_skip_button_and_press_skip()
            else:
                #The Add is no Skippable
                return self.skip_ad_flow()
                
    def change_video_resolution_flow(self):
        self.init_video_setting_button()
        self.video_setting_button_element.click()
        self.init_video_resolution_setting()
        self.video_resolution_setting_element.click()
        self.init_video_resolution_360p_button()
        time.sleep(1)
        self.video_resolution_360p_button.click()
        time.sleep(1)
        
        
        
        
    def get_current_video_resolution(self):
        self.init_video_setting_button()
        self.video_setting_button_element.click()
        self.init_video_resolution_setting_text()
        return self.video_resolution_setting_text.text
        