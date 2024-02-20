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

    #def test_run_grid_serial(self):
    #    self.title_change(self.cap_list[0])


    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.title_change, self.cap_list)

    def title_change(self, caps):
        driver_instance = Website_instance(self.HUB_URL,caps,self.WEBSITE_URL)
        driver_instance.skip_cookies_popup_flow()
        driver_instance.search_flow("FC Barcelona")
        current_title = driver_instance.get_page_title()
        print("test run on: ", caps.capabilities)
        self.assertIn('ברצלונה', current_title, "Title doesn't match expected value")
        driver_instance.close_page()
        
        
if __name__ == "__main__":
    unittest.main()