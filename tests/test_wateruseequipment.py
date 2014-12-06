import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_systems import WaterUseEquipment

log = logging.getLogger(__name__)

class TestWaterUseEquipment(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_wateruseequipment(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterUseEquipment()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_peak_flow_rate = 0.0
        obj.peak_flow_rate = var_peak_flow_rate
        # object-list
        var_flow_rate_fraction_schedule_name = "object-list|Flow Rate Fraction Schedule Name"
        obj.flow_rate_fraction_schedule_name = var_flow_rate_fraction_schedule_name
        # object-list
        var_target_temperature_schedule_name = "object-list|Target Temperature Schedule Name"
        obj.target_temperature_schedule_name = var_target_temperature_schedule_name
        # object-list
        var_hot_water_supply_temperature_schedule_name = "object-list|Hot Water Supply Temperature Schedule Name"
        obj.hot_water_supply_temperature_schedule_name = var_hot_water_supply_temperature_schedule_name
        # object-list
        var_cold_water_supply_temperature_schedule_name = "object-list|Cold Water Supply Temperature Schedule Name"
        obj.cold_water_supply_temperature_schedule_name = var_cold_water_supply_temperature_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_sensible_fraction_schedule_name = "object-list|Sensible Fraction Schedule Name"
        obj.sensible_fraction_schedule_name = var_sensible_fraction_schedule_name
        # object-list
        var_latent_fraction_schedule_name = "object-list|Latent Fraction Schedule Name"
        obj.latent_fraction_schedule_name = var_latent_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.wateruseequipments[0].name, var_name)
        self.assertEqual(idf2.wateruseequipments[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.wateruseequipments[0].peak_flow_rate, var_peak_flow_rate)
        self.assertEqual(idf2.wateruseequipments[0].flow_rate_fraction_schedule_name, var_flow_rate_fraction_schedule_name)
        self.assertEqual(idf2.wateruseequipments[0].target_temperature_schedule_name, var_target_temperature_schedule_name)
        self.assertEqual(idf2.wateruseequipments[0].hot_water_supply_temperature_schedule_name, var_hot_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.wateruseequipments[0].cold_water_supply_temperature_schedule_name, var_cold_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.wateruseequipments[0].zone_name, var_zone_name)
        self.assertEqual(idf2.wateruseequipments[0].sensible_fraction_schedule_name, var_sensible_fraction_schedule_name)
        self.assertEqual(idf2.wateruseequipments[0].latent_fraction_schedule_name, var_latent_fraction_schedule_name)