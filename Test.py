import time
import unittest
from selenium import webdriver
import concurrent.futures

from Logic import Website_instance

class GridTest(unittest.TestCase):
    HUB_URL = 'http://localhost:4444/wd/hub'
    WEBSITE_URL = "https://www.365scores.com/he"

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'Windows 11'
        self.fireFox_cap = webdriver.FirefoxOptions()
        self.fireFox_cap.capabilities['platformName'] = 'Windows 11'
        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'Windows 11'
        self.cap_list = [self.chrome_cap, self.fireFox_cap, self.edge_cap]
        self.test_functions = [self.title_change,self.follow_team,self.change_to_hockey_section,self.follow_leage_from_homepage,self.change_theme]
        self.inputs_list = [(test,browser) for test in self.test_functions for browser in self.cap_list]

        
    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers= len(self.inputs_list)) as executer:
            executer.map(self.init_tests, self.inputs_list)


    def init_tests(self,input):
        input[0](input[1])
        
    def title_change(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()
        driver_instance.search_flow("FC Barcelona")
        current_title = driver_instance.get_page_title()
        print("test title change on: ", caps.capabilities['browserName'])
        self.assertIn('ברצלונה', current_title, "Title doesn't match expected value")
        driver_instance.close_page()
        
    def follow_team(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()
        driver_instance.follow_team_flow("FC Barcelona")
        print("test follow team on: ", caps.capabilities['browserName'])
        follow_status = driver_instance.get_follow_status()
        self.assertEqual('עוקב', follow_status)
        driver_instance.close_page()

    def change_to_hockey_section(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()    
        driver_instance.change_to_kochkey_section_flow()
        print("test change to hockey section on: ", caps.capabilities['browserName'])
        current_title = driver_instance.get_page_title()
        self.assertIn('הוקי', current_title, "Title doesn't match expected value")
        driver_instance.close_page()
    
    def follow_leage_from_homepage(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()
        driver_instance.follow_leumi_leage_from_homepage()
        driver_instance.search_flow("ליגה לאומית")
        print("test follow leage from homepage on: ", caps.capabilities['browserName'])
        follow_status = driver_instance.get_follow_status()
        self.assertEqual('עוקב', follow_status)
        driver_instance.close_page()


    def change_theme(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()
        old_theme_class, new_theme_class = driver_instance.change_theme_flow()
        print("test change them on: ", caps.capabilities['browserName'])
        self.assertNotEqual(old_theme_class,new_theme_class)
        driver_instance.close_page()



if __name__ == "__main__":
    unittest.main()