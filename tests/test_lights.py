import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import Lights
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestLights(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lights(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Lights()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # alpha
        var_design_level_calculation_method = "LightingLevel"
        obj.design_level_calculation_method = var_design_level_calculation_method
        # real
        var_lighting_level = 0.0
        obj.lighting_level = var_lighting_level
        # real
        var_watts_per_zone_floor_area = 0.0
        obj.watts_per_zone_floor_area = var_watts_per_zone_floor_area
        # real
        var_watts_per_person = 0.0
        obj.watts_per_person = var_watts_per_person
        # real
        var_return_air_fraction = 0.5
        obj.return_air_fraction = var_return_air_fraction
        # real
        var_fraction_radiant = 0.5
        obj.fraction_radiant = var_fraction_radiant
        # real
        var_fraction_visible = 0.5
        obj.fraction_visible = var_fraction_visible
        # real
        var_fraction_replaceable = 0.5
        obj.fraction_replaceable = var_fraction_replaceable
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # alpha
        var_return_air_fraction_calculated_from_plenum_temperature = "Yes"
        obj.return_air_fraction_calculated_from_plenum_temperature = var_return_air_fraction_calculated_from_plenum_temperature
        # real
        var_return_air_fraction_function_of_plenum_temperature_coefficient_1 = 0.0
        obj.return_air_fraction_function_of_plenum_temperature_coefficient_1 = var_return_air_fraction_function_of_plenum_temperature_coefficient_1
        # real
        var_return_air_fraction_function_of_plenum_temperature_coefficient_2 = 0.0
        obj.return_air_fraction_function_of_plenum_temperature_coefficient_2 = var_return_air_fraction_function_of_plenum_temperature_coefficient_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lightss[0].name, var_name)
        self.assertEqual(idf2.lightss[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.lightss[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.lightss[0].design_level_calculation_method, var_design_level_calculation_method)
        self.assertAlmostEqual(idf2.lightss[0].lighting_level, var_lighting_level)
        self.assertAlmostEqual(idf2.lightss[0].watts_per_zone_floor_area, var_watts_per_zone_floor_area)
        self.assertAlmostEqual(idf2.lightss[0].watts_per_person, var_watts_per_person)
        self.assertAlmostEqual(idf2.lightss[0].return_air_fraction, var_return_air_fraction)
        self.assertAlmostEqual(idf2.lightss[0].fraction_radiant, var_fraction_radiant)
        self.assertAlmostEqual(idf2.lightss[0].fraction_visible, var_fraction_visible)
        self.assertAlmostEqual(idf2.lightss[0].fraction_replaceable, var_fraction_replaceable)
        self.assertEqual(idf2.lightss[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.lightss[0].return_air_fraction_calculated_from_plenum_temperature, var_return_air_fraction_calculated_from_plenum_temperature)
        self.assertAlmostEqual(idf2.lightss[0].return_air_fraction_function_of_plenum_temperature_coefficient_1, var_return_air_fraction_function_of_plenum_temperature_coefficient_1)
        self.assertAlmostEqual(idf2.lightss[0].return_air_fraction_function_of_plenum_temperature_coefficient_2, var_return_air_fraction_function_of_plenum_temperature_coefficient_2)