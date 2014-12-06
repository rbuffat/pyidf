import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputVariableDictionary
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputVariableDictionary(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputvariabledictionary(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputVariableDictionary()
        # alpha
        var_key_field = "IDF"
        obj.key_field = var_key_field
        # alpha
        var_sort_option = "Name"
        obj.sort_option = var_sort_option

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputvariabledictionarys[0].key_field, var_key_field)
        self.assertEqual(idf2.outputvariabledictionarys[0].sort_option, var_sort_option)