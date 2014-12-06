import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfaceConvectionAlgorithmOutsideUserCurve
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfaceConvectionAlgorithmOutsideUserCurve(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithmoutsideusercurve(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmOutsideUserCurve()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_wind_speed_type_for_curve = "WeatherFile"
        obj.wind_speed_type_for_curve = var_wind_speed_type_for_curve
        # alpha
        var_hf_function_of_wind_speed_curve_name = "Hf Function of Wind Speed Curve Name"
        obj.hf_function_of_wind_speed_curve_name = var_hf_function_of_wind_speed_curve_name
        # alpha
        var_hn_function_of_temperature_difference_curve_name = "Hn Function of Temperature Difference Curve Name"
        obj.hn_function_of_temperature_difference_curve_name = var_hn_function_of_temperature_difference_curve_name
        # alpha
        var_hn_function_of_temperature_difference_divided_by_height_curve_name = "Hn Function of Temperature Difference Divided by Height Curve Name"
        obj.hn_function_of_temperature_difference_divided_by_height_curve_name = var_hn_function_of_temperature_difference_divided_by_height_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideusercurves[0].name, var_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideusercurves[0].wind_speed_type_for_curve, var_wind_speed_type_for_curve)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideusercurves[0].hf_function_of_wind_speed_curve_name, var_hf_function_of_wind_speed_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideusercurves[0].hn_function_of_temperature_difference_curve_name, var_hn_function_of_temperature_difference_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideusercurves[0].hn_function_of_temperature_difference_divided_by_height_curve_name, var_hn_function_of_temperature_difference_divided_by_height_curve_name)