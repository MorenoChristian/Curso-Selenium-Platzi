import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from pyunitreport import HTMLTestRunner

#esta nueva funcion servirá para consultar nuestro archivo csv
def get_data(file_name):
    rows = [] #con esto indicaremos el numero de filas que hay
    data_file = open(file_name, 'r') #abrimos el archivo csv en modo lectura
    reader = csv.reader(data_file) #a la libreria csv le decimos que lea especificamente los datos de 'data_file'
    next(reader, None) # de esta forma omitimos la cabezera

    #con este ciclo for recorremos reader y lo guardamos en rows y lo retornamos
    for row in reader:
        rows.append(row)
    return rows


@ddt
class SeacrhDDT(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='C:/Users/Christian/Desktop/Informatorio/2da Etapa/Programación Web/Python/Platzi/Curso Selenium/ChromeDriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    #el decorador data va a incluir tuplas con los terminos que vamos a buscar
    @data(*get_data('testdata.csv'))
    @unpack #nos va a permitir desempaquetar las tuplas y consultarlas de forma individual
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        
        #lo pasamos a entero para que no haya ningun error al trabajar con expected_count
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results', message)

        print(f"Found {len(products)} products")


    def tearDown(self) -> None:
        self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Search_CSV_DDT'))