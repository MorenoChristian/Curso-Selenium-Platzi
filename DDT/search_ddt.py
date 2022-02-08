import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SeacrhDDT(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    #el decorador data va a incluir tuplas con los terminos que vamos a buscar
    @data(('dress', 5), ('music', 5))
    @unpack #nos va a permitir desempaquetar las tuplas y consultarlas de forma individual
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        
        print(f"Found {len(products)} products")

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))


    def tearDown(self) -> None:
        self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)