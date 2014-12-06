import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemOutputVariable

log = logging.getLogger(__name__)

class TestEnergyManagementSystemOutputVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemoutputvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemOutputVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_ems_variable_name = "EMS Variable Name"
        obj.ems_variable_name = var_ems_variable_name
        # alpha
        var_type_of_data_in_variable = "Averaged"
        obj.type_of_data_in_variable = var_type_of_data_in_variable
        # alpha
        var_update_frequency = "ZoneTimestep"
        obj.update_frequency = var_update_frequency
        # alpha
        var_ems_program_or_subroutine_name = "EMS Program or Subroutine Name"
        obj.ems_program_or_subroutine_name = var_ems_program_or_subroutine_name
        # alpha
        var_units = "Units"
        obj.units = var_units

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].ems_variable_name, var_ems_variable_name)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].type_of_data_in_variable, var_type_of_data_in_variable)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].update_frequency, var_update_frequency)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].ems_program_or_subroutine_name, var_ems_program_or_subroutine_name)
        self.assertEqual(idf2.energymanagementsystemoutputvariables[0].units, var_units)