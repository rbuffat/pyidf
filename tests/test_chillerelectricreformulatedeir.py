import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import ChillerElectricReformulatedEir

log = logging.getLogger(__name__)

class TestChillerElectricReformulatedEir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerelectricreformulatedeir(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerElectricReformulatedEir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_reference_capacity = 0.0001
        obj.reference_capacity = var_reference_capacity
        # real
        var_reference_cop = 0.0001
        obj.reference_cop = var_reference_cop
        # real
        var_reference_leaving_chilled_water_temperature = 4.4
        obj.reference_leaving_chilled_water_temperature = var_reference_leaving_chilled_water_temperature
        # real
        var_reference_leaving_condenser_water_temperature = 5.5
        obj.reference_leaving_condenser_water_temperature = var_reference_leaving_condenser_water_temperature
        # real
        var_reference_chilled_water_flow_rate = 0.0001
        obj.reference_chilled_water_flow_rate = var_reference_chilled_water_flow_rate
        # real
        var_reference_condenser_water_flow_rate = 0.0001
        obj.reference_condenser_water_flow_rate = var_reference_condenser_water_flow_rate
        # object-list
        var_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_capacity_function_of_temperature_curve_name = var_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = "object-list|Electric Input to Cooling Output Ratio Function of Temperature Curve Name"
        obj.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name
        # object-list
        var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = "object-list|Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"
        obj.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name
        # real
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0001
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0001
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_minimum_unloading_ratio = 0.0
        obj.minimum_unloading_ratio = var_minimum_unloading_ratio
        # node
        var_chilled_water_inlet_node_name = "node|Chilled Water Inlet Node Name"
        obj.chilled_water_inlet_node_name = var_chilled_water_inlet_node_name
        # node
        var_chilled_water_outlet_node_name = "node|Chilled Water Outlet Node Name"
        obj.chilled_water_outlet_node_name = var_chilled_water_outlet_node_name
        # node
        var_condenser_inlet_node_name = "node|Condenser Inlet Node Name"
        obj.condenser_inlet_node_name = var_condenser_inlet_node_name
        # node
        var_condenser_outlet_node_name = "node|Condenser Outlet Node Name"
        obj.condenser_outlet_node_name = var_condenser_outlet_node_name
        # real
        var_fraction_of_compressor_electric_consumption_rejected_by_condenser = 0.50005
        obj.fraction_of_compressor_electric_consumption_rejected_by_condenser = var_fraction_of_compressor_electric_consumption_rejected_by_condenser
        # real
        var_leaving_chilled_water_lower_temperature_limit = 20.2
        obj.leaving_chilled_water_lower_temperature_limit = var_leaving_chilled_water_lower_temperature_limit
        # alpha
        var_chiller_flow_mode_type = "ConstantFlow"
        obj.chiller_flow_mode_type = var_chiller_flow_mode_type
        # real
        var_design_heat_recovery_water_flow_rate = 0.0
        obj.design_heat_recovery_water_flow_rate = var_design_heat_recovery_water_flow_rate
        # node
        var_heat_recovery_inlet_node_name = "node|Heat Recovery Inlet Node Name"
        obj.heat_recovery_inlet_node_name = var_heat_recovery_inlet_node_name
        # node
        var_heat_recovery_outlet_node_name = "node|Heat Recovery Outlet Node Name"
        obj.heat_recovery_outlet_node_name = var_heat_recovery_outlet_node_name
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # real
        var_condenser_heat_recovery_relative_capacity_fraction = 0.5
        obj.condenser_heat_recovery_relative_capacity_fraction = var_condenser_heat_recovery_relative_capacity_fraction
        # object-list
        var_heat_recovery_inlet_high_temperature_limit_schedule_name = "object-list|Heat Recovery Inlet High Temperature Limit Schedule Name"
        obj.heat_recovery_inlet_high_temperature_limit_schedule_name = var_heat_recovery_inlet_high_temperature_limit_schedule_name
        # node
        var_heat_recovery_leaving_temperature_setpoint_node_name = "node|Heat Recovery Leaving Temperature Setpoint Node Name"
        obj.heat_recovery_leaving_temperature_setpoint_node_name = var_heat_recovery_leaving_temperature_setpoint_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].name, var_name)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_capacity, var_reference_capacity)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_cop, var_reference_cop)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_leaving_chilled_water_temperature, var_reference_leaving_chilled_water_temperature)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_leaving_condenser_water_temperature, var_reference_leaving_condenser_water_temperature)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_chilled_water_flow_rate, var_reference_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].reference_condenser_water_flow_rate, var_reference_condenser_water_flow_rate)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].cooling_capacity_function_of_temperature_curve_name, var_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].electric_input_to_cooling_output_ratio_function_of_temperature_curve_name, var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name, var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].minimum_unloading_ratio, var_minimum_unloading_ratio)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].fraction_of_compressor_electric_consumption_rejected_by_condenser, var_fraction_of_compressor_electric_consumption_rejected_by_condenser)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].leaving_chilled_water_lower_temperature_limit, var_leaving_chilled_water_lower_temperature_limit)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].chiller_flow_mode_type, var_chiller_flow_mode_type)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].heat_recovery_inlet_node_name, var_heat_recovery_inlet_node_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].heat_recovery_outlet_node_name, var_heat_recovery_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.chillerelectricreformulatedeirs[0].condenser_heat_recovery_relative_capacity_fraction, var_condenser_heat_recovery_relative_capacity_fraction)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].heat_recovery_inlet_high_temperature_limit_schedule_name, var_heat_recovery_inlet_high_temperature_limit_schedule_name)
        self.assertEqual(idf2.chillerelectricreformulatedeirs[0].heat_recovery_leaving_temperature_setpoint_node_name, var_heat_recovery_leaving_temperature_setpoint_node_name)