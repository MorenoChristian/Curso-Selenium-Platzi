from typing import _SpecialForm
from selenium import webdriver
from time import sleep

class AddRemovePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._ulr = "http://the-internet.herokuapp.com"


    #abrimos la pagina del test
    def open_addremove(self):
        self._driver.get(self._ulr)
        self._driver.find_element_by_link_text("Add/Remove Elements").click()
    
    def add_remove_elements(self):
        add = int(input("How many elements do you want add?: "))
        remove = int(input("How many elements do you want delete?: "))
        add_button = self._driver.find_element_by_xpath('//*[@id="content"]/div/button')
        

        # with this we got total elements in the screen
        total_elements = add - remove

        #this is to add elements
        for i in range(add):
            add_button.click()
            sleep(1)

        #this is to remove elements
        for i in range(remove):
            try:
                remove_button = self._driver.find_element_by_xpath('//*[@id="elements"]/button')
                remove_button.click()
                
            except:
                print("You´r trying to remove more elements than the exist")
                break
        
        if total_elements > 0:
            print(f"They are {total_elements} on screen")
        else:
            print("They are 0 elements on screen")
        sleep(2)

        

    

        