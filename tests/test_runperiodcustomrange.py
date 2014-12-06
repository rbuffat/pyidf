import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import RunPeriodCustomRange

log = logging.getLogger(__name__)

class TestRunPeriodCustomRange(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_runperiodcustomrange(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RunPeriodCustomRange()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_begin_month = 6
        obj.begin_month = var_begin_month
        # integer
        var_begin_day_of_month = 16
        obj.begin_day_of_month = var_begin_day_of_month
        # real
        var_begin_year = 4.4
        obj.begin_year = var_begin_year
        # integer
        var_end_month = 6
        obj.end_month = var_end_month
        # integer
        var_end_day_of_month = 16
        obj.end_day_of_month = var_end_day_of_month
        # real
        var_end_year = 7.7
        obj.end_year = var_end_year
        # alpha
        var_day_of_week_for_start_day = "Sunday"
        obj.day_of_week_for_start_day = var_day_of_week_for_start_day
        # alpha
        var_use_weather_file_holidays_and_special_days = "Yes"
        obj.use_weather_file_holidays_and_special_days = var_use_weather_file_holidays_and_special_days
        # alpha
        var_use_weather_file_daylight_saving_period = "Yes"
        obj.use_weather_file_daylight_saving_period = var_use_weather_file_daylight_saving_period
        # alpha
        var_apply_weekend_holiday_rule = "Yes"
        obj.apply_weekend_holiday_rule = var_apply_weekend_holiday_rule
        # alpha
        var_use_weather_file_rain_indicators = "Yes"
        obj.use_weather_file_rain_indicators = var_use_weather_file_rain_indicators
        # alpha
        var_use_weather_file_snow_indicators = "Yes"
        obj.use_weather_file_snow_indicators = var_use_weather_file_snow_indicators

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.runperiodcustomranges[0].name, var_name)
        self.assertEqual(idf2.runperiodcustomranges[0].begin_month, var_begin_month)
        self.assertEqual(idf2.runperiodcustomranges[0].begin_day_of_month, var_begin_day_of_month)
        self.assertAlmostEqual(idf2.runperiodcustomranges[0].begin_year, var_begin_year)
        self.assertEqual(idf2.runperiodcustomranges[0].end_month, var_end_month)
        self.assertEqual(idf2.runperiodcustomranges[0].end_day_of_month, var_end_day_of_month)
        self.assertAlmostEqual(idf2.runperiodcustomranges[0].end_year, var_end_year)
        self.assertEqual(idf2.runperiodcustomranges[0].day_of_week_for_start_day, var_day_of_week_for_start_day)
        self.assertEqual(idf2.runperiodcustomranges[0].use_weather_file_holidays_and_special_days, var_use_weather_file_holidays_and_special_days)
        self.assertEqual(idf2.runperiodcustomranges[0].use_weather_file_daylight_saving_period, var_use_weather_file_daylight_saving_period)
        self.assertEqual(idf2.runperiodcustomranges[0].apply_weekend_holiday_rule, var_apply_weekend_holiday_rule)
        self.assertEqual(idf2.runperiodcustomranges[0].use_weather_file_rain_indicators, var_use_weather_file_rain_indicators)
        self.assertEqual(idf2.runperiodcustomranges[0].use_weather_file_snow_indicators, var_use_weather_file_snow_indicators)