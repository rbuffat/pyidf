import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import ElectricLoadCenterGenerators
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestElectricLoadCenterGenerators(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcentergenerators(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterGenerators()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_generator_1_name = "object-list|Generator 1 Name"
        paras.append(var_generator_1_name)
        var_generator_1_object_type = "Generator:InternalCombustionEngine"
        paras.append(var_generator_1_object_type)
        var_generator_1_rated_electric_power_output = 4.4
        paras.append(var_generator_1_rated_electric_power_output)
        var_generator_1_availability_schedule_name = "object-list|Generator 1 Availability Schedule Name"
        paras.append(var_generator_1_availability_schedule_name)
        var_generator_1_rated_thermal_to_electrical_power_ratio = 6.6
        paras.append(var_generator_1_rated_thermal_to_electrical_power_ratio)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcentergeneratorss[0].name, var_name)
        index = obj.extensible_field_index("Generator 1 Name")
        self.assertEqual(idf2.electricloadcentergeneratorss[0].extensibles[0][index], var_generator_1_name)
        index = obj.extensible_field_index("Generator 1 Object Type")
        self.assertEqual(idf2.electricloadcentergeneratorss[0].extensibles[0][index], var_generator_1_object_type)
        index = obj.extensible_field_index("Generator 1 Rated Electric Power Output")
        self.assertAlmostEqual(idf2.electricloadcentergeneratorss[0].extensibles[0][index], var_generator_1_rated_electric_power_output)
        index = obj.extensible_field_index("Generator 1 Availability Schedule Name")
        self.assertEqual(idf2.electricloadcentergeneratorss[0].extensibles[0][index], var_generator_1_availability_schedule_name)
        index = obj.extensible_field_index("Generator 1 Rated Thermal to Electrical Power Ratio")
        self.assertAlmostEqual(idf2.electricloadcentergeneratorss[0].extensibles[0][index], var_generator_1_rated_thermal_to_electrical_power_ratio)