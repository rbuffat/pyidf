import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerWarmestTemperatureFlow
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerWarmestTemperatureFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerwarmesttemperatureflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerWarmestTemperatureFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # object-list
        var_hvac_air_loop_name = "object-list|HVAC Air Loop Name"
        obj.hvac_air_loop_name = var_hvac_air_loop_name
        # real
        var_minimum_setpoint_temperature = 0.0001
        obj.minimum_setpoint_temperature = var_minimum_setpoint_temperature
        # real
        var_maximum_setpoint_temperature = 0.0001
        obj.maximum_setpoint_temperature = var_maximum_setpoint_temperature
        # alpha
        var_strategy = "TemperatureFirst"
        obj.strategy = var_strategy
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name
        # real
        var_minimum_turndown_ratio = 0.0001
        obj.minimum_turndown_ratio = var_minimum_turndown_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagerwarmesttemperatureflows[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerwarmesttemperatureflows[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerwarmesttemperatureflows[0].hvac_air_loop_name, var_hvac_air_loop_name)
        self.assertAlmostEqual(idf2.setpointmanagerwarmesttemperatureflows[0].minimum_setpoint_temperature, var_minimum_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanagerwarmesttemperatureflows[0].maximum_setpoint_temperature, var_maximum_setpoint_temperature)
        self.assertEqual(idf2.setpointmanagerwarmesttemperatureflows[0].strategy, var_strategy)
        self.assertEqual(idf2.setpointmanagerwarmesttemperatureflows[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)
        self.assertAlmostEqual(idf2.setpointmanagerwarmesttemperatureflows[0].minimum_turndown_ratio, var_minimum_turndown_ratio)