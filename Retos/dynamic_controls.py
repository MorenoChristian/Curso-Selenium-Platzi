import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class DynamicControls(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Dynamic Controls').click()

    
    def test_dynamic_controls(self):
        driver = self.driver
        
#################### Identificamos el checkbox y el boton para remover y agregar, se agrega espera entre una accion y otra######################
        check_box = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        check_box.click()

        add_remove_button = driver.find_element_by_css_selector('#checkbox-example > button')
        add_remove_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        add_remove_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox')))

################ Identifico el botón para habilitar el textbox, esperamos y le agregamos un string ###################

        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()

        text_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > input[type=text]')))
        text_box.send_keys('Pero mas bien, loquita!!')
        sleep(2)



    


    def tearDown(self) -> None:
        self.driver.close()


if __name__=='__main__':
    unittest.main()