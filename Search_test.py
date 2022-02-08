import unittest
from pyunitreport.runner import HTMLTestRunner

from selenium import webdriver


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path = './ChromeDriver/chromedriver.exe')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        #'assert' validacion que hacemos en el código para verificar que una condicion se cumple o no
        # contamos que sean 3 imagenes de acuerdo a la longitud de banners
        self.assertEqual(3, len(banners))

    #encontrar imagen del medio con su xpath
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[3]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output='reportes', report_name='Search-Field'))