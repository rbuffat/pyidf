import os
import tempfile
import unittest
import pyidf
from pyidf.energy_management_system import EnergyManagementSystemInternalVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnergyManagementSystemInternalVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsysteminternalvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemInternalVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_internal_data_index_key_name = "Internal Data Index Key Name"
        obj.internal_data_index_key_name = var_internal_data_index_key_name
        # alpha
        var_internal_data_type = "Internal Data Type"
        obj.internal_data_type = var_internal_data_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsysteminternalvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsysteminternalvariables[0].internal_data_index_key_name, var_internal_data_index_key_name)
        self.assertEqual(idf2.energymanagementsysteminternalvariables[0].internal_data_type, var_internal_data_type)