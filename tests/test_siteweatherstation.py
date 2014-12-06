import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteWeatherStation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteWeatherStation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_siteweatherstation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteWeatherStation()
        # real
        var_wind_sensor_height_above_ground = 0.0001
        obj.wind_sensor_height_above_ground = var_wind_sensor_height_above_ground
        # real
        var_wind_speed_profile_exponent = 0.0
        obj.wind_speed_profile_exponent = var_wind_speed_profile_exponent
        # real
        var_wind_speed_profile_boundary_layer_thickness = 0.0
        obj.wind_speed_profile_boundary_layer_thickness = var_wind_speed_profile_boundary_layer_thickness
        # real
        var_air_temperature_sensor_height_above_ground = 0.0
        obj.air_temperature_sensor_height_above_ground = var_air_temperature_sensor_height_above_ground

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.siteweatherstations[0].wind_sensor_height_above_ground, var_wind_sensor_height_above_ground)
        self.assertAlmostEqual(idf2.siteweatherstations[0].wind_speed_profile_exponent, var_wind_speed_profile_exponent)
        self.assertAlmostEqual(idf2.siteweatherstations[0].wind_speed_profile_boundary_layer_thickness, var_wind_speed_profile_boundary_layer_thickness)
        self.assertAlmostEqual(idf2.siteweatherstations[0].air_temperature_sensor_height_above_ground, var_air_temperature_sensor_height_above_ground)