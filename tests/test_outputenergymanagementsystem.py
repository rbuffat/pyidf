import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputEnergyManagementSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputEnergyManagementSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputenergymanagementsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputEnergyManagementSystem()
        # alpha
        var_actuator_availability_dictionary_reporting = "None"
        obj.actuator_availability_dictionary_reporting = var_actuator_availability_dictionary_reporting
        # alpha
        var_internal_variable_availability_dictionary_reporting = "None"
        obj.internal_variable_availability_dictionary_reporting = var_internal_variable_availability_dictionary_reporting
        # alpha
        var_ems_runtime_language_debug_output_level = "None"
        obj.ems_runtime_language_debug_output_level = var_ems_runtime_language_debug_output_level

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputenergymanagementsystems[0].actuator_availability_dictionary_reporting, var_actuator_availability_dictionary_reporting)
        self.assertEqual(idf2.outputenergymanagementsystems[0].internal_variable_availability_dictionary_reporting, var_internal_variable_availability_dictionary_reporting)
        self.assertEqual(idf2.outputenergymanagementsystems[0].ems_runtime_language_debug_output_level, var_ems_runtime_language_debug_output_level)