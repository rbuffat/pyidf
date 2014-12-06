import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputControlTableStyle
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputControlTableStyle(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontroltablestyle(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlTableStyle()
        # alpha
        var_column_separator = "Comma"
        obj.column_separator = var_column_separator
        # alpha
        var_unit_conversion = "None"
        obj.unit_conversion = var_unit_conversion

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputcontroltablestyles[0].column_separator, var_column_separator)
        self.assertEqual(idf2.outputcontroltablestyles[0].unit_conversion, var_unit_conversion)