import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class ToggleSwitch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    
    def test_using_toggle(self):
        driver = self.driver
        driver.get('http://www.w3schools.com/howto/howto_css_switch.asp')

        toggle = driver.find_element_by_xpath('//*[@id="main"]/label[3]/div')
        toggle.click()
        sleep(2)
        toggle.click()
        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()