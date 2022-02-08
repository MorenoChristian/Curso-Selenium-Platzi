import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Typos').click()


    def test_typos(self):
        driver = self.driver

        tries = 1

        paragraph = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        test_paragraph = paragraph.text
        
        correct_paragraph = "Sometimes you'll see a typo, other times you won't."

        while test_paragraph != correct_paragraph:
            try:
                paragraph = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
                test_paragraph = paragraph.text
                self.assertEqual(test_paragraph, correct_paragraph)
            except:
                print("The paragraphs are diferent")
                tries += 1
                sleep(2)
                driver.refresh()

        print(f"Paragraph was found in {tries} attemps")

    def tearDown(self) -> None:
        self.driver.close()        


if __name__ == '__main__':
    unittest.main(verbosity=2)