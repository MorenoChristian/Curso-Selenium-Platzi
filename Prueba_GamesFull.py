import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class GamesFull(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.get('https://compragamer.com/?gclid=CjwKCAjw8KmLBhB8EiwAQbqNoDSwnJEIyj1WZBSUF9qmM2A5JVbMUKLd75x1lLdmiiQhrEEWEei5TBoCmIsQAvD_BwE')
        driver.maximize_window()
        driver.implicitly_wait(10)

    
    def test_search_field(self):
        driver = self.driver
        driver.find_element_by_class_name('product-search__field').send_keys('Intel Pentium')
        driver.find_element_by_id('botonBusqueda').click()
        driver.find_element_by_xpath('//*[@id="soyBody"]/div/cgw-patch/div/div/cgw-products/div/div/div/div[2]/cgw-products-list/div[3]/cgw-product-alone/div/div[2]/div[1]/a').click()
       
        
        




    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name = 'CompraGamer'))