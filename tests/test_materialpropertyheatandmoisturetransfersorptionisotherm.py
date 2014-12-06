import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialPropertyHeatAndMoistureTransferSorptionIsotherm
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMaterialPropertyHeatAndMoistureTransferSorptionIsotherm(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyheatandmoisturetransfersorptionisotherm(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyHeatAndMoistureTransferSorptionIsotherm()
        # object-list
        var_material_name = "object-list|Material Name"
        obj.material_name = var_material_name
        # integer
        var_number_of_isotherm_coordinates = 13
        obj.number_of_isotherm_coordinates = var_number_of_isotherm_coordinates
        # real
        var_relative_humidity_fraction_1 = 0.5
        obj.relative_humidity_fraction_1 = var_relative_humidity_fraction_1
        # real
        var_moisture_content_1 = 0.0
        obj.moisture_content_1 = var_moisture_content_1
        # real
        var_relative_humidity_fraction_2 = 0.5
        obj.relative_humidity_fraction_2 = var_relative_humidity_fraction_2
        # real
        var_moisture_content_2 = 0.0
        obj.moisture_content_2 = var_moisture_content_2
        # real
        var_relative_humidity_fraction_3 = 0.5
        obj.relative_humidity_fraction_3 = var_relative_humidity_fraction_3
        # real
        var_moisture_content_3 = 0.0
        obj.moisture_content_3 = var_moisture_content_3
        # real
        var_relative_humidity_fraction_4 = 0.5
        obj.relative_humidity_fraction_4 = var_relative_humidity_fraction_4
        # real
        var_moisture_content_4 = 0.0
        obj.moisture_content_4 = var_moisture_content_4
        # real
        var_relative_humidity_fraction_5 = 0.5
        obj.relative_humidity_fraction_5 = var_relative_humidity_fraction_5
        # real
        var_moisture_content_5 = 0.0
        obj.moisture_content_5 = var_moisture_content_5
        # real
        var_relative_humidity_fraction_6 = 0.5
        obj.relative_humidity_fraction_6 = var_relative_humidity_fraction_6
        # real
        var_moisture_content_6 = 0.0
        obj.moisture_content_6 = var_moisture_content_6
        # real
        var_relative_humidity_fraction_7 = 0.5
        obj.relative_humidity_fraction_7 = var_relative_humidity_fraction_7
        # real
        var_moisture_content_7 = 0.0
        obj.moisture_content_7 = var_moisture_content_7
        # real
        var_relative_humidity_fraction_8 = 0.5
        obj.relative_humidity_fraction_8 = var_relative_humidity_fraction_8
        # real
        var_moisture_content_8 = 0.0
        obj.moisture_content_8 = var_moisture_content_8
        # real
        var_relative_humidity_fraction_9 = 0.5
        obj.relative_humidity_fraction_9 = var_relative_humidity_fraction_9
        # real
        var_moisture_content_9 = 0.0
        obj.moisture_content_9 = var_moisture_content_9
        # real
        var_relative_humidity_fraction_10 = 0.5
        obj.relative_humidity_fraction_10 = var_relative_humidity_fraction_10
        # real
        var_moisture_content_10 = 0.0
        obj.moisture_content_10 = var_moisture_content_10
        # real
        var_relative_humidity_fraction_11 = 0.5
        obj.relative_humidity_fraction_11 = var_relative_humidity_fraction_11
        # real
        var_moisture_content_11 = 0.0
        obj.moisture_content_11 = var_moisture_content_11
        # real
        var_relative_humidity_fraction_12 = 0.5
        obj.relative_humidity_fraction_12 = var_relative_humidity_fraction_12
        # real
        var_moisture_content_12 = 0.0
        obj.moisture_content_12 = var_moisture_content_12
        # real
        var_relative_humidity_fraction_13 = 0.5
        obj.relative_humidity_fraction_13 = var_relative_humidity_fraction_13
        # real
        var_moisture_content_13 = 0.0
        obj.moisture_content_13 = var_moisture_content_13
        # real
        var_relative_humidity_fraction_14 = 0.5
        obj.relative_humidity_fraction_14 = var_relative_humidity_fraction_14
        # real
        var_moisture_content_14 = 0.0
        obj.moisture_content_14 = var_moisture_content_14
        # real
        var_relative_humidity_fraction_15 = 0.5
        obj.relative_humidity_fraction_15 = var_relative_humidity_fraction_15
        # real
        var_moisture_content_15 = 0.0
        obj.moisture_content_15 = var_moisture_content_15
        # real
        var_relative_humidity_fraction_16 = 0.5
        obj.relative_humidity_fraction_16 = var_relative_humidity_fraction_16
        # real
        var_moisture_content_16 = 0.0
        obj.moisture_content_16 = var_moisture_content_16
        # real
        var_relative_humidity_fraction_17 = 0.5
        obj.relative_humidity_fraction_17 = var_relative_humidity_fraction_17
        # real
        var_moisture_content_17 = 0.0
        obj.moisture_content_17 = var_moisture_content_17
        # real
        var_relative_humidity_fraction_18 = 0.5
        obj.relative_humidity_fraction_18 = var_relative_humidity_fraction_18
        # real
        var_moisture_content_18 = 0.0
        obj.moisture_content_18 = var_moisture_content_18
        # real
        var_relative_humidity_fraction_19 = 0.5
        obj.relative_humidity_fraction_19 = var_relative_humidity_fraction_19
        # real
        var_moisture_content_19 = 0.0
        obj.moisture_content_19 = var_moisture_content_19
        # real
        var_relative_humidity_fraction_20 = 0.5
        obj.relative_humidity_fraction_20 = var_relative_humidity_fraction_20
        # real
        var_moisture_content_20 = 0.0
        obj.moisture_content_20 = var_moisture_content_20
        # real
        var_relative_humidity_fraction_21 = 0.5
        obj.relative_humidity_fraction_21 = var_relative_humidity_fraction_21
        # real
        var_moisture_content_21 = 0.0
        obj.moisture_content_21 = var_moisture_content_21
        # real
        var_relative_humidity_fraction_22 = 0.5
        obj.relative_humidity_fraction_22 = var_relative_humidity_fraction_22
        # real
        var_moisture_content_22 = 0.0
        obj.moisture_content_22 = var_moisture_content_22
        # real
        var_relative_humidity_fraction_23 = 0.5
        obj.relative_humidity_fraction_23 = var_relative_humidity_fraction_23
        # real
        var_moisture_content_23 = 0.0
        obj.moisture_content_23 = var_moisture_content_23
        # real
        var_relative_humidity_fraction_24 = 0.5
        obj.relative_humidity_fraction_24 = var_relative_humidity_fraction_24
        # real
        var_moisture_content_24 = 0.0
        obj.moisture_content_24 = var_moisture_content_24
        # real
        var_relative_humidity_fraction_25 = 0.5
        obj.relative_humidity_fraction_25 = var_relative_humidity_fraction_25
        # real
        var_moisture_content_25 = 0.0
        obj.moisture_content_25 = var_moisture_content_25

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].material_name, var_material_name)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].number_of_isotherm_coordinates, var_number_of_isotherm_coordinates)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_1, var_relative_humidity_fraction_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_1, var_moisture_content_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_2, var_relative_humidity_fraction_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_2, var_moisture_content_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_3, var_relative_humidity_fraction_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_3, var_moisture_content_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_4, var_relative_humidity_fraction_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_4, var_moisture_content_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_5, var_relative_humidity_fraction_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_5, var_moisture_content_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_6, var_relative_humidity_fraction_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_6, var_moisture_content_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_7, var_relative_humidity_fraction_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_7, var_moisture_content_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_8, var_relative_humidity_fraction_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_8, var_moisture_content_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_9, var_relative_humidity_fraction_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_9, var_moisture_content_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_10, var_relative_humidity_fraction_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_10, var_moisture_content_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_11, var_relative_humidity_fraction_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_11, var_moisture_content_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_12, var_relative_humidity_fraction_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_12, var_moisture_content_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_13, var_relative_humidity_fraction_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_13, var_moisture_content_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_14, var_relative_humidity_fraction_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_14, var_moisture_content_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_15, var_relative_humidity_fraction_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_15, var_moisture_content_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_16, var_relative_humidity_fraction_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_16, var_moisture_content_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_17, var_relative_humidity_fraction_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_17, var_moisture_content_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_18, var_relative_humidity_fraction_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_18, var_moisture_content_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_19, var_relative_humidity_fraction_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_19, var_moisture_content_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_20, var_relative_humidity_fraction_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_20, var_moisture_content_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_21, var_relative_humidity_fraction_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_21, var_moisture_content_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_22, var_relative_humidity_fraction_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_22, var_moisture_content_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_23, var_relative_humidity_fraction_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_23, var_moisture_content_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_24, var_relative_humidity_fraction_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_24, var_moisture_content_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].relative_humidity_fraction_25, var_relative_humidity_fraction_25)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersorptionisotherms[0].moisture_content_25, var_moisture_content_25)