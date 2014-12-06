import os
import tempfile
import unittest
import pyidf
from pyidf.energy_management_system import EnergyManagementSystemProgram
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnergyManagementSystemProgram(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemprogram(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemProgram()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_program_line_1 = "Program Line 1"
        paras.append(var_program_line_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemprograms[0].name, var_name)
        index = obj.extensible_field_index("Program Line 1")
        self.assertEqual(idf2.energymanagementsystemprograms[0].extensibles[0][index], var_program_line_1)