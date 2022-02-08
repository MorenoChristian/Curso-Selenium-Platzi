import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ClickRadioButton(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')


    def test_using_radio_button(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')
        # wait 10 seconds until radio button is found
        WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.NAME, 'same')))

        # click on radio buttons
        radio_bt_two = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[4]')
        radio_bt_two.click()
        sleep(2)

        radio_bt_one = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[3]')
        radio_bt_one.click()
        sleep(2)



    def tearDown(self) -> None:
        self.driver.quit()


if __name__=='__main__':
    unittest.main()