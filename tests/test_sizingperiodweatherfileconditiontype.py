import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SizingPeriodWeatherFileConditionType

log = logging.getLogger(__name__)

class TestSizingPeriodWeatherFileConditionType(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingperiodweatherfileconditiontype(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingPeriodWeatherFileConditionType()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_period_selection = "SummerExtreme"
        obj.period_selection = var_period_selection
        # alpha
        var_day_of_week_for_start_day = "Sunday"
        obj.day_of_week_for_start_day = var_day_of_week_for_start_day
        # alpha
        var_use_weather_file_daylight_saving_period = "Yes"
        obj.use_weather_file_daylight_saving_period = var_use_weather_file_daylight_saving_period
        # alpha
        var_use_weather_file_rain_and_snow_indicators = "Yes"
        obj.use_weather_file_rain_and_snow_indicators = var_use_weather_file_rain_and_snow_indicators

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sizingperiodweatherfileconditiontypes[0].name, var_name)
        self.assertEqual(idf2.sizingperiodweatherfileconditiontypes[0].period_selection, var_period_selection)
        self.assertEqual(idf2.sizingperiodweatherfileconditiontypes[0].day_of_week_for_start_day, var_day_of_week_for_start_day)
        self.assertEqual(idf2.sizingperiodweatherfileconditiontypes[0].use_weather_file_daylight_saving_period, var_use_weather_file_daylight_saving_period)
        self.assertEqual(idf2.sizingperiodweatherfileconditiontypes[0].use_weather_file_rain_and_snow_indicators, var_use_weather_file_rain_and_snow_indicators)