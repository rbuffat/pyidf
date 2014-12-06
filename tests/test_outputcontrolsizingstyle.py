import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_design_objects import OutputControlSizingStyle
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputControlSizingStyle(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontrolsizingstyle(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlSizingStyle()
        # alpha
        var_column_separator = "Comma"
        obj.column_separator = var_column_separator

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputcontrolsizingstyles[0].column_separator, var_column_separator)