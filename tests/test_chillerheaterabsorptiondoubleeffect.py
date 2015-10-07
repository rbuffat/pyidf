import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import ChillerHeaterAbsorptionDoubleEffect

log = logging.getLogger(__name__)

class TestChillerHeaterAbsorptionDoubleEffect(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerheaterabsorptiondoubleeffect(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerHeaterAbsorptionDoubleEffect()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_nominal_cooling_capacity = 2.2
        obj.nominal_cooling_capacity = var_nominal_cooling_capacity
        # real
        var_heating_to_cooling_capacity_ratio = 0.0
        obj.heating_to_cooling_capacity_ratio = var_heating_to_cooling_capacity_ratio
        # real
        var_thermal_energy_input_to_cooling_output_ratio = 0.0001
        obj.thermal_energy_input_to_cooling_output_ratio = var_thermal_energy_input_to_cooling_output_ratio
        # real
        var_thermal_energy_input_to_heating_output_ratio = 0.0
        obj.thermal_energy_input_to_heating_output_ratio = var_thermal_energy_input_to_heating_output_ratio
        # real
        var_electric_input_to_cooling_output_ratio = 0.0
        obj.electric_input_to_cooling_output_ratio = var_electric_input_to_cooling_output_ratio
        # real
        var_electric_input_to_heating_output_ratio = 0.0
        obj.electric_input_to_heating_output_ratio = var_electric_input_to_heating_output_ratio
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
        # node
        var_hot_water_inlet_node_name = "node|Hot Water Inlet Node Name"
        obj.hot_water_inlet_node_name = var_hot_water_inlet_node_name
        # node
        var_hot_water_outlet_node_name = "node|Hot Water Outlet Node Name"
        obj.hot_water_outlet_node_name = var_hot_water_outlet_node_name
        # real
        var_minimum_part_load_ratio = 0.0001
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.5
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0001
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_design_entering_condenser_water_temperature = 17.17
        obj.design_entering_condenser_water_temperature = var_design_entering_condenser_water_temperature
        # real
        var_design_leaving_chilled_water_temperature = 18.18
        obj.design_leaving_chilled_water_temperature = var_design_leaving_chilled_water_temperature
        # real
        var_design_chilled_water_flow_rate = 19.19
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_water_flow_rate = 20.2
        obj.design_condenser_water_flow_rate = var_design_condenser_water_flow_rate
        # real
        var_design_hot_water_flow_rate = 21.21
        obj.design_hot_water_flow_rate = var_design_hot_water_flow_rate
        # object-list
        var_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_capacity_function_of_temperature_curve_name = var_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = "object-list|Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"
        obj.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = var_fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name
        # object-list
        var_fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = "object-list|Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"
        obj.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = var_fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name
        # object-list
        var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = "object-list|Electric Input to Cooling Output Ratio Function of Temperature Curve Name"
        obj.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name
        # object-list
        var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = "object-list|Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"
        obj.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name
        # object-list
        var_heating_capacity_function_of_cooling_capacity_curve_name = "object-list|Heating Capacity Function of Cooling Capacity Curve Name"
        obj.heating_capacity_function_of_cooling_capacity_curve_name = var_heating_capacity_function_of_cooling_capacity_curve_name
        # object-list
        var_fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = "object-list|Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"
        obj.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = var_fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name
        # alpha
        var_temperature_curve_input_variable = "LeavingCondenser"
        obj.temperature_curve_input_variable = var_temperature_curve_input_variable
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_chilled_water_temperature_lower_limit = 31.31
        obj.chilled_water_temperature_lower_limit = var_chilled_water_temperature_lower_limit
        # alpha
        var_exhaust_source_object_type = "Generator:MicroTurbine"
        obj.exhaust_source_object_type = var_exhaust_source_object_type
        # object-list
        var_exhaust_source_object_name = "object-list|Exhaust Source Object Name"
        obj.exhaust_source_object_name = var_exhaust_source_object_name
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].name, var_name)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].nominal_cooling_capacity, var_nominal_cooling_capacity)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].heating_to_cooling_capacity_ratio, var_heating_to_cooling_capacity_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].thermal_energy_input_to_cooling_output_ratio, var_thermal_energy_input_to_cooling_output_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].thermal_energy_input_to_heating_output_ratio, var_thermal_energy_input_to_heating_output_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].electric_input_to_cooling_output_ratio, var_electric_input_to_cooling_output_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].electric_input_to_heating_output_ratio, var_electric_input_to_heating_output_ratio)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].hot_water_inlet_node_name, var_hot_water_inlet_node_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].hot_water_outlet_node_name, var_hot_water_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].design_entering_condenser_water_temperature, var_design_entering_condenser_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].design_leaving_chilled_water_temperature, var_design_leaving_chilled_water_temperature)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].design_condenser_water_flow_rate, var_design_condenser_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].design_hot_water_flow_rate, var_design_hot_water_flow_rate)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].cooling_capacity_function_of_temperature_curve_name, var_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name, var_fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name, var_fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].electric_input_to_cooling_output_ratio_function_of_temperature_curve_name, var_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name, var_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].heating_capacity_function_of_cooling_capacity_curve_name, var_heating_capacity_function_of_cooling_capacity_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name, var_fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].temperature_curve_input_variable, var_temperature_curve_input_variable)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].chilled_water_temperature_lower_limit, var_chilled_water_temperature_lower_limit)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].exhaust_source_object_type, var_exhaust_source_object_type)
        self.assertEqual(idf2.chillerheaterabsorptiondoubleeffects[0].exhaust_source_object_name, var_exhaust_source_object_name)
        self.assertAlmostEqual(idf2.chillerheaterabsorptiondoubleeffects[0].sizing_factor, var_sizing_factor)