import unittest
from selenium import webdriver
from add_remove_page import AddRemovePage

class AddRemoveElements(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("./ChromeDriver/chromedriver.exe")
        driver = self.driver

    def test(self):
        addremove = AddRemovePage(self.driver)
        addremove.open_addremove()
        addremove.add_remove_elements()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2)