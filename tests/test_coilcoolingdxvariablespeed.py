import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxVariableSpeed

log = logging.getLogger(__name__)

class TestCoilCoolingDxVariableSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxvariablespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxVariableSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_indoor_air_inlet_node_name = "node|Indoor Air Inlet Node Name"
        obj.indoor_air_inlet_node_name = var_indoor_air_inlet_node_name
        # node
        var_indoor_air_outlet_node_name = "node|Indoor Air Outlet Node Name"
        obj.indoor_air_outlet_node_name = var_indoor_air_outlet_node_name
        # integer
        var_number_of_speeds = 5
        obj.number_of_speeds = var_number_of_speeds
        # integer
        var_nominal_speed_level = 5
        obj.nominal_speed_level = var_nominal_speed_level
        # real
        var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level = 6.6
        obj.gross_rated_total_cooling_capacity_at_selected_nominal_speed_level = var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level
        # real
        var_rated_air_flow_rate_at_selected_nominal_speed_level = 7.7
        obj.rated_air_flow_rate_at_selected_nominal_speed_level = var_rated_air_flow_rate_at_selected_nominal_speed_level
        # real
        var_nominal_time_for_condensate_to_begin_leaving_the_coil = 0.0
        obj.nominal_time_for_condensate_to_begin_leaving_the_coil = var_nominal_time_for_condensate_to_begin_leaving_the_coil
        # real
        var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity = 0.0
        obj.initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity = var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity
        # object-list
        var_energy_part_load_fraction_curve_name = "object-list|Energy Part Load Fraction Curve Name"
        obj.energy_part_load_fraction_curve_name = var_energy_part_load_fraction_curve_name
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_evaporative_condenser_pump_rated_power_consumption = 0.0
        obj.evaporative_condenser_pump_rated_power_consumption = var_evaporative_condenser_pump_rated_power_consumption
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_operating_schedule_name = "object-list|Basin Heater Operating Schedule Name"
        obj.basin_heater_operating_schedule_name = var_basin_heater_operating_schedule_name
        # real
        var_speed_1_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_1_reference_unit_gross_rated_total_cooling_capacity = var_speed_1_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_1_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_1_reference_unit_gross_rated_sensible_heat_ratio = var_speed_1_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_1_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_1_reference_unit_gross_rated_cooling_cop = var_speed_1_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_1_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_air_flow_rate = var_speed_1_reference_unit_rated_air_flow_rate
        # real
        var_speed_1_reference_unit_rated_condenser_air_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_condenser_air_flow_rate = var_speed_1_reference_unit_rated_condenser_air_flow_rate
        # real
        var_speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_1_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_temperature_curve_name = var_speed_1_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_1_energy_input_ratio_function_of_temperature_curve_name = var_speed_1_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_2_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_2_reference_unit_gross_rated_total_cooling_capacity = var_speed_2_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_2_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_2_reference_unit_gross_rated_sensible_heat_ratio = var_speed_2_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_2_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_2_reference_unit_gross_rated_cooling_cop = var_speed_2_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_2_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_air_flow_rate = var_speed_2_reference_unit_rated_air_flow_rate
        # real
        var_speed_2_reference_unit_rated_condenser_air_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_condenser_air_flow_rate = var_speed_2_reference_unit_rated_condenser_air_flow_rate
        # real
        var_speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_2_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_temperature_curve_name = var_speed_2_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_2_energy_input_ratio_function_of_temperature_curve_name = var_speed_2_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_3_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_3_reference_unit_gross_rated_total_cooling_capacity = var_speed_3_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_3_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_3_reference_unit_gross_rated_sensible_heat_ratio = var_speed_3_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_3_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_3_reference_unit_gross_rated_cooling_cop = var_speed_3_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_3_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_air_flow_rate = var_speed_3_reference_unit_rated_air_flow_rate
        # real
        var_speed_3_reference_unit_rated_condenser_air_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_condenser_air_flow_rate = var_speed_3_reference_unit_rated_condenser_air_flow_rate
        # real
        var_speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_3_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_temperature_curve_name = var_speed_3_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_3_energy_input_ratio_function_of_temperature_curve_name = var_speed_3_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_4_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_4_reference_unit_gross_rated_total_cooling_capacity = var_speed_4_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_4_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_4_reference_unit_gross_rated_sensible_heat_ratio = var_speed_4_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_4_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_4_reference_unit_gross_rated_cooling_cop = var_speed_4_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_4_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_air_flow_rate = var_speed_4_reference_unit_rated_air_flow_rate
        # real
        var_speed_4_reference_unit_rated_condenser_air_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_condenser_air_flow_rate = var_speed_4_reference_unit_rated_condenser_air_flow_rate
        # real
        var_speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_4_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_temperature_curve_name = var_speed_4_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_4_energy_input_ratio_function_of_temperature_curve_name = var_speed_4_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_5_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_5_reference_unit_gross_rated_total_cooling_capacity = var_speed_5_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_5_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_5_reference_unit_gross_rated_sensible_heat_ratio = var_speed_5_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_5_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_5_reference_unit_gross_rated_cooling_cop = var_speed_5_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_5_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_air_flow_rate = var_speed_5_reference_unit_rated_air_flow_rate
        # real
        var_speed_5_reference_unit_rated_condenser_air_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_condenser_air_flow_rate = var_speed_5_reference_unit_rated_condenser_air_flow_rate
        # real
        var_speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_5_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 5 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_5_total_cooling_capacity_function_of_temperature_curve_name = var_speed_5_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_5_energy_input_ratio_function_of_temperature_curve_name = var_speed_5_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_6_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_6_reference_unit_gross_rated_total_cooling_capacity = var_speed_6_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_6_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_6_reference_unit_gross_rated_sensible_heat_ratio = var_speed_6_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_6_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_6_reference_unit_gross_rated_cooling_cop = var_speed_6_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_6_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_air_flow_rate = var_speed_6_reference_unit_rated_air_flow_rate
        # real
        var_speed_6_reference_unit_condenser_air_flow_rate = 0.0
        obj.speed_6_reference_unit_condenser_air_flow_rate = var_speed_6_reference_unit_condenser_air_flow_rate
        # real
        var_speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_6_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 6 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_6_total_cooling_capacity_function_of_temperature_curve_name = var_speed_6_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_6_energy_input_ratio_function_of_temperature_curve_name = var_speed_6_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_7_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_7_reference_unit_gross_rated_total_cooling_capacity = var_speed_7_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_7_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_7_reference_unit_gross_rated_sensible_heat_ratio = var_speed_7_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_7_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_7_reference_unit_gross_rated_cooling_cop = var_speed_7_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_7_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_air_flow_rate = var_speed_7_reference_unit_rated_air_flow_rate
        # real
        var_speed_7_reference_unit_condenser_flow_rate = 0.0
        obj.speed_7_reference_unit_condenser_flow_rate = var_speed_7_reference_unit_condenser_flow_rate
        # real
        var_speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_7_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 7 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_7_total_cooling_capacity_function_of_temperature_curve_name = var_speed_7_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_7_energy_input_ratio_function_of_temperature_curve_name = var_speed_7_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_8_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_8_reference_unit_gross_rated_total_cooling_capacity = var_speed_8_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_8_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_8_reference_unit_gross_rated_sensible_heat_ratio = var_speed_8_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_8_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_8_reference_unit_gross_rated_cooling_cop = var_speed_8_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_8_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_air_flow_rate = var_speed_8_reference_unit_rated_air_flow_rate
        # real
        var_speed_8_reference_unit_condenser_air_flow_rate = 0.0
        obj.speed_8_reference_unit_condenser_air_flow_rate = var_speed_8_reference_unit_condenser_air_flow_rate
        # real
        var_speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_8_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 8 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_8_total_cooling_capacity_function_of_temperature_curve_name = var_speed_8_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_8_energy_input_ratio_function_of_temperature_curve_name = var_speed_8_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_9_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_9_reference_unit_gross_rated_total_cooling_capacity = var_speed_9_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_9_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_9_reference_unit_gross_rated_sensible_heat_ratio = var_speed_9_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_9_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_9_reference_unit_gross_rated_cooling_cop = var_speed_9_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_9_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_air_flow_rate = var_speed_9_reference_unit_rated_air_flow_rate
        # real
        var_speed_9_reference_unit_condenser_air_flow_rate = 0.0
        obj.speed_9_reference_unit_condenser_air_flow_rate = var_speed_9_reference_unit_condenser_air_flow_rate
        # real
        var_speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_9_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 9 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_9_total_cooling_capacity_function_of_temperature_curve_name = var_speed_9_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_9_energy_input_ratio_function_of_temperature_curve_name = var_speed_9_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_10_reference_unit_gross_rated_total_cooling_capacity = 0.0
        obj.speed_10_reference_unit_gross_rated_total_cooling_capacity = var_speed_10_reference_unit_gross_rated_total_cooling_capacity
        # real
        var_speed_10_reference_unit_gross_rated_sensible_heat_ratio = 0.5
        obj.speed_10_reference_unit_gross_rated_sensible_heat_ratio = var_speed_10_reference_unit_gross_rated_sensible_heat_ratio
        # real
        var_speed_10_reference_unit_gross_rated_cooling_cop = 0.0
        obj.speed_10_reference_unit_gross_rated_cooling_cop = var_speed_10_reference_unit_gross_rated_cooling_cop
        # real
        var_speed_10_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_air_flow_rate = var_speed_10_reference_unit_rated_air_flow_rate
        # real
        var_speed_10_reference_unit_condenser_air_flow_rate = 0.0
        obj.speed_10_reference_unit_condenser_air_flow_rate = var_speed_10_reference_unit_condenser_air_flow_rate
        # real
        var_speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling = 0.5
        obj.speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling = var_speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling
        # object-list
        var_speed_10_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Speed 10 Total Cooling Capacity Function of Temperature Curve Name"
        obj.speed_10_total_cooling_capacity_function_of_temperature_curve_name = var_speed_10_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Total Cooling Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name = var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_10_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 10 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_10_energy_input_ratio_function_of_temperature_curve_name = var_speed_10_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].indoor_air_inlet_node_name, var_indoor_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].indoor_air_outlet_node_name, var_indoor_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].number_of_speeds, var_number_of_speeds)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].nominal_speed_level, var_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].gross_rated_total_cooling_capacity_at_selected_nominal_speed_level, var_gross_rated_total_cooling_capacity_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].rated_air_flow_rate_at_selected_nominal_speed_level, var_rated_air_flow_rate_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].nominal_time_for_condensate_to_begin_leaving_the_coil, var_nominal_time_for_condensate_to_begin_leaving_the_coil)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity, var_initial_moisture_evaporation_rate_divided_by_steadystate_ac_latent_capacity)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].energy_part_load_fraction_curve_name, var_energy_part_load_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_gross_rated_total_cooling_capacity, var_speed_1_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_gross_rated_sensible_heat_ratio, var_speed_1_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_gross_rated_cooling_cop, var_speed_1_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_rated_air_flow_rate, var_speed_1_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_rated_condenser_air_flow_rate, var_speed_1_reference_unit_rated_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_total_cooling_capacity_function_of_temperature_curve_name, var_speed_1_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_energy_input_ratio_function_of_temperature_curve_name, var_speed_1_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_gross_rated_total_cooling_capacity, var_speed_2_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_gross_rated_sensible_heat_ratio, var_speed_2_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_gross_rated_cooling_cop, var_speed_2_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_rated_air_flow_rate, var_speed_2_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_rated_condenser_air_flow_rate, var_speed_2_reference_unit_rated_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_total_cooling_capacity_function_of_temperature_curve_name, var_speed_2_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_energy_input_ratio_function_of_temperature_curve_name, var_speed_2_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_gross_rated_total_cooling_capacity, var_speed_3_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_gross_rated_sensible_heat_ratio, var_speed_3_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_gross_rated_cooling_cop, var_speed_3_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_rated_air_flow_rate, var_speed_3_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_rated_condenser_air_flow_rate, var_speed_3_reference_unit_rated_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_total_cooling_capacity_function_of_temperature_curve_name, var_speed_3_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_energy_input_ratio_function_of_temperature_curve_name, var_speed_3_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_gross_rated_total_cooling_capacity, var_speed_4_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_gross_rated_sensible_heat_ratio, var_speed_4_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_gross_rated_cooling_cop, var_speed_4_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_rated_air_flow_rate, var_speed_4_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_rated_condenser_air_flow_rate, var_speed_4_reference_unit_rated_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_total_cooling_capacity_function_of_temperature_curve_name, var_speed_4_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_energy_input_ratio_function_of_temperature_curve_name, var_speed_4_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_gross_rated_total_cooling_capacity, var_speed_5_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_gross_rated_sensible_heat_ratio, var_speed_5_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_gross_rated_cooling_cop, var_speed_5_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_rated_air_flow_rate, var_speed_5_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_rated_condenser_air_flow_rate, var_speed_5_reference_unit_rated_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_total_cooling_capacity_function_of_temperature_curve_name, var_speed_5_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_energy_input_ratio_function_of_temperature_curve_name, var_speed_5_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_gross_rated_total_cooling_capacity, var_speed_6_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_gross_rated_sensible_heat_ratio, var_speed_6_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_gross_rated_cooling_cop, var_speed_6_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_rated_air_flow_rate, var_speed_6_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_condenser_air_flow_rate, var_speed_6_reference_unit_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_total_cooling_capacity_function_of_temperature_curve_name, var_speed_6_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_energy_input_ratio_function_of_temperature_curve_name, var_speed_6_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_gross_rated_total_cooling_capacity, var_speed_7_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_gross_rated_sensible_heat_ratio, var_speed_7_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_gross_rated_cooling_cop, var_speed_7_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_rated_air_flow_rate, var_speed_7_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_condenser_flow_rate, var_speed_7_reference_unit_condenser_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_total_cooling_capacity_function_of_temperature_curve_name, var_speed_7_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_energy_input_ratio_function_of_temperature_curve_name, var_speed_7_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_gross_rated_total_cooling_capacity, var_speed_8_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_gross_rated_sensible_heat_ratio, var_speed_8_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_gross_rated_cooling_cop, var_speed_8_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_rated_air_flow_rate, var_speed_8_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_condenser_air_flow_rate, var_speed_8_reference_unit_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_total_cooling_capacity_function_of_temperature_curve_name, var_speed_8_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_energy_input_ratio_function_of_temperature_curve_name, var_speed_8_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_gross_rated_total_cooling_capacity, var_speed_9_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_gross_rated_sensible_heat_ratio, var_speed_9_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_gross_rated_cooling_cop, var_speed_9_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_rated_air_flow_rate, var_speed_9_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_condenser_air_flow_rate, var_speed_9_reference_unit_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_total_cooling_capacity_function_of_temperature_curve_name, var_speed_9_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_energy_input_ratio_function_of_temperature_curve_name, var_speed_9_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_gross_rated_total_cooling_capacity, var_speed_10_reference_unit_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_gross_rated_sensible_heat_ratio, var_speed_10_reference_unit_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_gross_rated_cooling_cop, var_speed_10_reference_unit_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_rated_air_flow_rate, var_speed_10_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_condenser_air_flow_rate, var_speed_10_reference_unit_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling, var_speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_total_cooling_capacity_function_of_temperature_curve_name, var_speed_10_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name, var_speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_energy_input_ratio_function_of_temperature_curve_name, var_speed_10_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablespeeds[0].speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name)