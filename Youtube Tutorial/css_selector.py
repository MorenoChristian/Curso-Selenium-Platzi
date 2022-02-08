import unittest
from selenium import webdriver
from time import sleep

class CssSelector(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    
    def test_css_selector(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/html/default.asp')
        sleep(2)

        content = driver.find_element_by_css_selector('a.w3-blue')
        content.click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)