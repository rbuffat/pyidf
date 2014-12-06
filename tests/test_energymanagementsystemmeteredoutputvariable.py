import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemMeteredOutputVariable

log = logging.getLogger(__name__)

class TestEnergyManagementSystemMeteredOutputVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemmeteredoutputvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemMeteredOutputVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_ems_variable_name = "EMS Variable Name"
        obj.ems_variable_name = var_ems_variable_name
        # alpha
        var_update_frequency = "ZoneTimestep"
        obj.update_frequency = var_update_frequency
        # alpha
        var_ems_program_or_subroutine_name = "EMS Program or Subroutine Name"
        obj.ems_program_or_subroutine_name = var_ems_program_or_subroutine_name
        # alpha
        var_resource_type = "Electricity"
        obj.resource_type = var_resource_type
        # alpha
        var_group_type = "Building"
        obj.group_type = var_group_type
        # alpha
        var_enduse_category = "Heating"
        obj.enduse_category = var_enduse_category
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
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
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].ems_variable_name, var_ems_variable_name)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].update_frequency, var_update_frequency)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].ems_program_or_subroutine_name, var_ems_program_or_subroutine_name)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].resource_type, var_resource_type)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].group_type, var_group_type)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].enduse_category, var_enduse_category)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.energymanagementsystemmeteredoutputvariables[0].units, var_units)