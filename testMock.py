import clases
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):
    
    def testDeboReportarmeConsulta(self):
        clases.diasHastaFecha = MagicMock(return_value=16)
        a = clases.Consulta("Quiero saber cómo tener un abogado gratuito por cuota alimentaria", "pendiente", 11, 3, 2020).deboReportarme()
        
        esperado = True
        self.assertEqual(a, esperado)
        
if __name__ == '__main__':
    unittest.main()
