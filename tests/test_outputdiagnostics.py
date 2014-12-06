import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputDiagnostics
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputDiagnostics(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputdiagnostics(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputDiagnostics()
        # alpha
        var_key_1 = "DisplayAllWarnings"
        obj.key_1 = var_key_1
        # alpha
        var_key_2 = "DisplayAllWarnings"
        obj.key_2 = var_key_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputdiagnosticss[0].key_1, var_key_1)
        self.assertEqual(idf2.outputdiagnosticss[0].key_2, var_key_2)