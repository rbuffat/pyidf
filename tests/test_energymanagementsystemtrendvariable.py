import os
import tempfile
import unittest
import pyidf
from pyidf.energy_management_system import EnergyManagementSystemTrendVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnergyManagementSystemTrendVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemtrendvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemTrendVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_ems_variable_name = "EMS Variable Name"
        obj.ems_variable_name = var_ems_variable_name
        # integer
        var_number_of_timesteps_to_be_logged = 1
        obj.number_of_timesteps_to_be_logged = var_number_of_timesteps_to_be_logged

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemtrendvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemtrendvariables[0].ems_variable_name, var_ems_variable_name)
        self.assertEqual(idf2.energymanagementsystemtrendvariables[0].number_of_timesteps_to_be_logged, var_number_of_timesteps_to_be_logged)