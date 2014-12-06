import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneRefrigerationDoorMixing

log = logging.getLogger(__name__)

class TestZoneRefrigerationDoorMixing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonerefrigerationdoormixing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneRefrigerationDoorMixing()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_1_name = "object-list|Zone 1 Name"
        obj.zone_1_name = var_zone_1_name
        # object-list
        var_zone_2_name = "object-list|Zone 2 Name"
        obj.zone_2_name = var_zone_2_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_door_height = 25.0
        obj.door_height = var_door_height
        # real
        var_door_area = 200.0
        obj.door_area = var_door_area
        # alpha
        var_door_protection_type = "None"
        obj.door_protection_type = var_door_protection_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonerefrigerationdoormixings[0].name, var_name)
        self.assertEqual(idf2.zonerefrigerationdoormixings[0].zone_1_name, var_zone_1_name)
        self.assertEqual(idf2.zonerefrigerationdoormixings[0].zone_2_name, var_zone_2_name)
        self.assertEqual(idf2.zonerefrigerationdoormixings[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zonerefrigerationdoormixings[0].door_height, var_door_height)
        self.assertAlmostEqual(idf2.zonerefrigerationdoormixings[0].door_area, var_door_area)
        self.assertEqual(idf2.zonerefrigerationdoormixings[0].door_protection_type, var_door_protection_type)