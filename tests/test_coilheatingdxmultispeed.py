import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingDxMultiSpeed

log = logging.getLogger(__name__)

class TestCoilHeatingDxMultiSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdxmultispeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDxMultiSpeed()
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
        # real
        var_minimum_outdoor_drybulb_temperature_for_compressor_operation = 5.5
        obj.minimum_outdoor_drybulb_temperature_for_compressor_operation = var_minimum_outdoor_drybulb_temperature_for_compressor_operation
        # real
        var_outdoor_drybulb_temperature_to_turn_on_compressor = 6.6
        obj.outdoor_drybulb_temperature_to_turn_on_compressor = var_outdoor_drybulb_temperature_to_turn_on_compressor
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation
        # object-list
        var_defrost_energy_input_ratio_function_of_temperature_curve_name = "object-list|Defrost Energy Input Ratio Function of Temperature Curve Name"
        obj.defrost_energy_input_ratio_function_of_temperature_curve_name = var_defrost_energy_input_ratio_function_of_temperature_curve_name
        # real
        var_maximum_outdoor_drybulb_temperature_for_defrost_operation = 3.61
        obj.maximum_outdoor_drybulb_temperature_for_defrost_operation = var_maximum_outdoor_drybulb_temperature_for_defrost_operation
        # alpha
        var_defrost_strategy = "ReverseCycle"
        obj.defrost_strategy = var_defrost_strategy
        # alpha
        var_defrost_control = "Timed"
        obj.defrost_control = var_defrost_control
        # real
        var_defrost_time_period_fraction = 0.0
        obj.defrost_time_period_fraction = var_defrost_time_period_fraction
        # real
        var_resistive_defrost_heater_capacity = 0.0
        obj.resistive_defrost_heater_capacity = var_resistive_defrost_heater_capacity
        # alpha
        var_apply_part_load_fraction_to_speeds_greater_than_1 = "Yes"
        obj.apply_part_load_fraction_to_speeds_greater_than_1 = var_apply_part_load_fraction_to_speeds_greater_than_1
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
        # integer
        var_region_number_for_calculating_hspf = 3
        obj.region_number_for_calculating_hspf = var_region_number_for_calculating_hspf
        # integer
        var_number_of_speeds = 3
        obj.number_of_speeds = var_number_of_speeds
        # real
        var_speed_1_gross_rated_heating_capacity = 0.0001
        obj.speed_1_gross_rated_heating_capacity = var_speed_1_gross_rated_heating_capacity
        # real
        var_speed_1_gross_rated_heating_cop = 0.0001
        obj.speed_1_gross_rated_heating_cop = var_speed_1_gross_rated_heating_cop
        # real
        var_speed_1_rated_air_flow_rate = 0.0001
        obj.speed_1_rated_air_flow_rate = var_speed_1_rated_air_flow_rate
        # real
        var_speed_1_rated_supply_air_fan_power_per_volume_flow_rate = 625.0
        obj.speed_1_rated_supply_air_fan_power_per_volume_flow_rate = var_speed_1_rated_supply_air_fan_power_per_volume_flow_rate
        # object-list
        var_speed_1_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Heating Capacity Function of Temperature Curve Name"
        obj.speed_1_heating_capacity_function_of_temperature_curve_name = var_speed_1_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_heating_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 1 Heating Capacity Function of Flow Fraction Curve Name"
        obj.speed_1_heating_capacity_function_of_flow_fraction_curve_name = var_speed_1_heating_capacity_function_of_flow_fraction_curve_name
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
        var_speed_1_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_1_rated_waste_heat_fraction_of_power_input = var_speed_1_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_1_waste_heat_function_of_temperature_curve_name = "object-list|Speed 1 Waste Heat Function of Temperature Curve Name"
        obj.speed_1_waste_heat_function_of_temperature_curve_name = var_speed_1_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_2_gross_rated_heating_capacity = 0.0001
        obj.speed_2_gross_rated_heating_capacity = var_speed_2_gross_rated_heating_capacity
        # real
        var_speed_2_gross_rated_heating_cop = 0.0001
        obj.speed_2_gross_rated_heating_cop = var_speed_2_gross_rated_heating_cop
        # real
        var_speed_2_rated_air_flow_rate = 0.0001
        obj.speed_2_rated_air_flow_rate = var_speed_2_rated_air_flow_rate
        # real
        var_speed_2_rated_supply_air_fan_power_per_volume_flow_rate = 625.0
        obj.speed_2_rated_supply_air_fan_power_per_volume_flow_rate = var_speed_2_rated_supply_air_fan_power_per_volume_flow_rate
        # object-list
        var_speed_2_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Heating Capacity Function of Temperature Curve Name"
        obj.speed_2_heating_capacity_function_of_temperature_curve_name = var_speed_2_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_heating_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 2 Heating Capacity Function of Flow Fraction Curve Name"
        obj.speed_2_heating_capacity_function_of_flow_fraction_curve_name = var_speed_2_heating_capacity_function_of_flow_fraction_curve_name
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
        var_speed_2_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_2_rated_waste_heat_fraction_of_power_input = var_speed_2_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_2_waste_heat_function_of_temperature_curve_name = "object-list|Speed 2 Waste Heat Function of Temperature Curve Name"
        obj.speed_2_waste_heat_function_of_temperature_curve_name = var_speed_2_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_3_gross_rated_heating_capacity = 0.0001
        obj.speed_3_gross_rated_heating_capacity = var_speed_3_gross_rated_heating_capacity
        # real
        var_speed_3_gross_rated_heating_cop = 0.0001
        obj.speed_3_gross_rated_heating_cop = var_speed_3_gross_rated_heating_cop
        # real
        var_speed_3_rated_air_flow_rate = 0.0001
        obj.speed_3_rated_air_flow_rate = var_speed_3_rated_air_flow_rate
        # real
        var_speed_3_rated_supply_air_fan_power_per_volume_flow_rate = 625.0
        obj.speed_3_rated_supply_air_fan_power_per_volume_flow_rate = var_speed_3_rated_supply_air_fan_power_per_volume_flow_rate
        # object-list
        var_speed_3_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Heating Capacity Function of Temperature Curve Name"
        obj.speed_3_heating_capacity_function_of_temperature_curve_name = var_speed_3_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_heating_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 3 Heating Capacity Function of Flow Fraction Curve Name"
        obj.speed_3_heating_capacity_function_of_flow_fraction_curve_name = var_speed_3_heating_capacity_function_of_flow_fraction_curve_name
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
        var_speed_3_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_3_rated_waste_heat_fraction_of_power_input = var_speed_3_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_3_waste_heat_function_of_temperature_curve_name = "object-list|Speed 3 Waste Heat Function of Temperature Curve Name"
        obj.speed_3_waste_heat_function_of_temperature_curve_name = var_speed_3_waste_heat_function_of_temperature_curve_name
        # real
        var_speed_4_gross_rated_heating_capacity = 0.0001
        obj.speed_4_gross_rated_heating_capacity = var_speed_4_gross_rated_heating_capacity
        # real
        var_speed_4_gross_rated_heating_cop = 0.0001
        obj.speed_4_gross_rated_heating_cop = var_speed_4_gross_rated_heating_cop
        # real
        var_speed_4_rated_air_flow_rate = 0.0001
        obj.speed_4_rated_air_flow_rate = var_speed_4_rated_air_flow_rate
        # real
        var_speed_4_rated_supply_air_fan_power_per_volume_flow_rate = 625.0
        obj.speed_4_rated_supply_air_fan_power_per_volume_flow_rate = var_speed_4_rated_supply_air_fan_power_per_volume_flow_rate
        # object-list
        var_speed_4_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Heating Capacity Function of Temperature Curve Name"
        obj.speed_4_heating_capacity_function_of_temperature_curve_name = var_speed_4_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_heating_capacity_function_of_flow_fraction_curve_name = "object-list|Speed 4 Heating Capacity Function of Flow Fraction Curve Name"
        obj.speed_4_heating_capacity_function_of_flow_fraction_curve_name = var_speed_4_heating_capacity_function_of_flow_fraction_curve_name
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
        var_speed_4_rated_waste_heat_fraction_of_power_input = 0.50005
        obj.speed_4_rated_waste_heat_fraction_of_power_input = var_speed_4_rated_waste_heat_fraction_of_power_input
        # object-list
        var_speed_4_waste_heat_function_of_temperature_curve_name = "object-list|Speed 4 Waste Heat Function of Temperature Curve Name"
        obj.speed_4_waste_heat_function_of_temperature_curve_name = var_speed_4_waste_heat_function_of_temperature_curve_name
        # alpha
        var_zone_name_for_evaporator_placement = "Zone Name for Evaporator Placement"
        obj.zone_name_for_evaporator_placement = var_zone_name_for_evaporator_placement
        # real
        var_speed_1_secondary_coil_air_flow_rate = 0.0001
        obj.speed_1_secondary_coil_air_flow_rate = var_speed_1_secondary_coil_air_flow_rate
        # real
        var_speed_1_secondary_coil_fan_flow_scaling_factor = 0.0001
        obj.speed_1_secondary_coil_fan_flow_scaling_factor = var_speed_1_secondary_coil_fan_flow_scaling_factor
        # real
        var_speed_1_nominal_sensible_heat_ratio_of_secondary_coil = 0.50005
        obj.speed_1_nominal_sensible_heat_ratio_of_secondary_coil = var_speed_1_nominal_sensible_heat_ratio_of_secondary_coil
        # object-list
        var_speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name = "object-list|Speed 1 Sensible Heat Ratio Modifier Function of Temperature Curve Name"
        obj.speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name = var_speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = "object-list|Speed 1 Sensible Heat Ratio Modifier Function of Flow Fraction Curve Name"
        obj.speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = var_speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        # real
        var_speed_2_secondary_coil_air_flow_rate = 0.0001
        obj.speed_2_secondary_coil_air_flow_rate = var_speed_2_secondary_coil_air_flow_rate
        # real
        var_speed_2_secondary_coil_fan_flow_scaling_factor = 0.0001
        obj.speed_2_secondary_coil_fan_flow_scaling_factor = var_speed_2_secondary_coil_fan_flow_scaling_factor
        # real
        var_speed_2_nominal_sensible_heat_ratio_of_secondary_coil = 0.50005
        obj.speed_2_nominal_sensible_heat_ratio_of_secondary_coil = var_speed_2_nominal_sensible_heat_ratio_of_secondary_coil
        # object-list
        var_speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name = "object-list|Speed 2 Sensible Heat Ratio Modifier Function of Temperature Curve Name"
        obj.speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name = var_speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = "object-list|Speed 2 Sensible Heat Ratio Modifier Function of Flow Fraction Curve Name"
        obj.speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = var_speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        # real
        var_speed_3_secondary_coil_air_flow_rate = 0.0001
        obj.speed_3_secondary_coil_air_flow_rate = var_speed_3_secondary_coil_air_flow_rate
        # real
        var_speed_3_secondary_coil_fan_flow_scaling_factor = 0.0001
        obj.speed_3_secondary_coil_fan_flow_scaling_factor = var_speed_3_secondary_coil_fan_flow_scaling_factor
        # real
        var_speed_3_nominal_sensible_heat_ratio_of_secondary_coil = 0.50005
        obj.speed_3_nominal_sensible_heat_ratio_of_secondary_coil = var_speed_3_nominal_sensible_heat_ratio_of_secondary_coil
        # object-list
        var_speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name = "object-list|Speed 3 Sensible Heat Ratio Modifier Function of Temperature Curve Name"
        obj.speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name = var_speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = "object-list|Speed 3 Sensible Heat Ratio Modifier Function of Flow Fraction Curve Name"
        obj.speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = var_speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        # real
        var_speed_4_secondary_coil_air_flow_rate = 0.0001
        obj.speed_4_secondary_coil_air_flow_rate = var_speed_4_secondary_coil_air_flow_rate
        # real
        var_speed_4_secondary_coil_fan_flow_scaling_factor = 0.0001
        obj.speed_4_secondary_coil_fan_flow_scaling_factor = var_speed_4_secondary_coil_fan_flow_scaling_factor
        # real
        var_speed_4_nominal_sensible_heat_ratio_of_secondary_coil = 0.50005
        obj.speed_4_nominal_sensible_heat_ratio_of_secondary_coil = var_speed_4_nominal_sensible_heat_ratio_of_secondary_coil
        # object-list
        var_speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name = "object-list|Speed 4 Sensible Heat Ratio Modifier Function of Temperature Curve Name"
        obj.speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name = var_speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = "object-list|Speed 4 Sensible Heat Ratio Modifier Function of Flow Fraction Curve Name"
        obj.speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name = var_speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].name, var_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].minimum_outdoor_drybulb_temperature_for_compressor_operation, var_minimum_outdoor_drybulb_temperature_for_compressor_operation)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].outdoor_drybulb_temperature_to_turn_on_compressor, var_outdoor_drybulb_temperature_to_turn_on_compressor)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].defrost_energy_input_ratio_function_of_temperature_curve_name, var_defrost_energy_input_ratio_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].defrost_control, var_defrost_control)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].apply_part_load_fraction_to_speeds_greater_than_1, var_apply_part_load_fraction_to_speeds_greater_than_1)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].fuel_type, var_fuel_type)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].region_number_for_calculating_hspf, var_region_number_for_calculating_hspf)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].number_of_speeds, var_number_of_speeds)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_gross_rated_heating_capacity, var_speed_1_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_gross_rated_heating_cop, var_speed_1_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_rated_air_flow_rate, var_speed_1_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_rated_supply_air_fan_power_per_volume_flow_rate, var_speed_1_rated_supply_air_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_heating_capacity_function_of_temperature_curve_name, var_speed_1_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_heating_capacity_function_of_flow_fraction_curve_name, var_speed_1_heating_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_energy_input_ratio_function_of_temperature_curve_name, var_speed_1_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_part_load_fraction_correlation_curve_name, var_speed_1_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_rated_waste_heat_fraction_of_power_input, var_speed_1_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_waste_heat_function_of_temperature_curve_name, var_speed_1_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_gross_rated_heating_capacity, var_speed_2_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_gross_rated_heating_cop, var_speed_2_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_rated_air_flow_rate, var_speed_2_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_rated_supply_air_fan_power_per_volume_flow_rate, var_speed_2_rated_supply_air_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_heating_capacity_function_of_temperature_curve_name, var_speed_2_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_heating_capacity_function_of_flow_fraction_curve_name, var_speed_2_heating_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_energy_input_ratio_function_of_temperature_curve_name, var_speed_2_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_part_load_fraction_correlation_curve_name, var_speed_2_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_rated_waste_heat_fraction_of_power_input, var_speed_2_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_waste_heat_function_of_temperature_curve_name, var_speed_2_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_gross_rated_heating_capacity, var_speed_3_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_gross_rated_heating_cop, var_speed_3_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_rated_air_flow_rate, var_speed_3_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_rated_supply_air_fan_power_per_volume_flow_rate, var_speed_3_rated_supply_air_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_heating_capacity_function_of_temperature_curve_name, var_speed_3_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_heating_capacity_function_of_flow_fraction_curve_name, var_speed_3_heating_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_energy_input_ratio_function_of_temperature_curve_name, var_speed_3_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_part_load_fraction_correlation_curve_name, var_speed_3_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_rated_waste_heat_fraction_of_power_input, var_speed_3_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_waste_heat_function_of_temperature_curve_name, var_speed_3_waste_heat_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_gross_rated_heating_capacity, var_speed_4_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_gross_rated_heating_cop, var_speed_4_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_rated_air_flow_rate, var_speed_4_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_rated_supply_air_fan_power_per_volume_flow_rate, var_speed_4_rated_supply_air_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_heating_capacity_function_of_temperature_curve_name, var_speed_4_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_heating_capacity_function_of_flow_fraction_curve_name, var_speed_4_heating_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_energy_input_ratio_function_of_temperature_curve_name, var_speed_4_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_energy_input_ratio_function_of_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_part_load_fraction_correlation_curve_name, var_speed_4_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_rated_waste_heat_fraction_of_power_input, var_speed_4_rated_waste_heat_fraction_of_power_input)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_waste_heat_function_of_temperature_curve_name, var_speed_4_waste_heat_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].zone_name_for_evaporator_placement, var_zone_name_for_evaporator_placement)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_secondary_coil_air_flow_rate, var_speed_1_secondary_coil_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_secondary_coil_fan_flow_scaling_factor, var_speed_1_secondary_coil_fan_flow_scaling_factor)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_1_nominal_sensible_heat_ratio_of_secondary_coil, var_speed_1_nominal_sensible_heat_ratio_of_secondary_coil)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name, var_speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name, var_speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_secondary_coil_air_flow_rate, var_speed_2_secondary_coil_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_secondary_coil_fan_flow_scaling_factor, var_speed_2_secondary_coil_fan_flow_scaling_factor)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_2_nominal_sensible_heat_ratio_of_secondary_coil, var_speed_2_nominal_sensible_heat_ratio_of_secondary_coil)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name, var_speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name, var_speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_secondary_coil_air_flow_rate, var_speed_3_secondary_coil_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_secondary_coil_fan_flow_scaling_factor, var_speed_3_secondary_coil_fan_flow_scaling_factor)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_3_nominal_sensible_heat_ratio_of_secondary_coil, var_speed_3_nominal_sensible_heat_ratio_of_secondary_coil)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name, var_speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name, var_speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_secondary_coil_air_flow_rate, var_speed_4_secondary_coil_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_secondary_coil_fan_flow_scaling_factor, var_speed_4_secondary_coil_fan_flow_scaling_factor)
        self.assertAlmostEqual(idf2.coilheatingdxmultispeeds[0].speed_4_nominal_sensible_heat_ratio_of_secondary_coil, var_speed_4_nominal_sensible_heat_ratio_of_secondary_coil)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name, var_speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxmultispeeds[0].speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name, var_speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name)