import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import OutputControlIlluminanceMapStyle
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputControlIlluminanceMapStyle(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontrolilluminancemapstyle(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlIlluminanceMapStyle()
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
        self.assertEqual(idf2.outputcontrolilluminancemapstyles[0].column_separator, var_column_separator)