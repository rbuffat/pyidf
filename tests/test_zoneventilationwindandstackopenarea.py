import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneVentilationWindandStackOpenArea

log = logging.getLogger(__name__)

class TestZoneVentilationWindandStackOpenArea(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneventilationwindandstackopenarea(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneVentilationWindandStackOpenArea()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_opening_area = 0.0
        obj.opening_area = var_opening_area
        # object-list
        var_opening_area_fraction_schedule_name = "object-list|Opening Area Fraction Schedule Name"
        obj.opening_area_fraction_schedule_name = var_opening_area_fraction_schedule_name
        # real
        var_opening_effectiveness = 0.5
        obj.opening_effectiveness = var_opening_effectiveness
        # real
        var_effective_angle = 179.99995
        obj.effective_angle = var_effective_angle
        # real
        var_height_difference = 0.0
        obj.height_difference = var_height_difference
        # real
        var_discharge_coefficient_for_opening = 0.5
        obj.discharge_coefficient_for_opening = var_discharge_coefficient_for_opening
        # real
        var_minimum_indoor_temperature = 0.0
        obj.minimum_indoor_temperature = var_minimum_indoor_temperature
        # object-list
        var_minimum_indoor_temperature_schedule_name = "object-list|Minimum Indoor Temperature Schedule Name"
        obj.minimum_indoor_temperature_schedule_name = var_minimum_indoor_temperature_schedule_name
        # real
        var_maximum_indoor_temperature = 0.0
        obj.maximum_indoor_temperature = var_maximum_indoor_temperature
        # object-list
        var_maximum_indoor_temperature_schedule_name = "object-list|Maximum Indoor Temperature Schedule Name"
        obj.maximum_indoor_temperature_schedule_name = var_maximum_indoor_temperature_schedule_name
        # real
        var_delta_temperature = -100.0
        obj.delta_temperature = var_delta_temperature
        # object-list
        var_delta_temperature_schedule_name = "object-list|Delta Temperature Schedule Name"
        obj.delta_temperature_schedule_name = var_delta_temperature_schedule_name
        # real
        var_minimum_outdoor_temperature = 0.0
        obj.minimum_outdoor_temperature = var_minimum_outdoor_temperature
        # object-list
        var_minimum_outdoor_temperature_schedule_name = "object-list|Minimum Outdoor Temperature Schedule Name"
        obj.minimum_outdoor_temperature_schedule_name = var_minimum_outdoor_temperature_schedule_name
        # real
        var_maximum_outdoor_temperature = 0.0
        obj.maximum_outdoor_temperature = var_maximum_outdoor_temperature
        # object-list
        var_maximum_outdoor_temperature_schedule_name = "object-list|Maximum Outdoor Temperature Schedule Name"
        obj.maximum_outdoor_temperature_schedule_name = var_maximum_outdoor_temperature_schedule_name
        # real
        var_maximum_wind_speed = 20.0
        obj.maximum_wind_speed = var_maximum_wind_speed

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].name, var_name)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].opening_area, var_opening_area)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].opening_area_fraction_schedule_name, var_opening_area_fraction_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].opening_effectiveness, var_opening_effectiveness)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].effective_angle, var_effective_angle)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].height_difference, var_height_difference)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].discharge_coefficient_for_opening, var_discharge_coefficient_for_opening)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].minimum_indoor_temperature, var_minimum_indoor_temperature)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].minimum_indoor_temperature_schedule_name, var_minimum_indoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].maximum_indoor_temperature, var_maximum_indoor_temperature)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].maximum_indoor_temperature_schedule_name, var_maximum_indoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].delta_temperature, var_delta_temperature)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].delta_temperature_schedule_name, var_delta_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].minimum_outdoor_temperature, var_minimum_outdoor_temperature)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].minimum_outdoor_temperature_schedule_name, var_minimum_outdoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].maximum_outdoor_temperature, var_maximum_outdoor_temperature)
        self.assertEqual(idf2.zoneventilationwindandstackopenareas[0].maximum_outdoor_temperature_schedule_name, var_maximum_outdoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationwindandstackopenareas[0].maximum_wind_speed, var_maximum_wind_speed)