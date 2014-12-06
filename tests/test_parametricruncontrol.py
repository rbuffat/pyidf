import os
import tempfile
import unittest
import pyidf
from pyidf.parametrics import ParametricRunControl
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestParametricRunControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_parametricruncontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ParametricRunControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_perform_run_1 = "Yes"
        paras.append(var_perform_run_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.parametricruncontrols[0].name, var_name)
        index = obj.extensible_field_index("Perform Run 1")
        self.assertEqual(idf2.parametricruncontrols[0].extensibles[0][index], var_perform_run_1)