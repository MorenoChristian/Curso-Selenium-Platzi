import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep

from mercado_page import MercadoPage

class MercadoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        

    def test_country(self):
        mercado = MercadoPage(self.driver, 'http://mercadolibre.com')
        mercado.open()
        mercado.country("Colombia")
        mercado.search("playstation 4")
        
        self.driver.find_element_by_class_name('nav-new-cookie-disclaimer__button').click() #le damos click a los cookies sino da erros al querer clickear en algun filtro
        
        mercado.new_filter()
        self.assertTrue("nuevo" in self.driver.current_url)

        mercado.bogota_filter()
        self.assertTrue('bogota' in self.driver.current_url)

        mercado.low_price()
        sleep(3)

        nombre = mercado.order_first_elements()
        print("IMPRIMIENDO LISTA DE LOS PRIMEROS 5 NOMBRES DE CONSOLAS")
        print(nombre)
        
        


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'mercado libre'))