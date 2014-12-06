import os
import tempfile
import unittest
import pyidf
from pyidf.condenser_equipment_and_heat_exchangers import FluidCoolerTwoSpeed
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFluidCoolerTwoSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidcoolertwospeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidCoolerTwoSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # alpha
        var_performance_input_method = "UFactorTimesAreaAndDesignWaterFlowRate"
        obj.performance_input_method = var_performance_input_method
        # real
        var_high_fan_speed_ufactor_times_area_value = 1050000.00005
        obj.high_fan_speed_ufactor_times_area_value = var_high_fan_speed_ufactor_times_area_value
        # real
        var_low_fan_speed_ufactor_times_area_value = 150000.00005
        obj.low_fan_speed_ufactor_times_area_value = var_low_fan_speed_ufactor_times_area_value
        # real
        var_low_fan_speed_ufactor_times_area_sizing_factor = 7.7
        obj.low_fan_speed_ufactor_times_area_sizing_factor = var_low_fan_speed_ufactor_times_area_sizing_factor
        # real
        var_high_speed_nominal_capacity = 0.0001
        obj.high_speed_nominal_capacity = var_high_speed_nominal_capacity
        # real
        var_low_speed_nominal_capacity = 0.0001
        obj.low_speed_nominal_capacity = var_low_speed_nominal_capacity
        # real
        var_low_speed_nominal_capacity_sizing_factor = 10.1
        obj.low_speed_nominal_capacity_sizing_factor = var_low_speed_nominal_capacity_sizing_factor
        # real
        var_design_entering_water_temperature = 0.0001
        obj.design_entering_water_temperature = var_design_entering_water_temperature
        # real
        var_design_entering_air_temperature = 0.0001
        obj.design_entering_air_temperature = var_design_entering_air_temperature
        # real
        var_design_entering_air_wetbulb_temperature = 0.0001
        obj.design_entering_air_wetbulb_temperature = var_design_entering_air_wetbulb_temperature
        # real
        var_design_water_flow_rate = 0.0001
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_high_fan_speed_air_flow_rate = 0.0001
        obj.high_fan_speed_air_flow_rate = var_high_fan_speed_air_flow_rate
        # real
        var_high_fan_speed_fan_power = 0.0001
        obj.high_fan_speed_fan_power = var_high_fan_speed_fan_power
        # real
        var_low_fan_speed_air_flow_rate = 0.0001
        obj.low_fan_speed_air_flow_rate = var_low_fan_speed_air_flow_rate
        # real
        var_low_fan_speed_air_flow_rate_sizing_factor = 18.18
        obj.low_fan_speed_air_flow_rate_sizing_factor = var_low_fan_speed_air_flow_rate_sizing_factor
        # real
        var_low_fan_speed_fan_power = 0.0001
        obj.low_fan_speed_fan_power = var_low_fan_speed_fan_power
        # real
        var_low_fan_speed_fan_power_sizing_factor = 20.2
        obj.low_fan_speed_fan_power_sizing_factor = var_low_fan_speed_fan_power_sizing_factor
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidcoolertwospeeds[0].name, var_name)
        self.assertEqual(idf2.fluidcoolertwospeeds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.fluidcoolertwospeeds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.fluidcoolertwospeeds[0].performance_input_method, var_performance_input_method)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].high_fan_speed_ufactor_times_area_value, var_high_fan_speed_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_ufactor_times_area_value, var_low_fan_speed_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_ufactor_times_area_sizing_factor, var_low_fan_speed_ufactor_times_area_sizing_factor)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].high_speed_nominal_capacity, var_high_speed_nominal_capacity)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_speed_nominal_capacity, var_low_speed_nominal_capacity)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_speed_nominal_capacity_sizing_factor, var_low_speed_nominal_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].design_entering_water_temperature, var_design_entering_water_temperature)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].design_entering_air_temperature, var_design_entering_air_temperature)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].design_entering_air_wetbulb_temperature, var_design_entering_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].high_fan_speed_air_flow_rate, var_high_fan_speed_air_flow_rate)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].high_fan_speed_fan_power, var_high_fan_speed_fan_power)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_air_flow_rate, var_low_fan_speed_air_flow_rate)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_air_flow_rate_sizing_factor, var_low_fan_speed_air_flow_rate_sizing_factor)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_fan_power, var_low_fan_speed_fan_power)
        self.assertAlmostEqual(idf2.fluidcoolertwospeeds[0].low_fan_speed_fan_power_sizing_factor, var_low_fan_speed_fan_power_sizing_factor)
        self.assertEqual(idf2.fluidcoolertwospeeds[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)