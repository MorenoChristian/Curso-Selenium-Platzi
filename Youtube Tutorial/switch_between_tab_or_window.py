import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class SwitchTabWindow(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')



    def test_switch_tab_window(self):
        driver = self.driver
        driver.get('http://www.google.com')
        sleep(2)
                             # from opened window, we open another tab
        driver.execute_script("window.open(''); ")
        sleep(2)
                             # handles array in position 0 is google tab
                             # so we position in the second tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(2)
        driver.get('http://www.facebook.com')
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__=='__main__':
    unittest.main()
