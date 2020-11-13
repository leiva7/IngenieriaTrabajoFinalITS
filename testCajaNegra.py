import clases
import unittest

class TestClases(unittest.TestCase):
    
    def testDiasHastaFecha(self):
        self.assertEqual(clases.diasHastaFecha(2, 11, 2020, 11, 11, 2020), 9)

if __name__ == '__main__':
    unittest.main()


