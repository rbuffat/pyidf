import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteHeightVariation

log = logging.getLogger(__name__)

class TestSiteHeightVariation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_siteheightvariation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteHeightVariation()
        # real
        var_wind_speed_profile_exponent = 0.0
        obj.wind_speed_profile_exponent = var_wind_speed_profile_exponent
        # real
        var_wind_speed_profile_boundary_layer_thickness = 0.0001
        obj.wind_speed_profile_boundary_layer_thickness = var_wind_speed_profile_boundary_layer_thickness
        # real
        var_air_temperature_gradient_coefficient = 0.0
        obj.air_temperature_gradient_coefficient = var_air_temperature_gradient_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.siteheightvariations[0].wind_speed_profile_exponent, var_wind_speed_profile_exponent)
        self.assertAlmostEqual(idf2.siteheightvariations[0].wind_speed_profile_boundary_layer_thickness, var_wind_speed_profile_boundary_layer_thickness)
        self.assertAlmostEqual(idf2.siteheightvariations[0].air_temperature_gradient_coefficient, var_air_temperature_gradient_coefficient)