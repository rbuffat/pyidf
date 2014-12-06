import os
import tempfile
import unittest
import pyidf
from pyidf.performance_curves import CurveFanPressureRise
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCurveFanPressureRise(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvefanpressurerise(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveFanPressureRise()
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
        var_minimum_value_of_qfan = 6.6
        obj.minimum_value_of_qfan = var_minimum_value_of_qfan
        # real
        var_maximum_value_of_qfan = 7.7
        obj.maximum_value_of_qfan = var_maximum_value_of_qfan
        # real
        var_minimum_value_of_psm = 8.8
        obj.minimum_value_of_psm = var_minimum_value_of_psm
        # real
        var_maximum_value_of_psm = 9.9
        obj.maximum_value_of_psm = var_maximum_value_of_psm
        # real
        var_minimum_curve_output = 10.1
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 11.11
        obj.maximum_curve_output = var_maximum_curve_output

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvefanpressurerises[0].name, var_name)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].coefficient1_c1, var_coefficient1_c1)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].coefficient2_c2, var_coefficient2_c2)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].coefficient3_c3, var_coefficient3_c3)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].coefficient4_c4, var_coefficient4_c4)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].minimum_value_of_qfan, var_minimum_value_of_qfan)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].maximum_value_of_qfan, var_maximum_value_of_qfan)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].minimum_value_of_psm, var_minimum_value_of_psm)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].maximum_value_of_psm, var_maximum_value_of_psm)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvefanpressurerises[0].maximum_curve_output, var_maximum_curve_output)