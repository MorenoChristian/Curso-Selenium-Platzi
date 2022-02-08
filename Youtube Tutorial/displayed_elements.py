import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DisplayedElement(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    
    def test_displayed_element(self):
        driver = self.driver
        driver.get('http://www.google.com')

        # find web element 'feel lucky'
        displayed_element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')))

        print("'Feel lucky' is diplayed?:")
        print(displayed_element.is_displayed()) #return true or false if the element is displayed
        print("'Feel lucky' is enabled?:")
        print(displayed_element.is_enabled()) #return true or false if the element if enabled

        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
