import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.variable_refrigerant_flow_equipment import AirConditionerVariableRefrigerantFlow

log = logging.getLogger(__name__)

class TestAirConditionerVariableRefrigerantFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airconditionervariablerefrigerantflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirConditionerVariableRefrigerantFlow()
        # alpha
        var_heat_pump_name = "Heat Pump Name"
        obj.heat_pump_name = var_heat_pump_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_gross_rated_total_cooling_capacity = 0.0001
        obj.gross_rated_total_cooling_capacity = var_gross_rated_total_cooling_capacity
        # real
        var_gross_rated_cooling_cop = 0.0001
        obj.gross_rated_cooling_cop = var_gross_rated_cooling_cop
        # real
        var_minimum_outdoor_temperature_in_cooling_mode = 5.5
        obj.minimum_outdoor_temperature_in_cooling_mode = var_minimum_outdoor_temperature_in_cooling_mode
        # real
        var_maximum_outdoor_temperature_in_cooling_mode = 6.6
        obj.maximum_outdoor_temperature_in_cooling_mode = var_maximum_outdoor_temperature_in_cooling_mode
        # object-list
        var_cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name = "object-list|Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"
        obj.cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name = var_cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name
        # object-list
        var_cooling_capacity_ratio_boundary_curve_name = "object-list|Cooling Capacity Ratio Boundary Curve Name"
        obj.cooling_capacity_ratio_boundary_curve_name = var_cooling_capacity_ratio_boundary_curve_name
        # object-list
        var_cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name = "object-list|Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"
        obj.cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name = var_cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name
        # object-list
        var_cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name = "object-list|Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"
        obj.cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name = var_cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name
        # object-list
        var_cooling_energy_input_ratio_boundary_curve_name = "object-list|Cooling Energy Input Ratio Boundary Curve Name"
        obj.cooling_energy_input_ratio_boundary_curve_name = var_cooling_energy_input_ratio_boundary_curve_name
        # object-list
        var_cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name = "object-list|Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"
        obj.cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name = var_cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name
        # object-list
        var_cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = "object-list|Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"
        obj.cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = var_cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name
        # object-list
        var_cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = "object-list|Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"
        obj.cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = var_cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name
        # object-list
        var_cooling_combination_ratio_correction_factor_curve_name = "object-list|Cooling Combination Ratio Correction Factor Curve Name"
        obj.cooling_combination_ratio_correction_factor_curve_name = var_cooling_combination_ratio_correction_factor_curve_name
        # object-list
        var_cooling_partload_fraction_correlation_curve_name = "object-list|Cooling Part-Load Fraction Correlation Curve Name"
        obj.cooling_partload_fraction_correlation_curve_name = var_cooling_partload_fraction_correlation_curve_name
        # real
        var_gross_rated_heating_capacity = 17.17
        obj.gross_rated_heating_capacity = var_gross_rated_heating_capacity
        # real
        var_rated_heating_capacity_sizing_ratio = 1.0
        obj.rated_heating_capacity_sizing_ratio = var_rated_heating_capacity_sizing_ratio
        # real
        var_gross_rated_heating_cop = 19.19
        obj.gross_rated_heating_cop = var_gross_rated_heating_cop
        # real
        var_minimum_outdoor_temperature_in_heating_mode = 20.2
        obj.minimum_outdoor_temperature_in_heating_mode = var_minimum_outdoor_temperature_in_heating_mode
        # real
        var_maximum_outdoor_temperature_in_heating_mode = 21.21
        obj.maximum_outdoor_temperature_in_heating_mode = var_maximum_outdoor_temperature_in_heating_mode
        # object-list
        var_heating_capacity_ratio_modifier_function_of_low_temperature_curve_name = "object-list|Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"
        obj.heating_capacity_ratio_modifier_function_of_low_temperature_curve_name = var_heating_capacity_ratio_modifier_function_of_low_temperature_curve_name
        # object-list
        var_heating_capacity_ratio_boundary_curve_name = "object-list|Heating Capacity Ratio Boundary Curve Name"
        obj.heating_capacity_ratio_boundary_curve_name = var_heating_capacity_ratio_boundary_curve_name
        # object-list
        var_heating_capacity_ratio_modifier_function_of_high_temperature_curve_name = "object-list|Heating Capacity Ratio Modifier Function of High Temperature Curve Name"
        obj.heating_capacity_ratio_modifier_function_of_high_temperature_curve_name = var_heating_capacity_ratio_modifier_function_of_high_temperature_curve_name
        # object-list
        var_heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name = "object-list|Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"
        obj.heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name = var_heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name
        # object-list
        var_heating_energy_input_ratio_boundary_curve_name = "object-list|Heating Energy Input Ratio Boundary Curve Name"
        obj.heating_energy_input_ratio_boundary_curve_name = var_heating_energy_input_ratio_boundary_curve_name
        # object-list
        var_heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name = "object-list|Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"
        obj.heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name = var_heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name
        # alpha
        var_heating_performance_curve_outdoor_temperature_type = "DryBulbTemperature"
        obj.heating_performance_curve_outdoor_temperature_type = var_heating_performance_curve_outdoor_temperature_type
        # object-list
        var_heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = "object-list|Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"
        obj.heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = var_heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name
        # object-list
        var_heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = "object-list|Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"
        obj.heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = var_heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name
        # object-list
        var_heating_combination_ratio_correction_factor_curve_name = "object-list|Heating Combination Ratio Correction Factor Curve Name"
        obj.heating_combination_ratio_correction_factor_curve_name = var_heating_combination_ratio_correction_factor_curve_name
        # object-list
        var_heating_partload_fraction_correlation_curve_name = "object-list|Heating Part-Load Fraction Correlation Curve Name"
        obj.heating_partload_fraction_correlation_curve_name = var_heating_partload_fraction_correlation_curve_name
        # real
        var_minimum_heat_pump_partload_ratio = 33.33
        obj.minimum_heat_pump_partload_ratio = var_minimum_heat_pump_partload_ratio
        # object-list
        var_zone_name_for_master_thermostat_location = "object-list|Zone Name for Master Thermostat Location"
        obj.zone_name_for_master_thermostat_location = var_zone_name_for_master_thermostat_location
        # alpha
        var_master_thermostat_priority_control_type = "LoadPriority"
        obj.master_thermostat_priority_control_type = var_master_thermostat_priority_control_type
        # alpha
        var_thermostat_priority_schedule_name = "Thermostat Priority Schedule Name"
        obj.thermostat_priority_schedule_name = var_thermostat_priority_schedule_name
        # object-list
        var_zone_terminal_unit_list_name = "object-list|Zone Terminal Unit List Name"
        obj.zone_terminal_unit_list_name = var_zone_terminal_unit_list_name
        # alpha
        var_heat_pump_waste_heat_recovery = "No"
        obj.heat_pump_waste_heat_recovery = var_heat_pump_waste_heat_recovery
        # real
        var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = 39.39
        obj.equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode
        # real
        var_vertical_height_used_for_piping_correction_factor = 40.4
        obj.vertical_height_used_for_piping_correction_factor = var_vertical_height_used_for_piping_correction_factor
        # object-list
        var_piping_correction_factor_for_length_in_cooling_mode_curve_name = "object-list|Piping Correction Factor for Length in Cooling Mode Curve Name"
        obj.piping_correction_factor_for_length_in_cooling_mode_curve_name = var_piping_correction_factor_for_length_in_cooling_mode_curve_name
        # real
        var_piping_correction_factor_for_height_in_cooling_mode_coefficient = 42.42
        obj.piping_correction_factor_for_height_in_cooling_mode_coefficient = var_piping_correction_factor_for_height_in_cooling_mode_coefficient
        # real
        var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = 43.43
        obj.equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode
        # object-list
        var_piping_correction_factor_for_length_in_heating_mode_curve_name = "object-list|Piping Correction Factor for Length in Heating Mode Curve Name"
        obj.piping_correction_factor_for_length_in_heating_mode_curve_name = var_piping_correction_factor_for_length_in_heating_mode_curve_name
        # real
        var_piping_correction_factor_for_height_in_heating_mode_coefficient = 45.45
        obj.piping_correction_factor_for_height_in_heating_mode_coefficient = var_piping_correction_factor_for_height_in_heating_mode_coefficient
        # real
        var_crankcase_heater_power_per_compressor = 46.46
        obj.crankcase_heater_power_per_compressor = var_crankcase_heater_power_per_compressor
        # integer
        var_number_of_compressors = 47
        obj.number_of_compressors = var_number_of_compressors
        # real
        var_ratio_of_compressor_size_to_total_compressor_capacity = 48.48
        obj.ratio_of_compressor_size_to_total_compressor_capacity = var_ratio_of_compressor_size_to_total_compressor_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater = 49.49
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater
        # alpha
        var_defrost_strategy = "ReverseCycle"
        obj.defrost_strategy = var_defrost_strategy
        # alpha
        var_defrost_control = "Timed"
        obj.defrost_control = var_defrost_control
        # object-list
        var_defrost_energy_input_ratio_modifier_function_of_temperature_curve_name = "object-list|Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"
        obj.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name = var_defrost_energy_input_ratio_modifier_function_of_temperature_curve_name
        # real
        var_defrost_time_period_fraction = 0.0
        obj.defrost_time_period_fraction = var_defrost_time_period_fraction
        # real
        var_resistive_defrost_heater_capacity = 0.0
        obj.resistive_defrost_heater_capacity = var_resistive_defrost_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_defrost_operation = 55.55
        obj.maximum_outdoor_drybulb_temperature_for_defrost_operation = var_maximum_outdoor_drybulb_temperature_for_defrost_operation
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # node
        var_condenser_inlet_node_name = "node|Condenser Inlet Node Name"
        obj.condenser_inlet_node_name = var_condenser_inlet_node_name
        # node
        var_condenser_outlet_node_name = "node|Condenser Outlet Node Name"
        obj.condenser_outlet_node_name = var_condenser_outlet_node_name
        # real
        var_water_condenser_volume_flow_rate = 59.59
        obj.water_condenser_volume_flow_rate = var_water_condenser_volume_flow_rate
        # real
        var_evaporative_condenser_effectiveness = 0.5
        obj.evaporative_condenser_effectiveness = var_evaporative_condenser_effectiveness
        # real
        var_evaporative_condenser_air_flow_rate = 0.0001
        obj.evaporative_condenser_air_flow_rate = var_evaporative_condenser_air_flow_rate
        # real
        var_evaporative_condenser_pump_rated_power_consumption = 0.0
        obj.evaporative_condenser_pump_rated_power_consumption = var_evaporative_condenser_pump_rated_power_consumption
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
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
        # real
        var_minimum_outdoor_temperature_in_heat_recovery_mode = 68.68
        obj.minimum_outdoor_temperature_in_heat_recovery_mode = var_minimum_outdoor_temperature_in_heat_recovery_mode
        # real
        var_maximum_outdoor_temperature_in_heat_recovery_mode = 69.69
        obj.maximum_outdoor_temperature_in_heat_recovery_mode = var_maximum_outdoor_temperature_in_heat_recovery_mode
        # object-list
        var_heat_recovery_cooling_capacity_modifier_curve_name = "object-list|Heat Recovery Cooling Capacity Modifier Curve Name"
        obj.heat_recovery_cooling_capacity_modifier_curve_name = var_heat_recovery_cooling_capacity_modifier_curve_name
        # real
        var_initial_heat_recovery_cooling_capacity_fraction = 71.71
        obj.initial_heat_recovery_cooling_capacity_fraction = var_initial_heat_recovery_cooling_capacity_fraction
        # real
        var_heat_recovery_cooling_capacity_time_constant = 72.72
        obj.heat_recovery_cooling_capacity_time_constant = var_heat_recovery_cooling_capacity_time_constant
        # object-list
        var_heat_recovery_cooling_energy_modifier_curve_name = "object-list|Heat Recovery Cooling Energy Modifier Curve Name"
        obj.heat_recovery_cooling_energy_modifier_curve_name = var_heat_recovery_cooling_energy_modifier_curve_name
        # real
        var_initial_heat_recovery_cooling_energy_fraction = 74.74
        obj.initial_heat_recovery_cooling_energy_fraction = var_initial_heat_recovery_cooling_energy_fraction
        # real
        var_heat_recovery_cooling_energy_time_constant = 75.75
        obj.heat_recovery_cooling_energy_time_constant = var_heat_recovery_cooling_energy_time_constant
        # object-list
        var_heat_recovery_heating_capacity_modifier_curve_name = "object-list|Heat Recovery Heating Capacity Modifier Curve Name"
        obj.heat_recovery_heating_capacity_modifier_curve_name = var_heat_recovery_heating_capacity_modifier_curve_name
        # real
        var_initial_heat_recovery_heating_capacity_fraction = 77.77
        obj.initial_heat_recovery_heating_capacity_fraction = var_initial_heat_recovery_heating_capacity_fraction
        # real
        var_heat_recovery_heating_capacity_time_constant = 78.78
        obj.heat_recovery_heating_capacity_time_constant = var_heat_recovery_heating_capacity_time_constant
        # object-list
        var_heat_recovery_heating_energy_modifier_curve_name = "object-list|Heat Recovery Heating Energy Modifier Curve Name"
        obj.heat_recovery_heating_energy_modifier_curve_name = var_heat_recovery_heating_energy_modifier_curve_name
        # real
        var_initial_heat_recovery_heating_energy_fraction = 80.8
        obj.initial_heat_recovery_heating_energy_fraction = var_initial_heat_recovery_heating_energy_fraction
        # real
        var_heat_recovery_heating_energy_time_constant = 81.81
        obj.heat_recovery_heating_energy_time_constant = var_heat_recovery_heating_energy_time_constant

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_pump_name, var_heat_pump_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].gross_rated_cooling_cop, var_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].minimum_outdoor_temperature_in_cooling_mode, var_minimum_outdoor_temperature_in_cooling_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].maximum_outdoor_temperature_in_cooling_mode, var_maximum_outdoor_temperature_in_cooling_mode)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name, var_cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_capacity_ratio_boundary_curve_name, var_cooling_capacity_ratio_boundary_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name, var_cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name, var_cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_energy_input_ratio_boundary_curve_name, var_cooling_energy_input_ratio_boundary_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name, var_cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name, var_cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name, var_cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_combination_ratio_correction_factor_curve_name, var_cooling_combination_ratio_correction_factor_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].cooling_partload_fraction_correlation_curve_name, var_cooling_partload_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].gross_rated_heating_capacity, var_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].rated_heating_capacity_sizing_ratio, var_rated_heating_capacity_sizing_ratio)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].gross_rated_heating_cop, var_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].minimum_outdoor_temperature_in_heating_mode, var_minimum_outdoor_temperature_in_heating_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].maximum_outdoor_temperature_in_heating_mode, var_maximum_outdoor_temperature_in_heating_mode)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_capacity_ratio_modifier_function_of_low_temperature_curve_name, var_heating_capacity_ratio_modifier_function_of_low_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_capacity_ratio_boundary_curve_name, var_heating_capacity_ratio_boundary_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_capacity_ratio_modifier_function_of_high_temperature_curve_name, var_heating_capacity_ratio_modifier_function_of_high_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name, var_heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_energy_input_ratio_boundary_curve_name, var_heating_energy_input_ratio_boundary_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name, var_heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_performance_curve_outdoor_temperature_type, var_heating_performance_curve_outdoor_temperature_type)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name, var_heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name, var_heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_combination_ratio_correction_factor_curve_name, var_heating_combination_ratio_correction_factor_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heating_partload_fraction_correlation_curve_name, var_heating_partload_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].minimum_heat_pump_partload_ratio, var_minimum_heat_pump_partload_ratio)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].zone_name_for_master_thermostat_location, var_zone_name_for_master_thermostat_location)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].master_thermostat_priority_control_type, var_master_thermostat_priority_control_type)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].thermostat_priority_schedule_name, var_thermostat_priority_schedule_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].zone_terminal_unit_list_name, var_zone_terminal_unit_list_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_pump_waste_heat_recovery, var_heat_pump_waste_heat_recovery)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode, var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].vertical_height_used_for_piping_correction_factor, var_vertical_height_used_for_piping_correction_factor)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].piping_correction_factor_for_length_in_cooling_mode_curve_name, var_piping_correction_factor_for_length_in_cooling_mode_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].piping_correction_factor_for_height_in_cooling_mode_coefficient, var_piping_correction_factor_for_height_in_cooling_mode_coefficient)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode, var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].piping_correction_factor_for_length_in_heating_mode_curve_name, var_piping_correction_factor_for_length_in_heating_mode_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].piping_correction_factor_for_height_in_heating_mode_coefficient, var_piping_correction_factor_for_height_in_heating_mode_coefficient)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].crankcase_heater_power_per_compressor, var_crankcase_heater_power_per_compressor)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].number_of_compressors, var_number_of_compressors)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].ratio_of_compressor_size_to_total_compressor_capacity, var_ratio_of_compressor_size_to_total_compressor_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].defrost_control, var_defrost_control)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].defrost_energy_input_ratio_modifier_function_of_temperature_curve_name, var_defrost_energy_input_ratio_modifier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].water_condenser_volume_flow_rate, var_water_condenser_volume_flow_rate)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].evaporative_condenser_air_flow_rate, var_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].minimum_outdoor_temperature_in_heat_recovery_mode, var_minimum_outdoor_temperature_in_heat_recovery_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].maximum_outdoor_temperature_in_heat_recovery_mode, var_maximum_outdoor_temperature_in_heat_recovery_mode)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_cooling_capacity_modifier_curve_name, var_heat_recovery_cooling_capacity_modifier_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].initial_heat_recovery_cooling_capacity_fraction, var_initial_heat_recovery_cooling_capacity_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_cooling_capacity_time_constant, var_heat_recovery_cooling_capacity_time_constant)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_cooling_energy_modifier_curve_name, var_heat_recovery_cooling_energy_modifier_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].initial_heat_recovery_cooling_energy_fraction, var_initial_heat_recovery_cooling_energy_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_cooling_energy_time_constant, var_heat_recovery_cooling_energy_time_constant)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_heating_capacity_modifier_curve_name, var_heat_recovery_heating_capacity_modifier_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].initial_heat_recovery_heating_capacity_fraction, var_initial_heat_recovery_heating_capacity_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_heating_capacity_time_constant, var_heat_recovery_heating_capacity_time_constant)
        self.assertEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_heating_energy_modifier_curve_name, var_heat_recovery_heating_energy_modifier_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].initial_heat_recovery_heating_energy_fraction, var_initial_heat_recovery_heating_energy_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflows[0].heat_recovery_heating_energy_time_constant, var_heat_recovery_heating_energy_time_constant)