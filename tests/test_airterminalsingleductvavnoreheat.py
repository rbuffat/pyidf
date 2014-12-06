import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctVavNoReheat
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctVavNoReheat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductvavnoreheat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctVavNoReheat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
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
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavnoreheats[0].maximum_air_flow_rate, var_maximum_air_flow_rate)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].zone_minimum_air_flow_input_method, var_zone_minimum_air_flow_input_method)
        self.assertAlmostEqual(idf2.airterminalsingleductvavnoreheats[0].constant_minimum_air_flow_fraction, var_constant_minimum_air_flow_fraction)
        self.assertAlmostEqual(idf2.airterminalsingleductvavnoreheats[0].fixed_minimum_air_flow_rate, var_fixed_minimum_air_flow_rate)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].minimum_air_flow_fraction_schedule_name, var_minimum_air_flow_fraction_schedule_name)
        self.assertEqual(idf2.airterminalsingleductvavnoreheats[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)