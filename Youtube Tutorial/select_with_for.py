import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

class ToggleSwitch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    
    def test_select(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')

        select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select')
        # 'tag_name' refers to the tag in HTML
        options = select.find_elements_by_tag_name('option')
        sleep(2)

        for option in options:
            print(f"The values are {option.get_attribute('value')}: {option.text}")
            option.click()
        
        selecting = Select(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
        selecting.select_by_value("10")
        sleep(2)
        
    def test_select2(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')

        select = Select(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
        self.assertEqual(13, len(select.options))

        for option in select.options:
            print(f"Value: {option.get_attribute('value')} Marc: {option.text}")
        
        select.select_by_index(10)
        sleep(2)
        
        

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()