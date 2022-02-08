import unittest #servirá para traer todas nuestras pruebas
from pyunitreport import HTMLTestRunner #Ayudara a orquestar cada una de las preubas que ejecutemos junto con los reportes
from selenium import webdriver #para comunicarse con el navergador

#En primer lugar tenemos una clase que se divide en 3 componentes o mas
class HelloWorld(unittest.TestCase): 

    #con 'Classmethod' y agragando 'Class' a setup y a teardown, tmb cambiando self por 'cls' hacemos que las pruebas se realizen en una sola ventana de chrome
    @classmethod
    #setUp va a ejecutar todo lo necesario antes de hacer una prueba, va a preparar el entonro de la prueba misma
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10) #con esto le decimes al driver que espere 10 segundos antes de hacer la siguiente prueba

    #Nuestro caso de prueba, que va a realizar una serie de acciones para que el navegador los automatize
    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('http://www.wikipedia.org')
        

    @classmethod
    #va a ocurrir otras accioens para finalizar, "cerrar la ventana del navegador al hacer pruebas para evitar fuga de datos"
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))


