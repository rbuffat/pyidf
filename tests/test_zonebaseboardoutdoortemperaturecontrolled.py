import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ZoneBaseboardOutdoorTemperatureControlled
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneBaseboardOutdoorTemperatureControlled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonebaseboardoutdoortemperaturecontrolled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneBaseboardOutdoorTemperatureControlled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_capacity_at_low_temperature = 0.0001
        obj.capacity_at_low_temperature = var_capacity_at_low_temperature
        # real
        var_low_temperature = 5.5
        obj.low_temperature = var_low_temperature
        # real
        var_capacity_at_high_temperature = 0.0
        obj.capacity_at_high_temperature = var_capacity_at_high_temperature
        # real
        var_high_temperature = 7.7
        obj.high_temperature = var_high_temperature
        # real
        var_fraction_radiant = 0.5
        obj.fraction_radiant = var_fraction_radiant
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].name, var_name)
        self.assertEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].capacity_at_low_temperature, var_capacity_at_low_temperature)
        self.assertAlmostEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].low_temperature, var_low_temperature)
        self.assertAlmostEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].capacity_at_high_temperature, var_capacity_at_high_temperature)
        self.assertAlmostEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].high_temperature, var_high_temperature)
        self.assertAlmostEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].fraction_radiant, var_fraction_radiant)
        self.assertEqual(idf2.zonebaseboardoutdoortemperaturecontrolleds[0].enduse_subcategory, var_enduse_subcategory)