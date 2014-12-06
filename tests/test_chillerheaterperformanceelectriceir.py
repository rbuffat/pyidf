import os
import tempfile
import unittest
import pyidf
from pyidf.plant_heating_and_cooling_equipment import ChillerHeaterPerformanceElectricEir
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestChillerHeaterPerformanceElectricEir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerheaterperformanceelectriceir(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerHeaterPerformanceElectricEir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_reference_cooling_mode_evaporator_capacity = 0.0001
        obj.reference_cooling_mode_evaporator_capacity = var_reference_cooling_mode_evaporator_capacity
        # real
        var_reference_cooling_mode_cop = 0.0001
        obj.reference_cooling_mode_cop = var_reference_cooling_mode_cop
        # real
        var_reference_cooling_mode_leaving_chilled_water_temperature = 4.4
        obj.reference_cooling_mode_leaving_chilled_water_temperature = var_reference_cooling_mode_leaving_chilled_water_temperature
        # real
        var_reference_cooling_mode_entering_condenser_fluid_temperature = 5.5
        obj.reference_cooling_mode_entering_condenser_fluid_temperature = var_reference_cooling_mode_entering_condenser_fluid_temperature
        # real
        var_reference_cooling_mode_leaving_condenser_water_temperature = 6.6
        obj.reference_cooling_mode_leaving_condenser_water_temperature = var_reference_cooling_mode_leaving_condenser_water_temperature
        # real
        var_reference_heating_mode_cooling_capacity_ratio = 7.7
        obj.reference_heating_mode_cooling_capacity_ratio = var_reference_heating_mode_cooling_capacity_ratio
        # real
        var_reference_heating_mode_cooling_power_input_ratio = 0.0001
        obj.reference_heating_mode_cooling_power_input_ratio = var_reference_heating_mode_cooling_power_input_ratio
        # real
        var_reference_heating_mode_leaving_chilled_water_temperature = 9.9
        obj.reference_heating_mode_leaving_chilled_water_temperature = var_reference_heating_mode_leaving_chilled_water_temperature
        # real
        var_reference_heating_mode_leaving_condenser_water_temperature = 10.1
        obj.reference_heating_mode_leaving_condenser_water_temperature = var_reference_heating_mode_leaving_condenser_water_temperature
        # real
        var_reference_heating_mode_entering_condenser_fluid_temperature = 11.11
        obj.reference_heating_mode_entering_condenser_fluid_temperature = var_reference_heating_mode_entering_condenser_fluid_temperature
        # real
        var_heating_mode_entering_chilled_water_temperature_low_limit = 12.12
        obj.heating_mode_entering_chilled_water_temperature_low_limit = var_heating_mode_entering_chilled_water_temperature_low_limit
        # alpha
        var_chilled_water_flow_mode_type = "ConstantFlow"
        obj.chilled_water_flow_mode_type = var_chilled_water_flow_mode_type
        # real
        var_design_chilled_water_flow_rate = 0.0001
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_water_flow_rate = 0.0001
        obj.design_condenser_water_flow_rate = var_design_condenser_water_flow_rate
        # real
        var_design_hot_water_flow_rate = 0.0
        obj.design_hot_water_flow_rate = var_design_hot_water_flow_rate
        # real
        var_compressor_motor_efficiency = 0.5
        obj.compressor_motor_efficiency = var_compressor_motor_efficiency
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # alpha
        var_cooling_mode_temperature_curve_condenser_water_independent_variable = "EnteringCondenser"
        obj.cooling_mode_temperature_curve_condenser_water_independent_variable = var_cooling_mode_temperature_curve_condenser_water_independent_variable
        # object-list
        var_cooling_mode_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling Mode Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_mode_cooling_capacity_function_of_temperature_curve_name = var_cooling_mode_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = "object-list|Cooling Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"
        obj.cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = "object-list|Cooling Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"
        obj.cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name
        # real
        var_cooling_mode_cooling_capacity_optimum_part_load_ratio = 0.0001
        obj.cooling_mode_cooling_capacity_optimum_part_load_ratio = var_cooling_mode_cooling_capacity_optimum_part_load_ratio
        # alpha
        var_heating_mode_temperature_curve_condenser_water_independent_variable = "EnteringCondenser"
        obj.heating_mode_temperature_curve_condenser_water_independent_variable = var_heating_mode_temperature_curve_condenser_water_independent_variable
        # object-list
        var_heating_mode_cooling_capacity_function_of_temperature_curve_name = "object-list|Heating Mode Cooling Capacity Function of Temperature Curve Name"
        obj.heating_mode_cooling_capacity_function_of_temperature_curve_name = var_heating_mode_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = "object-list|Heating Mode Electric Input to Cooling Output Ratio Function of Temperature Curve Name"
        obj.heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = var_heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name
        # object-list
        var_heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = "object-list|Heating Mode Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"
        obj.heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = var_heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name
        # real
        var_heating_mode_cooling_capacity_optimum_part_load_ratio = 0.0001
        obj.heating_mode_cooling_capacity_optimum_part_load_ratio = var_heating_mode_cooling_capacity_optimum_part_load_ratio
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].name, var_name)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_cooling_mode_evaporator_capacity, var_reference_cooling_mode_evaporator_capacity)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_cooling_mode_cop, var_reference_cooling_mode_cop)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_cooling_mode_leaving_chilled_water_temperature, var_reference_cooling_mode_leaving_chilled_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_cooling_mode_entering_condenser_fluid_temperature, var_reference_cooling_mode_entering_condenser_fluid_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_cooling_mode_leaving_condenser_water_temperature, var_reference_cooling_mode_leaving_condenser_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_heating_mode_cooling_capacity_ratio, var_reference_heating_mode_cooling_capacity_ratio)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_heating_mode_cooling_power_input_ratio, var_reference_heating_mode_cooling_power_input_ratio)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_heating_mode_leaving_chilled_water_temperature, var_reference_heating_mode_leaving_chilled_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_heating_mode_leaving_condenser_water_temperature, var_reference_heating_mode_leaving_condenser_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].reference_heating_mode_entering_condenser_fluid_temperature, var_reference_heating_mode_entering_condenser_fluid_temperature)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_entering_chilled_water_temperature_low_limit, var_heating_mode_entering_chilled_water_temperature_low_limit)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].chilled_water_flow_mode_type, var_chilled_water_flow_mode_type)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].design_condenser_water_flow_rate, var_design_condenser_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].design_hot_water_flow_rate, var_design_hot_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].compressor_motor_efficiency, var_compressor_motor_efficiency)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].cooling_mode_temperature_curve_condenser_water_independent_variable, var_cooling_mode_temperature_curve_condenser_water_independent_variable)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].cooling_mode_cooling_capacity_function_of_temperature_curve_name, var_cooling_mode_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name, var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name, var_cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].cooling_mode_cooling_capacity_optimum_part_load_ratio, var_cooling_mode_cooling_capacity_optimum_part_load_ratio)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_temperature_curve_condenser_water_independent_variable, var_heating_mode_temperature_curve_condenser_water_independent_variable)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_cooling_capacity_function_of_temperature_curve_name, var_heating_mode_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name, var_heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name, var_heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].heating_mode_cooling_capacity_optimum_part_load_ratio, var_heating_mode_cooling_capacity_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerheaterperformanceelectriceirs[0].sizing_factor, var_sizing_factor)