'''Page Object Model es un patrón de diseño utilizado en Testing, el cual, tiene beneficios para la elaboración de Tests.
Funcionamiento:
-En vez de tener nuestros Test en un solo archivo, los tendremos abstraídos en una nueva capa llamada Pages, donde tendremos los Tests en archivos independientes, haciendo referencia al sitio donde se aplica (Home, Login, etc).

A los archivos independientes se les agregará un nuevo archivo que es el Page Object, el cual se encargará de tomar los Tests que se están realizando y validarlas contra los Tests Cases.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    def __init__(self, driver) -> None:
        self._driver = driver
        self._url = 'http://google.com'
        self.search_locator = 'q'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()
    
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()