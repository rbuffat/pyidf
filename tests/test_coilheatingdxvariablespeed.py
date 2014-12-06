import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilHeatingDxVariableSpeed
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilHeatingDxVariableSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdxvariablespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDxVariableSpeed()
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
        var_rated_heating_capacity_at_selected_nominal_speed_level = 6.6
        obj.rated_heating_capacity_at_selected_nominal_speed_level = var_rated_heating_capacity_at_selected_nominal_speed_level
        # real
        var_rated_air_flow_rate_at_selected_nominal_speed_level = 7.7
        obj.rated_air_flow_rate_at_selected_nominal_speed_level = var_rated_air_flow_rate_at_selected_nominal_speed_level
        # object-list
        var_energy_part_load_fraction_curve_name = "object-list|Energy Part Load Fraction Curve Name"
        obj.energy_part_load_fraction_curve_name = var_energy_part_load_fraction_curve_name
        # object-list
        var_defrost_energy_input_ratio_function_of_temperature_curve_name = "object-list|Defrost Energy Input Ratio Function of Temperature Curve Name"
        obj.defrost_energy_input_ratio_function_of_temperature_curve_name = var_defrost_energy_input_ratio_function_of_temperature_curve_name
        # real
        var_minimum_outdoor_drybulb_temperature_for_compressor_operation = -50.0
        obj.minimum_outdoor_drybulb_temperature_for_compressor_operation = var_minimum_outdoor_drybulb_temperature_for_compressor_operation
        # real
        var_outdoor_drybulb_temperature_to_turn_on_compressor = 11.11
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
        # real
        var_speed_1_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_1_reference_unit_gross_rated_heating_capacity = var_speed_1_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_1_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_1_reference_unit_gross_rated_heating_cop = var_speed_1_reference_unit_gross_rated_heating_cop
        # real
        var_speed_1_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_air_flow_rate = var_speed_1_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_1_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Heating Capacity Function of Temperature Curve Name"
        obj.speed_1_heating_capacity_function_of_temperature_curve_name = var_speed_1_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Total  Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_1_energy_input_ratio_function_of_temperature_curve_name = var_speed_1_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_2_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_2_reference_unit_gross_rated_heating_capacity = var_speed_2_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_2_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_2_reference_unit_gross_rated_heating_cop = var_speed_2_reference_unit_gross_rated_heating_cop
        # real
        var_speed_2_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_air_flow_rate = var_speed_2_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_2_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Heating Capacity Function of Temperature Curve Name"
        obj.speed_2_heating_capacity_function_of_temperature_curve_name = var_speed_2_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Total  Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_2_energy_input_ratio_function_of_temperature_curve_name = var_speed_2_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_3_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_3_reference_unit_gross_rated_heating_capacity = var_speed_3_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_3_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_3_reference_unit_gross_rated_heating_cop = var_speed_3_reference_unit_gross_rated_heating_cop
        # real
        var_speed_3_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_air_flow_rate = var_speed_3_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_3_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Heating Capacity Function of Temperature Curve Name"
        obj.speed_3_heating_capacity_function_of_temperature_curve_name = var_speed_3_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Total  Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_3_energy_input_ratio_function_of_temperature_curve_name = var_speed_3_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_4_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_4_reference_unit_gross_rated_heating_capacity = var_speed_4_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_4_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_4_reference_unit_gross_rated_heating_cop = var_speed_4_reference_unit_gross_rated_heating_cop
        # real
        var_speed_4_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_air_flow_rate = var_speed_4_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_4_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Heating Capacity Function of Temperature Curve Name"
        obj.speed_4_heating_capacity_function_of_temperature_curve_name = var_speed_4_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_4_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_4_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_4_energy_input_ratio_function_of_temperature_curve_name = var_speed_4_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_5_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_5_reference_unit_gross_rated_heating_capacity = var_speed_5_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_5_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_5_reference_unit_gross_rated_heating_cop = var_speed_5_reference_unit_gross_rated_heating_cop
        # real
        var_speed_5_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_air_flow_rate = var_speed_5_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_5_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 5 Heating Capacity Function of Temperature Curve Name"
        obj.speed_5_heating_capacity_function_of_temperature_curve_name = var_speed_5_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_5_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_5_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_5_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_5_energy_input_ratio_function_of_temperature_curve_name = var_speed_5_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_6_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_6_reference_unit_gross_rated_heating_capacity = var_speed_6_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_6_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_6_reference_unit_gross_rated_heating_cop = var_speed_6_reference_unit_gross_rated_heating_cop
        # real
        var_speed_6_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_air_flow_rate = var_speed_6_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_6_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 6 Heating Capacity Function of Temperature Curve Name"
        obj.speed_6_heating_capacity_function_of_temperature_curve_name = var_speed_6_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_6_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_6_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_6_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_6_energy_input_ratio_function_of_temperature_curve_name = var_speed_6_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_7_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_7_reference_unit_gross_rated_heating_capacity = var_speed_7_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_7_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_7_reference_unit_gross_rated_heating_cop = var_speed_7_reference_unit_gross_rated_heating_cop
        # real
        var_speed_7_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_air_flow_rate = var_speed_7_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_7_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 7 Heating Capacity Function of Temperature Curve Name"
        obj.speed_7_heating_capacity_function_of_temperature_curve_name = var_speed_7_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_7_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_7_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_7_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_7_energy_input_ratio_function_of_temperature_curve_name = var_speed_7_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_8_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_8_reference_unit_gross_rated_heating_capacity = var_speed_8_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_8_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_8_reference_unit_gross_rated_heating_cop = var_speed_8_reference_unit_gross_rated_heating_cop
        # real
        var_speed_8_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_air_flow_rate = var_speed_8_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_8_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 8 Heating Capacity Function of Temperature Curve Name"
        obj.speed_8_heating_capacity_function_of_temperature_curve_name = var_speed_8_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_8_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_8_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_8_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_8_energy_input_ratio_function_of_temperature_curve_name = var_speed_8_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_9_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_9_reference_unit_gross_rated_heating_capacity = var_speed_9_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_9_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_9_reference_unit_gross_rated_heating_cop = var_speed_9_reference_unit_gross_rated_heating_cop
        # real
        var_speed_9_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_air_flow_rate = var_speed_9_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_9_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 9 Heating Capacity Function of Temperature Curve Name"
        obj.speed_9_heating_capacity_function_of_temperature_curve_name = var_speed_9_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_9_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_9_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_9_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_temperature_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Temperature Curve Name"
        obj.speed_9_energy_input_ratio_function_of_temperature_curve_name = var_speed_9_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Energy Input Ratio Function of Air Flow Fraction Curve Name"
        obj.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name = var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        # real
        var_speed_10_reference_unit_gross_rated_heating_capacity = 0.0
        obj.speed_10_reference_unit_gross_rated_heating_capacity = var_speed_10_reference_unit_gross_rated_heating_capacity
        # real
        var_speed_10_reference_unit_gross_rated_heating_cop = 0.0
        obj.speed_10_reference_unit_gross_rated_heating_cop = var_speed_10_reference_unit_gross_rated_heating_cop
        # real
        var_speed_10_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_air_flow_rate = var_speed_10_reference_unit_rated_air_flow_rate
        # object-list
        var_speed_10_heating_capacity_function_of_temperature_curve_name = "object-list|Speed 10 Heating Capacity Function of Temperature Curve Name"
        obj.speed_10_heating_capacity_function_of_temperature_curve_name = var_speed_10_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_10_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_10_heating_capacity_function_of_air_flow_fraction_curve_name = var_speed_10_heating_capacity_function_of_air_flow_fraction_curve_name
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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].name, var_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].indoor_air_inlet_node_name, var_indoor_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].indoor_air_outlet_node_name, var_indoor_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].number_of_speeds, var_number_of_speeds)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].nominal_speed_level, var_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].rated_heating_capacity_at_selected_nominal_speed_level, var_rated_heating_capacity_at_selected_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].rated_air_flow_rate_at_selected_nominal_speed_level, var_rated_air_flow_rate_at_selected_nominal_speed_level)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].energy_part_load_fraction_curve_name, var_energy_part_load_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].defrost_energy_input_ratio_function_of_temperature_curve_name, var_defrost_energy_input_ratio_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].minimum_outdoor_drybulb_temperature_for_compressor_operation, var_minimum_outdoor_drybulb_temperature_for_compressor_operation)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].outdoor_drybulb_temperature_to_turn_on_compressor, var_outdoor_drybulb_temperature_to_turn_on_compressor)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].maximum_outdoor_drybulb_temperature_for_defrost_operation, var_maximum_outdoor_drybulb_temperature_for_defrost_operation)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].defrost_strategy, var_defrost_strategy)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].defrost_control, var_defrost_control)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].defrost_time_period_fraction, var_defrost_time_period_fraction)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].resistive_defrost_heater_capacity, var_resistive_defrost_heater_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_reference_unit_gross_rated_heating_capacity, var_speed_1_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_reference_unit_gross_rated_heating_cop, var_speed_1_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_reference_unit_rated_air_flow_rate, var_speed_1_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_heating_capacity_function_of_temperature_curve_name, var_speed_1_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_energy_input_ratio_function_of_temperature_curve_name, var_speed_1_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_reference_unit_gross_rated_heating_capacity, var_speed_2_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_reference_unit_gross_rated_heating_cop, var_speed_2_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_reference_unit_rated_air_flow_rate, var_speed_2_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_heating_capacity_function_of_temperature_curve_name, var_speed_2_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_energy_input_ratio_function_of_temperature_curve_name, var_speed_2_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_reference_unit_gross_rated_heating_capacity, var_speed_3_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_reference_unit_gross_rated_heating_cop, var_speed_3_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_reference_unit_rated_air_flow_rate, var_speed_3_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_heating_capacity_function_of_temperature_curve_name, var_speed_3_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_energy_input_ratio_function_of_temperature_curve_name, var_speed_3_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_reference_unit_gross_rated_heating_capacity, var_speed_4_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_reference_unit_gross_rated_heating_cop, var_speed_4_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_reference_unit_rated_air_flow_rate, var_speed_4_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_heating_capacity_function_of_temperature_curve_name, var_speed_4_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_4_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_energy_input_ratio_function_of_temperature_curve_name, var_speed_4_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_reference_unit_gross_rated_heating_capacity, var_speed_5_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_reference_unit_gross_rated_heating_cop, var_speed_5_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_reference_unit_rated_air_flow_rate, var_speed_5_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_heating_capacity_function_of_temperature_curve_name, var_speed_5_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_5_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_energy_input_ratio_function_of_temperature_curve_name, var_speed_5_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_reference_unit_gross_rated_heating_capacity, var_speed_6_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_reference_unit_gross_rated_heating_cop, var_speed_6_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_reference_unit_rated_air_flow_rate, var_speed_6_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_heating_capacity_function_of_temperature_curve_name, var_speed_6_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_6_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_energy_input_ratio_function_of_temperature_curve_name, var_speed_6_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_reference_unit_gross_rated_heating_capacity, var_speed_7_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_reference_unit_gross_rated_heating_cop, var_speed_7_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_reference_unit_rated_air_flow_rate, var_speed_7_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_heating_capacity_function_of_temperature_curve_name, var_speed_7_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_7_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_energy_input_ratio_function_of_temperature_curve_name, var_speed_7_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_reference_unit_gross_rated_heating_capacity, var_speed_8_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_reference_unit_gross_rated_heating_cop, var_speed_8_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_reference_unit_rated_air_flow_rate, var_speed_8_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_heating_capacity_function_of_temperature_curve_name, var_speed_8_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_8_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_energy_input_ratio_function_of_temperature_curve_name, var_speed_8_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_reference_unit_gross_rated_heating_capacity, var_speed_9_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_reference_unit_gross_rated_heating_cop, var_speed_9_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_reference_unit_rated_air_flow_rate, var_speed_9_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_heating_capacity_function_of_temperature_curve_name, var_speed_9_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_9_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_energy_input_ratio_function_of_temperature_curve_name, var_speed_9_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_reference_unit_gross_rated_heating_capacity, var_speed_10_reference_unit_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_reference_unit_gross_rated_heating_cop, var_speed_10_reference_unit_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_reference_unit_rated_air_flow_rate, var_speed_10_reference_unit_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_heating_capacity_function_of_temperature_curve_name, var_speed_10_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_heating_capacity_function_of_air_flow_fraction_curve_name, var_speed_10_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_energy_input_ratio_function_of_temperature_curve_name, var_speed_10_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablespeeds[0].speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name, var_speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name)