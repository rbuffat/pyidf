import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxMultiSpeed

log = logging.getLogger(__name__)

class TestCoilCoolingDxMultiSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxmultispeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxMultiSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name
        # alpha
        var_apply_part_load_fraction_to_speeds_greater_than_1 = "Yes"
        obj.apply_part_load_fraction_to_speeds_greater_than_1 = var_apply_part_load_fraction_to_speeds_greater_than_1
        # alpha
        var_apply_latent_degradation_to_speeds_greater_than_1 = "Yes"
        obj.apply_latent_degradation_to_speeds_greater_than_1 = var_apply_latent_degradation_to_speeds_greater_than_1
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_operating_schedule_name = "object-list|Basin Heater Operating Schedule Name"
        obj.basin_heater_operating_schedule_name = var_basin_heater_operating_schedule_name
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
        # integer
        var_number_of_speeds = 3
        obj.number_of_speeds = var_number_of_speeds
        # real
        var_speed_1_gross_rated_total_cooling_capacity = 0.0001
        obj.speed_1_gross_rated_total_cooling_capacity = var_speed_1_gross_rated_total_cooling_capacity
        # real
        var_speed_1_gross_rated_sensible_heat_ratio = 0.75
        obj.speed_1_gross_rated_sensible_heat_ratio = var_speed_1_gross_rated_sensible_heat_ratio
        # real
        var_speed_1_gross_rated_cooling_cop = 0.0001
        obj.speed_1_gross_rated_cooling_cop = var_speed_1_gross_rated_cooling_cop
        # real
        var_speed_1_rated_air_flow_rate = 0.0001
        obj.speed_1_rated_air_flow_rate = var_speed_1_rated_air_flow_rate
        # real
        var_rated_evaporator_fan_power_per_volume_flow_rate = 625.0
        obj.rated_evaporator_fan_power_per_volume_flow_rate = var_rated_evaporator_fan_power_per_volume_flow_rate
        # object-list
        var_speed_1_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_temperature_curve_name = var_speed_1_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Flow Fraction Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name = var_speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_1_energy_input_ratio_function_of_temperature_curve_name = var_speed_1_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.speed_1_energy_input_ratio_function_of_flow_fraction_curve_name = var_speed_1_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_speed_1_part_load_fraction_correlation_curve_name = "object-list|Speed 1 Part Load Fraction Correlation Curve Name"
        obj.speed_1_part_load_fraction_correlation_curve_name = var_speed_1_part_load_fraction_correlation_curve_name
        # real
        var_speed_1_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.speed_1_nominal_time_for_condensate_removal_to_begin = var_speed_1_nominal_time_for_condensate_removal_to_begin
        # real
        var_speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_speed_1_maximum_cycling_rate = 2.5
        obj.speed_1_maximum_cycling_rate = var_speed_1_maximum_cycling_rate
        # real
        var_speed_1_latent_capacity_time_constant = 250.0
        obj.speed_1_latent_capacity_time_constant = var_speed_1_latent_capacity_time_constant
        # real
        var_speed_1_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_1_rated_waste_heat_fraction_of_power_input = var_speed_1_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_1_waste_heat_function_of_temperature_curve_name = "object-list|Speed 1 Waste Heat Function of Temperature Curve Name"
        obj.speed_1_waste_heat_function_of_temperature_curve_name = var_speed_1_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_1_evaporative_condenser_effectiveness = 0.5
        obj.speed_1_evaporative_condenser_effectiveness = var_speed_1_evaporative_condenser_effectiveness
        # real
        var_speed_1_evaporative_condenser_air_flow_rate = 0.0001
        obj.speed_1_evaporative_condenser_air_flow_rate = var_speed_1_evaporative_condenser_air_flow_rate
        # real
        var_speed_1_rated_evaporative_condenser_pump_power_consumption = 0.0
        obj.speed_1_rated_evaporative_condenser_pump_power_consumption = var_speed_1_rated_evaporative_condenser_pump_power_consumption
        # real
        var_speed_2_gross_rated_total_cooling_capacity = 0.0001
        obj.speed_2_gross_rated_total_cooling_capacity = var_speed_2_gross_rated_total_cooling_capacity
        # real
        var_speed_2_gross_rated_sensible_heat_ratio = 0.75
        obj.speed_2_gross_rated_sensible_heat_ratio = var_speed_2_gross_rated_sensible_heat_ratio
        # real
        var_speed_2_gross_rated_cooling_cop = 0.0001
        obj.speed_2_gross_rated_cooling_cop = var_speed_2_gross_rated_cooling_cop
        # real
        var_speed_2_rated_air_flow_rate = 0.0001
        obj.speed_2_rated_air_flow_rate = var_speed_2_rated_air_flow_rate
        # real
        var_rated_evaporator_fan_power_per_volume_flow_rate_v3 = 625.0
        obj.rated_evaporator_fan_power_per_volume_flow_rate_v3 = var_rated_evaporator_fan_power_per_volume_flow_rate_v3
        # object-list
        var_speed_2_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_temperature_curve_name = var_speed_2_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Flow Fraction Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name = var_speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_2_energy_input_ratio_function_of_temperature_curve_name = var_speed_2_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.speed_2_energy_input_ratio_function_of_flow_fraction_curve_name = var_speed_2_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_speed_2_part_load_fraction_correlation_curve_name = "object-list|Speed 2 Part Load Fraction Correlation Curve Name"
        obj.speed_2_part_load_fraction_correlation_curve_name = var_speed_2_part_load_fraction_correlation_curve_name
        # real
        var_speed_2_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.speed_2_nominal_time_for_condensate_removal_to_begin = var_speed_2_nominal_time_for_condensate_removal_to_begin
        # real
        var_speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_speed_2_maximum_cycling_rate = 2.5
        obj.speed_2_maximum_cycling_rate = var_speed_2_maximum_cycling_rate
        # real
        var_speed_2_latent_capacity_time_constant = 250.0
        obj.speed_2_latent_capacity_time_constant = var_speed_2_latent_capacity_time_constant
        # real
        var_speed_2_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_2_rated_waste_heat_fraction_of_power_input = var_speed_2_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_2_waste_heat_function_of_temperature_curve_name = "object-list|Speed 2 Waste Heat Function of Temperature Curve Name"
        obj.speed_2_waste_heat_function_of_temperature_curve_name = var_speed_2_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_2_evaporative_condenser_effectiveness = 0.5
        obj.speed_2_evaporative_condenser_effectiveness = var_speed_2_evaporative_condenser_effectiveness
        # real
        var_speed_2_evaporative_condenser_air_flow_rate = 0.0001
        obj.speed_2_evaporative_condenser_air_flow_rate = var_speed_2_evaporative_condenser_air_flow_rate
        # real
        var_speed_2_rated_evaporative_condenser_pump_power_consumption = 0.0
        obj.speed_2_rated_evaporative_condenser_pump_power_consumption = var_speed_2_rated_evaporative_condenser_pump_power_consumption
        # real
        var_speed_3_gross_rated_total_cooling_capacity = 0.0001
        obj.speed_3_gross_rated_total_cooling_capacity = var_speed_3_gross_rated_total_cooling_capacity
        # real
        var_speed_3_gross_rated_sensible_heat_ratio = 0.75
        obj.speed_3_gross_rated_sensible_heat_ratio = var_speed_3_gross_rated_sensible_heat_ratio
        # real
        var_speed_3_gross_rated_cooling_cop = 0.0001
        obj.speed_3_gross_rated_cooling_cop = var_speed_3_gross_rated_cooling_cop
        # real
        var_speed_3_rated_air_flow_rate = 0.0001
        obj.speed_3_rated_air_flow_rate = var_speed_3_rated_air_flow_rate
        # real
        var_rated_evaporator_fan_power_per_volume_flow_rate_v4 = 625.0
        obj.rated_evaporator_fan_power_per_volume_flow_rate_v4 = var_rated_evaporator_fan_power_per_volume_flow_rate_v4
        # object-list
        var_speed_3_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_temperature_curve_name = var_speed_3_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Flow Fraction Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name = var_speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_3_energy_input_ratio_function_of_temperature_curve_name = var_speed_3_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.speed_3_energy_input_ratio_function_of_flow_fraction_curve_name = var_speed_3_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_speed_3_part_load_fraction_correlation_curve_name = "object-list|Speed 3 Part Load Fraction Correlation Curve Name"
        obj.speed_3_part_load_fraction_correlation_curve_name = var_speed_3_part_load_fraction_correlation_curve_name
        # real
        var_speed_3_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.speed_3_nominal_time_for_condensate_removal_to_begin = var_speed_3_nominal_time_for_condensate_removal_to_begin
        # real
        var_speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_speed_3_maximum_cycling_rate = 2.5
        obj.speed_3_maximum_cycling_rate = var_speed_3_maximum_cycling_rate
        # real
        var_speed_3_latent_capacity_time_constant = 250.0
        obj.speed_3_latent_capacity_time_constant = var_speed_3_latent_capacity_time_constant
        # real
        var_speed_3_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_3_rated_waste_heat_fraction_of_power_input = var_speed_3_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_3_waste_heat_function_of_temperature_curve_name = "object-list|Speed 3 Waste Heat Function of Temperature Curve Name"
        obj.speed_3_waste_heat_function_of_temperature_curve_name = var_speed_3_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_3_evaporative_condenser_effectiveness = 0.5
        obj.speed_3_evaporative_condenser_effectiveness = var_speed_3_evaporative_condenser_effectiveness
        # real
        var_speed_3_evaporative_condenser_air_flow_rate = 0.0001
        obj.speed_3_evaporative_condenser_air_flow_rate = var_speed_3_evaporative_condenser_air_flow_rate
        # real
        var_speed_3_rated_evaporative_condenser_pump_power_consumption = 0.0
        obj.speed_3_rated_evaporative_condenser_pump_power_consumption = var_speed_3_rated_evaporative_condenser_pump_power_consumption
        # real
        var_speed_4_gross_rated_total_cooling_capacity = 0.0001
        obj.speed_4_gross_rated_total_cooling_capacity = var_speed_4_gross_rated_total_cooling_capacity
        # real
        var_speed_4_gross_rated_sensible_heat_ratio = 0.75
        obj.speed_4_gross_rated_sensible_heat_ratio = var_speed_4_gross_rated_sensible_heat_ratio
        # real
        var_speed_4_gross_rated_cooling_cop = 0.0001
        obj.speed_4_gross_rated_cooling_cop = var_speed_4_gross_rated_cooling_cop
        # real
        var_speed_4_rated_air_flow_rate = 0.0001
        obj.speed_4_rated_air_flow_rate = var_speed_4_rated_air_flow_rate
        # real
        var_rated_evaporator_fan_power_per_volume_flow_rate_v5 = 625.0
        obj.rated_evaporator_fan_power_per_volume_flow_rate_v5 = var_rated_evaporator_fan_power_per_volume_flow_rate_v5
        # object-list
        var_speed_4_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_temperature_curve_name = var_speed_4_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Flow Fraction Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name = var_speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_4_energy_input_ratio_function_of_temperature_curve_name = var_speed_4_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.speed_4_energy_input_ratio_function_of_flow_fraction_curve_name = var_speed_4_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_speed_4_part_load_fraction_correlation_curve_name = "object-list|Speed 4 Part Load Fraction Correlation Curve Name"
        obj.speed_4_part_load_fraction_correlation_curve_name = var_speed_4_part_load_fraction_correlation_curve_name
        # real
        var_speed_4_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.speed_4_nominal_time_for_condensate_removal_to_begin = var_speed_4_nominal_time_for_condensate_removal_to_begin
        # real
        var_speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_speed_4_maximum_cycling_rate = 2.5
        obj.speed_4_maximum_cycling_rate = var_speed_4_maximum_cycling_rate
        # real
        var_speed_4_latent_capacity_time_constant = 250.0
        obj.speed_4_latent_capacity_time_constant = var_speed_4_latent_capacity_time_constant
        # real
        var_speed_4_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_4_rated_waste_heat_fraction_of_power_input = var_speed_4_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_4_waste_heat_function_of_temperature_curve_name = "object-list|Speed 4 Waste Heat Function of Temperature Curve Name"
        obj.speed_4_waste_heat_function_of_temperature_curve_name = var_speed_4_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_4_evaporative_condenser_effectiveness = 0.5
        obj.speed_4_evaporative_condenser_effectiveness = var_speed_4_evaporative_condenser_effectiveness
        # real
        var_speed_4_evaporative_condenser_air_flow_rate = 0.0001
        obj.speed_4_evaporative_condenser_air_flow_rate = var_speed_4_evaporative_condenser_air_flow_rate
        # real
        var_speed_4_rated_evaporative_condenser_pump_power_consumption = 0.0
        obj.speed_4_rated_evaporative_condenser_pump_power_consumption = var_speed_4_rated_evaporative_condenser_pump_power_consumption

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].apply_part_load_fraction_to_speeds_greater_than_1, var_apply_part_load_fraction_to_speeds_greater_than_1)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].apply_latent_degradation_to_speeds_greater_than_1, var_apply_latent_degradation_to_speeds_greater_than_1)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].fuel_type, var_fuel_type)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].number_of_speeds, var_number_of_speeds)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_gross_rated_total_cooling_capacity, var_speed_1_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_gross_rated_sensible_heat_ratio, var_speed_1_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_gross_rated_cooling_cop, var_speed_1_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_rated_air_flow_rate, var_speed_1_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].rated_evaporator_fan_power_per_volume_flow_rate, var_rated_evaporator_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_total_cooling_capacity_function_of_temperature_curve_name, var_speed_1_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name, var_speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_energy_input_ratio_function_of_temperature_curve_name, var_speed_1_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_part_load_fraction_correlation_curve_name, var_speed_1_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_nominal_time_for_condensate_removal_to_begin, var_speed_1_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_maximum_cycling_rate, var_speed_1_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_latent_capacity_time_constant, var_speed_1_latent_capacity_time_constant)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_rated_waste_heat_fraction_of_power_input, var_speed_1_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_waste_heat_function_of_temperature_curve_name, var_speed_1_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_evaporative_condenser_effectiveness, var_speed_1_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_evaporative_condenser_air_flow_rate, var_speed_1_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_1_rated_evaporative_condenser_pump_power_consumption, var_speed_1_rated_evaporative_condenser_pump_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_gross_rated_total_cooling_capacity, var_speed_2_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_gross_rated_sensible_heat_ratio, var_speed_2_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_gross_rated_cooling_cop, var_speed_2_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_rated_air_flow_rate, var_speed_2_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].rated_evaporator_fan_power_per_volume_flow_rate_v3, var_rated_evaporator_fan_power_per_volume_flow_rate_v3)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_total_cooling_capacity_function_of_temperature_curve_name, var_speed_2_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name, var_speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_energy_input_ratio_function_of_temperature_curve_name, var_speed_2_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_part_load_fraction_correlation_curve_name, var_speed_2_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_nominal_time_for_condensate_removal_to_begin, var_speed_2_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_maximum_cycling_rate, var_speed_2_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_latent_capacity_time_constant, var_speed_2_latent_capacity_time_constant)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_rated_waste_heat_fraction_of_power_input, var_speed_2_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_waste_heat_function_of_temperature_curve_name, var_speed_2_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_evaporative_condenser_effectiveness, var_speed_2_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_evaporative_condenser_air_flow_rate, var_speed_2_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_2_rated_evaporative_condenser_pump_power_consumption, var_speed_2_rated_evaporative_condenser_pump_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_gross_rated_total_cooling_capacity, var_speed_3_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_gross_rated_sensible_heat_ratio, var_speed_3_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_gross_rated_cooling_cop, var_speed_3_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_rated_air_flow_rate, var_speed_3_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].rated_evaporator_fan_power_per_volume_flow_rate_v4, var_rated_evaporator_fan_power_per_volume_flow_rate_v4)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_total_cooling_capacity_function_of_temperature_curve_name, var_speed_3_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name, var_speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_energy_input_ratio_function_of_temperature_curve_name, var_speed_3_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_part_load_fraction_correlation_curve_name, var_speed_3_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_nominal_time_for_condensate_removal_to_begin, var_speed_3_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_maximum_cycling_rate, var_speed_3_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_latent_capacity_time_constant, var_speed_3_latent_capacity_time_constant)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_rated_waste_heat_fraction_of_power_input, var_speed_3_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_waste_heat_function_of_temperature_curve_name, var_speed_3_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_evaporative_condenser_effectiveness, var_speed_3_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_evaporative_condenser_air_flow_rate, var_speed_3_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_3_rated_evaporative_condenser_pump_power_consumption, var_speed_3_rated_evaporative_condenser_pump_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_gross_rated_total_cooling_capacity, var_speed_4_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_gross_rated_sensible_heat_ratio, var_speed_4_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_gross_rated_cooling_cop, var_speed_4_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_rated_air_flow_rate, var_speed_4_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].rated_evaporator_fan_power_per_volume_flow_rate_v5, var_rated_evaporator_fan_power_per_volume_flow_rate_v5)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_total_cooling_capacity_function_of_temperature_curve_name, var_speed_4_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name, var_speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_energy_input_ratio_function_of_temperature_curve_name, var_speed_4_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_part_load_fraction_correlation_curve_name, var_speed_4_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_nominal_time_for_condensate_removal_to_begin, var_speed_4_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_maximum_cycling_rate, var_speed_4_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_latent_capacity_time_constant, var_speed_4_latent_capacity_time_constant)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_rated_waste_heat_fraction_of_power_input, var_speed_4_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_waste_heat_function_of_temperature_curve_name, var_speed_4_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_evaporative_condenser_effectiveness, var_speed_4_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_evaporative_condenser_air_flow_rate, var_speed_4_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxmultispeeds[0].speed_4_rated_evaporative_condenser_pump_power_consumption, var_speed_4_rated_evaporative_condenser_pump_power_consumption)