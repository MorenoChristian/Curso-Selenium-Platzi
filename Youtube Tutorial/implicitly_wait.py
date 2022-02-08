import unittest
from selenium import webdriver

class ImplicitlyWait(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    def test_implicitly_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('http://www.google.com')
        myDinamicElement = driver.find_element_by_name('q')

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()