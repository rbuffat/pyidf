import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneWindPressureCoefficientArray

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneWindPressureCoefficientArray(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonewindpressurecoefficientarray(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneWindPressureCoefficientArray()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_wind_direction_1 = 180.0
        obj.wind_direction_1 = var_wind_direction_1
        # real
        var_wind_direction_2 = 180.0
        obj.wind_direction_2 = var_wind_direction_2
        # real
        var_wind_direction_3 = 180.0
        obj.wind_direction_3 = var_wind_direction_3
        # real
        var_wind_direction_4 = 180.0
        obj.wind_direction_4 = var_wind_direction_4
        # real
        var_wind_direction_5 = 180.0
        obj.wind_direction_5 = var_wind_direction_5
        # real
        var_wind_direction_6 = 180.0
        obj.wind_direction_6 = var_wind_direction_6
        # real
        var_wind_direction_7 = 180.0
        obj.wind_direction_7 = var_wind_direction_7
        # real
        var_wind_direction_8 = 180.0
        obj.wind_direction_8 = var_wind_direction_8
        # real
        var_wind_direction_9 = 180.0
        obj.wind_direction_9 = var_wind_direction_9
        # real
        var_wind_direction_10 = 180.0
        obj.wind_direction_10 = var_wind_direction_10
        # real
        var_wind_direction_11 = 180.0
        obj.wind_direction_11 = var_wind_direction_11
        # real
        var_wind_direction_12 = 180.0
        obj.wind_direction_12 = var_wind_direction_12
        # real
        var_wind_direction_13 = 180.0
        obj.wind_direction_13 = var_wind_direction_13
        # real
        var_wind_direction_14 = 180.0
        obj.wind_direction_14 = var_wind_direction_14
        # real
        var_wind_direction_15 = 180.0
        obj.wind_direction_15 = var_wind_direction_15
        # real
        var_wind_direction_16 = 180.0
        obj.wind_direction_16 = var_wind_direction_16
        # real
        var_wind_direction_17 = 180.0
        obj.wind_direction_17 = var_wind_direction_17
        # real
        var_wind_direction_18 = 180.0
        obj.wind_direction_18 = var_wind_direction_18
        # real
        var_wind_direction_19 = 180.0
        obj.wind_direction_19 = var_wind_direction_19
        # real
        var_wind_direction_20 = 180.0
        obj.wind_direction_20 = var_wind_direction_20
        # real
        var_wind_direction_21 = 180.0
        obj.wind_direction_21 = var_wind_direction_21
        # real
        var_wind_direction_22 = 180.0
        obj.wind_direction_22 = var_wind_direction_22
        # real
        var_wind_direction_23 = 180.0
        obj.wind_direction_23 = var_wind_direction_23
        # real
        var_wind_direction_24 = 180.0
        obj.wind_direction_24 = var_wind_direction_24
        # real
        var_wind_direction_25 = 180.0
        obj.wind_direction_25 = var_wind_direction_25
        # real
        var_wind_direction_26 = 180.0
        obj.wind_direction_26 = var_wind_direction_26
        # real
        var_wind_direction_27 = 180.0
        obj.wind_direction_27 = var_wind_direction_27
        # real
        var_wind_direction_28 = 180.0
        obj.wind_direction_28 = var_wind_direction_28
        # real
        var_wind_direction_29 = 180.0
        obj.wind_direction_29 = var_wind_direction_29
        # real
        var_wind_direction_30 = 180.0
        obj.wind_direction_30 = var_wind_direction_30
        # real
        var_wind_direction_31 = 180.0
        obj.wind_direction_31 = var_wind_direction_31
        # real
        var_wind_direction_32 = 180.0
        obj.wind_direction_32 = var_wind_direction_32
        # real
        var_wind_direction_33 = 180.0
        obj.wind_direction_33 = var_wind_direction_33
        # real
        var_wind_direction_34 = 180.0
        obj.wind_direction_34 = var_wind_direction_34
        # real
        var_wind_direction_35 = 180.0
        obj.wind_direction_35 = var_wind_direction_35
        # real
        var_wind_direction_36 = 180.0
        obj.wind_direction_36 = var_wind_direction_36

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_1, var_wind_direction_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_2, var_wind_direction_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_3, var_wind_direction_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_4, var_wind_direction_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_5, var_wind_direction_5)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_6, var_wind_direction_6)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_7, var_wind_direction_7)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_8, var_wind_direction_8)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_9, var_wind_direction_9)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_10, var_wind_direction_10)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_11, var_wind_direction_11)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_12, var_wind_direction_12)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_13, var_wind_direction_13)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_14, var_wind_direction_14)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_15, var_wind_direction_15)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_16, var_wind_direction_16)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_17, var_wind_direction_17)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_18, var_wind_direction_18)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_19, var_wind_direction_19)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_20, var_wind_direction_20)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_21, var_wind_direction_21)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_22, var_wind_direction_22)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_23, var_wind_direction_23)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_24, var_wind_direction_24)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_25, var_wind_direction_25)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_26, var_wind_direction_26)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_27, var_wind_direction_27)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_28, var_wind_direction_28)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_29, var_wind_direction_29)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_30, var_wind_direction_30)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_31, var_wind_direction_31)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_32, var_wind_direction_32)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_33, var_wind_direction_33)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_34, var_wind_direction_34)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_35, var_wind_direction_35)
        self.assertAlmostEqual(idf2.airflownetworkmultizonewindpressurecoefficientarrays[0].wind_direction_36, var_wind_direction_36)