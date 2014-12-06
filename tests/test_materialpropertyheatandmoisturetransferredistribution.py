import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialPropertyHeatAndMoistureTransferRedistribution

log = logging.getLogger(__name__)

class TestMaterialPropertyHeatAndMoistureTransferRedistribution(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyheatandmoisturetransferredistribution(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyHeatAndMoistureTransferRedistribution()
        # object-list
        var_material_name = "object-list|Material Name"
        obj.material_name = var_material_name
        # integer
        var_number_of_redistribution_points = 13
        obj.number_of_redistribution_points = var_number_of_redistribution_points
        # real
        var_moisture_content_1 = 0.0
        obj.moisture_content_1 = var_moisture_content_1
        # real
        var_liquid_transport_coefficient_1 = 0.0
        obj.liquid_transport_coefficient_1 = var_liquid_transport_coefficient_1
        # real
        var_moisture_content_2 = 0.0
        obj.moisture_content_2 = var_moisture_content_2
        # real
        var_liquid_transport_coefficient_2 = 0.0
        obj.liquid_transport_coefficient_2 = var_liquid_transport_coefficient_2
        # real
        var_moisture_content_3 = 0.0
        obj.moisture_content_3 = var_moisture_content_3
        # real
        var_liquid_transport_coefficient_3 = 0.0
        obj.liquid_transport_coefficient_3 = var_liquid_transport_coefficient_3
        # real
        var_moisture_content_4 = 0.0
        obj.moisture_content_4 = var_moisture_content_4
        # real
        var_liquid_transport_coefficient_4 = 0.0
        obj.liquid_transport_coefficient_4 = var_liquid_transport_coefficient_4
        # real
        var_moisture_content_5 = 0.0
        obj.moisture_content_5 = var_moisture_content_5
        # real
        var_liquid_transport_coefficient_5 = 0.0
        obj.liquid_transport_coefficient_5 = var_liquid_transport_coefficient_5
        # real
        var_moisture_content_6 = 0.0
        obj.moisture_content_6 = var_moisture_content_6
        # real
        var_liquid_transport_coefficient_6 = 0.0
        obj.liquid_transport_coefficient_6 = var_liquid_transport_coefficient_6
        # real
        var_moisture_content_7 = 0.0
        obj.moisture_content_7 = var_moisture_content_7
        # real
        var_liquid_transport_coefficient_7 = 0.0
        obj.liquid_transport_coefficient_7 = var_liquid_transport_coefficient_7
        # real
        var_moisture_content_8 = 0.0
        obj.moisture_content_8 = var_moisture_content_8
        # real
        var_liquid_transport_coefficient_8 = 0.0
        obj.liquid_transport_coefficient_8 = var_liquid_transport_coefficient_8
        # real
        var_moisture_content_9 = 0.0
        obj.moisture_content_9 = var_moisture_content_9
        # real
        var_liquid_transport_coefficient_9 = 0.0
        obj.liquid_transport_coefficient_9 = var_liquid_transport_coefficient_9
        # real
        var_moisture_content_10 = 0.0
        obj.moisture_content_10 = var_moisture_content_10
        # real
        var_liquid_transport_coefficient_10 = 0.0
        obj.liquid_transport_coefficient_10 = var_liquid_transport_coefficient_10
        # real
        var_moisture_content_11 = 0.0
        obj.moisture_content_11 = var_moisture_content_11
        # real
        var_liquid_transport_coefficient_11 = 0.0
        obj.liquid_transport_coefficient_11 = var_liquid_transport_coefficient_11
        # real
        var_moisture_content_12 = 0.0
        obj.moisture_content_12 = var_moisture_content_12
        # real
        var_liquid_transport_coefficient_12 = 0.0
        obj.liquid_transport_coefficient_12 = var_liquid_transport_coefficient_12
        # real
        var_moisture_content_13 = 0.0
        obj.moisture_content_13 = var_moisture_content_13
        # real
        var_liquid_transport_coefficient_13 = 0.0
        obj.liquid_transport_coefficient_13 = var_liquid_transport_coefficient_13
        # real
        var_moisture_content_14 = 0.0
        obj.moisture_content_14 = var_moisture_content_14
        # real
        var_liquid_transport_coefficient_14 = 0.0
        obj.liquid_transport_coefficient_14 = var_liquid_transport_coefficient_14
        # real
        var_moisture_content_15 = 0.0
        obj.moisture_content_15 = var_moisture_content_15
        # real
        var_liquid_transport_coefficient_15 = 0.0
        obj.liquid_transport_coefficient_15 = var_liquid_transport_coefficient_15
        # real
        var_moisture_content_16 = 0.0
        obj.moisture_content_16 = var_moisture_content_16
        # real
        var_liquid_transport_coefficient_16 = 0.0
        obj.liquid_transport_coefficient_16 = var_liquid_transport_coefficient_16
        # real
        var_moisture_content_17 = 0.0
        obj.moisture_content_17 = var_moisture_content_17
        # real
        var_liquid_transport_coefficient_17 = 0.0
        obj.liquid_transport_coefficient_17 = var_liquid_transport_coefficient_17
        # real
        var_moisture_content_18 = 0.0
        obj.moisture_content_18 = var_moisture_content_18
        # real
        var_liquid_transport_coefficient_18 = 0.0
        obj.liquid_transport_coefficient_18 = var_liquid_transport_coefficient_18
        # real
        var_moisture_content_19 = 0.0
        obj.moisture_content_19 = var_moisture_content_19
        # real
        var_liquid_transport_coefficient_19 = 0.0
        obj.liquid_transport_coefficient_19 = var_liquid_transport_coefficient_19
        # real
        var_moisture_content_20 = 0.0
        obj.moisture_content_20 = var_moisture_content_20
        # real
        var_liquid_transport_coefficient_20 = 0.0
        obj.liquid_transport_coefficient_20 = var_liquid_transport_coefficient_20
        # real
        var_moisture_content_21 = 0.0
        obj.moisture_content_21 = var_moisture_content_21
        # real
        var_liquid_transport_coefficient_21 = 0.0
        obj.liquid_transport_coefficient_21 = var_liquid_transport_coefficient_21
        # real
        var_moisture_content_22 = 0.0
        obj.moisture_content_22 = var_moisture_content_22
        # real
        var_liquid_transport_coefficient_22 = 0.0
        obj.liquid_transport_coefficient_22 = var_liquid_transport_coefficient_22
        # real
        var_moisture_content_23 = 0.0
        obj.moisture_content_23 = var_moisture_content_23
        # real
        var_liquid_transport_coefficient_23 = 0.0
        obj.liquid_transport_coefficient_23 = var_liquid_transport_coefficient_23
        # real
        var_moisture_content_24 = 0.0
        obj.moisture_content_24 = var_moisture_content_24
        # real
        var_liquid_transport_coefficient_24 = 0.0
        obj.liquid_transport_coefficient_24 = var_liquid_transport_coefficient_24
        # real
        var_moisture_content_25 = 0.0
        obj.moisture_content_25 = var_moisture_content_25
        # real
        var_liquid_transport_coefficient_25 = 0.0
        obj.liquid_transport_coefficient_25 = var_liquid_transport_coefficient_25

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].material_name, var_material_name)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].number_of_redistribution_points, var_number_of_redistribution_points)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_1, var_moisture_content_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_1, var_liquid_transport_coefficient_1)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_2, var_moisture_content_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_2, var_liquid_transport_coefficient_2)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_3, var_moisture_content_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_3, var_liquid_transport_coefficient_3)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_4, var_moisture_content_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_4, var_liquid_transport_coefficient_4)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_5, var_moisture_content_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_5, var_liquid_transport_coefficient_5)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_6, var_moisture_content_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_6, var_liquid_transport_coefficient_6)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_7, var_moisture_content_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_7, var_liquid_transport_coefficient_7)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_8, var_moisture_content_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_8, var_liquid_transport_coefficient_8)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_9, var_moisture_content_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_9, var_liquid_transport_coefficient_9)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_10, var_moisture_content_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_10, var_liquid_transport_coefficient_10)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_11, var_moisture_content_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_11, var_liquid_transport_coefficient_11)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_12, var_moisture_content_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_12, var_liquid_transport_coefficient_12)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_13, var_moisture_content_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_13, var_liquid_transport_coefficient_13)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_14, var_moisture_content_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_14, var_liquid_transport_coefficient_14)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_15, var_moisture_content_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_15, var_liquid_transport_coefficient_15)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_16, var_moisture_content_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_16, var_liquid_transport_coefficient_16)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_17, var_moisture_content_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_17, var_liquid_transport_coefficient_17)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_18, var_moisture_content_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_18, var_liquid_transport_coefficient_18)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_19, var_moisture_content_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_19, var_liquid_transport_coefficient_19)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_20, var_moisture_content_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_20, var_liquid_transport_coefficient_20)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_21, var_moisture_content_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_21, var_liquid_transport_coefficient_21)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_22, var_moisture_content_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_22, var_liquid_transport_coefficient_22)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_23, var_moisture_content_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_23, var_liquid_transport_coefficient_23)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_24, var_moisture_content_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_24, var_liquid_transport_coefficient_24)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].moisture_content_25, var_moisture_content_25)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransferredistributions[0].liquid_transport_coefficient_25, var_liquid_transport_coefficient_25)