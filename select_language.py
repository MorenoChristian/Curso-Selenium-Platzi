import unittest
from selenium import webdriver
from selenium.webdriver.support import select
# Sirve para poder elegir opciones en un dropdown (lista desplegable)
from selenium.webdriver.support.ui import Select

class SelectLanguage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')


    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        #para acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))

        #validamos que el dropdown tenga 3 opciones
        self.assertEqual(3, len(select_language.options)) # .options nos permite ingresar a las opciones del dropdown

        #vamos a iterar por cada una de las opciones que tiene el dropdown
        for option in select_language.options:
            act_options.append(option.text) # añadimos el texto de la opcion, no la opcion en sí

        #comparamos si las listas son iguales
        self.assertListEqual(exp_options, act_options)

        #Verificamos que 'English' sea la opcion que tiene por defecto el dropdown, es simplemente una validacion
        self.assertEqual('English', select_language.first_selected_option.text)

        #seleccionamos el idioma ALEMAN por el texto visible
        select_language.select_by_visible_text('German')
        
        #verificamos que esté verdaderamente seleccionado el idioma aleman comparando la url de la página
        self.assertTrue('store=german' in self.driver.current_url)

        # otra opcion de elegir un idioma es a traves del indice (index)
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(1)
        



    def tearDown(self) -> None:
        self.driver.implicitly_wait(15)
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)