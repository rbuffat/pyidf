import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemConstructionIndexVariable

log = logging.getLogger(__name__)

class TestEnergyManagementSystemConstructionIndexVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemconstructionindexvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemConstructionIndexVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_object_name = "object-list|Construction Object Name"
        obj.construction_object_name = var_construction_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemconstructionindexvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemconstructionindexvariables[0].construction_object_name, var_construction_object_name)