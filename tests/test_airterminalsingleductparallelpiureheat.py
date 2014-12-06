import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctParallelPiuReheat

log = logging.getLogger(__name__)

class TestAirTerminalSingleDuctParallelPiuReheat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductparallelpiureheat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctParallelPiuReheat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_primary_air_flow_rate = 0.0
        obj.maximum_primary_air_flow_rate = var_maximum_primary_air_flow_rate
        # real
        var_maximum_secondary_air_flow_rate = 0.0
        obj.maximum_secondary_air_flow_rate = var_maximum_secondary_air_flow_rate
        # real
        var_minimum_primary_air_flow_fraction = 0.5
        obj.minimum_primary_air_flow_fraction = var_minimum_primary_air_flow_fraction
        # real
        var_fan_on_flow_fraction = 0.5
        obj.fan_on_flow_fraction = var_fan_on_flow_fraction
        # node
        var_supply_air_inlet_node_name = "node|Supply Air Inlet Node Name"
        obj.supply_air_inlet_node_name = var_supply_air_inlet_node_name
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # node
        var_reheat_coil_air_inlet_node_name = "node|Reheat Coil Air Inlet Node Name"
        obj.reheat_coil_air_inlet_node_name = var_reheat_coil_air_inlet_node_name
        # object-list
        var_zone_mixer_name = "object-list|Zone Mixer Name"
        obj.zone_mixer_name = var_zone_mixer_name
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # alpha
        var_reheat_coil_object_type = "Coil:Heating:Water"
        obj.reheat_coil_object_type = var_reheat_coil_object_type
        # object-list
        var_reheat_coil_name = "object-list|Reheat Coil Name"
        obj.reheat_coil_name = var_reheat_coil_name
        # real
        var_maximum_hot_water_or_steam_flow_rate = 15.15
        obj.maximum_hot_water_or_steam_flow_rate = var_maximum_hot_water_or_steam_flow_rate
        # real
        var_minimum_hot_water_or_steam_flow_rate = 0.0
        obj.minimum_hot_water_or_steam_flow_rate = var_minimum_hot_water_or_steam_flow_rate
        # node
        var_hot_water_or_steam_inlet_node_name = "node|Hot Water or Steam Inlet Node Name"
        obj.hot_water_or_steam_inlet_node_name = var_hot_water_or_steam_inlet_node_name
        # real
        var_convergence_tolerance = 0.0001
        obj.convergence_tolerance = var_convergence_tolerance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].maximum_primary_air_flow_rate, var_maximum_primary_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].maximum_secondary_air_flow_rate, var_maximum_secondary_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].minimum_primary_air_flow_fraction, var_minimum_primary_air_flow_fraction)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].fan_on_flow_fraction, var_fan_on_flow_fraction)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].supply_air_inlet_node_name, var_supply_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].reheat_coil_air_inlet_node_name, var_reheat_coil_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].zone_mixer_name, var_zone_mixer_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].fan_name, var_fan_name)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].reheat_coil_object_type, var_reheat_coil_object_type)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].reheat_coil_name, var_reheat_coil_name)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].maximum_hot_water_or_steam_flow_rate, var_maximum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].minimum_hot_water_or_steam_flow_rate, var_minimum_hot_water_or_steam_flow_rate)
        self.assertEqual(idf2.airterminalsingleductparallelpiureheats[0].hot_water_or_steam_inlet_node_name, var_hot_water_or_steam_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductparallelpiureheats[0].convergence_tolerance, var_convergence_tolerance)