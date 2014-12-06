import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantChiller
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantChiller(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantchiller(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantChiller()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_chiller_type = "DistrictChilledWater"
        obj.chiller_type = var_chiller_type
        # real
        var_capacity = 0.0001
        obj.capacity = var_capacity
        # real
        var_nominal_cop = 0.0001
        obj.nominal_cop = var_nominal_cop
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # alpha
        var_priority = "Priority"
        obj.priority = var_priority
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # real
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0001
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0001
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_minimum_unloading_ratio = 0.0
        obj.minimum_unloading_ratio = var_minimum_unloading_ratio
        # real
        var_leaving_chilled_water_lower_temperature_limit = 12.12
        obj.leaving_chilled_water_lower_temperature_limit = var_leaving_chilled_water_lower_temperature_limit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantchillers[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantchillers[0].chiller_type, var_chiller_type)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].capacity, var_capacity)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].nominal_cop, var_nominal_cop)
        self.assertEqual(idf2.hvactemplateplantchillers[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.hvactemplateplantchillers[0].priority, var_priority)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].minimum_unloading_ratio, var_minimum_unloading_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantchillers[0].leaving_chilled_water_lower_temperature_limit, var_leaving_chilled_water_lower_temperature_limit)