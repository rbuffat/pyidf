import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_curves import CurveChillerPartLoadWithLift

log = logging.getLogger(__name__)

class TestCurveChillerPartLoadWithLift(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvechillerpartloadwithlift(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveChillerPartLoadWithLift()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_c1 = 2.2
        obj.coefficient1_c1 = var_coefficient1_c1
        # real
        var_coefficient2_c2 = 3.3
        obj.coefficient2_c2 = var_coefficient2_c2
        # real
        var_coefficient3_c3 = 4.4
        obj.coefficient3_c3 = var_coefficient3_c3
        # real
        var_coefficient4_c4 = 5.5
        obj.coefficient4_c4 = var_coefficient4_c4
        # real
        var_coefficient5_c5 = 6.6
        obj.coefficient5_c5 = var_coefficient5_c5
        # real
        var_coefficient6_c6 = 7.7
        obj.coefficient6_c6 = var_coefficient6_c6
        # real
        var_coefficient7_c7 = 8.8
        obj.coefficient7_c7 = var_coefficient7_c7
        # real
        var_coefficient8_c8 = 9.9
        obj.coefficient8_c8 = var_coefficient8_c8
        # real
        var_coefficient9_c9 = 10.1
        obj.coefficient9_c9 = var_coefficient9_c9
        # real
        var_coefficient10_c10 = 11.11
        obj.coefficient10_c10 = var_coefficient10_c10
        # real
        var_coefficient11_c11 = 12.12
        obj.coefficient11_c11 = var_coefficient11_c11
        # real
        var_coefficient12_c12 = 13.13
        obj.coefficient12_c12 = var_coefficient12_c12
        # real
        var_minimum_value_of_x = 14.14
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 15.15
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_value_of_y = 16.16
        obj.minimum_value_of_y = var_minimum_value_of_y
        # real
        var_maximum_value_of_y = 17.17
        obj.maximum_value_of_y = var_maximum_value_of_y
        # real
        var_minimum_value_of_z = 18.18
        obj.minimum_value_of_z = var_minimum_value_of_z
        # real
        var_maximum_value_of_z = 19.19
        obj.maximum_value_of_z = var_maximum_value_of_z
        # real
        var_minimum_curve_output = 20.2
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 21.21
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_input_unit_type_for_y = "Dimensionless"
        obj.input_unit_type_for_y = var_input_unit_type_for_y
        # alpha
        var_input_unit_type_for_z = "Dimensionless"
        obj.input_unit_type_for_z = var_input_unit_type_for_z
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvechillerpartloadwithlifts[0].name, var_name)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient1_c1, var_coefficient1_c1)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient2_c2, var_coefficient2_c2)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient3_c3, var_coefficient3_c3)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient4_c4, var_coefficient4_c4)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient5_c5, var_coefficient5_c5)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient6_c6, var_coefficient6_c6)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient7_c7, var_coefficient7_c7)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient8_c8, var_coefficient8_c8)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient9_c9, var_coefficient9_c9)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient10_c10, var_coefficient10_c10)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient11_c11, var_coefficient11_c11)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].coefficient12_c12, var_coefficient12_c12)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].minimum_value_of_y, var_minimum_value_of_y)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].maximum_value_of_y, var_maximum_value_of_y)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].minimum_value_of_z, var_minimum_value_of_z)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].maximum_value_of_z, var_maximum_value_of_z)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvechillerpartloadwithlifts[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvechillerpartloadwithlifts[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvechillerpartloadwithlifts[0].input_unit_type_for_y, var_input_unit_type_for_y)
        self.assertEqual(idf2.curvechillerpartloadwithlifts[0].input_unit_type_for_z, var_input_unit_type_for_z)
        self.assertEqual(idf2.curvechillerpartloadwithlifts[0].output_unit_type, var_output_unit_type)