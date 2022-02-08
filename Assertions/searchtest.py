import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get('http://demo-store.seleniumacademy.com')


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear() #limpiará el campo de busqueda en el caso que contenga texto

        search_field.send_keys('tee') #al field busqueda le mando por teclado la palabra 'tee'
        search_field.submit() #le decimos al search_field que envie estos datos


    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        #la forma rapida de obtener una lista de elementos es atravéz de su Xpath
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        #identificamos si la cantidad de productos encontrados es 1 o no
        self.assertEqual(1, len(products))



    def tearDown(self) -> None:
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)