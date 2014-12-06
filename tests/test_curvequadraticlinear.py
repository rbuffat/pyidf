import os
import tempfile
import unittest
import pyidf
from pyidf.performance_curves import CurveQuadraticLinear
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCurveQuadraticLinear(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvequadraticlinear(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveQuadraticLinear()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_x = 3.3
        obj.coefficient2_x = var_coefficient2_x
        # real
        var_coefficient3_x2 = 4.4
        obj.coefficient3_x2 = var_coefficient3_x2
        # real
        var_coefficient4_y = 5.5
        obj.coefficient4_y = var_coefficient4_y
        # real
        var_coefficient5_xy = 6.6
        obj.coefficient5_xy = var_coefficient5_xy
        # real
        var_coefficient6_x2y = 7.7
        obj.coefficient6_x2y = var_coefficient6_x2y
        # real
        var_minimum_value_of_x = 8.8
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 9.9
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_value_of_y = 10.1
        obj.minimum_value_of_y = var_minimum_value_of_y
        # real
        var_maximum_value_of_y = 11.11
        obj.maximum_value_of_y = var_maximum_value_of_y
        # real
        var_minimum_curve_output = 12.12
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 13.13
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_input_unit_type_for_y = "Dimensionless"
        obj.input_unit_type_for_y = var_input_unit_type_for_y
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvequadraticlinears[0].name, var_name)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient2_x, var_coefficient2_x)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient3_x2, var_coefficient3_x2)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient4_y, var_coefficient4_y)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient5_xy, var_coefficient5_xy)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].coefficient6_x2y, var_coefficient6_x2y)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].minimum_value_of_y, var_minimum_value_of_y)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].maximum_value_of_y, var_maximum_value_of_y)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvequadraticlinears[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvequadraticlinears[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvequadraticlinears[0].input_unit_type_for_y, var_input_unit_type_for_y)
        self.assertEqual(idf2.curvequadraticlinears[0].output_unit_type, var_output_unit_type)