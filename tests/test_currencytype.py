import os
import tempfile
import unittest
import pyidf
from pyidf.economics import CurrencyType
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCurrencyType(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_currencytype(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurrencyType()
        # alpha
        var_monetary_unit = "USD"
        obj.monetary_unit = var_monetary_unit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.currencytypes[0].monetary_unit, var_monetary_unit)