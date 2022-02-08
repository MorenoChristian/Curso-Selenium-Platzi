import unittest
from selenium import webdriver

from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = cls.driver

    def test_search(self):
        google = GooglePage(self.driver) #llamamos al driver de este objeto
        google.open() #esto es para que realice todas las operaciones que le indicamos
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)
    
        print(google.keyword)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)