import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #sirve como una excepcion cuando queramos validar la presencia de un elemento
from selenium.webdriver.common.by import By #nos ayudara a llamar a la excepciones que queremos validar

#Assertions:
# Métodos que permiten validar un valor esperado en la ejecución del test
# Si el resultado es verdadero el test continua, en caso contrario falla y termina
# Ejemplo: assertEqual(price.text, "300")

class AssertionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get('http://demo-store.seleniumacademy.com')


    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    
    def test_language_Option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    #esto nos va a permitir encontrar a los elementos
    # es una funcion de utilidad para encontrar cuando un elemento está presente de acuerdo a sus parámetros
    def is_element_present(self, how, what): #how = tipo de selector, what = valor que tiene
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)


