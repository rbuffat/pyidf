import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerReturnTemperatureHotWater

log = logging.getLogger(__name__)

class TestSetpointManagerReturnTemperatureHotWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerreturntemperaturehotwater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerReturnTemperatureHotWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_plant_loop_supply_outlet_node = "node|Plant Loop Supply Outlet Node"
        obj.plant_loop_supply_outlet_node = var_plant_loop_supply_outlet_node
        # node
        var_plant_loop_supply_inlet_node = "node|Plant Loop Supply Inlet Node"
        obj.plant_loop_supply_inlet_node = var_plant_loop_supply_inlet_node
        # real
        var_minimum_supply_temperature_setpoint = 4.4
        obj.minimum_supply_temperature_setpoint = var_minimum_supply_temperature_setpoint
        # real
        var_maximum_supply_temperature_setpoint = 5.5
        obj.maximum_supply_temperature_setpoint = var_maximum_supply_temperature_setpoint
        # alpha
        var_return_temperature_setpoint_input_type = "Constant"
        obj.return_temperature_setpoint_input_type = var_return_temperature_setpoint_input_type
        # real
        var_return_temperature_setpoint_constant_value = 7.7
        obj.return_temperature_setpoint_constant_value = var_return_temperature_setpoint_constant_value
        # object-list
        var_return_temperature_setpoint_schedule_name = "object-list|Return Temperature Setpoint Schedule Name"
        obj.return_temperature_setpoint_schedule_name = var_return_temperature_setpoint_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].plant_loop_supply_outlet_node, var_plant_loop_supply_outlet_node)
        self.assertEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].plant_loop_supply_inlet_node, var_plant_loop_supply_inlet_node)
        self.assertAlmostEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].minimum_supply_temperature_setpoint, var_minimum_supply_temperature_setpoint)
        self.assertAlmostEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].maximum_supply_temperature_setpoint, var_maximum_supply_temperature_setpoint)
        self.assertEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].return_temperature_setpoint_input_type, var_return_temperature_setpoint_input_type)
        self.assertAlmostEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].return_temperature_setpoint_constant_value, var_return_temperature_setpoint_constant_value)
        self.assertEqual(idf2.setpointmanagerreturntemperaturehotwaters[0].return_temperature_setpoint_schedule_name, var_return_temperature_setpoint_schedule_name)