import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_systems import WaterUseRainCollector

log = logging.getLogger(__name__)

class TestWaterUseRainCollector(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_wateruseraincollector(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterUseRainCollector()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_storage_tank_name = "object-list|Storage Tank Name"
        obj.storage_tank_name = var_storage_tank_name
        # alpha
        var_loss_factor_mode = "Constant"
        obj.loss_factor_mode = var_loss_factor_mode
        # real
        var_collection_loss_factor = 4.4
        obj.collection_loss_factor = var_collection_loss_factor
        # object-list
        var_collection_loss_factor_schedule_name = "object-list|Collection Loss Factor Schedule Name"
        obj.collection_loss_factor_schedule_name = var_collection_loss_factor_schedule_name
        # real
        var_maximum_collection_rate = 6.6
        obj.maximum_collection_rate = var_maximum_collection_rate
        paras = []
        var_collection_surface_1_name = "object-list|Collection Surface 1 Name"
        paras.append(var_collection_surface_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.wateruseraincollectors[0].name, var_name)
        self.assertEqual(idf2.wateruseraincollectors[0].storage_tank_name, var_storage_tank_name)
        self.assertEqual(idf2.wateruseraincollectors[0].loss_factor_mode, var_loss_factor_mode)
        self.assertAlmostEqual(idf2.wateruseraincollectors[0].collection_loss_factor, var_collection_loss_factor)
        self.assertEqual(idf2.wateruseraincollectors[0].collection_loss_factor_schedule_name, var_collection_loss_factor_schedule_name)
        self.assertAlmostEqual(idf2.wateruseraincollectors[0].maximum_collection_rate, var_maximum_collection_rate)
        index = obj.extensible_field_index("Collection Surface 1 Name")
        self.assertEqual(idf2.wateruseraincollectors[0].extensibles[0][index], var_collection_surface_1_name)