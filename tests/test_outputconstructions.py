import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputConstructions
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputConstructions(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputconstructions(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputConstructions()
        # alpha
        var_details_type_1 = "Constructions"
        obj.details_type_1 = var_details_type_1
        # alpha
        var_details_type_2 = "Constructions"
        obj.details_type_2 = var_details_type_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputconstructionss[0].details_type_1, var_details_type_1)
        self.assertEqual(idf2.outputconstructionss[0].details_type_2, var_details_type_2)