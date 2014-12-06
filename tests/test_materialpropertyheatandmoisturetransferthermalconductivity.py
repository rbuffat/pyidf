import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialPropertyHeatAndMoistureTransferThermalConductivity
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMaterialPropertyHeatAndMoistureTransferThermalConductivity(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyheatandmoisturetransferthermalconductivity(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyHeatAndMoistureTransferThermalConductivity()
        # object-list
        var_material_name = "object-list|Material Name"
        obj.material_name = var_material_name
        # integer
        var_number_of_thermal_coordinates = 13
        obj.number_of_thermal_coordinates = var_number_of_thermal_coordinates
        # real
        var_moisture_content_1 = 0.0
        obj.moisture_content_1 = var_moisture_content_1
        # real
        var_thermal_conductivity_1 = 0.0001
        obj.thermal_conductivity_1 = var_thermal_conductivity_1
        # real
        var_moisture_content_2 = 0.0
        obj.moisture_content_2 = var_moisture_content_2
        # real
        var_thermal_conductivity_2 = 0.0001
        obj.thermal_conductivity_2 = var_thermal_conductivity_2
        # real
        var_moisture_content_3 = 0.0
        obj.moisture_content_3 = var_moisture_content_3
        # real
        var_thermal_conductivity_3 = 0.0001
        obj.thermal_conductivity_3 = var_thermal_conductivity_3
        # real
        var_moisture_content_4 = 0.0
        obj.moisture_content_4 = var_moisture_content_4
        # real
        var_thermal_conductivity_4 = 0.0001
        obj.thermal_conductivity_4 = var_thermal_conductivity_4
        # real
        var_moisture_content_5 = 0.0
        obj.moisture_content_5 = var_moisture_content_5
        # real
        var_thermal_conductivity_5 = 0.0001
        obj.thermal_conductivity_5 = var_thermal_conductivity_5
        # real
        var_moisture_content_6 = 0.0
        obj.moisture_content_6 = var_moisture_content_6
        # real
        var_thermal_conductivity_6 = 0.0001
        obj.thermal_conductivity_6 = var_thermal_conductivity_6
        # real
        var_moisture_content_7 = 0.0
        obj.moisture_content_7 = var_moisture_content_7
        # real
        var_thermal_conductivity_7 = 0.0001
        obj.thermal_conductivity_7 = var_thermal_conductivity_7
        # real
        var_moisture_content_8 = 0.0
        obj.moisture_content_8 = var_moisture_content_8
        # real
        var_thermal_conductivity_8 = 0.0001
        obj.thermal_conductivity_8 = var_thermal_conductivity_8
        # real
        var_moisture_content_9 = 0.0
        obj.moisture_content_9 = var_moisture_content_9
        # real
        var_thermal_conductivity_9 = 0.0001
        obj.thermal_conductivity_9 = var_thermal_conductivity_9
        # real
        var_moisture_content_10 = 0.0
        obj.moisture_content_10 = var_moisture_content_10
        # real
        var_thermal_conductivity_10 = 0.0001
        obj.thermal_conductivity_10 = var_thermal_conductivity_10
        # real
        var_moisture_content_11 = 0.0
        obj.moisture_content_11 = var_moisture_content_11
        # real
        var_thermal_conductivity_11 = 0.0001
        obj.thermal_conductivity_11 = var_thermal_conductivity_11
        # real
        var_moisture_content_12 = 0.0
        obj.moisture_content_12 = var_moisture_content_12
        # real
        var_thermal_conductivity_12 = 0.0001
        obj.thermal_conductivity_12 = var_thermal_conductivity_12
        # real
        var_moisture_content_13 = 0.0
        obj.moisture_content_13 = var_moisture_content_13
        # real
        var_thermal_conductivity_13 = 0.0001
        obj.thermal_conductivity_13 = var_thermal_conductivity_13
        # real
        var_moisture_content_14 = 0.0
        obj.moisture_content_14 = var_moisture_content_14
        # real
        var_thermal_conductivity_14 = 0.0001
        obj.thermal_conductivity_14 = var_thermal_conductivity_14
        # real
        var_moisture_content_15 = 0.0
        obj.moisture_content_15 = var_moisture_content_15
        # real
        var_thermal_conductivity_15 = 0.0001
        obj.thermal_conductivity_15 = var_thermal_conductivity_15
        # real
        var_moisture_content_16 = 0.0
        obj.moisture_content_16 = var_moisture_content_16
        # real
        var_thermal_conductivity_16 = 0.0001
        obj.thermal_conductivity_16 = var_thermal_conductivity_16
        # real
        var_moisture_content_17 = 0.0
        obj.moisture_content_17 = var_moisture_content_17
        # real
        var_thermal_conductivity_17 = 0.0001
        obj.thermal_conductivity_17 = var_thermal_conductivity_17
        # real
        var_moisture_content_18 = 0.0
        obj.moisture_content_18 = var_moisture_content_18
        # real
        var_thermal_conductivity_18 = 0.0001
        obj.thermal_conductivity_18 = var_thermal_conductivity_18
        # real
        var_moisture_content_19 = 0.0
        obj.moisture_content_19 = var_moisture_content_19
        # real
        var_thermal_conductivity_19 = 0.0001
        obj.thermal_conductivity_19 = var_thermal_conductivity_19
        # real
        var_moisture_content_20 = 0.0
        obj.moisture_content_20 = var_moisture_content_20
        # real
        var_thermal_conductivity_20 = 0.0001
        obj.thermal_conductivity_20 = var_thermal_conductivity_20
        # real
        var_moisture_content_21 = 0.0
        obj.moisture_content_21 = var_moisture_content_21
        # real
        var_thermal_conductivity_21 = 0.0001
        obj.thermal_conductivity_21 = var_thermal_conductivity_21
        # real
        var_moisture_content_22 = 0.0
        obj.moisture_content_22 = var_moisture_content_22
        # real
        var_thermal_conductivity_22 = 0.0001
        obj.thermal_conductivity_22 = var_thermal_conductivity_22
        # real
        var_moisture_content_23 = 0.0
        obj.moisture_content_23 = var_moisture_content_23
        # real
        var_thermal_conductivity_23 = 0.0001
        obj.thermal_conductivity_23 = var_thermal_conductivity_23
        # real
        var_moisture_content_24 = 0.0
        obj.moisture_content_24 = var_moisture_content_24
        # real
        var_thermal_conductivity_24 = 0.0001
        obj.thermal_conductivity_24 = var_thermal_conductivity_24
        # real
        var_moisture_content_25 = 0.0
        obj.moisture_content_25 = var_moisture_content_25
        # real
        var_thermal_conductivity_25 = 0.0001
        obj.thermal_conductivity_25 = var_thermal_conductivity_25

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].material_name, var_material_name)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].number_of_thermal_coordinates, var_number_of_thermal_coordinates)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_1, var_moisture_content_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_1, var_thermal_conductivity_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_2, var_moisture_content_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_2, var_thermal_conductivity_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_3, var_moisture_content_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_3, var_thermal_conductivity_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_4, var_moisture_content_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_4, var_thermal_conductivity_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_5, var_moisture_content_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_5, var_thermal_conductivity_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_6, var_moisture_content_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_6, var_thermal_conductivity_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_7, var_moisture_content_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_7, var_thermal_conductivity_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_8, var_moisture_content_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_8, var_thermal_conductivity_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_9, var_moisture_content_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_9, var_thermal_conductivity_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_10, var_moisture_content_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_10, var_thermal_conductivity_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_11, var_moisture_content_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_11, var_thermal_conductivity_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_12, var_moisture_content_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_12, var_thermal_conductivity_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_13, var_moisture_content_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_13, var_thermal_conductivity_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_14, var_moisture_content_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_14, var_thermal_conductivity_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_15, var_moisture_content_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_15, var_thermal_conductivity_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_16, var_moisture_content_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_16, var_thermal_conductivity_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_17, var_moisture_content_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_17, var_thermal_conductivity_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_18, var_moisture_content_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_18, var_thermal_conductivity_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_19, var_moisture_content_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_19, var_thermal_conductivity_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_20, var_moisture_content_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_20, var_thermal_conductivity_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_21, var_moisture_content_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_21, var_thermal_conductivity_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_22, var_moisture_content_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_22, var_thermal_conductivity_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_23, var_moisture_content_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_23, var_thermal_conductivity_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_24, var_moisture_content_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_24, var_thermal_conductivity_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].moisture_content_25, var_moisture_content_25)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferthermalconductivitys[0].thermal_conductivity_25, var_thermal_conductivity_25)