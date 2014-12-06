import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfacePropertyConvectionCoefficients

log = logging.getLogger(__name__)

class TestSurfacePropertyConvectionCoefficients(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyconvectioncoefficients(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyConvectionCoefficients()
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_convection_coefficient_1_location = "Outside"
        obj.convection_coefficient_1_location = var_convection_coefficient_1_location
        # alpha
        var_convection_coefficient_1_type = "Value"
        obj.convection_coefficient_1_type = var_convection_coefficient_1_type
        # real
        var_convection_coefficient_1 = 4.4
        obj.convection_coefficient_1 = var_convection_coefficient_1
        # object-list
        var_convection_coefficient_1_schedule_name = "object-list|Convection Coefficient 1 Schedule Name"
        obj.convection_coefficient_1_schedule_name = var_convection_coefficient_1_schedule_name
        # object-list
        var_convection_coefficient_1_user_curve_name = "object-list|Convection Coefficient 1 User Curve Name"
        obj.convection_coefficient_1_user_curve_name = var_convection_coefficient_1_user_curve_name
        # alpha
        var_convection_coefficient_2_location = "Outside"
        obj.convection_coefficient_2_location = var_convection_coefficient_2_location
        # alpha
        var_convection_coefficient_2_type = "Value"
        obj.convection_coefficient_2_type = var_convection_coefficient_2_type
        # real
        var_convection_coefficient_2 = 9.9
        obj.convection_coefficient_2 = var_convection_coefficient_2
        # object-list
        var_convection_coefficient_2_schedule_name = "object-list|Convection Coefficient 2 Schedule Name"
        obj.convection_coefficient_2_schedule_name = var_convection_coefficient_2_schedule_name
        # object-list
        var_convection_coefficient_2_user_curve_name = "object-list|Convection Coefficient 2 User Curve Name"
        obj.convection_coefficient_2_user_curve_name = var_convection_coefficient_2_user_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].surface_name, var_surface_name)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_1_location, var_convection_coefficient_1_location)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_1_type, var_convection_coefficient_1_type)
        self.assertAlmostEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_1, var_convection_coefficient_1)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_1_schedule_name, var_convection_coefficient_1_schedule_name)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_1_user_curve_name, var_convection_coefficient_1_user_curve_name)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_2_location, var_convection_coefficient_2_location)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_2_type, var_convection_coefficient_2_type)
        self.assertAlmostEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_2, var_convection_coefficient_2)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_2_schedule_name, var_convection_coefficient_2_schedule_name)
        self.assertEqual(idf2.surfacepropertyconvectioncoefficientss[0].convection_coefficient_2_user_curve_name, var_convection_coefficient_2_user_curve_name)