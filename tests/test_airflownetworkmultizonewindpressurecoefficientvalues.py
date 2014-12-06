import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneWindPressureCoefficientValues
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneWindPressureCoefficientValues(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonewindpressurecoefficientvalues(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneWindPressureCoefficientValues()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_airflownetworkmultizonewindpressurecoefficientarray_name = "object-list|AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"
        obj.airflownetworkmultizonewindpressurecoefficientarray_name = var_airflownetworkmultizonewindpressurecoefficientarray_name
        # real
        var_wind_pressure_coefficient_value_1 = 3.3
        obj.wind_pressure_coefficient_value_1 = var_wind_pressure_coefficient_value_1
        # real
        var_wind_pressure_coefficient_value_2 = 4.4
        obj.wind_pressure_coefficient_value_2 = var_wind_pressure_coefficient_value_2
        # real
        var_wind_pressure_coefficient_value_3 = 5.5
        obj.wind_pressure_coefficient_value_3 = var_wind_pressure_coefficient_value_3
        # real
        var_wind_pressure_coefficient_value_4 = 6.6
        obj.wind_pressure_coefficient_value_4 = var_wind_pressure_coefficient_value_4
        # real
        var_wind_pressure_coefficient_value_5 = 7.7
        obj.wind_pressure_coefficient_value_5 = var_wind_pressure_coefficient_value_5
        # real
        var_wind_pressure_coefficient_value_6 = 8.8
        obj.wind_pressure_coefficient_value_6 = var_wind_pressure_coefficient_value_6
        # real
        var_wind_pressure_coefficient_value_7 = 9.9
        obj.wind_pressure_coefficient_value_7 = var_wind_pressure_coefficient_value_7
        # real
        var_wind_pressure_coefficient_value_8 = 10.1
        obj.wind_pressure_coefficient_value_8 = var_wind_pressure_coefficient_value_8
        # real
        var_wind_pressure_coefficient_value_9 = 11.11
        obj.wind_pressure_coefficient_value_9 = var_wind_pressure_coefficient_value_9
        # real
        var_wind_pressure_coefficient_value_10 = 12.12
        obj.wind_pressure_coefficient_value_10 = var_wind_pressure_coefficient_value_10
        # real
        var_wind_pressure_coefficient_value_11 = 13.13
        obj.wind_pressure_coefficient_value_11 = var_wind_pressure_coefficient_value_11
        # real
        var_wind_pressure_coefficient_value_12 = 14.14
        obj.wind_pressure_coefficient_value_12 = var_wind_pressure_coefficient_value_12
        # real
        var_wind_pressure_coefficient_value_13 = 15.15
        obj.wind_pressure_coefficient_value_13 = var_wind_pressure_coefficient_value_13
        # real
        var_wind_pressure_coefficient_value_14 = 16.16
        obj.wind_pressure_coefficient_value_14 = var_wind_pressure_coefficient_value_14
        # real
        var_wind_pressure_coefficient_value_15 = 17.17
        obj.wind_pressure_coefficient_value_15 = var_wind_pressure_coefficient_value_15
        # real
        var_wind_pressure_coefficient_value_16 = 18.18
        obj.wind_pressure_coefficient_value_16 = var_wind_pressure_coefficient_value_16
        # real
        var_wind_pressure_coefficient_value_17 = 19.19
        obj.wind_pressure_coefficient_value_17 = var_wind_pressure_coefficient_value_17
        # real
        var_wind_pressure_coefficient_value_18 = 20.2
        obj.wind_pressure_coefficient_value_18 = var_wind_pressure_coefficient_value_18
        # real
        var_wind_pressure_coefficient_value_19 = 21.21
        obj.wind_pressure_coefficient_value_19 = var_wind_pressure_coefficient_value_19
        # real
        var_wind_pressure_coefficient_value_20 = 22.22
        obj.wind_pressure_coefficient_value_20 = var_wind_pressure_coefficient_value_20
        # real
        var_wind_pressure_coefficient_value_21 = 23.23
        obj.wind_pressure_coefficient_value_21 = var_wind_pressure_coefficient_value_21
        # real
        var_wind_pressure_coefficient_value_22 = 24.24
        obj.wind_pressure_coefficient_value_22 = var_wind_pressure_coefficient_value_22
        # real
        var_wind_pressure_coefficient_value_23 = 25.25
        obj.wind_pressure_coefficient_value_23 = var_wind_pressure_coefficient_value_23
        # real
        var_wind_pressure_coefficient_value_24 = 26.26
        obj.wind_pressure_coefficient_value_24 = var_wind_pressure_coefficient_value_24
        # real
        var_wind_pressure_coefficient_value_25 = 27.27
        obj.wind_pressure_coefficient_value_25 = var_wind_pressure_coefficient_value_25
        # real
        var_wind_pressure_coefficient_value_26 = 28.28
        obj.wind_pressure_coefficient_value_26 = var_wind_pressure_coefficient_value_26
        # real
        var_wind_pressure_coefficient_value_27 = 29.29
        obj.wind_pressure_coefficient_value_27 = var_wind_pressure_coefficient_value_27
        # real
        var_wind_pressure_coefficient_value_28 = 30.3
        obj.wind_pressure_coefficient_value_28 = var_wind_pressure_coefficient_value_28
        # real
        var_wind_pressure_coefficient_value_29 = 31.31
        obj.wind_pressure_coefficient_value_29 = var_wind_pressure_coefficient_value_29
        # real
        var_wind_pressure_coefficient_value_30 = 32.32
        obj.wind_pressure_coefficient_value_30 = var_wind_pressure_coefficient_value_30
        # real
        var_wind_pressure_coefficient_value_31 = 33.33
        obj.wind_pressure_coefficient_value_31 = var_wind_pressure_coefficient_value_31
        # real
        var_wind_pressure_coefficient_value_32 = 34.34
        obj.wind_pressure_coefficient_value_32 = var_wind_pressure_coefficient_value_32
        # real
        var_wind_pressure_coefficient_value_33 = 35.35
        obj.wind_pressure_coefficient_value_33 = var_wind_pressure_coefficient_value_33
        # real
        var_wind_pressure_coefficient_value_34 = 36.36
        obj.wind_pressure_coefficient_value_34 = var_wind_pressure_coefficient_value_34
        # real
        var_wind_pressure_coefficient_value_35 = 37.37
        obj.wind_pressure_coefficient_value_35 = var_wind_pressure_coefficient_value_35
        # real
        var_wind_pressure_coefficient_value_36 = 38.38
        obj.wind_pressure_coefficient_value_36 = var_wind_pressure_coefficient_value_36

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].name, var_name)
        self.assertEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].airflownetworkmultizonewindpressurecoefficientarray_name, var_airflownetworkmultizonewindpressurecoefficientarray_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_1, var_wind_pressure_coefficient_value_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_2, var_wind_pressure_coefficient_value_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_3, var_wind_pressure_coefficient_value_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_4, var_wind_pressure_coefficient_value_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_5, var_wind_pressure_coefficient_value_5)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_6, var_wind_pressure_coefficient_value_6)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_7, var_wind_pressure_coefficient_value_7)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_8, var_wind_pressure_coefficient_value_8)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_9, var_wind_pressure_coefficient_value_9)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_10, var_wind_pressure_coefficient_value_10)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_11, var_wind_pressure_coefficient_value_11)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_12, var_wind_pressure_coefficient_value_12)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_13, var_wind_pressure_coefficient_value_13)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_14, var_wind_pressure_coefficient_value_14)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_15, var_wind_pressure_coefficient_value_15)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_16, var_wind_pressure_coefficient_value_16)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_17, var_wind_pressure_coefficient_value_17)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_18, var_wind_pressure_coefficient_value_18)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_19, var_wind_pressure_coefficient_value_19)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_20, var_wind_pressure_coefficient_value_20)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_21, var_wind_pressure_coefficient_value_21)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_22, var_wind_pressure_coefficient_value_22)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_23, var_wind_pressure_coefficient_value_23)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_24, var_wind_pressure_coefficient_value_24)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_25, var_wind_pressure_coefficient_value_25)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_26, var_wind_pressure_coefficient_value_26)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_27, var_wind_pressure_coefficient_value_27)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_28, var_wind_pressure_coefficient_value_28)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_29, var_wind_pressure_coefficient_value_29)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_30, var_wind_pressure_coefficient_value_30)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_31, var_wind_pressure_coefficient_value_31)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_32, var_wind_pressure_coefficient_value_32)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_33, var_wind_pressure_coefficient_value_33)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_34, var_wind_pressure_coefficient_value_34)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_35, var_wind_pressure_coefficient_value_35)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientvaluess[0].wind_pressure_coefficient_value_36, var_wind_pressure_coefficient_value_36)