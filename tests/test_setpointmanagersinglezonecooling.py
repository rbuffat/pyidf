import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerSingleZoneCooling
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerSingleZoneCooling(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagersinglezonecooling(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerSingleZoneCooling()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # real
        var_minimum_supply_air_temperature = 3.3
        obj.minimum_supply_air_temperature = var_minimum_supply_air_temperature
        # real
        var_maximum_supply_air_temperature = 4.4
        obj.maximum_supply_air_temperature = var_maximum_supply_air_temperature
        # object-list
        var_control_zone_name = "object-list|Control Zone Name"
        obj.control_zone_name = var_control_zone_name
        # node
        var_zone_node_name = "node|Zone Node Name"
        obj.zone_node_name = var_zone_node_name
        # node
        var_zone_inlet_node_name = "node|Zone Inlet Node Name"
        obj.zone_inlet_node_name = var_zone_inlet_node_name
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
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].name, var_name)
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].control_variable, var_control_variable)
        self.assertAlmostEqual(idf2.setpointmanagersinglezonecoolings[0].minimum_supply_air_temperature, var_minimum_supply_air_temperature)
        self.assertAlmostEqual(idf2.setpointmanagersinglezonecoolings[0].maximum_supply_air_temperature, var_maximum_supply_air_temperature)
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].control_zone_name, var_control_zone_name)
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].zone_node_name, var_zone_node_name)
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].zone_inlet_node_name, var_zone_inlet_node_name)
        self.assertEqual(idf2.setpointmanagersinglezonecoolings[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)