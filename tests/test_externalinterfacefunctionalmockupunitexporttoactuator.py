import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitExportToActuator

log = logging.getLogger(__name__)

class TestExternalInterfaceFunctionalMockupUnitExportToActuator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitexporttoactuator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitExportToActuator()
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
        # alpha
        var_fmu_variable_name = "FMU Variable Name"
        obj.fmu_variable_name = var_fmu_variable_name
        # real
        var_initial_value = 6.6
        obj.initial_value = var_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].name, var_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].actuated_component_unique_name, var_actuated_component_unique_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].actuated_component_type, var_actuated_component_type)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].actuated_component_control_type, var_actuated_component_control_type)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].fmu_variable_name, var_fmu_variable_name)
        self.assertAlmostEqual(idf2.externalinterfacefunctionalmockupunitexporttoactuators[0].initial_value, var_initial_value)