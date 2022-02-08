import unittest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class HyperLink(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')


    def test_hyper_links(self):
        driver = self.driver
        driver.get('https://www.w3schools.com')
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Learn PHP')))

        find_link = driver.find_element_by_link_text('Learn PHP')
        find_link.click()

        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()