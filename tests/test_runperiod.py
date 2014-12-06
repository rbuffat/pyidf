import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import RunPeriod
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRunPeriod(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_runperiod(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RunPeriod()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_begin_month = 6
        obj.begin_month = var_begin_month
        # integer
        var_begin_day_of_month = 16
        obj.begin_day_of_month = var_begin_day_of_month
        # integer
        var_end_month = 6
        obj.end_month = var_end_month
        # integer
        var_end_day_of_month = 16
        obj.end_day_of_month = var_end_day_of_month
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
        # integer
        var_number_of_times_runperiod_to_be_repeated = 1
        obj.number_of_times_runperiod_to_be_repeated = var_number_of_times_runperiod_to_be_repeated
        # alpha
        var_increment_day_of_week_on_repeat = "Yes"
        obj.increment_day_of_week_on_repeat = var_increment_day_of_week_on_repeat
        # real
        var_start_year = 14.14
        obj.start_year = var_start_year

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.runperiods[0].name, var_name)
        self.assertEqual(idf2.runperiods[0].begin_month, var_begin_month)
        self.assertEqual(idf2.runperiods[0].begin_day_of_month, var_begin_day_of_month)
        self.assertEqual(idf2.runperiods[0].end_month, var_end_month)
        self.assertEqual(idf2.runperiods[0].end_day_of_month, var_end_day_of_month)
        self.assertEqual(idf2.runperiods[0].day_of_week_for_start_day, var_day_of_week_for_start_day)
        self.assertEqual(idf2.runperiods[0].use_weather_file_holidays_and_special_days, var_use_weather_file_holidays_and_special_days)
        self.assertEqual(idf2.runperiods[0].use_weather_file_daylight_saving_period, var_use_weather_file_daylight_saving_period)
        self.assertEqual(idf2.runperiods[0].apply_weekend_holiday_rule, var_apply_weekend_holiday_rule)
        self.assertEqual(idf2.runperiods[0].use_weather_file_rain_indicators, var_use_weather_file_rain_indicators)
        self.assertEqual(idf2.runperiods[0].use_weather_file_snow_indicators, var_use_weather_file_snow_indicators)
        self.assertEqual(idf2.runperiods[0].number_of_times_runperiod_to_be_repeated, var_number_of_times_runperiod_to_be_repeated)
        self.assertEqual(idf2.runperiods[0].increment_day_of_week_on_repeat, var_increment_day_of_week_on_repeat)
        self.assertAlmostEqual(idf2.runperiods[0].start_year, var_start_year)