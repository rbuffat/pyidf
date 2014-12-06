import os
import tempfile
import unittest
import pyidf
from pyidf.economics import UtilityCostComputation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestUtilityCostComputation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostcomputation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostComputation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_tariff_name = "Tariff Name"
        obj.tariff_name = var_tariff_name
        # alpha
        var_compute_step_1 = "Compute Step 1"
        obj.compute_step_1 = var_compute_step_1
        # alpha
        var_compute_step_2 = "Compute Step 2"
        obj.compute_step_2 = var_compute_step_2
        # alpha
        var_compute_step_3 = "Compute Step 3"
        obj.compute_step_3 = var_compute_step_3
        # alpha
        var_compute_step_4 = "Compute Step 4"
        obj.compute_step_4 = var_compute_step_4
        # alpha
        var_compute_step_5 = "Compute Step 5"
        obj.compute_step_5 = var_compute_step_5
        # alpha
        var_compute_step_6 = "Compute Step 6"
        obj.compute_step_6 = var_compute_step_6
        # alpha
        var_compute_step_7 = "Compute Step 7"
        obj.compute_step_7 = var_compute_step_7
        # alpha
        var_compute_step_8 = "Compute Step 8"
        obj.compute_step_8 = var_compute_step_8
        # alpha
        var_compute_step_9 = "Compute Step 9"
        obj.compute_step_9 = var_compute_step_9
        # alpha
        var_compute_step_10 = "Compute Step 10"
        obj.compute_step_10 = var_compute_step_10
        # alpha
        var_compute_step_11 = "Compute Step 11"
        obj.compute_step_11 = var_compute_step_11
        # alpha
        var_compute_step_12 = "Compute Step 12"
        obj.compute_step_12 = var_compute_step_12
        # alpha
        var_compute_step_13 = "Compute Step 13"
        obj.compute_step_13 = var_compute_step_13
        # alpha
        var_compute_step_14 = "Compute Step 14"
        obj.compute_step_14 = var_compute_step_14
        # alpha
        var_compute_step_15 = "Compute Step 15"
        obj.compute_step_15 = var_compute_step_15
        # alpha
        var_compute_step_16 = "Compute Step 16"
        obj.compute_step_16 = var_compute_step_16
        # alpha
        var_compute_step_17 = "Compute Step 17"
        obj.compute_step_17 = var_compute_step_17
        # alpha
        var_compute_step_18 = "Compute Step 18"
        obj.compute_step_18 = var_compute_step_18
        # alpha
        var_compute_step_19 = "Compute Step 19"
        obj.compute_step_19 = var_compute_step_19
        # alpha
        var_compute_step_20 = "Compute Step 20"
        obj.compute_step_20 = var_compute_step_20
        # alpha
        var_compute_step_21 = "Compute Step 21"
        obj.compute_step_21 = var_compute_step_21
        # alpha
        var_compute_step_22 = "Compute Step 22"
        obj.compute_step_22 = var_compute_step_22
        # alpha
        var_compute_step_23 = "Compute Step 23"
        obj.compute_step_23 = var_compute_step_23
        # alpha
        var_compute_step_24 = "Compute Step 24"
        obj.compute_step_24 = var_compute_step_24
        # alpha
        var_compute_step_25 = "Compute Step 25"
        obj.compute_step_25 = var_compute_step_25
        # alpha
        var_compute_step_26 = "Compute Step 26"
        obj.compute_step_26 = var_compute_step_26
        # alpha
        var_compute_step_27 = "Compute Step 27"
        obj.compute_step_27 = var_compute_step_27
        # alpha
        var_compute_step_28 = "Compute Step 28"
        obj.compute_step_28 = var_compute_step_28
        # alpha
        var_compute_step_29 = "Compute Step 29"
        obj.compute_step_29 = var_compute_step_29
        # alpha
        var_compute_step_30 = "Compute Step 30"
        obj.compute_step_30 = var_compute_step_30

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostcomputations[0].name, var_name)
        self.assertEqual(idf2.utilitycostcomputations[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_1, var_compute_step_1)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_2, var_compute_step_2)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_3, var_compute_step_3)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_4, var_compute_step_4)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_5, var_compute_step_5)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_6, var_compute_step_6)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_7, var_compute_step_7)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_8, var_compute_step_8)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_9, var_compute_step_9)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_10, var_compute_step_10)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_11, var_compute_step_11)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_12, var_compute_step_12)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_13, var_compute_step_13)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_14, var_compute_step_14)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_15, var_compute_step_15)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_16, var_compute_step_16)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_17, var_compute_step_17)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_18, var_compute_step_18)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_19, var_compute_step_19)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_20, var_compute_step_20)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_21, var_compute_step_21)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_22, var_compute_step_22)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_23, var_compute_step_23)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_24, var_compute_step_24)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_25, var_compute_step_25)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_26, var_compute_step_26)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_27, var_compute_step_27)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_28, var_compute_step_28)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_29, var_compute_step_29)
        self.assertEqual(idf2.utilitycostcomputations[0].compute_step_30, var_compute_step_30)