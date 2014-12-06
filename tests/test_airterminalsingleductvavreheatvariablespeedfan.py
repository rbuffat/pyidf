import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctVavReheatVariableSpeedFan

log = logging.getLogger(__name__)

class TestAirTerminalSingleDuctVavReheatVariableSpeedFan(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductvavreheatvariablespeedfan(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctVavReheatVariableSpeedFan()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_cooling_air_flow_rate = 0.0
        obj.maximum_cooling_air_flow_rate = var_maximum_cooling_air_flow_rate
        # real
        var_maximum_heating_air_flow_rate = 0.0
        obj.maximum_heating_air_flow_rate = var_maximum_heating_air_flow_rate
        # real
        var_zone_minimum_air_flow_fraction = 0.5
        obj.zone_minimum_air_flow_fraction = var_zone_minimum_air_flow_fraction
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_heating_coil_air_inlet_node_name = "node|Heating Coil Air Inlet Node Name"
        obj.heating_coil_air_inlet_node_name = var_heating_coil_air_inlet_node_name
        # node
        var_hot_water_or_steam_inlet_node_name = "node|Hot Water or Steam Inlet Node Name"
        obj.hot_water_or_steam_inlet_node_name = var_hot_water_or_steam_inlet_node_name
        # alpha
        var_fan_object_type = "Fan:VariableVolume"
        obj.fan_object_type = var_fan_object_type
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Water"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_maximum_hot_water_or_steam_flow_rate = 14.14
        obj.maximum_hot_water_or_steam_flow_rate = var_maximum_hot_water_or_steam_flow_rate
        # real
        var_minimum_hot_water_or_steam_flow_rate = 0.0
        obj.minimum_hot_water_or_steam_flow_rate = var_minimum_hot_water_or_steam_flow_rate
        # real
        var_heating_convergence_tolerance = 0.0001
        obj.heating_convergence_tolerance = var_heating_convergence_tolerance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].maximum_cooling_air_flow_rate, var_maximum_cooling_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].maximum_heating_air_flow_rate, var_maximum_heating_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].zone_minimum_air_flow_fraction, var_zone_minimum_air_flow_fraction)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].heating_coil_air_inlet_node_name, var_heating_coil_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].hot_water_or_steam_inlet_node_name, var_hot_water_or_steam_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].fan_object_type, var_fan_object_type)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].fan_name, var_fan_name)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].maximum_hot_water_or_steam_flow_rate, var_maximum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].minimum_hot_water_or_steam_flow_rate, var_minimum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheatvariablespeedfans[0].heating_convergence_tolerance, var_heating_convergence_tolerance)