import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoggleMapsSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_mapsgoogle_page(self):
        driver = self.driver
        driver.get("https://www.google.com/maps")
        self.assertIn("Google Maps", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("santander")
        elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
