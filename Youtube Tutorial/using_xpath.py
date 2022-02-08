import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_xpath(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')


    def test_search_by_xpath(self):
        driver = self.driver
        driver.get('https://www.google.com')
        sleep(1)
        # xpath is used when we don´t have id, name, class or the code is changing very often
        # Absolute Xpath: It uses Complete path from the Root Element to the desire element.
        #                 utiliza la ruta completa desde el elemento raiz hasta el elemento deseado

        # Relative Xpath: You can simply start by referencing the element you want and go from there.
        #                 simplemente puedes comenzar haciendo referencia del elemento que quieras e ir desde allí

        # Relative Xpaths are always preferred as they are not the complete paths from the root element. 
        # los xpath relativos siempre se prefieren, ya que no son las rutas completas desde el elemento raiz

        # (//html//body). Because in future, if any webelement is added/removed, then the absolute Xpath changes. So Always use Relative Xpaths in your Automation.
        # porque en el futuro si un elemento de la web se adhiere o elimina, entonces el xpath absoluto cambia. Entonces siempre utiliza el xpath relativo en tus automatizaciones

        search_by_xpath = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        sleep(1)
        search_by_xpath.send_keys("selenium", Keys.ARROW_DOWN, Keys.ENTER)
        sleep(1)


    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

