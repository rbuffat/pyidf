import os
import tempfile
import unittest
import pyidf
from pyidf.performance_curves import CurveQuadLinear
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCurveQuadLinear(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvequadlinear(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveQuadLinear()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_w = 3.3
        obj.coefficient2_w = var_coefficient2_w
        # real
        var_coefficient3_x = 4.4
        obj.coefficient3_x = var_coefficient3_x
        # real
        var_coefficient4_y = 5.5
        obj.coefficient4_y = var_coefficient4_y
        # real
        var_coefficient5_z = 6.6
        obj.coefficient5_z = var_coefficient5_z
        # real
        var_minimum_value_of_w = 7.7
        obj.minimum_value_of_w = var_minimum_value_of_w
        # real
        var_maximum_value_of_w = 8.8
        obj.maximum_value_of_w = var_maximum_value_of_w
        # real
        var_minimum_value_of_x = 9.9
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 10.1
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_value_of_y = 11.11
        obj.minimum_value_of_y = var_minimum_value_of_y
        # real
        var_maximum_value_of_y = 12.12
        obj.maximum_value_of_y = var_maximum_value_of_y
        # real
        var_minimum_value_of_z = 13.13
        obj.minimum_value_of_z = var_minimum_value_of_z
        # real
        var_maximum_value_of_z = 14.14
        obj.maximum_value_of_z = var_maximum_value_of_z
        # real
        var_minimum_curve_output = 15.15
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 16.16
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_w = "Dimensionless"
        obj.input_unit_type_for_w = var_input_unit_type_for_w
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_input_unit_type_for_y = "Dimensionless"
        obj.input_unit_type_for_y = var_input_unit_type_for_y
        # alpha
        var_input_unit_type_for_z = "Dimensionless"
        obj.input_unit_type_for_z = var_input_unit_type_for_z

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvequadlinears[0].name, var_name)
        self.assertAlmostEqual(idf2.curvequadlinears[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvequadlinears[0].coefficient2_w, var_coefficient2_w)
        self.assertAlmostEqual(idf2.curvequadlinears[0].coefficient3_x, var_coefficient3_x)
        self.assertAlmostEqual(idf2.curvequadlinears[0].coefficient4_y, var_coefficient4_y)
        self.assertAlmostEqual(idf2.curvequadlinears[0].coefficient5_z, var_coefficient5_z)
        self.assertAlmostEqual(idf2.curvequadlinears[0].minimum_value_of_w, var_minimum_value_of_w)
        self.assertAlmostEqual(idf2.curvequadlinears[0].maximum_value_of_w, var_maximum_value_of_w)
        self.assertAlmostEqual(idf2.curvequadlinears[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvequadlinears[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvequadlinears[0].minimum_value_of_y, var_minimum_value_of_y)
        self.assertAlmostEqual(idf2.curvequadlinears[0].maximum_value_of_y, var_maximum_value_of_y)
        self.assertAlmostEqual(idf2.curvequadlinears[0].minimum_value_of_z, var_minimum_value_of_z)
        self.assertAlmostEqual(idf2.curvequadlinears[0].maximum_value_of_z, var_maximum_value_of_z)
        self.assertAlmostEqual(idf2.curvequadlinears[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvequadlinears[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvequadlinears[0].input_unit_type_for_w, var_input_unit_type_for_w)
        self.assertEqual(idf2.curvequadlinears[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvequadlinears[0].input_unit_type_for_y, var_input_unit_type_for_y)
        self.assertEqual(idf2.curvequadlinears[0].input_unit_type_for_z, var_input_unit_type_for_z)