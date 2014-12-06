import os
import tempfile
import unittest
import pyidf
from pyidf.energy_management_system import EnergyManagementSystemSensor
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnergyManagementSystemSensor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemsensor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemSensor()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_outputvariable_or_outputmeter_index_key_name = "Output:Variable or Output:Meter Index Key Name"
        obj.outputvariable_or_outputmeter_index_key_name = var_outputvariable_or_outputmeter_index_key_name
        # external-list
        var_outputvariable_or_outputmeter_name = "external-list|Output:Variable or Output:Meter Name"
        obj.outputvariable_or_outputmeter_name = var_outputvariable_or_outputmeter_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemsensors[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemsensors[0].outputvariable_or_outputmeter_index_key_name, var_outputvariable_or_outputmeter_index_key_name)
        self.assertEqual(idf2.energymanagementsystemsensors[0].outputvariable_or_outputmeter_name, var_outputvariable_or_outputmeter_name)