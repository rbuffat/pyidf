import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostatStagedDualSetpoint
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneControlThermostatStagedDualSetpoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolthermostatstageddualsetpoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlThermostatStagedDualSetpoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # integer
        var_number_of_heating_stages = 2
        obj.number_of_heating_stages = var_number_of_heating_stages
        # object-list
        var_heating_temperature_setpoint_schedule_name = "object-list|Heating Temperature Setpoint Schedule Name"
        obj.heating_temperature_setpoint_schedule_name = var_heating_temperature_setpoint_schedule_name
        # real
        var_heating_throttling_temperature_range = 0.0
        obj.heating_throttling_temperature_range = var_heating_throttling_temperature_range
        # real
        var_stage_1_heating_temperature_offset = 0.0
        obj.stage_1_heating_temperature_offset = var_stage_1_heating_temperature_offset
        # real
        var_stage_2_heating_temperature_offset = 0.0
        obj.stage_2_heating_temperature_offset = var_stage_2_heating_temperature_offset
        # real
        var_stage_3_heating_temperature_offset = 0.0
        obj.stage_3_heating_temperature_offset = var_stage_3_heating_temperature_offset
        # real
        var_stage_4_heating_temperature_offset = 0.0
        obj.stage_4_heating_temperature_offset = var_stage_4_heating_temperature_offset
        # integer
        var_number_of_cooling_stages = 2
        obj.number_of_cooling_stages = var_number_of_cooling_stages
        # object-list
        var_cooling_temperature_setpoint_base_schedule_name = "object-list|Cooling Temperature Setpoint Base Schedule Name"
        obj.cooling_temperature_setpoint_base_schedule_name = var_cooling_temperature_setpoint_base_schedule_name
        # real
        var_cooling_throttling_temperature_range = 0.0
        obj.cooling_throttling_temperature_range = var_cooling_throttling_temperature_range
        # real
        var_stage_1_cooling_temperature_offset = 0.0
        obj.stage_1_cooling_temperature_offset = var_stage_1_cooling_temperature_offset
        # real
        var_stage_2_cooling_temperature_offset = 0.0
        obj.stage_2_cooling_temperature_offset = var_stage_2_cooling_temperature_offset
        # real
        var_stage_3_cooling_temperature_offset = 0.0
        obj.stage_3_cooling_temperature_offset = var_stage_3_cooling_temperature_offset
        # real
        var_stage_4_cooling_temperature_offset = 0.0
        obj.stage_4_cooling_temperature_offset = var_stage_4_cooling_temperature_offset

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].name, var_name)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].number_of_heating_stages, var_number_of_heating_stages)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].heating_temperature_setpoint_schedule_name, var_heating_temperature_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].heating_throttling_temperature_range, var_heating_throttling_temperature_range)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_1_heating_temperature_offset, var_stage_1_heating_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_2_heating_temperature_offset, var_stage_2_heating_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_3_heating_temperature_offset, var_stage_3_heating_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_4_heating_temperature_offset, var_stage_4_heating_temperature_offset)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].number_of_cooling_stages, var_number_of_cooling_stages)
        self.assertEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].cooling_temperature_setpoint_base_schedule_name, var_cooling_temperature_setpoint_base_schedule_name)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].cooling_throttling_temperature_range, var_cooling_throttling_temperature_range)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_1_cooling_temperature_offset, var_stage_1_cooling_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_2_cooling_temperature_offset, var_stage_2_cooling_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_3_cooling_temperature_offset, var_stage_3_cooling_temperature_offset)
        self.assertAlmostEqual(idf2.zonecontrolthermostatstageddualsetpoints[0].stage_4_cooling_temperature_offset, var_stage_4_cooling_temperature_offset)