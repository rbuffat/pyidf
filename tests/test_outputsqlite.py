import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputSqlite
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputSqlite(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputsqlite(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputSqlite()
        # alpha
        var_option_type = "Simple"
        obj.option_type = var_option_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputsqlites[0].option_type, var_option_type)