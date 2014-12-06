import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemProgramCallingManager

log = logging.getLogger(__name__)

class TestEnergyManagementSystemProgramCallingManager(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemprogramcallingmanager(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemProgramCallingManager()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_energyplus_model_calling_point = "BeginNewEnvironment"
        obj.energyplus_model_calling_point = var_energyplus_model_calling_point
        paras = []
        var_program_name_1 = "object-list|Program Name 1"
        paras.append(var_program_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemprogramcallingmanagers[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemprogramcallingmanagers[0].energyplus_model_calling_point, var_energyplus_model_calling_point)
        index = obj.extensible_field_index("Program Name 1")
        self.assertEqual(idf2.energymanagementsystemprogramcallingmanagers[0].extensibles[0][index], var_program_name_1)