import os
import tempfile
import unittest
import pyidf
from pyidf.energy_management_system import EnergyManagementSystemGlobalVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnergyManagementSystemGlobalVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemglobalvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemGlobalVariable()
        paras = []
        var_erl_variable_1_name = "Erl Variable 1 Name"
        paras.append(var_erl_variable_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        index = obj.extensible_field_index("Erl Variable 1 Name")
        self.assertEqual(idf2.energymanagementsystemglobalvariables[0].extensibles[0][index], var_erl_variable_1_name)