import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilWaterHeatingAirToWaterHeatPumpVariableSpeed

log = logging.getLogger(__name__)

class TestCoilWaterHeatingAirToWaterHeatPumpVariableSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilwaterheatingairtowaterheatpumpvariablespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilWaterHeatingAirToWaterHeatPumpVariableSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_number_of_speeds = 5
        obj.number_of_speeds = var_number_of_speeds
        # integer
        var_nominal_speed_level = 3
        obj.nominal_speed_level = var_nominal_speed_level
        # real
        var_rated_water_heating_capacity = 0.0001
        obj.rated_water_heating_capacity = var_rated_water_heating_capacity
        # real
        var_rated_evaporator_inlet_air_drybulb_temperature = 5.0001
        obj.rated_evaporator_inlet_air_drybulb_temperature = var_rated_evaporator_inlet_air_drybulb_temperature
        # real
        var_rated_evaporator_inlet_air_wetbulb_temperature = 5.0001
        obj.rated_evaporator_inlet_air_wetbulb_temperature = var_rated_evaporator_inlet_air_wetbulb_temperature
        # real
        var_rated_condenser_inlet_water_temperature = 25.0001
        obj.rated_condenser_inlet_water_temperature = var_rated_condenser_inlet_water_temperature
        # real
        var_rated_evaporator_air_flow_rate = 0.0001
        obj.rated_evaporator_air_flow_rate = var_rated_evaporator_air_flow_rate
        # real
        var_rated_condenser_water_flow_rate = 0.0001
        obj.rated_condenser_water_flow_rate = var_rated_condenser_water_flow_rate
        # alpha
        var_evaporator_fan_power_included_in_rated_cop = "Yes"
        obj.evaporator_fan_power_included_in_rated_cop = var_evaporator_fan_power_included_in_rated_cop
        # alpha
        var_condenser_pump_power_included_in_rated_cop = "Yes"
        obj.condenser_pump_power_included_in_rated_cop = var_condenser_pump_power_included_in_rated_cop
        # alpha
        var_condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop = "Yes"
        obj.condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop = var_condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop
        # real
        var_fraction_of_condenser_pump_heat_to_water = 0.5
        obj.fraction_of_condenser_pump_heat_to_water = var_fraction_of_condenser_pump_heat_to_water
        # node
        var_evaporator_air_inlet_node_name = "node|Evaporator Air Inlet Node Name"
        obj.evaporator_air_inlet_node_name = var_evaporator_air_inlet_node_name
        # node
        var_evaporator_air_outlet_node_name = "node|Evaporator Air Outlet Node Name"
        obj.evaporator_air_outlet_node_name = var_evaporator_air_outlet_node_name
        # node
        var_condenser_water_inlet_node_name = "node|Condenser Water Inlet Node Name"
        obj.condenser_water_inlet_node_name = var_condenser_water_inlet_node_name
        # node
        var_condenser_water_outlet_node_name = "node|Condenser Water Outlet Node Name"
        obj.condenser_water_outlet_node_name = var_condenser_water_outlet_node_name
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_ambient_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_ambient_temperature_for_crankcase_heater_operation = var_maximum_ambient_temperature_for_crankcase_heater_operation
        # alpha
        var_evaporator_air_temperature_type_for_curve_objects = "DryBulbTemperature"
        obj.evaporator_air_temperature_type_for_curve_objects = var_evaporator_air_temperature_type_for_curve_objects
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_1 = 0.0001
        obj.rated_water_heating_capacity_at_speed_1 = var_rated_water_heating_capacity_at_speed_1
        # real
        var_rated_water_heating_cop_at_speed_1 = 0.0001
        obj.rated_water_heating_cop_at_speed_1 = var_rated_water_heating_cop_at_speed_1
        # real
        var_rated_sensible_heat_ratio_at_speed_1 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_1 = var_rated_sensible_heat_ratio_at_speed_1
        # real
        var_speed_1_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_air_flow_rate = var_speed_1_reference_unit_rated_air_flow_rate
        # real
        var_speed_1_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_1_reference_unit_rated_water_flow_rate = var_speed_1_reference_unit_rated_water_flow_rate
        # real
        var_speed_1_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_1_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_1_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_1_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 1 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_1_total_wh_capacity_function_of_temperature_curve_name = var_speed_1_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 1 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_1_cop_function_of_temperature_curve_name = "object-list|Speed 1 COP Function of Temperature Curve Name"
        obj.speed_1_cop_function_of_temperature_curve_name = var_speed_1_cop_function_of_temperature_curve_name
        # object-list
        var_speed_1_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 1 COP Function of Air Flow Fraction Curve Name"
        obj.speed_1_cop_function_of_air_flow_fraction_curve_name = var_speed_1_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_1_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 1 COP Function of Water Flow Fraction Curve Name"
        obj.speed_1_cop_function_of_water_flow_fraction_curve_name = var_speed_1_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_2 = 0.0001
        obj.rated_water_heating_capacity_at_speed_2 = var_rated_water_heating_capacity_at_speed_2
        # real
        var_rated_water_heating_cop_at_speed_2 = 0.0001
        obj.rated_water_heating_cop_at_speed_2 = var_rated_water_heating_cop_at_speed_2
        # real
        var_rated_sensible_heat_ratio_at_speed_2 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_2 = var_rated_sensible_heat_ratio_at_speed_2
        # real
        var_speed_2_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_air_flow_rate = var_speed_2_reference_unit_rated_air_flow_rate
        # real
        var_speed_2_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_2_reference_unit_rated_water_flow_rate = var_speed_2_reference_unit_rated_water_flow_rate
        # real
        var_speed_2_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_2_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_2_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_2_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 2 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_2_total_wh_capacity_function_of_temperature_curve_name = var_speed_2_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 2 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_2_cop_function_of_temperature_curve_name = "object-list|Speed 2 COP Function of Temperature Curve Name"
        obj.speed_2_cop_function_of_temperature_curve_name = var_speed_2_cop_function_of_temperature_curve_name
        # object-list
        var_speed_2_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 2 COP Function of Air Flow Fraction Curve Name"
        obj.speed_2_cop_function_of_air_flow_fraction_curve_name = var_speed_2_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_2_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 2 COP Function of Water Flow Fraction Curve Name"
        obj.speed_2_cop_function_of_water_flow_fraction_curve_name = var_speed_2_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_3 = 0.0001
        obj.rated_water_heating_capacity_at_speed_3 = var_rated_water_heating_capacity_at_speed_3
        # real
        var_rated_water_heating_cop_at_speed_3 = 0.0001
        obj.rated_water_heating_cop_at_speed_3 = var_rated_water_heating_cop_at_speed_3
        # real
        var_rated_sensible_heat_ratio_at_speed_3 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_3 = var_rated_sensible_heat_ratio_at_speed_3
        # real
        var_speed_3_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_air_flow_rate = var_speed_3_reference_unit_rated_air_flow_rate
        # real
        var_speed_3_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_3_reference_unit_rated_water_flow_rate = var_speed_3_reference_unit_rated_water_flow_rate
        # real
        var_speed_3_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_3_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_3_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_3_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 3 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_3_total_wh_capacity_function_of_temperature_curve_name = var_speed_3_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 3 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_3_cop_function_of_temperature_curve_name = "object-list|Speed 3 COP Function of Temperature Curve Name"
        obj.speed_3_cop_function_of_temperature_curve_name = var_speed_3_cop_function_of_temperature_curve_name
        # object-list
        var_speed_3_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 3 COP Function of Air Flow Fraction Curve Name"
        obj.speed_3_cop_function_of_air_flow_fraction_curve_name = var_speed_3_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_3_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 3 COP Function of Water Flow Fraction Curve Name"
        obj.speed_3_cop_function_of_water_flow_fraction_curve_name = var_speed_3_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_4 = 0.0001
        obj.rated_water_heating_capacity_at_speed_4 = var_rated_water_heating_capacity_at_speed_4
        # real
        var_rated_water_heating_cop_at_speed_4 = 0.0001
        obj.rated_water_heating_cop_at_speed_4 = var_rated_water_heating_cop_at_speed_4
        # real
        var_rated_sensible_heat_ratio_at_speed_4 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_4 = var_rated_sensible_heat_ratio_at_speed_4
        # real
        var_speed_4_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_air_flow_rate = var_speed_4_reference_unit_rated_air_flow_rate
        # real
        var_speed_4_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_4_reference_unit_rated_water_flow_rate = var_speed_4_reference_unit_rated_water_flow_rate
        # real
        var_speed_4_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_4_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_4_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_4_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 4 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_4_total_wh_capacity_function_of_temperature_curve_name = var_speed_4_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 4 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_4_cop_function_of_temperature_curve_name = "object-list|Speed 4 COP Function of Temperature Curve Name"
        obj.speed_4_cop_function_of_temperature_curve_name = var_speed_4_cop_function_of_temperature_curve_name
        # object-list
        var_speed_4_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 4 COP Function of Air Flow Fraction Curve Name"
        obj.speed_4_cop_function_of_air_flow_fraction_curve_name = var_speed_4_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_4_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 4 COP Function of Water Flow Fraction Curve Name"
        obj.speed_4_cop_function_of_water_flow_fraction_curve_name = var_speed_4_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_5 = 0.0001
        obj.rated_water_heating_capacity_at_speed_5 = var_rated_water_heating_capacity_at_speed_5
        # real
        var_rated_water_heating_cop_at_speed_5 = 0.0001
        obj.rated_water_heating_cop_at_speed_5 = var_rated_water_heating_cop_at_speed_5
        # real
        var_rated_sensible_heat_ratio_at_speed_5 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_5 = var_rated_sensible_heat_ratio_at_speed_5
        # real
        var_speed_5_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_air_flow_rate = var_speed_5_reference_unit_rated_air_flow_rate
        # real
        var_speed_5_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_5_reference_unit_rated_water_flow_rate = var_speed_5_reference_unit_rated_water_flow_rate
        # real
        var_speed_5_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_5_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_5_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_5_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 5 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_5_total_wh_capacity_function_of_temperature_curve_name = var_speed_5_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 5 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_5_cop_function_of_temperature_curve_name = "object-list|Speed 5 COP Function of Temperature Curve Name"
        obj.speed_5_cop_function_of_temperature_curve_name = var_speed_5_cop_function_of_temperature_curve_name
        # object-list
        var_speed_5_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 5 COP Function of Air Flow Fraction Curve Name"
        obj.speed_5_cop_function_of_air_flow_fraction_curve_name = var_speed_5_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_5_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 5 COP Function of Water Flow Fraction Curve Name"
        obj.speed_5_cop_function_of_water_flow_fraction_curve_name = var_speed_5_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_6 = 0.0001
        obj.rated_water_heating_capacity_at_speed_6 = var_rated_water_heating_capacity_at_speed_6
        # real
        var_rated_water_heating_cop_at_speed_6 = 0.0001
        obj.rated_water_heating_cop_at_speed_6 = var_rated_water_heating_cop_at_speed_6
        # real
        var_rated_sensible_heat_ratio_at_speed_6 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_6 = var_rated_sensible_heat_ratio_at_speed_6
        # real
        var_speed_6_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_air_flow_rate = var_speed_6_reference_unit_rated_air_flow_rate
        # real
        var_speed_6_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_6_reference_unit_rated_water_flow_rate = var_speed_6_reference_unit_rated_water_flow_rate
        # real
        var_speed_6_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_6_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_6_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_6_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 6 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_6_total_wh_capacity_function_of_temperature_curve_name = var_speed_6_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 6 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_6_cop_function_of_temperature_curve_name = "object-list|Speed 6 COP Function of Temperature Curve Name"
        obj.speed_6_cop_function_of_temperature_curve_name = var_speed_6_cop_function_of_temperature_curve_name
        # object-list
        var_speed_6_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 6 COP Function of Air Flow Fraction Curve Name"
        obj.speed_6_cop_function_of_air_flow_fraction_curve_name = var_speed_6_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_6_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 6 COP Function of Water Flow Fraction Curve Name"
        obj.speed_6_cop_function_of_water_flow_fraction_curve_name = var_speed_6_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_7 = 0.0001
        obj.rated_water_heating_capacity_at_speed_7 = var_rated_water_heating_capacity_at_speed_7
        # real
        var_rated_water_heating_cop_at_speed_7 = 0.0001
        obj.rated_water_heating_cop_at_speed_7 = var_rated_water_heating_cop_at_speed_7
        # real
        var_rated_sensible_heat_ratio_at_speed_7 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_7 = var_rated_sensible_heat_ratio_at_speed_7
        # real
        var_speed_7_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_air_flow_rate = var_speed_7_reference_unit_rated_air_flow_rate
        # real
        var_speed_7_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_7_reference_unit_rated_water_flow_rate = var_speed_7_reference_unit_rated_water_flow_rate
        # real
        var_speed_7_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_7_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_7_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_7_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 7 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_7_total_wh_capacity_function_of_temperature_curve_name = var_speed_7_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 7 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_7_cop_function_of_temperature_curve_name = "object-list|Speed 7 COP Function of Temperature Curve Name"
        obj.speed_7_cop_function_of_temperature_curve_name = var_speed_7_cop_function_of_temperature_curve_name
        # object-list
        var_speed_7_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 7 COP Function of Air Flow Fraction Curve Name"
        obj.speed_7_cop_function_of_air_flow_fraction_curve_name = var_speed_7_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_7_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 7 COP Function of Water Flow Fraction Curve Name"
        obj.speed_7_cop_function_of_water_flow_fraction_curve_name = var_speed_7_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_8 = 0.0001
        obj.rated_water_heating_capacity_at_speed_8 = var_rated_water_heating_capacity_at_speed_8
        # real
        var_rated_water_heating_cop_at_speed_8 = 0.0001
        obj.rated_water_heating_cop_at_speed_8 = var_rated_water_heating_cop_at_speed_8
        # real
        var_rated_sensible_heat_ratio_at_speed_8 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_8 = var_rated_sensible_heat_ratio_at_speed_8
        # real
        var_speed_8_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_air_flow_rate = var_speed_8_reference_unit_rated_air_flow_rate
        # real
        var_speed_8_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_8_reference_unit_rated_water_flow_rate = var_speed_8_reference_unit_rated_water_flow_rate
        # real
        var_speed_8_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_8_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_8_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_8_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 8 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_8_total_wh_capacity_function_of_temperature_curve_name = var_speed_8_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 8 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_8_cop_function_of_temperature_curve_name = "object-list|Speed 8 COP Function of Temperature Curve Name"
        obj.speed_8_cop_function_of_temperature_curve_name = var_speed_8_cop_function_of_temperature_curve_name
        # object-list
        var_speed_8_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 8 COP Function of Air Flow Fraction Curve Name"
        obj.speed_8_cop_function_of_air_flow_fraction_curve_name = var_speed_8_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_8_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 8 COP Function of Water Flow Fraction Curve Name"
        obj.speed_8_cop_function_of_water_flow_fraction_curve_name = var_speed_8_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_9 = 0.0001
        obj.rated_water_heating_capacity_at_speed_9 = var_rated_water_heating_capacity_at_speed_9
        # real
        var_rated_water_heating_cop_at_speed_9 = 0.0001
        obj.rated_water_heating_cop_at_speed_9 = var_rated_water_heating_cop_at_speed_9
        # real
        var_rated_sensible_heat_ratio_at_speed_9 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_9 = var_rated_sensible_heat_ratio_at_speed_9
        # real
        var_speed_9_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_air_flow_rate = var_speed_9_reference_unit_rated_air_flow_rate
        # real
        var_speed_9_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_9_reference_unit_rated_water_flow_rate = var_speed_9_reference_unit_rated_water_flow_rate
        # real
        var_speed_9_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_9_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_9_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_9_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 9 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_9_total_wh_capacity_function_of_temperature_curve_name = var_speed_9_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 9 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_9_cop_function_of_temperature_curve_name = "object-list|Speed 9 COP Function of Temperature Curve Name"
        obj.speed_9_cop_function_of_temperature_curve_name = var_speed_9_cop_function_of_temperature_curve_name
        # object-list
        var_speed_9_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 9 COP Function of Air Flow Fraction Curve Name"
        obj.speed_9_cop_function_of_air_flow_fraction_curve_name = var_speed_9_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_9_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 9 COP Function of Water Flow Fraction Curve Name"
        obj.speed_9_cop_function_of_water_flow_fraction_curve_name = var_speed_9_cop_function_of_water_flow_fraction_curve_name
        # real
        var_rated_water_heating_capacity_at_speed_10 = 0.0001
        obj.rated_water_heating_capacity_at_speed_10 = var_rated_water_heating_capacity_at_speed_10
        # real
        var_rated_water_heating_cop_at_speed_10 = 0.0001
        obj.rated_water_heating_cop_at_speed_10 = var_rated_water_heating_cop_at_speed_10
        # real
        var_rated_sensible_heat_ratio_at_speed_10 = 0.75
        obj.rated_sensible_heat_ratio_at_speed_10 = var_rated_sensible_heat_ratio_at_speed_10
        # real
        var_speed_10_reference_unit_rated_air_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_air_flow_rate = var_speed_10_reference_unit_rated_air_flow_rate
        # real
        var_speed_10_reference_unit_rated_water_flow_rate = 0.0
        obj.speed_10_reference_unit_rated_water_flow_rate = var_speed_10_reference_unit_rated_water_flow_rate
        # real
        var_speed_10_reference_unit_water_pump_input_power_at_rated_conditions = 0.0
        obj.speed_10_reference_unit_water_pump_input_power_at_rated_conditions = var_speed_10_reference_unit_water_pump_input_power_at_rated_conditions
        # object-list
        var_speed_10_total_wh_capacity_function_of_temperature_curve_name = "object-list|Speed 10 Total WH Capacity Function of Temperature Curve Name"
        obj.speed_10_total_wh_capacity_function_of_temperature_curve_name = var_speed_10_total_wh_capacity_function_of_temperature_curve_name
        # object-list
        var_speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 Total WH Capacity Function of Air Flow Fraction Curve Name"
        obj.speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name = var_speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name = "object-list|Speed 10 Total WH Capacity Function of Water Flow Fraction Curve Name"
        obj.speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name = var_speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name
        # object-list
        var_speed_10_cop_function_of_temperature_curve_name = "object-list|Speed 10 COP Function of Temperature Curve Name"
        obj.speed_10_cop_function_of_temperature_curve_name = var_speed_10_cop_function_of_temperature_curve_name
        # object-list
        var_speed_10_cop_function_of_air_flow_fraction_curve_name = "object-list|Speed 10 COP Function of Air Flow Fraction Curve Name"
        obj.speed_10_cop_function_of_air_flow_fraction_curve_name = var_speed_10_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_speed_10_cop_function_of_water_flow_fraction_curve_name = "object-list|Speed 10 COP Function of Water Flow Fraction Curve Name"
        obj.speed_10_cop_function_of_water_flow_fraction_curve_name = var_speed_10_cop_function_of_water_flow_fraction_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].name, var_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].number_of_speeds, var_number_of_speeds)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].nominal_speed_level, var_nominal_speed_level)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity, var_rated_water_heating_capacity)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_evaporator_inlet_air_drybulb_temperature, var_rated_evaporator_inlet_air_drybulb_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_evaporator_inlet_air_wetbulb_temperature, var_rated_evaporator_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_condenser_inlet_water_temperature, var_rated_condenser_inlet_water_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_evaporator_air_flow_rate, var_rated_evaporator_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_condenser_water_flow_rate, var_rated_condenser_water_flow_rate)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].evaporator_fan_power_included_in_rated_cop, var_evaporator_fan_power_included_in_rated_cop)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].condenser_pump_power_included_in_rated_cop, var_condenser_pump_power_included_in_rated_cop)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop, var_condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].fraction_of_condenser_pump_heat_to_water, var_fraction_of_condenser_pump_heat_to_water)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].evaporator_air_inlet_node_name, var_evaporator_air_inlet_node_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].evaporator_air_outlet_node_name, var_evaporator_air_outlet_node_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].condenser_water_inlet_node_name, var_condenser_water_inlet_node_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].condenser_water_outlet_node_name, var_condenser_water_outlet_node_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].maximum_ambient_temperature_for_crankcase_heater_operation, var_maximum_ambient_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].evaporator_air_temperature_type_for_curve_objects, var_evaporator_air_temperature_type_for_curve_objects)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_1, var_rated_water_heating_capacity_at_speed_1)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_1, var_rated_water_heating_cop_at_speed_1)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_1, var_rated_sensible_heat_ratio_at_speed_1)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_reference_unit_rated_air_flow_rate, var_speed_1_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_reference_unit_rated_water_flow_rate, var_speed_1_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_1_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_total_wh_capacity_function_of_temperature_curve_name, var_speed_1_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_cop_function_of_temperature_curve_name, var_speed_1_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_cop_function_of_air_flow_fraction_curve_name, var_speed_1_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_1_cop_function_of_water_flow_fraction_curve_name, var_speed_1_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_2, var_rated_water_heating_capacity_at_speed_2)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_2, var_rated_water_heating_cop_at_speed_2)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_2, var_rated_sensible_heat_ratio_at_speed_2)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_reference_unit_rated_air_flow_rate, var_speed_2_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_reference_unit_rated_water_flow_rate, var_speed_2_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_2_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_total_wh_capacity_function_of_temperature_curve_name, var_speed_2_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_cop_function_of_temperature_curve_name, var_speed_2_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_cop_function_of_air_flow_fraction_curve_name, var_speed_2_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_2_cop_function_of_water_flow_fraction_curve_name, var_speed_2_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_3, var_rated_water_heating_capacity_at_speed_3)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_3, var_rated_water_heating_cop_at_speed_3)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_3, var_rated_sensible_heat_ratio_at_speed_3)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_reference_unit_rated_air_flow_rate, var_speed_3_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_reference_unit_rated_water_flow_rate, var_speed_3_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_3_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_total_wh_capacity_function_of_temperature_curve_name, var_speed_3_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_cop_function_of_temperature_curve_name, var_speed_3_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_cop_function_of_air_flow_fraction_curve_name, var_speed_3_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_3_cop_function_of_water_flow_fraction_curve_name, var_speed_3_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_4, var_rated_water_heating_capacity_at_speed_4)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_4, var_rated_water_heating_cop_at_speed_4)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_4, var_rated_sensible_heat_ratio_at_speed_4)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_reference_unit_rated_air_flow_rate, var_speed_4_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_reference_unit_rated_water_flow_rate, var_speed_4_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_4_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_total_wh_capacity_function_of_temperature_curve_name, var_speed_4_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_cop_function_of_temperature_curve_name, var_speed_4_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_cop_function_of_air_flow_fraction_curve_name, var_speed_4_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_4_cop_function_of_water_flow_fraction_curve_name, var_speed_4_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_5, var_rated_water_heating_capacity_at_speed_5)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_5, var_rated_water_heating_cop_at_speed_5)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_5, var_rated_sensible_heat_ratio_at_speed_5)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_reference_unit_rated_air_flow_rate, var_speed_5_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_reference_unit_rated_water_flow_rate, var_speed_5_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_5_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_total_wh_capacity_function_of_temperature_curve_name, var_speed_5_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_cop_function_of_temperature_curve_name, var_speed_5_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_cop_function_of_air_flow_fraction_curve_name, var_speed_5_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_5_cop_function_of_water_flow_fraction_curve_name, var_speed_5_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_6, var_rated_water_heating_capacity_at_speed_6)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_6, var_rated_water_heating_cop_at_speed_6)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_6, var_rated_sensible_heat_ratio_at_speed_6)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_reference_unit_rated_air_flow_rate, var_speed_6_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_reference_unit_rated_water_flow_rate, var_speed_6_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_6_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_total_wh_capacity_function_of_temperature_curve_name, var_speed_6_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_cop_function_of_temperature_curve_name, var_speed_6_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_cop_function_of_air_flow_fraction_curve_name, var_speed_6_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_6_cop_function_of_water_flow_fraction_curve_name, var_speed_6_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_7, var_rated_water_heating_capacity_at_speed_7)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_7, var_rated_water_heating_cop_at_speed_7)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_7, var_rated_sensible_heat_ratio_at_speed_7)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_reference_unit_rated_air_flow_rate, var_speed_7_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_reference_unit_rated_water_flow_rate, var_speed_7_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_7_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_total_wh_capacity_function_of_temperature_curve_name, var_speed_7_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_cop_function_of_temperature_curve_name, var_speed_7_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_cop_function_of_air_flow_fraction_curve_name, var_speed_7_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_7_cop_function_of_water_flow_fraction_curve_name, var_speed_7_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_8, var_rated_water_heating_capacity_at_speed_8)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_8, var_rated_water_heating_cop_at_speed_8)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_8, var_rated_sensible_heat_ratio_at_speed_8)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_reference_unit_rated_air_flow_rate, var_speed_8_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_reference_unit_rated_water_flow_rate, var_speed_8_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_8_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_total_wh_capacity_function_of_temperature_curve_name, var_speed_8_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_cop_function_of_temperature_curve_name, var_speed_8_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_cop_function_of_air_flow_fraction_curve_name, var_speed_8_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_8_cop_function_of_water_flow_fraction_curve_name, var_speed_8_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_9, var_rated_water_heating_capacity_at_speed_9)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_9, var_rated_water_heating_cop_at_speed_9)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_9, var_rated_sensible_heat_ratio_at_speed_9)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_reference_unit_rated_air_flow_rate, var_speed_9_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_reference_unit_rated_water_flow_rate, var_speed_9_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_9_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_total_wh_capacity_function_of_temperature_curve_name, var_speed_9_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_cop_function_of_temperature_curve_name, var_speed_9_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_cop_function_of_air_flow_fraction_curve_name, var_speed_9_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_9_cop_function_of_water_flow_fraction_curve_name, var_speed_9_cop_function_of_water_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_capacity_at_speed_10, var_rated_water_heating_capacity_at_speed_10)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_water_heating_cop_at_speed_10, var_rated_water_heating_cop_at_speed_10)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].rated_sensible_heat_ratio_at_speed_10, var_rated_sensible_heat_ratio_at_speed_10)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_reference_unit_rated_air_flow_rate, var_speed_10_reference_unit_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_reference_unit_rated_water_flow_rate, var_speed_10_reference_unit_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_reference_unit_water_pump_input_power_at_rated_conditions, var_speed_10_reference_unit_water_pump_input_power_at_rated_conditions)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_total_wh_capacity_function_of_temperature_curve_name, var_speed_10_total_wh_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name, var_speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name, var_speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_cop_function_of_temperature_curve_name, var_speed_10_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_cop_function_of_air_flow_fraction_curve_name, var_speed_10_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpvariablespeeds[0].speed_10_cop_function_of_water_flow_fraction_curve_name, var_speed_10_cop_function_of_water_flow_fraction_curve_name)