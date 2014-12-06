import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilHeatingSteam
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilHeatingSteam(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingsteam(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingSteam()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_steam_flow_rate = 0.0001
        obj.maximum_steam_flow_rate = var_maximum_steam_flow_rate
        # real
        var_degree_of_subcooling = 3.0
        obj.degree_of_subcooling = var_degree_of_subcooling
        # real
        var_degree_of_loop_subcooling = 10.0
        obj.degree_of_loop_subcooling = var_degree_of_loop_subcooling
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_coil_control_type = "TemperatureSetpointControl"
        obj.coil_control_type = var_coil_control_type
        # node
        var_temperature_setpoint_node_name = "node|Temperature Setpoint Node Name"
        obj.temperature_setpoint_node_name = var_temperature_setpoint_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingsteams[0].name, var_name)
        self.assertEqual(idf2.coilheatingsteams[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilheatingsteams[0].maximum_steam_flow_rate, var_maximum_steam_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingsteams[0].degree_of_subcooling, var_degree_of_subcooling)
        self.assertAlmostEqual(idf2.coilheatingsteams[0].degree_of_loop_subcooling, var_degree_of_loop_subcooling)
        self.assertEqual(idf2.coilheatingsteams[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilheatingsteams[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilheatingsteams[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingsteams[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingsteams[0].coil_control_type, var_coil_control_type)
        self.assertEqual(idf2.coilheatingsteams[0].temperature_setpoint_node_name, var_temperature_setpoint_node_name)