import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC

class MercadoPage(object):
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    def open(self):
        self._driver.get(self._url)

    def country(self, pais):
        self._driver.find_element_by_link_text(pais).click()

    def type_search(self, keyword):
        search_field = self._driver.find_element_by_name('as_word')
        search_field.clear()
        search_field.send_keys(keyword)

    def click_submit(self):
        search_field = self._driver.find_element_by_name('as_word')
        search_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    def new_filter(self):
        self._driver.find_element_by_partial_link_text('Nuevo').click()

    def bogota_filter(self):
        self._driver.find_element_by_partial_link_text('Bogotá D.C.').click()

    def low_price(self):
        self._driver.find_element_by_class_name('andes-dropdown__trigger').click()
        self._driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[1]/div[2]/div[2]/div').click()

    def order_first_elements(self):
        names = []
        
        for i in range(3):
            article_name = self._driver.find_element_by_xpath(f"/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2").text
            names.append(article_name)
        
        return names
        