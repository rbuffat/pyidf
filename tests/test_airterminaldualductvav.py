import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalDualDuctVav
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalDualDuctVav(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminaldualductvav(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalDualDuctVav()
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
        var_hot_air_inlet_node_name = "node|Hot Air Inlet Node Name"
        obj.hot_air_inlet_node_name = var_hot_air_inlet_node_name
        # node
        var_cold_air_inlet_node_name = "node|Cold Air Inlet Node Name"
        obj.cold_air_inlet_node_name = var_cold_air_inlet_node_name
        # real
        var_maximum_damper_air_flow_rate = 0.0
        obj.maximum_damper_air_flow_rate = var_maximum_damper_air_flow_rate
        # real
        var_zone_minimum_air_flow_fraction = 0.5
        obj.zone_minimum_air_flow_fraction = var_zone_minimum_air_flow_fraction
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
        self.assertEqual(idf2.airterminaldualductvavs[0].name, var_name)
        self.assertEqual(idf2.airterminaldualductvavs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminaldualductvavs[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminaldualductvavs[0].hot_air_inlet_node_name, var_hot_air_inlet_node_name)
        self.assertEqual(idf2.airterminaldualductvavs[0].cold_air_inlet_node_name, var_cold_air_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminaldualductvavs[0].maximum_damper_air_flow_rate, var_maximum_damper_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminaldualductvavs[0].zone_minimum_air_flow_fraction, var_zone_minimum_air_flow_fraction)
        self.assertEqual(idf2.airterminaldualductvavs[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)