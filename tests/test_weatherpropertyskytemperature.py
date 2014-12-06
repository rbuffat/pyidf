import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import WeatherPropertySkyTemperature
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWeatherPropertySkyTemperature(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_weatherpropertyskytemperature(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WeatherPropertySkyTemperature()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # alpha
        var_calculation_type = "ScheduleValue"
        obj.calculation_type = var_calculation_type
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.weatherpropertyskytemperatures[0].name, var_name)
        self.assertEqual(idf2.weatherpropertyskytemperatures[0].calculation_type, var_calculation_type)
        self.assertEqual(idf2.weatherpropertyskytemperatures[0].schedule_name, var_schedule_name)