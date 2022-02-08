from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

#llamamos a nuestros archivos de prueba y las clases de prueba de cada uno
from assertions import AssertionTest
from searchtest import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

# Ahora debemos construir nuestra suit de pruebas
smoke_test = TestSuite([assertions_test, search_test]) #como parametro le pasamos la lista de las variables donde cargamos las pruebas

# ahora indicamos los parametros para generar el reporte

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)