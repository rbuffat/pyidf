import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitImportToActuator
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterfaceFunctionalMockupUnitImportToActuator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitimporttoactuator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitImportToActuator()
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
        # object-list
        var_fmu_file_name = "object-list|FMU File Name"
        obj.fmu_file_name = var_fmu_file_name
        # alpha
        var_fmu_instance_name = "FMU Instance Name"
        obj.fmu_instance_name = var_fmu_instance_name
        # alpha
        var_fmu_variable_name = "FMU Variable Name"
        obj.fmu_variable_name = var_fmu_variable_name
        # real
        var_initial_value = 8.8
        obj.initial_value = var_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].name, var_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].actuated_component_unique_name, var_actuated_component_unique_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].actuated_component_type, var_actuated_component_type)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].actuated_component_control_type, var_actuated_component_control_type)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].fmu_file_name, var_fmu_file_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].fmu_instance_name, var_fmu_instance_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].fmu_variable_name, var_fmu_variable_name)
        self.assertAlmostEqual(idf2.externalinterfacefunctionalmockupunitimporttoactuators[0].initial_value, var_initial_value)