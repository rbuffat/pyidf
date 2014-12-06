import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostat
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneControlThermostat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolthermostat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlThermostat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # object-list
        var_control_type_schedule_name = "object-list|Control Type Schedule Name"
        obj.control_type_schedule_name = var_control_type_schedule_name
        # alpha
        var_control_1_object_type = "ThermostatSetpoint:SingleHeating"
        obj.control_1_object_type = var_control_1_object_type
        # object-list
        var_control_1_name = "object-list|Control 1 Name"
        obj.control_1_name = var_control_1_name
        # alpha
        var_control_2_object_type = "ThermostatSetpoint:SingleHeating"
        obj.control_2_object_type = var_control_2_object_type
        # object-list
        var_control_2_name = "object-list|Control 2 Name"
        obj.control_2_name = var_control_2_name
        # alpha
        var_control_3_object_type = "ThermostatSetpoint:SingleHeating"
        obj.control_3_object_type = var_control_3_object_type
        # object-list
        var_control_3_name = "object-list|Control 3 Name"
        obj.control_3_name = var_control_3_name
        # alpha
        var_control_4_object_type = "ThermostatSetpoint:SingleHeating"
        obj.control_4_object_type = var_control_4_object_type
        # object-list
        var_control_4_name = "object-list|Control 4 Name"
        obj.control_4_name = var_control_4_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolthermostats[0].name, var_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_type_schedule_name, var_control_type_schedule_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_1_object_type, var_control_1_object_type)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_1_name, var_control_1_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_2_object_type, var_control_2_object_type)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_2_name, var_control_2_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_3_object_type, var_control_3_object_type)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_3_name, var_control_3_name)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_4_object_type, var_control_4_object_type)
        self.assertEqual(idf2.zonecontrolthermostats[0].control_4_name, var_control_4_name)