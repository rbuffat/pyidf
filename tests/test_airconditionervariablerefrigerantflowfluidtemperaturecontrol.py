import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.variable_refrigerant_flow_equipment import AirConditionerVariableRefrigerantFlowFluidTemperatureControl

log = logging.getLogger(__name__)

class TestAirConditionerVariableRefrigerantFlowFluidTemperatureControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airconditionervariablerefrigerantflowfluidtemperaturecontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirConditionerVariableRefrigerantFlowFluidTemperatureControl()
        # alpha
        var_heat_pump_name = "Heat Pump Name"
        obj.heat_pump_name = var_heat_pump_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_terminal_unit_list_name = "object-list|Zone Terminal Unit List Name"
        obj.zone_terminal_unit_list_name = var_zone_terminal_unit_list_name
        # object-list
        var_refrigerant_type = "object-list|Refrigerant Type"
        obj.refrigerant_type = var_refrigerant_type
        # real
        var_rated_evaporative_capacity = 0.0001
        obj.rated_evaporative_capacity = var_rated_evaporative_capacity
        # real
        var_rated_compressor_power_per_unit_of_rated_evaporative_capacity = 0.0001
        obj.rated_compressor_power_per_unit_of_rated_evaporative_capacity = var_rated_compressor_power_per_unit_of_rated_evaporative_capacity
        # real
        var_minimum_outdoor_air_temperature_in_cooling_mode = 7.7
        obj.minimum_outdoor_air_temperature_in_cooling_mode = var_minimum_outdoor_air_temperature_in_cooling_mode
        # real
        var_maximum_outdoor_air_temperature_in_cooling_mode = 8.8
        obj.maximum_outdoor_air_temperature_in_cooling_mode = var_maximum_outdoor_air_temperature_in_cooling_mode
        # real
        var_minimum_outdoor_air_temperature_in_heating_mode = 9.9
        obj.minimum_outdoor_air_temperature_in_heating_mode = var_minimum_outdoor_air_temperature_in_heating_mode
        # real
        var_maximum_outdoor_air_temperature_in_heating_mode = 10.1
        obj.maximum_outdoor_air_temperature_in_heating_mode = var_maximum_outdoor_air_temperature_in_heating_mode
        # real
        var_reference_outdoor_unit_superheating = 11.11
        obj.reference_outdoor_unit_superheating = var_reference_outdoor_unit_superheating
        # real
        var_reference_outdoor_unit_subcooling = 12.12
        obj.reference_outdoor_unit_subcooling = var_reference_outdoor_unit_subcooling
        # alpha
        var_refrigerant_temperature_control_algorithm_for_indoor_unit = "ConstantTemp"
        obj.refrigerant_temperature_control_algorithm_for_indoor_unit = var_refrigerant_temperature_control_algorithm_for_indoor_unit
        # real
        var_reference_evaporating_temperature_for_indoor_unit = 14.14
        obj.reference_evaporating_temperature_for_indoor_unit = var_reference_evaporating_temperature_for_indoor_unit
        # real
        var_reference_condensing_temperature_for_indoor_unit = 15.15
        obj.reference_condensing_temperature_for_indoor_unit = var_reference_condensing_temperature_for_indoor_unit
        # real
        var_variable_evaporating_temperature_minimum_for_indoor_unit = 16.16
        obj.variable_evaporating_temperature_minimum_for_indoor_unit = var_variable_evaporating_temperature_minimum_for_indoor_unit
        # real
        var_variable_evaporating_temperature_maximum_for_indoor_unit = 17.17
        obj.variable_evaporating_temperature_maximum_for_indoor_unit = var_variable_evaporating_temperature_maximum_for_indoor_unit
        # real
        var_variable_condensing_temperature_minimum_for_indoor_unit = 18.18
        obj.variable_condensing_temperature_minimum_for_indoor_unit = var_variable_condensing_temperature_minimum_for_indoor_unit
        # real
        var_variable_condensing_temperature_maximum_for_indoor_unit = 19.19
        obj.variable_condensing_temperature_maximum_for_indoor_unit = var_variable_condensing_temperature_maximum_for_indoor_unit
        # real
        var_outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity = 0.0001
        obj.outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity = var_outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity
        # real
        var_outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity = 0.0001
        obj.outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity = var_outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity
        # object-list
        var_outdoor_unit_evaporating_temperature_function_of_superheating_curve_name = "object-list|Outdoor Unit Evaporating Temperature Function of Superheating Curve Name"
        obj.outdoor_unit_evaporating_temperature_function_of_superheating_curve_name = var_outdoor_unit_evaporating_temperature_function_of_superheating_curve_name
        # object-list
        var_outdoor_unit_condensing_temperature_function_of_subcooling_curve_name = "object-list|Outdoor Unit Condensing Temperature Function of Subcooling Curve Name"
        obj.outdoor_unit_condensing_temperature_function_of_subcooling_curve_name = var_outdoor_unit_condensing_temperature_function_of_subcooling_curve_name
        # real
        var_diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units = 0.0
        obj.diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units = var_diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units
        # real
        var_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units = 0.0
        obj.length_of_main_pipe_connecting_outdoor_unit_to_indoor_units = var_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units
        # real
        var_equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units = 0.0
        obj.equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units = var_equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units
        # real
        var_height_difference_between_outdoor_unit_and_indoor_units = 27.27
        obj.height_difference_between_outdoor_unit_and_indoor_units = var_height_difference_between_outdoor_unit_and_indoor_units
        # real
        var_main_pipe_insulation_thickness = 0.0
        obj.main_pipe_insulation_thickness = var_main_pipe_insulation_thickness
        # real
        var_main_pipe_insulation_thermal_conductivity = 0.0
        obj.main_pipe_insulation_thermal_conductivity = var_main_pipe_insulation_thermal_conductivity
        # real
        var_crankcase_heater_power_per_compressor = 30.3
        obj.crankcase_heater_power_per_compressor = var_crankcase_heater_power_per_compressor
        # integer
        var_number_of_compressors = 31
        obj.number_of_compressors = var_number_of_compressors
        # real
        var_ratio_of_compressor_size_to_total_compressor_capacity = 32.32
        obj.ratio_of_compressor_size_to_total_compressor_capacity = var_ratio_of_compressor_size_to_total_compressor_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater = 33.33
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
        var_maximum_outdoor_drybulb_temperature_for_defrost_operation = 39.39
        obj.maximum_outdoor_drybulb_temperature_for_defrost_operation = var_maximum_outdoor_drybulb_temperature_for_defrost_operation
        # real
        var_compressor_maximum_delta_pressure = 25000000.0
        obj.compressor_maximum_delta_pressure = var_compressor_maximum_delta_pressure
        # integer
        var_number_of_compressor_loading_index_entries = 5
        obj.number_of_compressor_loading_index_entries = var_number_of_compressor_loading_index_entries
        # real
        var_compressor_speed_at_loading_index_1 = 0.0001
        obj.compressor_speed_at_loading_index_1 = var_compressor_speed_at_loading_index_1
        # object-list
        var_loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 1 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 1 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_2 = 0.0001
        obj.compressor_speed_at_loading_index_2 = var_compressor_speed_at_loading_index_2
        # object-list
        var_loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 2 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 2 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_3 = 0.0001
        obj.compressor_speed_at_loading_index_3 = var_compressor_speed_at_loading_index_3
        # object-list
        var_loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 3 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 3 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_4 = 0.0001
        obj.compressor_speed_at_loading_index_4 = var_compressor_speed_at_loading_index_4
        # object-list
        var_loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 4 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 4 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_5 = 0.0001
        obj.compressor_speed_at_loading_index_5 = var_compressor_speed_at_loading_index_5
        # object-list
        var_loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 5 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 5 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_6 = 0.0001
        obj.compressor_speed_at_loading_index_6 = var_compressor_speed_at_loading_index_6
        # object-list
        var_loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 6 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 6 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_7 = 0.0001
        obj.compressor_speed_at_loading_index_7 = var_compressor_speed_at_loading_index_7
        # object-list
        var_loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 7 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # alpha
        var_loading_index_7_list = "Loading Index 7 list"
        obj.loading_index_7_list = var_loading_index_7_list
        # real
        var_compressor_speed_at_loading_index_8 = 0.0001
        obj.compressor_speed_at_loading_index_8 = var_compressor_speed_at_loading_index_8
        # object-list
        var_loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 8 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 8 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name
        # real
        var_compressor_speed_at_loading_index_9 = 0.0001
        obj.compressor_speed_at_loading_index_9 = var_compressor_speed_at_loading_index_9
        # object-list
        var_loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 9 Evaporative Capacity Multiplier Function of Temperature Curve Name"
        obj.loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name = var_loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name
        # object-list
        var_loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name = "object-list|Loading Index 9 Compressor Power Multiplier Function of Temperature Curve Name"
        obj.loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name = var_loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].heat_pump_name, var_heat_pump_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].zone_terminal_unit_list_name, var_zone_terminal_unit_list_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].refrigerant_type, var_refrigerant_type)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].rated_evaporative_capacity, var_rated_evaporative_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].rated_compressor_power_per_unit_of_rated_evaporative_capacity, var_rated_compressor_power_per_unit_of_rated_evaporative_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].minimum_outdoor_air_temperature_in_cooling_mode, var_minimum_outdoor_air_temperature_in_cooling_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].maximum_outdoor_air_temperature_in_cooling_mode, var_maximum_outdoor_air_temperature_in_cooling_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].minimum_outdoor_air_temperature_in_heating_mode, var_minimum_outdoor_air_temperature_in_heating_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].maximum_outdoor_air_temperature_in_heating_mode, var_maximum_outdoor_air_temperature_in_heating_mode)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].reference_outdoor_unit_superheating, var_reference_outdoor_unit_superheating)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].reference_outdoor_unit_subcooling, var_reference_outdoor_unit_subcooling)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].refrigerant_temperature_control_algorithm_for_indoor_unit, var_refrigerant_temperature_control_algorithm_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].reference_evaporating_temperature_for_indoor_unit, var_reference_evaporating_temperature_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].reference_condensing_temperature_for_indoor_unit, var_reference_condensing_temperature_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].variable_evaporating_temperature_minimum_for_indoor_unit, var_variable_evaporating_temperature_minimum_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].variable_evaporating_temperature_maximum_for_indoor_unit, var_variable_evaporating_temperature_maximum_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].variable_condensing_temperature_minimum_for_indoor_unit, var_variable_condensing_temperature_minimum_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].variable_condensing_temperature_maximum_for_indoor_unit, var_variable_condensing_temperature_maximum_for_indoor_unit)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity, var_outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity, var_outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].outdoor_unit_evaporating_temperature_function_of_superheating_curve_name, var_outdoor_unit_evaporating_temperature_function_of_superheating_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].outdoor_unit_condensing_temperature_function_of_subcooling_curve_name, var_outdoor_unit_condensing_temperature_function_of_subcooling_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units, var_diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].length_of_main_pipe_connecting_outdoor_unit_to_indoor_units, var_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units, var_equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].height_difference_between_outdoor_unit_and_indoor_units, var_height_difference_between_outdoor_unit_and_indoor_units)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].main_pipe_insulation_thickness, var_main_pipe_insulation_thickness)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].main_pipe_insulation_thermal_conductivity, var_main_pipe_insulation_thermal_conductivity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].crankcase_heater_power_per_compressor, var_crankcase_heater_power_per_compressor)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].number_of_compressors, var_number_of_compressors)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].ratio_of_compressor_size_to_total_compressor_capacity, var_ratio_of_compressor_size_to_total_compressor_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].defrost_control, var_defrost_control)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].defrost_energy_input_ratio_modifier_function_of_temperature_curve_name, var_defrost_energy_input_ratio_modifier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_maximum_delta_pressure, var_compressor_maximum_delta_pressure)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].number_of_compressor_loading_index_entries, var_number_of_compressor_loading_index_entries)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_1, var_compressor_speed_at_loading_index_1)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_2, var_compressor_speed_at_loading_index_2)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_3, var_compressor_speed_at_loading_index_3)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_4, var_compressor_speed_at_loading_index_4)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_5, var_compressor_speed_at_loading_index_5)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_6, var_compressor_speed_at_loading_index_6)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_7, var_compressor_speed_at_loading_index_7)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_7_list, var_loading_index_7_list)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_8, var_compressor_speed_at_loading_index_8)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].compressor_speed_at_loading_index_9, var_compressor_speed_at_loading_index_9)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name, var_loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name)
        self.assertEqual(idf2.airconditionervariablerefrigerantflowfluidtemperaturecontrols[0].loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name, var_loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name)