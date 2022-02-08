import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep

class GetIntoGmail(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()


    def test_gmail(self):
        driver = self.driver
        driver.get('https://www.google.com/intl/es-419/gmail/about/')

        driver.find_element_by_link_text('Acceder').click()
        
    def test_gmail_account(self):

        #try to found mail account field
        account_field = self.driver.find_element_by_name('identifier')
        account_field.send_keys('christian10moreno@gmail.com')
        # ENTER key press
        account_field.send_keys(Keys.ENTER)
        sleep(3)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()





if __name__=='__main__':
    unittest.main(verbosity=2)
    
