import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingDxSingleSpeed

log = logging.getLogger(__name__)

class TestCoilHeatingDxSingleSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdxsinglespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDxSingleSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_gross_rated_heating_capacity = 0.0001
        obj.gross_rated_heating_capacity = var_gross_rated_heating_capacity
        # real
        var_gross_rated_heating_cop = 0.0001
        obj.gross_rated_heating_cop = var_gross_rated_heating_cop
        # real
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # real
        var_rated_supply_fan_power_per_volume_flow_rate = 625.0
        obj.rated_supply_fan_power_per_volume_flow_rate = var_rated_supply_fan_power_per_volume_flow_rate
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_heating_capacity_function_of_temperature_curve_name = "object-list|Heating Capacity Function of Temperature Curve Name"
        obj.heating_capacity_function_of_temperature_curve_name = var_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_heating_capacity_function_of_flow_fraction_curve_name = "object-list|Heating Capacity Function of Flow Fraction Curve Name"
        obj.heating_capacity_function_of_flow_fraction_curve_name = var_heating_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_energy_input_ratio_function_of_temperature_curve_name = "object-list|Energy Input Ratio Function of Temperature Curve Name"
        obj.energy_input_ratio_function_of_temperature_curve_name = var_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.energy_input_ratio_function_of_flow_fraction_curve_name = var_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name
        # object-list
        var_defrost_energy_input_ratio_function_of_temperature_curve_name = "object-list|Defrost Energy Input Ratio Function of Temperature Curve Name"
        obj.defrost_energy_input_ratio_function_of_temperature_curve_name = var_defrost_energy_input_ratio_function_of_temperature_curve_name
        # real
        var_minimum_outdoor_drybulb_temperature_for_compressor_operation = -20.0
        obj.minimum_outdoor_drybulb_temperature_for_compressor_operation = var_minimum_outdoor_drybulb_temperature_for_compressor_operation
        # real
        var_outdoor_drybulb_temperature_to_turn_on_compressor = 16.16
        obj.outdoor_drybulb_temperature_to_turn_on_compressor = var_outdoor_drybulb_temperature_to_turn_on_compressor
        # real
        var_maximum_outdoor_drybulb_temperature_for_defrost_operation = 3.61
        obj.maximum_outdoor_drybulb_temperature_for_defrost_operation = var_maximum_outdoor_drybulb_temperature_for_defrost_operation
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation
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
        # integer
        var_region_number_for_calculating_hspf = 3
        obj.region_number_for_calculating_hspf = var_region_number_for_calculating_hspf
        # node
        var_evaporator_air_inlet_node_name = "node|Evaporator Air Inlet Node Name"
        obj.evaporator_air_inlet_node_name = var_evaporator_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].name, var_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].gross_rated_heating_capacity, var_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].gross_rated_heating_cop, var_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].rated_supply_fan_power_per_volume_flow_rate, var_rated_supply_fan_power_per_volume_flow_rate)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].heating_capacity_function_of_temperature_curve_name, var_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].heating_capacity_function_of_flow_fraction_curve_name, var_heating_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].energy_input_ratio_function_of_temperature_curve_name, var_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].energy_input_ratio_function_of_flow_fraction_curve_name, var_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].defrost_energy_input_ratio_function_of_temperature_curve_name, var_defrost_energy_input_ratio_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].minimum_outdoor_drybulb_temperature_for_compressor_operation, var_minimum_outdoor_drybulb_temperature_for_compressor_operation)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].outdoor_drybulb_temperature_to_turn_on_compressor, var_outdoor_drybulb_temperature_to_turn_on_compressor)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].defrost_control, var_defrost_control)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.coilheatingdxsinglespeeds[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].region_number_for_calculating_hspf, var_region_number_for_calculating_hspf)
        self.assertEqual(idf2.coilheatingdxsinglespeeds[0].evaporator_air_inlet_node_name, var_evaporator_air_inlet_node_name)