import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfacePropertyOtherSideCoefficients
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfacePropertyOtherSideCoefficients(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyothersidecoefficients(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyOtherSideCoefficients()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_combined_convective_or_radiative_film_coefficient = 2.2
        obj.combined_convective_or_radiative_film_coefficient = var_combined_convective_or_radiative_film_coefficient
        # real
        var_constant_temperature = 3.3
        obj.constant_temperature = var_constant_temperature
        # real
        var_constant_temperature_coefficient = 4.4
        obj.constant_temperature_coefficient = var_constant_temperature_coefficient
        # real
        var_external_drybulb_temperature_coefficient = 5.5
        obj.external_drybulb_temperature_coefficient = var_external_drybulb_temperature_coefficient
        # real
        var_ground_temperature_coefficient = 6.6
        obj.ground_temperature_coefficient = var_ground_temperature_coefficient
        # real
        var_wind_speed_coefficient = 7.7
        obj.wind_speed_coefficient = var_wind_speed_coefficient
        # real
        var_zone_air_temperature_coefficient = 8.8
        obj.zone_air_temperature_coefficient = var_zone_air_temperature_coefficient
        # object-list
        var_constant_temperature_schedule_name = "object-list|Constant Temperature Schedule Name"
        obj.constant_temperature_schedule_name = var_constant_temperature_schedule_name
        # alpha
        var_sinusoidal_variation_of_constant_temperature_coefficient = "Yes"
        obj.sinusoidal_variation_of_constant_temperature_coefficient = var_sinusoidal_variation_of_constant_temperature_coefficient
        # real
        var_period_of_sinusoidal_variation = 0.0001
        obj.period_of_sinusoidal_variation = var_period_of_sinusoidal_variation
        # real
        var_previous_other_side_temperature_coefficient = 12.12
        obj.previous_other_side_temperature_coefficient = var_previous_other_side_temperature_coefficient
        # real
        var_minimum_other_side_temperature_limit = 13.13
        obj.minimum_other_side_temperature_limit = var_minimum_other_side_temperature_limit
        # real
        var_maximum_other_side_temperature_limit = 14.14
        obj.maximum_other_side_temperature_limit = var_maximum_other_side_temperature_limit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyothersidecoefficientss[0].name, var_name)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].combined_convective_or_radiative_film_coefficient, var_combined_convective_or_radiative_film_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].constant_temperature, var_constant_temperature)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].constant_temperature_coefficient, var_constant_temperature_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].external_drybulb_temperature_coefficient, var_external_drybulb_temperature_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].ground_temperature_coefficient, var_ground_temperature_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].wind_speed_coefficient, var_wind_speed_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].zone_air_temperature_coefficient, var_zone_air_temperature_coefficient)
        self.assertEqual(idf2.surfacepropertyothersidecoefficientss[0].constant_temperature_schedule_name, var_constant_temperature_schedule_name)
        self.assertEqual(idf2.surfacepropertyothersidecoefficientss[0].sinusoidal_variation_of_constant_temperature_coefficient, var_sinusoidal_variation_of_constant_temperature_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].period_of_sinusoidal_variation, var_period_of_sinusoidal_variation)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].previous_other_side_temperature_coefficient, var_previous_other_side_temperature_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].minimum_other_side_temperature_limit, var_minimum_other_side_temperature_limit)
        self.assertAlmostEqual(idf2.surfacepropertyothersidecoefficientss[0].maximum_other_side_temperature_limit, var_maximum_other_side_temperature_limit)