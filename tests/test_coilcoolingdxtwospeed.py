import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxTwoSpeed

log = logging.getLogger(__name__)

class TestCoilCoolingDxTwoSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxtwospeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxTwoSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_high_speed_gross_rated_total_cooling_capacity = 0.0001
        obj.high_speed_gross_rated_total_cooling_capacity = var_high_speed_gross_rated_total_cooling_capacity
        # real
        var_high_speed_rated_sensible_heat_ratio = 0.75
        obj.high_speed_rated_sensible_heat_ratio = var_high_speed_rated_sensible_heat_ratio
        # real
        var_high_speed_gross_rated_cooling_cop = 0.0001
        obj.high_speed_gross_rated_cooling_cop = var_high_speed_gross_rated_cooling_cop
        # real
        var_high_speed_rated_air_flow_rate = 0.0001
        obj.high_speed_rated_air_flow_rate = var_high_speed_rated_air_flow_rate
        # real
        var_unit_internal_static_air_pressure = 0.0001
        obj.unit_internal_static_air_pressure = var_unit_internal_static_air_pressure
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
        var_low_speed_gross_rated_total_cooling_capacity = 0.0001
        obj.low_speed_gross_rated_total_cooling_capacity = var_low_speed_gross_rated_total_cooling_capacity
        # real
        var_low_speed_gross_rated_sensible_heat_ratio = 0.75
        obj.low_speed_gross_rated_sensible_heat_ratio = var_low_speed_gross_rated_sensible_heat_ratio
        # real
        var_low_speed_gross_rated_cooling_cop = 0.0001
        obj.low_speed_gross_rated_cooling_cop = var_low_speed_gross_rated_cooling_cop
        # real
        var_low_speed_rated_air_flow_rate = 0.0001
        obj.low_speed_rated_air_flow_rate = var_low_speed_rated_air_flow_rate
        # object-list
        var_low_speed_total_cooling_capacity_function_of_temperature_curve_name = "object-list|Low Speed Total Cooling Capacity Function of Temperature Curve Name"
        obj.low_speed_total_cooling_capacity_function_of_temperature_curve_name = var_low_speed_total_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_low_speed_energy_input_ratio_function_of_temperature_curve_name = "object-list|Low Speed Energy Input Ratio Function of Temperature Curve Name"
        obj.low_speed_energy_input_ratio_function_of_temperature_curve_name = var_low_speed_energy_input_ratio_function_of_temperature_curve_name
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_high_speed_evaporative_condenser_effectiveness = 0.5
        obj.high_speed_evaporative_condenser_effectiveness = var_high_speed_evaporative_condenser_effectiveness
        # real
        var_high_speed_evaporative_condenser_air_flow_rate = 0.0001
        obj.high_speed_evaporative_condenser_air_flow_rate = var_high_speed_evaporative_condenser_air_flow_rate
        # real
        var_high_speed_evaporative_condenser_pump_rated_power_consumption = 0.0
        obj.high_speed_evaporative_condenser_pump_rated_power_consumption = var_high_speed_evaporative_condenser_pump_rated_power_consumption
        # real
        var_low_speed_evaporative_condenser_effectiveness = 0.5
        obj.low_speed_evaporative_condenser_effectiveness = var_low_speed_evaporative_condenser_effectiveness
        # real
        var_low_speed_evaporative_condenser_air_flow_rate = 0.0001
        obj.low_speed_evaporative_condenser_air_flow_rate = var_low_speed_evaporative_condenser_air_flow_rate
        # real
        var_low_speed_evaporative_condenser_pump_rated_power_consumption = 0.0
        obj.low_speed_evaporative_condenser_pump_rated_power_consumption = var_low_speed_evaporative_condenser_pump_rated_power_consumption
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
        # object-list
        var_low_speed_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Low Speed Sensible Heat Ratio Function of Temperature Curve Name"
        obj.low_speed_sensible_heat_ratio_function_of_temperature_curve_name = var_low_speed_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Low Speed Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name = var_low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name
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
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_gross_rated_total_cooling_capacity, var_high_speed_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_rated_sensible_heat_ratio, var_high_speed_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_gross_rated_cooling_cop, var_high_speed_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_rated_air_flow_rate, var_high_speed_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].unit_internal_static_air_pressure, var_unit_internal_static_air_pressure)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].total_cooling_capacity_function_of_temperature_curve_name, var_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].total_cooling_capacity_function_of_flow_fraction_curve_name, var_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].energy_input_ratio_function_of_temperature_curve_name, var_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].energy_input_ratio_function_of_flow_fraction_curve_name, var_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_gross_rated_total_cooling_capacity, var_low_speed_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_gross_rated_sensible_heat_ratio, var_low_speed_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_gross_rated_cooling_cop, var_low_speed_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_rated_air_flow_rate, var_low_speed_rated_air_flow_rate)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_total_cooling_capacity_function_of_temperature_curve_name, var_low_speed_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_energy_input_ratio_function_of_temperature_curve_name, var_low_speed_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_evaporative_condenser_effectiveness, var_high_speed_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_evaporative_condenser_air_flow_rate, var_high_speed_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].high_speed_evaporative_condenser_pump_rated_power_consumption, var_high_speed_evaporative_condenser_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_evaporative_condenser_effectiveness, var_low_speed_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_evaporative_condenser_air_flow_rate, var_low_speed_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_evaporative_condenser_pump_rated_power_consumption, var_low_speed_evaporative_condenser_pump_rated_power_consumption)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxtwospeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].sensible_heat_ratio_function_of_temperature_curve_name, var_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].sensible_heat_ratio_function_of_flow_fraction_curve_name, var_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_sensible_heat_ratio_function_of_temperature_curve_name, var_low_speed_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name, var_low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxtwospeeds[0].zone_name_for_condenser_placement, var_zone_name_for_condenser_placement)