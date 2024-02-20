import time
import unittest
from selenium import webdriver
import concurrent.futures


class GridTest(unittest.TestCase):
    HUB_URL = 'http://localhost:4444/wd/hub'

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'Windows 11'

        self.fireFox_cap = webdriver.FirefoxOptions()
        self.fireFox_cap.capabilities['platformName'] = 'Windows 11'

        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'Windows 11'

        self.cap_list = [self.chrome_cap, self.fireFox_cap, self.edge_cap]

    def test_run_grid_serial(self):
        for caps in self.cap_list:
            self.test_execute(caps)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_execute, self.cap_list)

    def test_execute(self, caps):
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        driver.get("https://.saucedemo.com/")

        pass
        title = driver.title
        expected_title = "Swag Labs"
        print("test run on: ", caps.capabilities)
        self.assertEqual(expected_title, title, "Title doesn't match expected value")
        time.sleep(10)
        driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()