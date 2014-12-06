import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctVavReheat
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctVavReheat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductvavreheat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctVavReheat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_damper_air_outlet_node_name = "node|Damper Air Outlet Node Name"
        obj.damper_air_outlet_node_name = var_damper_air_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # real
        var_maximum_air_flow_rate = 0.0
        obj.maximum_air_flow_rate = var_maximum_air_flow_rate
        # alpha
        var_zone_minimum_air_flow_input_method = "Constant"
        obj.zone_minimum_air_flow_input_method = var_zone_minimum_air_flow_input_method
        # real
        var_constant_minimum_air_flow_fraction = 7.7
        obj.constant_minimum_air_flow_fraction = var_constant_minimum_air_flow_fraction
        # real
        var_fixed_minimum_air_flow_rate = 8.8
        obj.fixed_minimum_air_flow_rate = var_fixed_minimum_air_flow_rate
        # object-list
        var_minimum_air_flow_fraction_schedule_name = "object-list|Minimum Air Flow Fraction Schedule Name"
        obj.minimum_air_flow_fraction_schedule_name = var_minimum_air_flow_fraction_schedule_name
        # alpha
        var_reheat_coil_object_type = "Coil:Heating:Water"
        obj.reheat_coil_object_type = var_reheat_coil_object_type
        # object-list
        var_reheat_coil_name = "object-list|Reheat Coil Name"
        obj.reheat_coil_name = var_reheat_coil_name
        # real
        var_maximum_hot_water_or_steam_flow_rate = 0.0
        obj.maximum_hot_water_or_steam_flow_rate = var_maximum_hot_water_or_steam_flow_rate
        # real
        var_minimum_hot_water_or_steam_flow_rate = 0.0
        obj.minimum_hot_water_or_steam_flow_rate = var_minimum_hot_water_or_steam_flow_rate
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # real
        var_convergence_tolerance = 0.0001
        obj.convergence_tolerance = var_convergence_tolerance
        # alpha
        var_damper_heating_action = "Normal"
        obj.damper_heating_action = var_damper_heating_action
        # real
        var_maximum_flow_per_zone_floor_area_during_reheat = 17.17
        obj.maximum_flow_per_zone_floor_area_during_reheat = var_maximum_flow_per_zone_floor_area_during_reheat
        # real
        var_maximum_flow_fraction_during_reheat = 18.18
        obj.maximum_flow_fraction_during_reheat = var_maximum_flow_fraction_during_reheat
        # real
        var_maximum_reheat_air_temperature = 0.0001
        obj.maximum_reheat_air_temperature = var_maximum_reheat_air_temperature
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].damper_air_outlet_node_name, var_damper_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].maximum_air_flow_rate, var_maximum_air_flow_rate)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].zone_minimum_air_flow_input_method, var_zone_minimum_air_flow_input_method)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].constant_minimum_air_flow_fraction, var_constant_minimum_air_flow_fraction)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].fixed_minimum_air_flow_rate, var_fixed_minimum_air_flow_rate)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].minimum_air_flow_fraction_schedule_name, var_minimum_air_flow_fraction_schedule_name)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].reheat_coil_object_type, var_reheat_coil_object_type)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].reheat_coil_name, var_reheat_coil_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].maximum_hot_water_or_steam_flow_rate, var_maximum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].minimum_hot_water_or_steam_flow_rate, var_minimum_hot_water_or_steam_flow_rate)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].convergence_tolerance, var_convergence_tolerance)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].damper_heating_action, var_damper_heating_action)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].maximum_flow_per_zone_floor_area_during_reheat, var_maximum_flow_per_zone_floor_area_during_reheat)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].maximum_flow_fraction_during_reheat, var_maximum_flow_fraction_during_reheat)
        self.assertAlmostEqual(idf2.airterminalsingleductvavreheats[0].maximum_reheat_air_temperature, var_maximum_reheat_air_temperature)
        self.assertEqual(idf2.airterminalsingleductvavreheats[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)