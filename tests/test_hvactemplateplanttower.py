import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantTower
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantTower(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplanttower(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantTower()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_tower_type = "SingleSpeed"
        obj.tower_type = var_tower_type
        # real
        var_high_speed_nominal_capacity = 0.0001
        obj.high_speed_nominal_capacity = var_high_speed_nominal_capacity
        # real
        var_high_speed_fan_power = 0.0001
        obj.high_speed_fan_power = var_high_speed_fan_power
        # real
        var_low_speed_nominal_capacity = 0.0001
        obj.low_speed_nominal_capacity = var_low_speed_nominal_capacity
        # real
        var_low_speed_fan_power = 0.0001
        obj.low_speed_fan_power = var_low_speed_fan_power
        # real
        var_free_convection_capacity = 0.0
        obj.free_convection_capacity = var_free_convection_capacity
        # alpha
        var_priority = "Priority"
        obj.priority = var_priority
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # alpha
        var_template_plant_loop_type = "ChilledWater"
        obj.template_plant_loop_type = var_template_plant_loop_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplanttowers[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplanttowers[0].tower_type, var_tower_type)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].high_speed_nominal_capacity, var_high_speed_nominal_capacity)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].high_speed_fan_power, var_high_speed_fan_power)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].low_speed_nominal_capacity, var_low_speed_nominal_capacity)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].low_speed_fan_power, var_low_speed_fan_power)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].free_convection_capacity, var_free_convection_capacity)
        self.assertEqual(idf2.hvactemplateplanttowers[0].priority, var_priority)
        self.assertAlmostEqual(idf2.hvactemplateplanttowers[0].sizing_factor, var_sizing_factor)
        self.assertEqual(idf2.hvactemplateplanttowers[0].template_plant_loop_type, var_template_plant_loop_type)