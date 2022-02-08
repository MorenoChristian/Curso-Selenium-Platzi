import unittest
from selenium import webdriver
# selenium library for mouse actions
from selenium.webdriver import ActionChains

from time import sleep

class HoverAction(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    def test_hover_action(self):
        driver = self.driver
        driver.get('http://www.google.com')
        sleep(2)

        element = driver.find_element_by_link_text('Privacidad')
        
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
