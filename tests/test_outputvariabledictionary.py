import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputVariableDictionary

log = logging.getLogger(__name__)

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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputvariabledictionarys[0].key_field, var_key_field)
        self.assertEqual(idf2.outputvariabledictionarys[0].sort_option, var_sort_option)