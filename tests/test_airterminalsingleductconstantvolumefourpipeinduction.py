import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctConstantVolumeFourPipeInduction
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctConstantVolumeFourPipeInduction(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductconstantvolumefourpipeinduction(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctConstantVolumeFourPipeInduction()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_total_air_flow_rate = 0.0
        obj.maximum_total_air_flow_rate = var_maximum_total_air_flow_rate
        # real
        var_induction_ratio = 0.0
        obj.induction_ratio = var_induction_ratio
        # node
        var_supply_air_inlet_node_name = "node|Supply Air Inlet Node Name"
        obj.supply_air_inlet_node_name = var_supply_air_inlet_node_name
        # node
        var_induced_air_inlet_node_name = "node|Induced Air Inlet Node Name"
        obj.induced_air_inlet_node_name = var_induced_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_hot_water_inlet_node_name = "node|Hot Water Inlet Node Name"
        obj.hot_water_inlet_node_name = var_hot_water_inlet_node_name
        # node
        var_cold_water_inlet_node_name = "node|Cold Water Inlet Node Name"
        obj.cold_water_inlet_node_name = var_cold_water_inlet_node_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Water"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_maximum_hot_water_flow_rate = 12.12
        obj.maximum_hot_water_flow_rate = var_maximum_hot_water_flow_rate
        # real
        var_minimum_hot_water_flow_rate = 0.0
        obj.minimum_hot_water_flow_rate = var_minimum_hot_water_flow_rate
        # real
        var_heating_convergence_tolerance = 0.0001
        obj.heating_convergence_tolerance = var_heating_convergence_tolerance
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:Water"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # real
        var_maximum_cold_water_flow_rate = 17.17
        obj.maximum_cold_water_flow_rate = var_maximum_cold_water_flow_rate
        # real
        var_minimum_cold_water_flow_rate = 0.0
        obj.minimum_cold_water_flow_rate = var_minimum_cold_water_flow_rate
        # real
        var_cooling_convergence_tolerance = 0.0001
        obj.cooling_convergence_tolerance = var_cooling_convergence_tolerance
        # object-list
        var_zone_mixer_name = "object-list|Zone Mixer Name"
        obj.zone_mixer_name = var_zone_mixer_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].maximum_total_air_flow_rate, var_maximum_total_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].induction_ratio, var_induction_ratio)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].supply_air_inlet_node_name, var_supply_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].induced_air_inlet_node_name, var_induced_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].hot_water_inlet_node_name, var_hot_water_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].cold_water_inlet_node_name, var_cold_water_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].maximum_hot_water_flow_rate, var_maximum_hot_water_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].minimum_hot_water_flow_rate, var_minimum_hot_water_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].heating_convergence_tolerance, var_heating_convergence_tolerance)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].cooling_coil_name, var_cooling_coil_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].maximum_cold_water_flow_rate, var_maximum_cold_water_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].minimum_cold_water_flow_rate, var_minimum_cold_water_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].cooling_convergence_tolerance, var_cooling_convergence_tolerance)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipeinductions[0].zone_mixer_name, var_zone_mixer_name)