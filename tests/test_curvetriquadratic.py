import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_curves import CurveTriquadratic

log = logging.getLogger(__name__)

class TestCurveTriquadratic(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvetriquadratic(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveTriquadratic()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_x2 = 3.3
        obj.coefficient2_x2 = var_coefficient2_x2
        # real
        var_coefficient3_x = 4.4
        obj.coefficient3_x = var_coefficient3_x
        # real
        var_coefficient4_y2 = 5.5
        obj.coefficient4_y2 = var_coefficient4_y2
        # real
        var_coefficient5_y = 6.6
        obj.coefficient5_y = var_coefficient5_y
        # real
        var_coefficient6_z2 = 7.7
        obj.coefficient6_z2 = var_coefficient6_z2
        # real
        var_coefficient7_z = 8.8
        obj.coefficient7_z = var_coefficient7_z
        # real
        var_coefficient8_x2y2 = 9.9
        obj.coefficient8_x2y2 = var_coefficient8_x2y2
        # real
        var_coefficient9_xy = 10.1
        obj.coefficient9_xy = var_coefficient9_xy
        # real
        var_coefficient10_xy2 = 11.11
        obj.coefficient10_xy2 = var_coefficient10_xy2
        # real
        var_coefficient11_x2y = 12.12
        obj.coefficient11_x2y = var_coefficient11_x2y
        # real
        var_coefficient12_x2z2 = 13.13
        obj.coefficient12_x2z2 = var_coefficient12_x2z2
        # real
        var_coefficient13_xz = 14.14
        obj.coefficient13_xz = var_coefficient13_xz
        # real
        var_coefficient14_xz2 = 15.15
        obj.coefficient14_xz2 = var_coefficient14_xz2
        # real
        var_coefficient15_x2z = 16.16
        obj.coefficient15_x2z = var_coefficient15_x2z
        # real
        var_coefficient16_y2z2 = 17.17
        obj.coefficient16_y2z2 = var_coefficient16_y2z2
        # real
        var_coefficient17_yz = 18.18
        obj.coefficient17_yz = var_coefficient17_yz
        # real
        var_coefficient18_yz2 = 19.19
        obj.coefficient18_yz2 = var_coefficient18_yz2
        # real
        var_coefficient19_y2z = 20.2
        obj.coefficient19_y2z = var_coefficient19_y2z
        # real
        var_coefficient20_x2y2z2 = 21.21
        obj.coefficient20_x2y2z2 = var_coefficient20_x2y2z2
        # real
        var_coefficient21_x2y2z = 22.22
        obj.coefficient21_x2y2z = var_coefficient21_x2y2z
        # real
        var_coefficient22_x2yz2 = 23.23
        obj.coefficient22_x2yz2 = var_coefficient22_x2yz2
        # real
        var_coefficient23_xy2z2 = 24.24
        obj.coefficient23_xy2z2 = var_coefficient23_xy2z2
        # real
        var_coefficient24_x2yz = 25.25
        obj.coefficient24_x2yz = var_coefficient24_x2yz
        # real
        var_coefficient25_xy2z = 26.26
        obj.coefficient25_xy2z = var_coefficient25_xy2z
        # real
        var_coefficient26_xyz2 = 27.27
        obj.coefficient26_xyz2 = var_coefficient26_xyz2
        # real
        var_coefficient27_xyz = 28.28
        obj.coefficient27_xyz = var_coefficient27_xyz
        # real
        var_minimum_value_of_x = 29.29
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 30.3
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_value_of_y = 31.31
        obj.minimum_value_of_y = var_minimum_value_of_y
        # real
        var_maximum_value_of_y = 32.32
        obj.maximum_value_of_y = var_maximum_value_of_y
        # real
        var_minimum_value_of_z = 33.33
        obj.minimum_value_of_z = var_minimum_value_of_z
        # real
        var_maximum_value_of_z = 34.34
        obj.maximum_value_of_z = var_maximum_value_of_z
        # real
        var_minimum_curve_output = 35.35
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 36.36
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
        self.assertEqual(idf2.curvetriquadratics[0].name, var_name)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient2_x2, var_coefficient2_x2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient3_x, var_coefficient3_x)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient4_y2, var_coefficient4_y2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient5_y, var_coefficient5_y)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient6_z2, var_coefficient6_z2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient7_z, var_coefficient7_z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient8_x2y2, var_coefficient8_x2y2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient9_xy, var_coefficient9_xy)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient10_xy2, var_coefficient10_xy2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient11_x2y, var_coefficient11_x2y)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient12_x2z2, var_coefficient12_x2z2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient13_xz, var_coefficient13_xz)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient14_xz2, var_coefficient14_xz2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient15_x2z, var_coefficient15_x2z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient16_y2z2, var_coefficient16_y2z2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient17_yz, var_coefficient17_yz)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient18_yz2, var_coefficient18_yz2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient19_y2z, var_coefficient19_y2z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient20_x2y2z2, var_coefficient20_x2y2z2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient21_x2y2z, var_coefficient21_x2y2z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient22_x2yz2, var_coefficient22_x2yz2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient23_xy2z2, var_coefficient23_xy2z2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient24_x2yz, var_coefficient24_x2yz)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient25_xy2z, var_coefficient25_xy2z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient26_xyz2, var_coefficient26_xyz2)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].coefficient27_xyz, var_coefficient27_xyz)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].minimum_value_of_y, var_minimum_value_of_y)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].maximum_value_of_y, var_maximum_value_of_y)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].minimum_value_of_z, var_minimum_value_of_z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].maximum_value_of_z, var_maximum_value_of_z)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvetriquadratics[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvetriquadratics[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvetriquadratics[0].input_unit_type_for_y, var_input_unit_type_for_y)
        self.assertEqual(idf2.curvetriquadratics[0].input_unit_type_for_z, var_input_unit_type_for_z)
        self.assertEqual(idf2.curvetriquadratics[0].output_unit_type, var_output_unit_type)