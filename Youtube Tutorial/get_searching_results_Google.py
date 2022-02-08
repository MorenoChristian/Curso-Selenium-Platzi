import unittest
from selenium import webdriver
from time import sleep

class GetResults(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')

    def test_get_results(self):
        driver = self.driver
        driver.get('http://www.google.com')

        search = 'seleni'

        search_field = driver.find_element_by_name('q')
        search_field.send_keys(search)
        sleep(2)

        result_list = []
        
        for i in range(10):
            result = driver.find_element_by_xpath(f'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[{(i + 1)}]/div/div[2]/div[1]/span')
            result_list.append(result.text)

        print("Showing the result list: ")

        for i in result_list:
            print(i)
                                                   
    
    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
