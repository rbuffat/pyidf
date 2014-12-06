import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterfaceActuator
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterfaceActuator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfaceactuator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceActuator()
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
        # real
        var_optional_initial_value = 5.5
        obj.optional_initial_value = var_optional_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfaceactuators[0].name, var_name)
        self.assertEqual(idf2.externalinterfaceactuators[0].actuated_component_unique_name, var_actuated_component_unique_name)
        self.assertEqual(idf2.externalinterfaceactuators[0].actuated_component_type, var_actuated_component_type)
        self.assertEqual(idf2.externalinterfaceactuators[0].actuated_component_control_type, var_actuated_component_control_type)
        self.assertAlmostEqual(idf2.externalinterfaceactuators[0].optional_initial_value, var_optional_initial_value)