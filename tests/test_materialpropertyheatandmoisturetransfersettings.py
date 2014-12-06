import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialPropertyHeatAndMoistureTransferSettings

log = logging.getLogger(__name__)

class TestMaterialPropertyHeatAndMoistureTransferSettings(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyheatandmoisturetransfersettings(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyHeatAndMoistureTransferSettings()
        # object-list
        var_material_name = "object-list|Material Name"
        obj.material_name = var_material_name
        # real
        var_porosity = 0.5
        obj.porosity = var_porosity
        # real
        var_initial_water_content_ratio = 0.0
        obj.initial_water_content_ratio = var_initial_water_content_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyheatandmoisturetransfersettingss[0].material_name, var_material_name)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersettingss[0].porosity, var_porosity)
        self.assertAlmostEqual(idf2.materialpropertyheatandmoisturetransfersettingss[0].initial_water_content_ratio, var_initial_water_content_ratio)