import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Google_Page(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://google.com'

    # open google.com
    def open_google(self):
        self._driver.get(self._url)
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.NAME, 'q')))
    
    def _search_gmail_google(self, keyword):
        search_field = self._driver.find_element_by_name('q')
        search_field.send_keys(keyword)

    def _submit_search(self):
        search_field = self._driver.find_element_by_name('q')
        search_field.submit()

    def search(self, keyword):
        self._search_gmail_google(keyword)
        self._submit_search()

    def open_gmail(self):
        self._driver.find_element_by_css_selector('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a').click()
        





        