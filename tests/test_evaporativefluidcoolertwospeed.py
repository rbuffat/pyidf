import os
import tempfile
import unittest
import pyidf
from pyidf.condenser_equipment_and_heat_exchangers import EvaporativeFluidCoolerTwoSpeed
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEvaporativeFluidCoolerTwoSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativefluidcoolertwospeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeFluidCoolerTwoSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
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
        var_low_fan_speed_air_flow_rate_sizing_factor = 7.7
        obj.low_fan_speed_air_flow_rate_sizing_factor = var_low_fan_speed_air_flow_rate_sizing_factor
        # real
        var_low_fan_speed_fan_power = 0.0001
        obj.low_fan_speed_fan_power = var_low_fan_speed_fan_power
        # real
        var_low_fan_speed_fan_power_sizing_factor = 9.9
        obj.low_fan_speed_fan_power_sizing_factor = var_low_fan_speed_fan_power_sizing_factor
        # real
        var_design_spray_water_flow_rate = 0.0001
        obj.design_spray_water_flow_rate = var_design_spray_water_flow_rate
        # alpha
        var_performance_input_method = "UFactorTimesAreaAndDesignWaterFlowRate"
        obj.performance_input_method = var_performance_input_method
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name
        # real
        var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio = 13.13
        obj.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio
        # real
        var_high_speed_standard_design_capacity = 0.0001
        obj.high_speed_standard_design_capacity = var_high_speed_standard_design_capacity
        # real
        var_low_speed_standard_design_capacity = 0.0001
        obj.low_speed_standard_design_capacity = var_low_speed_standard_design_capacity
        # real
        var_low_speed_standard_capacity_sizing_factor = 16.16
        obj.low_speed_standard_capacity_sizing_factor = var_low_speed_standard_capacity_sizing_factor
        # real
        var_high_fan_speed_ufactor_times_area_value = 1050000.00005
        obj.high_fan_speed_ufactor_times_area_value = var_high_fan_speed_ufactor_times_area_value
        # real
        var_low_fan_speed_ufactor_times_area_value = 150000.00005
        obj.low_fan_speed_ufactor_times_area_value = var_low_fan_speed_ufactor_times_area_value
        # real
        var_low_fan_speed_ufactor_times_area_sizing_factor = 19.19
        obj.low_fan_speed_ufactor_times_area_sizing_factor = var_low_fan_speed_ufactor_times_area_sizing_factor
        # real
        var_design_water_flow_rate = 0.0001
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_high_speed_user_specified_design_capacity = 0.0001
        obj.high_speed_user_specified_design_capacity = var_high_speed_user_specified_design_capacity
        # real
        var_low_speed_user_specified_design_capacity = 0.0001
        obj.low_speed_user_specified_design_capacity = var_low_speed_user_specified_design_capacity
        # real
        var_low_speed_user_specified_design_capacity_sizing_factor = 23.23
        obj.low_speed_user_specified_design_capacity_sizing_factor = var_low_speed_user_specified_design_capacity_sizing_factor
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
        var_high_speed_sizing_factor = 0.0001
        obj.high_speed_sizing_factor = var_high_speed_sizing_factor
        # alpha
        var_evaporation_loss_mode = "LossFactor"
        obj.evaporation_loss_mode = var_evaporation_loss_mode
        # real
        var_evaporation_loss_factor = 29.29
        obj.evaporation_loss_factor = var_evaporation_loss_factor
        # real
        var_drift_loss_percent = 30.3
        obj.drift_loss_percent = var_drift_loss_percent
        # alpha
        var_blowdown_calculation_mode = "ConcentrationRatio"
        obj.blowdown_calculation_mode = var_blowdown_calculation_mode
        # real
        var_blowdown_concentration_ratio = 2.0
        obj.blowdown_concentration_ratio = var_blowdown_concentration_ratio
        # object-list
        var_blowdown_makeup_water_usage_schedule_name = "object-list|Blowdown Makeup Water Usage Schedule Name"
        obj.blowdown_makeup_water_usage_schedule_name = var_blowdown_makeup_water_usage_schedule_name
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].name, var_name)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_fan_speed_air_flow_rate, var_high_fan_speed_air_flow_rate)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_fan_speed_fan_power, var_high_fan_speed_fan_power)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_air_flow_rate, var_low_fan_speed_air_flow_rate)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_air_flow_rate_sizing_factor, var_low_fan_speed_air_flow_rate_sizing_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_fan_power, var_low_fan_speed_fan_power)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_fan_power_sizing_factor, var_low_fan_speed_fan_power_sizing_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].design_spray_water_flow_rate, var_design_spray_water_flow_rate)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].performance_input_method, var_performance_input_method)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].heat_rejection_capacity_and_nominal_capacity_sizing_ratio, var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_speed_standard_design_capacity, var_high_speed_standard_design_capacity)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_speed_standard_design_capacity, var_low_speed_standard_design_capacity)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_speed_standard_capacity_sizing_factor, var_low_speed_standard_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_fan_speed_ufactor_times_area_value, var_high_fan_speed_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_ufactor_times_area_value, var_low_fan_speed_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_fan_speed_ufactor_times_area_sizing_factor, var_low_fan_speed_ufactor_times_area_sizing_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_speed_user_specified_design_capacity, var_high_speed_user_specified_design_capacity)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_speed_user_specified_design_capacity, var_low_speed_user_specified_design_capacity)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].low_speed_user_specified_design_capacity_sizing_factor, var_low_speed_user_specified_design_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].design_entering_water_temperature, var_design_entering_water_temperature)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].design_entering_air_temperature, var_design_entering_air_temperature)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].design_entering_air_wetbulb_temperature, var_design_entering_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].high_speed_sizing_factor, var_high_speed_sizing_factor)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].evaporation_loss_mode, var_evaporation_loss_mode)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].evaporation_loss_factor, var_evaporation_loss_factor)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].drift_loss_percent, var_drift_loss_percent)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].blowdown_calculation_mode, var_blowdown_calculation_mode)
        self.assertAlmostEqual(idf2.evaporativefluidcoolertwospeeds[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].blowdown_makeup_water_usage_schedule_name, var_blowdown_makeup_water_usage_schedule_name)
        self.assertEqual(idf2.evaporativefluidcoolertwospeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)