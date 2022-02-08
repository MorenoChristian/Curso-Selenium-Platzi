import unittest
from selenium import webdriver
from time import sleep

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com')


    
    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()


        # Retroceder una pagina, avanzar una pagina y refrescar
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    

    def tearDown(self) -> None:
        self.driver.implicitly_wait(15)
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)