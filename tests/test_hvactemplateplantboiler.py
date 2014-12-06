import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantBoiler
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantBoiler(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantboiler(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantBoiler()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_boiler_type = "DistrictHotWater"
        obj.boiler_type = var_boiler_type
        # real
        var_capacity = 0.0001
        obj.capacity = var_capacity
        # real
        var_efficiency = 0.5
        obj.efficiency = var_efficiency
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
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
        var_maximum_part_load_ratio = 0.0
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_water_outlet_upper_temperature_limit = 11.11
        obj.water_outlet_upper_temperature_limit = var_water_outlet_upper_temperature_limit
        # alpha
        var_template_plant_loop_type = "HotWater"
        obj.template_plant_loop_type = var_template_plant_loop_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantboilers[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantboilers[0].boiler_type, var_boiler_type)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].capacity, var_capacity)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].efficiency, var_efficiency)
        self.assertEqual(idf2.hvactemplateplantboilers[0].fuel_type, var_fuel_type)
        self.assertEqual(idf2.hvactemplateplantboilers[0].priority, var_priority)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.hvactemplateplantboilers[0].water_outlet_upper_temperature_limit, var_water_outlet_upper_temperature_limit)
        self.assertEqual(idf2.hvactemplateplantboilers[0].template_plant_loop_type, var_template_plant_loop_type)