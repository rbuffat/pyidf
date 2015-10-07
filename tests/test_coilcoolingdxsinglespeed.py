import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxSingleSpeed

log = logging.getLogger(__name__)

class TestCoilCoolingDxSingleSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxsinglespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxSingleSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_gross_rated_total_cooling_capacity = 0.0001
        obj.gross_rated_total_cooling_capacity = var_gross_rated_total_cooling_capacity
        # real
        var_gross_rated_sensible_heat_ratio = 0.75
        obj.gross_rated_sensible_heat_ratio = var_gross_rated_sensible_heat_ratio
        # real
        var_gross_rated_cooling_cop = 0.0001
        obj.gross_rated_cooling_cop = var_gross_rated_cooling_cop
        # real
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # real
        var_rated_evaporator_fan_power_per_volume_flow_rate = 625.0
        obj.rated_evaporator_fan_power_per_volume_flow_rate = var_rated_evaporator_fan_power_per_volume_flow_rate
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Total Cooling Capacity Function of Temperature Curve Name"
        obj.total_cooling_capacity_function_of_temperature_curve_name = var_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_total_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Total Cooling Capacity Function of Flow Fraction Curve Name"
        obj.total_cooling_capacity_function_of_flow_fraction_curve_name = var_total_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_energy_input_ratio_function_of_temperature_curve_name = "object-list|Energy Input Ratio Function of Temperature Curve Name"
        obj.energy_input_ratio_function_of_temperature_curve_name = var_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.energy_input_ratio_function_of_flow_fraction_curve_name = var_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name
        # real
        var_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.nominal_time_for_condensate_removal_to_begin = var_nominal_time_for_condensate_removal_to_begin
        # real
        var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_maximum_cycling_rate = 2.5
        obj.maximum_cycling_rate = var_maximum_cycling_rate
        # real
        var_latent_capacity_time_constant = 250.0
        obj.latent_capacity_time_constant = var_latent_capacity_time_constant
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
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
        # object-list
        var_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Sensible Heat Ratio Function of Temperature Curve Name"
        obj.sensible_heat_ratio_function_of_temperature_curve_name = var_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.sensible_heat_ratio_function_of_flow_fraction_curve_name = var_sensible_heat_ratio_function_of_flow_fraction_curve_name
        # alpha
        var_report_ashrae_standard_127_performance_ratings = "Yes"
        obj.report_ashrae_standard_127_performance_ratings = var_report_ashrae_standard_127_performance_ratings
        # object-list
        var_zone_name_for_condenser_placement = "object-list|Zone Name for Condenser Placement"
        obj.zone_name_for_condenser_placement = var_zone_name_for_condenser_placement

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].gross_rated_sensible_heat_ratio, var_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].gross_rated_cooling_cop, var_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].rated_evaporator_fan_power_per_volume_flow_rate, var_rated_evaporator_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].total_cooling_capacity_function_of_temperature_curve_name, var_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].total_cooling_capacity_function_of_flow_fraction_curve_name, var_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].energy_input_ratio_function_of_temperature_curve_name, var_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].energy_input_ratio_function_of_flow_fraction_curve_name, var_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].nominal_time_for_condensate_removal_to_begin, var_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].maximum_cycling_rate, var_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].latent_capacity_time_constant, var_latent_capacity_time_constant)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].evaporative_condenser_air_flow_rate, var_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].sensible_heat_ratio_function_of_temperature_curve_name, var_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].sensible_heat_ratio_function_of_flow_fraction_curve_name, var_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].report_ashrae_standard_127_performance_ratings, var_report_ashrae_standard_127_performance_ratings)
        self.assertEqual(idf2.coilcoolingdxsinglespeeds[0].zone_name_for_condenser_placement, var_zone_name_for_condenser_placement)