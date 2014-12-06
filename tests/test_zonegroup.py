import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import ZoneGroup

log = logging.getLogger(__name__)

class TestZoneGroup(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonegroup(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneGroup()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_list_name = "object-list|Zone List Name"
        obj.zone_list_name = var_zone_list_name
        # integer
        var_zone_list_multiplier = 1
        obj.zone_list_multiplier = var_zone_list_multiplier

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonegroups[0].name, var_name)
        self.assertEqual(idf2.zonegroups[0].zone_list_name, var_zone_list_name)
        self.assertEqual(idf2.zonegroups[0].zone_list_multiplier, var_zone_list_multiplier)