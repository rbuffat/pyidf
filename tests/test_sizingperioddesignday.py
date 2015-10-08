import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SizingPeriodDesignDay

log = logging.getLogger(__name__)

class TestSizingPeriodDesignDay(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingperioddesignday(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingPeriodDesignDay()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_month = 6
        obj.month = var_month
        # integer
        var_day_of_month = 16
        obj.day_of_month = var_day_of_month
        # alpha
        var_day_type = "Sunday"
        obj.day_type = var_day_type
        # real
        var_maximum_drybulb_temperature = -10.0
        obj.maximum_drybulb_temperature = var_maximum_drybulb_temperature
        # real
        var_daily_drybulb_temperature_range = 0.0
        obj.daily_drybulb_temperature_range = var_daily_drybulb_temperature_range
        # alpha
        var_drybulb_temperature_range_modifier_type = "MultiplierSchedule"
        obj.drybulb_temperature_range_modifier_type = var_drybulb_temperature_range_modifier_type
        # object-list
        var_drybulb_temperature_range_modifier_day_schedule_name = "object-list|Dry-Bulb Temperature Range Modifier Day Schedule Name"
        obj.drybulb_temperature_range_modifier_day_schedule_name = var_drybulb_temperature_range_modifier_day_schedule_name
        # alpha
        var_humidity_condition_type = "WetBulb"
        obj.humidity_condition_type = var_humidity_condition_type
        # real
        var_wetbulb_or_dewpoint_at_maximum_drybulb = 10.1
        obj.wetbulb_or_dewpoint_at_maximum_drybulb = var_wetbulb_or_dewpoint_at_maximum_drybulb
        # object-list
        var_humidity_condition_day_schedule_name = "object-list|Humidity Condition Day Schedule Name"
        obj.humidity_condition_day_schedule_name = var_humidity_condition_day_schedule_name
        # real
        var_humidity_ratio_at_maximum_drybulb = 12.12
        obj.humidity_ratio_at_maximum_drybulb = var_humidity_ratio_at_maximum_drybulb
        # real
        var_enthalpy_at_maximum_drybulb = 13.13
        obj.enthalpy_at_maximum_drybulb = var_enthalpy_at_maximum_drybulb
        # real
        var_daily_wetbulb_temperature_range = 14.14
        obj.daily_wetbulb_temperature_range = var_daily_wetbulb_temperature_range
        # real
        var_barometric_pressure = 75500.0
        obj.barometric_pressure = var_barometric_pressure
        # real
        var_wind_speed = 20.0
        obj.wind_speed = var_wind_speed
        # real
        var_wind_direction = 180.0
        obj.wind_direction = var_wind_direction
        # alpha
        var_rain_indicator = "Yes"
        obj.rain_indicator = var_rain_indicator
        # alpha
        var_snow_indicator = "Yes"
        obj.snow_indicator = var_snow_indicator
        # alpha
        var_daylight_saving_time_indicator = "Yes"
        obj.daylight_saving_time_indicator = var_daylight_saving_time_indicator
        # alpha
        var_solar_model_indicator = "ASHRAEClearSky"
        obj.solar_model_indicator = var_solar_model_indicator
        # object-list
        var_beam_solar_day_schedule_name = "object-list|Beam Solar Day Schedule Name"
        obj.beam_solar_day_schedule_name = var_beam_solar_day_schedule_name
        # object-list
        var_diffuse_solar_day_schedule_name = "object-list|Diffuse Solar Day Schedule Name"
        obj.diffuse_solar_day_schedule_name = var_diffuse_solar_day_schedule_name
        # real
        var_ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = 0.6
        obj.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = var_ashrae_clear_sky_optical_depth_for_beam_irradiance_taub
        # real
        var_ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = 1.5
        obj.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = var_ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud
        # real
        var_sky_clearness = 0.6
        obj.sky_clearness = var_sky_clearness

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sizingperioddesigndays[0].name, var_name)
        self.assertEqual(idf2.sizingperioddesigndays[0].month, var_month)
        self.assertEqual(idf2.sizingperioddesigndays[0].day_of_month, var_day_of_month)
        self.assertEqual(idf2.sizingperioddesigndays[0].day_type, var_day_type)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].maximum_drybulb_temperature, var_maximum_drybulb_temperature)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].daily_drybulb_temperature_range, var_daily_drybulb_temperature_range)
        self.assertEqual(idf2.sizingperioddesigndays[0].drybulb_temperature_range_modifier_type, var_drybulb_temperature_range_modifier_type)
        self.assertEqual(idf2.sizingperioddesigndays[0].drybulb_temperature_range_modifier_day_schedule_name, var_drybulb_temperature_range_modifier_day_schedule_name)
        self.assertEqual(idf2.sizingperioddesigndays[0].humidity_condition_type, var_humidity_condition_type)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].wetbulb_or_dewpoint_at_maximum_drybulb, var_wetbulb_or_dewpoint_at_maximum_drybulb)
        self.assertEqual(idf2.sizingperioddesigndays[0].humidity_condition_day_schedule_name, var_humidity_condition_day_schedule_name)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].humidity_ratio_at_maximum_drybulb, var_humidity_ratio_at_maximum_drybulb)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].enthalpy_at_maximum_drybulb, var_enthalpy_at_maximum_drybulb)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].daily_wetbulb_temperature_range, var_daily_wetbulb_temperature_range)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].barometric_pressure, var_barometric_pressure)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].wind_speed, var_wind_speed)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].wind_direction, var_wind_direction)
        self.assertEqual(idf2.sizingperioddesigndays[0].rain_indicator, var_rain_indicator)
        self.assertEqual(idf2.sizingperioddesigndays[0].snow_indicator, var_snow_indicator)
        self.assertEqual(idf2.sizingperioddesigndays[0].daylight_saving_time_indicator, var_daylight_saving_time_indicator)
        self.assertEqual(idf2.sizingperioddesigndays[0].solar_model_indicator, var_solar_model_indicator)
        self.assertEqual(idf2.sizingperioddesigndays[0].beam_solar_day_schedule_name, var_beam_solar_day_schedule_name)
        self.assertEqual(idf2.sizingperioddesigndays[0].diffuse_solar_day_schedule_name, var_diffuse_solar_day_schedule_name)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].ashrae_clear_sky_optical_depth_for_beam_irradiance_taub, var_ashrae_clear_sky_optical_depth_for_beam_irradiance_taub)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud, var_ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud)
        self.assertAlmostEqual(idf2.sizingperioddesigndays[0].sky_clearness, var_sky_clearness)