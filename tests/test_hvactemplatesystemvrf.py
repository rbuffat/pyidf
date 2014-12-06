import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateSystemVrf
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateSystemVrf(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemvrf(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemVrf()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
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
        # real
        var_gross_rated_heating_capacity = 7.7
        obj.gross_rated_heating_capacity = var_gross_rated_heating_capacity
        # real
        var_rated_heating_capacity_sizing_ratio = 1.0
        obj.rated_heating_capacity_sizing_ratio = var_rated_heating_capacity_sizing_ratio
        # real
        var_gross_rated_heating_cop = 9.9
        obj.gross_rated_heating_cop = var_gross_rated_heating_cop
        # real
        var_minimum_outdoor_temperature_in_heating_mode = 10.1
        obj.minimum_outdoor_temperature_in_heating_mode = var_minimum_outdoor_temperature_in_heating_mode
        # real
        var_maximum_outdoor_temperature_in_heating_mode = 11.11
        obj.maximum_outdoor_temperature_in_heating_mode = var_maximum_outdoor_temperature_in_heating_mode
        # real
        var_minimum_heat_pump_partload_ratio = 12.12
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
        # alpha
        var_heat_pump_waste_heat_recovery = "No"
        obj.heat_pump_waste_heat_recovery = var_heat_pump_waste_heat_recovery
        # real
        var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = 17.17
        obj.equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode
        # real
        var_vertical_height_used_for_piping_correction_factor = 18.18
        obj.vertical_height_used_for_piping_correction_factor = var_vertical_height_used_for_piping_correction_factor
        # real
        var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = 19.19
        obj.equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode
        # real
        var_crankcase_heater_power_per_compressor = 20.2
        obj.crankcase_heater_power_per_compressor = var_crankcase_heater_power_per_compressor
        # integer
        var_number_of_compressors = 21
        obj.number_of_compressors = var_number_of_compressors
        # real
        var_ratio_of_compressor_size_to_total_compressor_capacity = 22.22
        obj.ratio_of_compressor_size_to_total_compressor_capacity = var_ratio_of_compressor_size_to_total_compressor_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater = 23.23
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater
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
        # real
        var_maximum_outdoor_drybulb_temperature_for_defrost_operation = 28.28
        obj.maximum_outdoor_drybulb_temperature_for_defrost_operation = var_maximum_outdoor_drybulb_temperature_for_defrost_operation
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_water_condenser_volume_flow_rate = 30.3
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
        var_minimum_outdoor_temperature_in_heat_recovery_mode = 38.38
        obj.minimum_outdoor_temperature_in_heat_recovery_mode = var_minimum_outdoor_temperature_in_heat_recovery_mode
        # real
        var_maximum_outdoor_temperature_in_heat_recovery_mode = 39.39
        obj.maximum_outdoor_temperature_in_heat_recovery_mode = var_maximum_outdoor_temperature_in_heat_recovery_mode

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].gross_rated_cooling_cop, var_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].minimum_outdoor_temperature_in_cooling_mode, var_minimum_outdoor_temperature_in_cooling_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].maximum_outdoor_temperature_in_cooling_mode, var_maximum_outdoor_temperature_in_cooling_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].gross_rated_heating_capacity, var_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].rated_heating_capacity_sizing_ratio, var_rated_heating_capacity_sizing_ratio)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].gross_rated_heating_cop, var_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].minimum_outdoor_temperature_in_heating_mode, var_minimum_outdoor_temperature_in_heating_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].maximum_outdoor_temperature_in_heating_mode, var_maximum_outdoor_temperature_in_heating_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].minimum_heat_pump_partload_ratio, var_minimum_heat_pump_partload_ratio)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].zone_name_for_master_thermostat_location, var_zone_name_for_master_thermostat_location)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].master_thermostat_priority_control_type, var_master_thermostat_priority_control_type)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].thermostat_priority_schedule_name, var_thermostat_priority_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].heat_pump_waste_heat_recovery, var_heat_pump_waste_heat_recovery)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode, var_equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].vertical_height_used_for_piping_correction_factor, var_vertical_height_used_for_piping_correction_factor)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode, var_equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].crankcase_heater_power_per_compressor, var_crankcase_heater_power_per_compressor)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].number_of_compressors, var_number_of_compressors)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].ratio_of_compressor_size_to_total_compressor_capacity, var_ratio_of_compressor_size_to_total_compressor_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].defrost_control, var_defrost_control)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].water_condenser_volume_flow_rate, var_water_condenser_volume_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].evaporative_condenser_air_flow_rate, var_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvrfs[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].minimum_outdoor_temperature_in_heat_recovery_mode, var_minimum_outdoor_temperature_in_heat_recovery_mode)
        self.assertAlmostEqual(idf2.hvactemplatesystemvrfs[0].maximum_outdoor_temperature_in_heat_recovery_mode, var_maximum_outdoor_temperature_in_heat_recovery_mode)