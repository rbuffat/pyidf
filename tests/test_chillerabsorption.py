import os
import tempfile
import unittest
import pyidf
from pyidf.plant_heating_and_cooling_equipment import ChillerAbsorption
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestChillerAbsorption(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerabsorption(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerAbsorption()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_nominal_capacity = 0.0001
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_nominal_pumping_power = 0.0
        obj.nominal_pumping_power = var_nominal_pumping_power
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
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_design_condenser_inlet_temperature = 11.11
        obj.design_condenser_inlet_temperature = var_design_condenser_inlet_temperature
        # real
        var_design_chilled_water_flow_rate = 0.0001
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_water_flow_rate = 0.0001
        obj.design_condenser_water_flow_rate = var_design_condenser_water_flow_rate
        # real
        var_coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve = 14.14
        obj.coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve = var_coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve
        # real
        var_coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve = 15.15
        obj.coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve = var_coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve
        # real
        var_coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve = 16.16
        obj.coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve = var_coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve
        # real
        var_coefficient_1_of_the_pump_electric_use_part_load_ratio_curve = 17.17
        obj.coefficient_1_of_the_pump_electric_use_part_load_ratio_curve = var_coefficient_1_of_the_pump_electric_use_part_load_ratio_curve
        # real
        var_coefficient_2_of_the_pump_electric_use_part_load_ratio_curve = 18.18
        obj.coefficient_2_of_the_pump_electric_use_part_load_ratio_curve = var_coefficient_2_of_the_pump_electric_use_part_load_ratio_curve
        # real
        var_coefficient_3_of_the_pump_electric_use_part_load_ratio_curve = 19.19
        obj.coefficient_3_of_the_pump_electric_use_part_load_ratio_curve = var_coefficient_3_of_the_pump_electric_use_part_load_ratio_curve
        # real
        var_chilled_water_outlet_temperature_lower_limit = 20.2
        obj.chilled_water_outlet_temperature_lower_limit = var_chilled_water_outlet_temperature_lower_limit
        # node
        var_generator_inlet_node_name = "node|Generator Inlet Node Name"
        obj.generator_inlet_node_name = var_generator_inlet_node_name
        # node
        var_generator_outlet_node_name = "node|Generator Outlet Node Name"
        obj.generator_outlet_node_name = var_generator_outlet_node_name
        # alpha
        var_chiller_flow_mode = "ConstantFlow"
        obj.chiller_flow_mode = var_chiller_flow_mode
        # alpha
        var_generator_heat_source_type = "Steam"
        obj.generator_heat_source_type = var_generator_heat_source_type
        # real
        var_design_generator_fluid_flow_rate = 0.0001
        obj.design_generator_fluid_flow_rate = var_design_generator_fluid_flow_rate
        # real
        var_degree_of_subcooling_in_steam_generator = 26.26
        obj.degree_of_subcooling_in_steam_generator = var_degree_of_subcooling_in_steam_generator
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
        self.assertEqual(idf2.chillerabsorptions[0].name, var_name)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].nominal_pumping_power, var_nominal_pumping_power)
        self.assertEqual(idf2.chillerabsorptions[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerabsorptions[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerabsorptions[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerabsorptions[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].design_condenser_inlet_temperature, var_design_condenser_inlet_temperature)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].design_condenser_water_flow_rate, var_design_condenser_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve, var_coefficient_1_of_the_hot_water_or_steam_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve, var_coefficient_2_of_the_hot_water_or_steam_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve, var_coefficient_3_of_the_hot_water_or_steam_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_1_of_the_pump_electric_use_part_load_ratio_curve, var_coefficient_1_of_the_pump_electric_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_2_of_the_pump_electric_use_part_load_ratio_curve, var_coefficient_2_of_the_pump_electric_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].coefficient_3_of_the_pump_electric_use_part_load_ratio_curve, var_coefficient_3_of_the_pump_electric_use_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].chilled_water_outlet_temperature_lower_limit, var_chilled_water_outlet_temperature_lower_limit)
        self.assertEqual(idf2.chillerabsorptions[0].generator_inlet_node_name, var_generator_inlet_node_name)
        self.assertEqual(idf2.chillerabsorptions[0].generator_outlet_node_name, var_generator_outlet_node_name)
        self.assertEqual(idf2.chillerabsorptions[0].chiller_flow_mode, var_chiller_flow_mode)
        self.assertEqual(idf2.chillerabsorptions[0].generator_heat_source_type, var_generator_heat_source_type)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].design_generator_fluid_flow_rate, var_design_generator_fluid_flow_rate)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].degree_of_subcooling_in_steam_generator, var_degree_of_subcooling_in_steam_generator)
        self.assertAlmostEqual(idf2.chillerabsorptions[0].sizing_factor, var_sizing_factor)