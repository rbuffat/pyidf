import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostatThermalComfort
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneControlThermostatThermalComfort(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolthermostatthermalcomfort(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlThermostatThermalComfort()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # alpha
        var_averaging_method = "SpecificObject"
        obj.averaging_method = var_averaging_method
        # object-list
        var_specific_people_name = "object-list|Specific People Name"
        obj.specific_people_name = var_specific_people_name
        # real
        var_minimum_drybulb_temperature_setpoint = 25.0
        obj.minimum_drybulb_temperature_setpoint = var_minimum_drybulb_temperature_setpoint
        # real
        var_maximum_drybulb_temperature_setpoint = 25.0
        obj.maximum_drybulb_temperature_setpoint = var_maximum_drybulb_temperature_setpoint
        # object-list
        var_thermal_comfort_control_type_schedule_name = "object-list|Thermal Comfort Control Type Schedule Name"
        obj.thermal_comfort_control_type_schedule_name = var_thermal_comfort_control_type_schedule_name
        # alpha
        var_thermal_comfort_control_1_object_type = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
        obj.thermal_comfort_control_1_object_type = var_thermal_comfort_control_1_object_type
        # object-list
        var_thermal_comfort_control_1_name = "object-list|Thermal Comfort Control 1 Name"
        obj.thermal_comfort_control_1_name = var_thermal_comfort_control_1_name
        # alpha
        var_thermal_comfort_control_2_object_type = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
        obj.thermal_comfort_control_2_object_type = var_thermal_comfort_control_2_object_type
        # object-list
        var_thermal_comfort_control_2_name = "object-list|Thermal Comfort Control 2 Name"
        obj.thermal_comfort_control_2_name = var_thermal_comfort_control_2_name
        # alpha
        var_thermal_comfort_control_3_object_type = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
        obj.thermal_comfort_control_3_object_type = var_thermal_comfort_control_3_object_type
        # object-list
        var_thermal_comfort_control_3_name = "object-list|Thermal Comfort Control 3 Name"
        obj.thermal_comfort_control_3_name = var_thermal_comfort_control_3_name
        # alpha
        var_thermal_comfort_control_4_object_type = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
        obj.thermal_comfort_control_4_object_type = var_thermal_comfort_control_4_object_type
        # object-list
        var_thermal_comfort_control_4_name = "object-list|Thermal Comfort Control 4 Name"
        obj.thermal_comfort_control_4_name = var_thermal_comfort_control_4_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].name, var_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].averaging_method, var_averaging_method)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].specific_people_name, var_specific_people_name)
        self.assertAlmostEqual(idf2.zonecontrolthermostatthermalcomforts[0].minimum_drybulb_temperature_setpoint, var_minimum_drybulb_temperature_setpoint)
        self.assertAlmostEqual(idf2.zonecontrolthermostatthermalcomforts[0].maximum_drybulb_temperature_setpoint, var_maximum_drybulb_temperature_setpoint)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_type_schedule_name, var_thermal_comfort_control_type_schedule_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_1_object_type, var_thermal_comfort_control_1_object_type)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_1_name, var_thermal_comfort_control_1_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_2_object_type, var_thermal_comfort_control_2_object_type)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_2_name, var_thermal_comfort_control_2_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_3_object_type, var_thermal_comfort_control_3_object_type)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_3_name, var_thermal_comfort_control_3_name)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_4_object_type, var_thermal_comfort_control_4_object_type)
        self.assertEqual(idf2.zonecontrolthermostatthermalcomforts[0].thermal_comfort_control_4_name, var_thermal_comfort_control_4_name)