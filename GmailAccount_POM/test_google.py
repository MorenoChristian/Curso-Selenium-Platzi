import unittest
from selenium import webdriver
from time import sleep

from google_page import Google_Page

class GoogleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        

    def test_search_gmail(self):
        google = Google_Page(self.driver)
        google.open_google()
        google.search("gmail")
        google.open_gmail()
        sleep(2)

    
    def tearDown(self) -> None:
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity=2)