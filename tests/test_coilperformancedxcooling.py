import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilPerformanceDxCooling

log = logging.getLogger(__name__)

class TestCoilPerformanceDxCooling(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilperformancedxcooling(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilPerformanceDxCooling()
        # alpha
        var_name = "Name"
        obj.name = var_name
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
        var_fraction_of_air_flow_bypassed_around_coil = 0.49995
        obj.fraction_of_air_flow_bypassed_around_coil = var_fraction_of_air_flow_bypassed_around_coil
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
        # object-list
        var_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Sensible Heat Ratio Function of Temperature Curve Name"
        obj.sensible_heat_ratio_function_of_temperature_curve_name = var_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.sensible_heat_ratio_function_of_flow_fraction_curve_name = var_sensible_heat_ratio_function_of_flow_fraction_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilperformancedxcoolings[0].name, var_name)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].gross_rated_sensible_heat_ratio, var_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].gross_rated_cooling_cop, var_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].fraction_of_air_flow_bypassed_around_coil, var_fraction_of_air_flow_bypassed_around_coil)
        self.assertEqual(idf2.coilperformancedxcoolings[0].total_cooling_capacity_function_of_temperature_curve_name, var_total_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].total_cooling_capacity_function_of_flow_fraction_curve_name, var_total_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].energy_input_ratio_function_of_temperature_curve_name, var_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].energy_input_ratio_function_of_flow_fraction_curve_name, var_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].nominal_time_for_condensate_removal_to_begin, var_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].maximum_cycling_rate, var_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].latent_capacity_time_constant, var_latent_capacity_time_constant)
        self.assertEqual(idf2.coilperformancedxcoolings[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].evaporative_condenser_air_flow_rate, var_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.coilperformancedxcoolings[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertEqual(idf2.coilperformancedxcoolings[0].sensible_heat_ratio_function_of_temperature_curve_name, var_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilperformancedxcoolings[0].sensible_heat_ratio_function_of_flow_fraction_curve_name, var_sensible_heat_ratio_function_of_flow_fraction_curve_name)