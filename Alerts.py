import unittest
from selenium import webdriver
from time import sleep


class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')


    def test_compare_products_removal_alert(self):
        driver = self.driver
        #identificamos la barra de busqueda
        search_field = driver.find_element_by_name('q')
        #como buena practica limpiamos la barra de busqueda
        search_field.clear()

        #buscamos las remeras
        search_field.send_keys('tee')
        search_field.submit()

        #identificamos el boton 'add to compare'
        driver.find_element_by_class_name('link-compare').click()

        #hacemos click en el enlace para eliminar la comparacion
        driver.find_element_by_link_text('Clear All').click()

        #hacemos que el driver haga un cambio del focus al alert, preste atencion al alert
        alert = driver.switch_to.alert
        alert_text = alert.text

        #verificamos si el texto que muestra el alert, es el que queremos
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        sleep(3)

        #simulamos un click en el boton 'aceptar
        alert.accept()
        sleep(3)
        

    

    def tearDown(self) -> None:
        self.driver.implicitly_wait(15)
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)