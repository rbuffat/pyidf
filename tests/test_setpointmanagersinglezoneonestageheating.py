import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerSingleZoneOneStageHeating
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerSingleZoneOneStageHeating(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagersinglezoneonestageheating(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerSingleZoneOneStageHeating()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_heating_stage_on_supply_air_setpoint_temperature = 2.2
        obj.heating_stage_on_supply_air_setpoint_temperature = var_heating_stage_on_supply_air_setpoint_temperature
        # real
        var_heating_stage_off_supply_air_setpoint_temperature = 3.3
        obj.heating_stage_off_supply_air_setpoint_temperature = var_heating_stage_off_supply_air_setpoint_temperature
        # object-list
        var_control_zone_name = "object-list|Control Zone Name"
        obj.control_zone_name = var_control_zone_name
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagersinglezoneonestageheatings[0].name, var_name)
        self.assertAlmostEqual(idf2.setpointmanagersinglezoneonestageheatings[0].heating_stage_on_supply_air_setpoint_temperature, var_heating_stage_on_supply_air_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanagersinglezoneonestageheatings[0].heating_stage_off_supply_air_setpoint_temperature, var_heating_stage_off_supply_air_setpoint_temperature)
        self.assertEqual(idf2.setpointmanagersinglezoneonestageheatings[0].control_zone_name, var_control_zone_name)
        self.assertEqual(idf2.setpointmanagersinglezoneonestageheatings[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)