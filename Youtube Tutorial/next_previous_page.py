import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class NextPreviousPage(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    
    def test_next_previous_page(self):
        driver = self.driver
        driver.get('http://www.gmail.com')
        sleep(2)
        driver.get('http://www.google.com')
        sleep(2)
        driver.get('http://www.youtube.com')
        sleep(2)

        #with 'back' we can go to the previous page
        driver.back()
        sleep(2)
        driver.back()
        sleep(2)
        #with 'forward' we can go to the next page or forward
        driver.forward()
        sleep(2)



    def tearDown(self) -> None:
        self.driver.quit()

    
if __name__=='__main__':
    unittest.main()