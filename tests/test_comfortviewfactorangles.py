import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.internal_gains import ComfortViewFactorAngles

log = logging.getLogger(__name__)

class TestComfortViewFactorAngles(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_comfortviewfactorangles(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComfortViewFactorAngles()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_surface_1_name = "object-list|Surface 1 Name"
        obj.surface_1_name = var_surface_1_name
        # real
        var_angle_factor_1 = 0.5
        obj.angle_factor_1 = var_angle_factor_1
        # object-list
        var_surface_2_name = "object-list|Surface 2 Name"
        obj.surface_2_name = var_surface_2_name
        # real
        var_angle_factor_2 = 0.5
        obj.angle_factor_2 = var_angle_factor_2
        # object-list
        var_surface_3_name = "object-list|Surface 3 Name"
        obj.surface_3_name = var_surface_3_name
        # real
        var_angle_factor_3 = 0.5
        obj.angle_factor_3 = var_angle_factor_3
        # object-list
        var_surface_4_name = "object-list|Surface 4 Name"
        obj.surface_4_name = var_surface_4_name
        # real
        var_angle_factor_4 = 0.5
        obj.angle_factor_4 = var_angle_factor_4
        # object-list
        var_surface_5_name = "object-list|Surface 5 Name"
        obj.surface_5_name = var_surface_5_name
        # real
        var_angle_factor_5 = 0.5
        obj.angle_factor_5 = var_angle_factor_5
        # object-list
        var_surface_6_name = "object-list|Surface 6 Name"
        obj.surface_6_name = var_surface_6_name
        # real
        var_angle_factor_6 = 0.5
        obj.angle_factor_6 = var_angle_factor_6
        # object-list
        var_surface_7_name = "object-list|Surface 7 Name"
        obj.surface_7_name = var_surface_7_name
        # real
        var_angle_factor_7 = 0.5
        obj.angle_factor_7 = var_angle_factor_7
        # object-list
        var_surface_8_name = "object-list|Surface 8 Name"
        obj.surface_8_name = var_surface_8_name
        # real
        var_angle_factor_8 = 0.5
        obj.angle_factor_8 = var_angle_factor_8
        # object-list
        var_surface_9_name = "object-list|Surface 9 Name"
        obj.surface_9_name = var_surface_9_name
        # real
        var_angle_factor_9 = 0.5
        obj.angle_factor_9 = var_angle_factor_9
        # object-list
        var_surface_10_name = "object-list|Surface 10 Name"
        obj.surface_10_name = var_surface_10_name
        # real
        var_angle_factor_10 = 0.5
        obj.angle_factor_10 = var_angle_factor_10
        # object-list
        var_surface_11_name = "object-list|Surface 11 Name"
        obj.surface_11_name = var_surface_11_name
        # real
        var_angle_factor_11 = 0.5
        obj.angle_factor_11 = var_angle_factor_11
        # object-list
        var_surface_12_name = "object-list|Surface 12 Name"
        obj.surface_12_name = var_surface_12_name
        # real
        var_angle_factor_12 = 0.5
        obj.angle_factor_12 = var_angle_factor_12
        # object-list
        var_surface_13_name = "object-list|Surface 13 Name"
        obj.surface_13_name = var_surface_13_name
        # real
        var_angle_factor_13 = 0.5
        obj.angle_factor_13 = var_angle_factor_13
        # object-list
        var_surface_14_name = "object-list|Surface 14 Name"
        obj.surface_14_name = var_surface_14_name
        # real
        var_angle_factor_14 = 0.5
        obj.angle_factor_14 = var_angle_factor_14
        # object-list
        var_surface_15_name = "object-list|Surface 15 Name"
        obj.surface_15_name = var_surface_15_name
        # real
        var_angle_factor_15 = 0.5
        obj.angle_factor_15 = var_angle_factor_15
        # object-list
        var_surface_16_name = "object-list|Surface 16 Name"
        obj.surface_16_name = var_surface_16_name
        # real
        var_angle_factor_16 = 0.5
        obj.angle_factor_16 = var_angle_factor_16
        # object-list
        var_surface_17_name = "object-list|Surface 17 Name"
        obj.surface_17_name = var_surface_17_name
        # real
        var_angle_factor_17 = 0.5
        obj.angle_factor_17 = var_angle_factor_17
        # object-list
        var_surface_18_name = "object-list|Surface 18 Name"
        obj.surface_18_name = var_surface_18_name
        # real
        var_angle_factor_18 = 0.5
        obj.angle_factor_18 = var_angle_factor_18
        # object-list
        var_surface_19_name = "object-list|Surface 19 Name"
        obj.surface_19_name = var_surface_19_name
        # real
        var_angle_factor_19 = 0.5
        obj.angle_factor_19 = var_angle_factor_19
        # object-list
        var_surface_20_name = "object-list|Surface 20 Name"
        obj.surface_20_name = var_surface_20_name
        # real
        var_angle_factor_20 = 0.5
        obj.angle_factor_20 = var_angle_factor_20

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.comfortviewfactorangless[0].name, var_name)
        self.assertEqual(idf2.comfortviewfactorangless[0].zone_name, var_zone_name)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_1_name, var_surface_1_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_1, var_angle_factor_1)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_2_name, var_surface_2_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_2, var_angle_factor_2)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_3_name, var_surface_3_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_3, var_angle_factor_3)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_4_name, var_surface_4_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_4, var_angle_factor_4)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_5_name, var_surface_5_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_5, var_angle_factor_5)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_6_name, var_surface_6_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_6, var_angle_factor_6)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_7_name, var_surface_7_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_7, var_angle_factor_7)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_8_name, var_surface_8_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_8, var_angle_factor_8)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_9_name, var_surface_9_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_9, var_angle_factor_9)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_10_name, var_surface_10_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_10, var_angle_factor_10)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_11_name, var_surface_11_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_11, var_angle_factor_11)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_12_name, var_surface_12_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_12, var_angle_factor_12)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_13_name, var_surface_13_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_13, var_angle_factor_13)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_14_name, var_surface_14_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_14, var_angle_factor_14)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_15_name, var_surface_15_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_15, var_angle_factor_15)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_16_name, var_surface_16_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_16, var_angle_factor_16)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_17_name, var_surface_17_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_17, var_angle_factor_17)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_18_name, var_surface_18_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_18, var_angle_factor_18)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_19_name, var_surface_19_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_19, var_angle_factor_19)
        self.assertEqual(idf2.comfortviewfactorangless[0].surface_20_name, var_surface_20_name)
        self.assertAlmostEqual(idf2.comfortviewfactorangless[0].angle_factor_20, var_angle_factor_20)