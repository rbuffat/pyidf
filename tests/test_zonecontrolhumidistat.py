import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlHumidistat
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneControlHumidistat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolhumidistat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlHumidistat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_humidifying_relative_humidity_setpoint_schedule_name = "object-list|Humidifying Relative Humidity Setpoint Schedule Name"
        obj.humidifying_relative_humidity_setpoint_schedule_name = var_humidifying_relative_humidity_setpoint_schedule_name
        # object-list
        var_dehumidifying_relative_humidity_setpoint_schedule_name = "object-list|Dehumidifying Relative Humidity Setpoint Schedule Name"
        obj.dehumidifying_relative_humidity_setpoint_schedule_name = var_dehumidifying_relative_humidity_setpoint_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolhumidistats[0].name, var_name)
        self.assertEqual(idf2.zonecontrolhumidistats[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonecontrolhumidistats[0].humidifying_relative_humidity_setpoint_schedule_name, var_humidifying_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.zonecontrolhumidistats[0].dehumidifying_relative_humidity_setpoint_schedule_name, var_dehumidifying_relative_humidity_setpoint_schedule_name)