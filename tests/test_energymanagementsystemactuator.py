import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemActuator

log = logging.getLogger(__name__)

class TestEnergyManagementSystemActuator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemactuator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemActuator()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_actuated_component_unique_name = "Actuated Component Unique Name"
        obj.actuated_component_unique_name = var_actuated_component_unique_name
        # alpha
        var_actuated_component_type = "Actuated Component Type"
        obj.actuated_component_type = var_actuated_component_type
        # alpha
        var_actuated_component_control_type = "Actuated Component Control Type"
        obj.actuated_component_control_type = var_actuated_component_control_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemactuators[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemactuators[0].actuated_component_unique_name, var_actuated_component_unique_name)
        self.assertEqual(idf2.energymanagementsystemactuators[0].actuated_component_type, var_actuated_component_type)
        self.assertEqual(idf2.energymanagementsystemactuators[0].actuated_component_control_type, var_actuated_component_control_type)