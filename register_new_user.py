import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")


    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #verificamos que el boton 'crear cuenta nueva' esté visible para el usuario y verificamos que esté habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        #ahora hacemos click sobre el boton habiendo verificado lo anterior
        create_account_button.click()

        #corroboramos que estamos en la página que el anterior click nos deberia llevar
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        new_letter_suscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')
        
        #ahora verificamos que cada elemento esté habilitado, a simple vista se puede ver, pero es una buena practica hacerlo de todas maneras

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and new_letter_suscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        #ahora necesitamos enviar datos a cada uno de esos campos (fields)
        first_name.send_keys('Test')
        driver.implicitly_wait(1)
        middle_name.send_keys('Test')
        driver.implicitly_wait(1)
        last_name.send_keys('Test')
        driver.implicitly_wait(1)
        email_address.send_keys('Test@testingmail.com')
        driver.implicitly_wait(1)
        password.send_keys('Test')
        driver.implicitly_wait(1)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(1)
        submit_button.click()
        


    def tearDown(self) -> None:
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)