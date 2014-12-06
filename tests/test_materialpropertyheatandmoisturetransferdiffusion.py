import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialPropertyHeatAndMoistureTransferDiffusion
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMaterialPropertyHeatAndMoistureTransferDiffusion(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyheatandmoisturetransferdiffusion(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyHeatAndMoistureTransferDiffusion()
        # object-list
        var_material_name = "object-list|Material Name"
        obj.material_name = var_material_name
        # integer
        var_number_of_data_pairs = 13
        obj.number_of_data_pairs = var_number_of_data_pairs
        # real
        var_relative_humidity_fraction_1 = 0.5
        obj.relative_humidity_fraction_1 = var_relative_humidity_fraction_1
        # real
        var_water_vapor_diffusion_resistance_factor_1 = 0.0
        obj.water_vapor_diffusion_resistance_factor_1 = var_water_vapor_diffusion_resistance_factor_1
        # real
        var_relative_humidity_fraction_2 = 0.5
        obj.relative_humidity_fraction_2 = var_relative_humidity_fraction_2
        # real
        var_water_vapor_diffusion_resistance_factor_2 = 0.0
        obj.water_vapor_diffusion_resistance_factor_2 = var_water_vapor_diffusion_resistance_factor_2
        # real
        var_relative_humidity_fraction_3 = 0.5
        obj.relative_humidity_fraction_3 = var_relative_humidity_fraction_3
        # real
        var_water_vapor_diffusion_resistance_factor_3 = 0.0
        obj.water_vapor_diffusion_resistance_factor_3 = var_water_vapor_diffusion_resistance_factor_3
        # real
        var_relative_humidity_fraction_4 = 0.5
        obj.relative_humidity_fraction_4 = var_relative_humidity_fraction_4
        # real
        var_water_vapor_diffusion_resistance_factor_4 = 0.0
        obj.water_vapor_diffusion_resistance_factor_4 = var_water_vapor_diffusion_resistance_factor_4
        # real
        var_relative_humidity_fraction_5 = 0.5
        obj.relative_humidity_fraction_5 = var_relative_humidity_fraction_5
        # real
        var_water_vapor_diffusion_resistance_factor_5 = 0.0
        obj.water_vapor_diffusion_resistance_factor_5 = var_water_vapor_diffusion_resistance_factor_5
        # real
        var_relative_humidity_fraction_6 = 0.5
        obj.relative_humidity_fraction_6 = var_relative_humidity_fraction_6
        # real
        var_water_vapor_diffusion_resistance_factor_6 = 0.0
        obj.water_vapor_diffusion_resistance_factor_6 = var_water_vapor_diffusion_resistance_factor_6
        # real
        var_relative_humidity_fraction_7 = 0.5
        obj.relative_humidity_fraction_7 = var_relative_humidity_fraction_7
        # real
        var_water_vapor_diffusion_resistance_factor_7 = 0.0
        obj.water_vapor_diffusion_resistance_factor_7 = var_water_vapor_diffusion_resistance_factor_7
        # real
        var_relative_humidity_fraction_8 = 0.5
        obj.relative_humidity_fraction_8 = var_relative_humidity_fraction_8
        # real
        var_water_vapor_diffusion_resistance_factor_8 = 0.0
        obj.water_vapor_diffusion_resistance_factor_8 = var_water_vapor_diffusion_resistance_factor_8
        # real
        var_relative_humidity_fraction_9 = 0.5
        obj.relative_humidity_fraction_9 = var_relative_humidity_fraction_9
        # real
        var_water_vapor_diffusion_resistance_factor_9 = 0.0
        obj.water_vapor_diffusion_resistance_factor_9 = var_water_vapor_diffusion_resistance_factor_9
        # real
        var_relative_humidity_fraction_10 = 0.5
        obj.relative_humidity_fraction_10 = var_relative_humidity_fraction_10
        # real
        var_water_vapor_diffusion_resistance_factor_10 = 0.0
        obj.water_vapor_diffusion_resistance_factor_10 = var_water_vapor_diffusion_resistance_factor_10
        # real
        var_relative_humidity_fraction_11 = 0.5
        obj.relative_humidity_fraction_11 = var_relative_humidity_fraction_11
        # real
        var_water_vapor_diffusion_resistance_factor_11 = 0.0
        obj.water_vapor_diffusion_resistance_factor_11 = var_water_vapor_diffusion_resistance_factor_11
        # real
        var_relative_humidity_fraction_12 = 0.5
        obj.relative_humidity_fraction_12 = var_relative_humidity_fraction_12
        # real
        var_water_vapor_diffusion_resistance_factor_12 = 0.0
        obj.water_vapor_diffusion_resistance_factor_12 = var_water_vapor_diffusion_resistance_factor_12
        # real
        var_relative_humidity_fraction_13 = 0.5
        obj.relative_humidity_fraction_13 = var_relative_humidity_fraction_13
        # real
        var_water_vapor_diffusion_resistance_factor_13 = 0.0
        obj.water_vapor_diffusion_resistance_factor_13 = var_water_vapor_diffusion_resistance_factor_13
        # real
        var_relative_humidity_fraction_14 = 0.5
        obj.relative_humidity_fraction_14 = var_relative_humidity_fraction_14
        # real
        var_water_vapor_diffusion_resistance_factor_14 = 0.0
        obj.water_vapor_diffusion_resistance_factor_14 = var_water_vapor_diffusion_resistance_factor_14
        # real
        var_relative_humidity_fraction_15 = 0.5
        obj.relative_humidity_fraction_15 = var_relative_humidity_fraction_15
        # real
        var_water_vapor_diffusion_resistance_factor_15 = 0.0
        obj.water_vapor_diffusion_resistance_factor_15 = var_water_vapor_diffusion_resistance_factor_15
        # real
        var_relative_humidity_fraction_16 = 0.5
        obj.relative_humidity_fraction_16 = var_relative_humidity_fraction_16
        # real
        var_water_vapor_diffusion_resistance_factor_16 = 0.0
        obj.water_vapor_diffusion_resistance_factor_16 = var_water_vapor_diffusion_resistance_factor_16
        # real
        var_relative_humidity_fraction_17 = 0.5
        obj.relative_humidity_fraction_17 = var_relative_humidity_fraction_17
        # real
        var_water_vapor_diffusion_resistance_factor_17 = 0.0
        obj.water_vapor_diffusion_resistance_factor_17 = var_water_vapor_diffusion_resistance_factor_17
        # real
        var_relative_humidity_fraction_18 = 0.5
        obj.relative_humidity_fraction_18 = var_relative_humidity_fraction_18
        # real
        var_water_vapor_diffusion_resistance_factor_18 = 0.0
        obj.water_vapor_diffusion_resistance_factor_18 = var_water_vapor_diffusion_resistance_factor_18
        # real
        var_relative_humidity_fraction_19 = 0.5
        obj.relative_humidity_fraction_19 = var_relative_humidity_fraction_19
        # real
        var_water_vapor_diffusion_resistance_factor_19 = 0.0
        obj.water_vapor_diffusion_resistance_factor_19 = var_water_vapor_diffusion_resistance_factor_19
        # real
        var_relative_humidity_fraction_20 = 0.5
        obj.relative_humidity_fraction_20 = var_relative_humidity_fraction_20
        # real
        var_water_vapor_diffusion_resistance_factor_20 = 0.0
        obj.water_vapor_diffusion_resistance_factor_20 = var_water_vapor_diffusion_resistance_factor_20
        # real
        var_relative_humidity_fraction_21 = 0.5
        obj.relative_humidity_fraction_21 = var_relative_humidity_fraction_21
        # real
        var_water_vapor_diffusion_resistance_factor_21 = 0.0
        obj.water_vapor_diffusion_resistance_factor_21 = var_water_vapor_diffusion_resistance_factor_21
        # real
        var_relative_humidity_fraction_22 = 0.5
        obj.relative_humidity_fraction_22 = var_relative_humidity_fraction_22
        # real
        var_water_vapor_diffusion_resistance_factor_22 = 0.0
        obj.water_vapor_diffusion_resistance_factor_22 = var_water_vapor_diffusion_resistance_factor_22
        # real
        var_relative_humidity_fraction_23 = 0.5
        obj.relative_humidity_fraction_23 = var_relative_humidity_fraction_23
        # real
        var_water_vapor_diffusion_resistance_factor_23 = 0.0
        obj.water_vapor_diffusion_resistance_factor_23 = var_water_vapor_diffusion_resistance_factor_23
        # real
        var_relative_humidity_fraction_24 = 0.5
        obj.relative_humidity_fraction_24 = var_relative_humidity_fraction_24
        # real
        var_water_vapor_diffusion_resistance_factor_24 = 0.0
        obj.water_vapor_diffusion_resistance_factor_24 = var_water_vapor_diffusion_resistance_factor_24
        # real
        var_relative_humidity_fraction_25 = 0.5
        obj.relative_humidity_fraction_25 = var_relative_humidity_fraction_25
        # real
        var_water_vapor_diffusion_resistance_factor_25 = 0.0
        obj.water_vapor_diffusion_resistance_factor_25 = var_water_vapor_diffusion_resistance_factor_25

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].material_name, var_material_name)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].number_of_data_pairs, var_number_of_data_pairs)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_1, var_relative_humidity_fraction_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_1, var_water_vapor_diffusion_resistance_factor_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_2, var_relative_humidity_fraction_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_2, var_water_vapor_diffusion_resistance_factor_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_3, var_relative_humidity_fraction_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_3, var_water_vapor_diffusion_resistance_factor_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_4, var_relative_humidity_fraction_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_4, var_water_vapor_diffusion_resistance_factor_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_5, var_relative_humidity_fraction_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_5, var_water_vapor_diffusion_resistance_factor_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_6, var_relative_humidity_fraction_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_6, var_water_vapor_diffusion_resistance_factor_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_7, var_relative_humidity_fraction_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_7, var_water_vapor_diffusion_resistance_factor_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_8, var_relative_humidity_fraction_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_8, var_water_vapor_diffusion_resistance_factor_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_9, var_relative_humidity_fraction_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_9, var_water_vapor_diffusion_resistance_factor_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_10, var_relative_humidity_fraction_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_10, var_water_vapor_diffusion_resistance_factor_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_11, var_relative_humidity_fraction_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_11, var_water_vapor_diffusion_resistance_factor_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_12, var_relative_humidity_fraction_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_12, var_water_vapor_diffusion_resistance_factor_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_13, var_relative_humidity_fraction_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_13, var_water_vapor_diffusion_resistance_factor_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_14, var_relative_humidity_fraction_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_14, var_water_vapor_diffusion_resistance_factor_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_15, var_relative_humidity_fraction_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_15, var_water_vapor_diffusion_resistance_factor_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_16, var_relative_humidity_fraction_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_16, var_water_vapor_diffusion_resistance_factor_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_17, var_relative_humidity_fraction_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_17, var_water_vapor_diffusion_resistance_factor_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_18, var_relative_humidity_fraction_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_18, var_water_vapor_diffusion_resistance_factor_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_19, var_relative_humidity_fraction_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_19, var_water_vapor_diffusion_resistance_factor_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_20, var_relative_humidity_fraction_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_20, var_water_vapor_diffusion_resistance_factor_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_21, var_relative_humidity_fraction_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_21, var_water_vapor_diffusion_resistance_factor_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_22, var_relative_humidity_fraction_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_22, var_water_vapor_diffusion_resistance_factor_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_23, var_relative_humidity_fraction_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_23, var_water_vapor_diffusion_resistance_factor_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_24, var_relative_humidity_fraction_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_24, var_water_vapor_diffusion_resistance_factor_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].relative_humidity_fraction_25, var_relative_humidity_fraction_25)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferdiffusions[0].water_vapor_diffusion_resistance_factor_25, var_water_vapor_diffusion_resistance_factor_25)