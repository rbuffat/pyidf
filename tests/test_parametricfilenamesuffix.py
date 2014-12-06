import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.parametrics import ParametricFileNameSuffix

log = logging.getLogger(__name__)

class TestParametricFileNameSuffix(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_parametricfilenamesuffix(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ParametricFileNameSuffix()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_suffix_for_file_name_in_run_1 = "Suffix for File Name in Run 1"
        paras.append(var_suffix_for_file_name_in_run_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.parametricfilenamesuffixs[0].name, var_name)
        index = obj.extensible_field_index("Suffix for File Name in Run 1")
        self.assertEqual(idf2.parametricfilenamesuffixs[0].extensibles[0][index], var_suffix_for_file_name_in_run_1)