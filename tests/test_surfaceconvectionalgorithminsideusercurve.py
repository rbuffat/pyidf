import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfaceConvectionAlgorithmInsideUserCurve

log = logging.getLogger(__name__)

class TestSurfaceConvectionAlgorithmInsideUserCurve(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithminsideusercurve(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmInsideUserCurve()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_reference_temperature_for_convection_heat_transfer = "MeanAirTemperature"
        obj.reference_temperature_for_convection_heat_transfer = var_reference_temperature_for_convection_heat_transfer
        # object-list
        var_hc_function_of_temperature_difference_curve_name = "object-list|Hc Function of Temperature Difference Curve Name"
        obj.hc_function_of_temperature_difference_curve_name = var_hc_function_of_temperature_difference_curve_name
        # object-list
        var_hc_function_of_temperature_difference_divided_by_height_curve_name = "object-list|Hc Function of Temperature Difference Divided by Height Curve Name"
        obj.hc_function_of_temperature_difference_divided_by_height_curve_name = var_hc_function_of_temperature_difference_divided_by_height_curve_name
        # object-list
        var_hc_function_of_air_change_rate_curve_name = "object-list|Hc Function of Air Change Rate Curve Name"
        obj.hc_function_of_air_change_rate_curve_name = var_hc_function_of_air_change_rate_curve_name
        # object-list
        var_hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = "object-list|Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"
        obj.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = var_hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].name, var_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].reference_temperature_for_convection_heat_transfer, var_reference_temperature_for_convection_heat_transfer)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].hc_function_of_temperature_difference_curve_name, var_hc_function_of_temperature_difference_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].hc_function_of_temperature_difference_divided_by_height_curve_name, var_hc_function_of_temperature_difference_divided_by_height_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].hc_function_of_air_change_rate_curve_name, var_hc_function_of_air_change_rate_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideusercurves[0].hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name, var_hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name)