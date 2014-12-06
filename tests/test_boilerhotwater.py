import os
import tempfile
import unittest
import pyidf
from pyidf.plant_heating_and_cooling_equipment import BoilerHotWater
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestBoilerHotWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_boilerhotwater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = BoilerHotWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
        # real
        var_nominal_capacity = 0.0
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_nominal_thermal_efficiency = 0.50005
        obj.nominal_thermal_efficiency = var_nominal_thermal_efficiency
        # alpha
        var_efficiency_curve_temperature_evaluation_variable = "EnteringBoiler"
        obj.efficiency_curve_temperature_evaluation_variable = var_efficiency_curve_temperature_evaluation_variable
        # object-list
        var_normalized_boiler_efficiency_curve_name = "object-list|Normalized Boiler Efficiency Curve Name"
        obj.normalized_boiler_efficiency_curve_name = var_normalized_boiler_efficiency_curve_name
        # real
        var_design_water_outlet_temperature = 7.7
        obj.design_water_outlet_temperature = var_design_water_outlet_temperature
        # real
        var_design_water_flow_rate = 0.0
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # node
        var_boiler_water_inlet_node_name = "node|Boiler Water Inlet Node Name"
        obj.boiler_water_inlet_node_name = var_boiler_water_inlet_node_name
        # node
        var_boiler_water_outlet_node_name = "node|Boiler Water Outlet Node Name"
        obj.boiler_water_outlet_node_name = var_boiler_water_outlet_node_name
        # real
        var_water_outlet_upper_temperature_limit = 14.14
        obj.water_outlet_upper_temperature_limit = var_water_outlet_upper_temperature_limit
        # alpha
        var_boiler_flow_mode = "ConstantFlow"
        obj.boiler_flow_mode = var_boiler_flow_mode
        # real
        var_parasitic_electric_load = 0.0
        obj.parasitic_electric_load = var_parasitic_electric_load
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
        self.assertEqual(idf2.boilerhotwaters[0].name, var_name)
        self.assertEqual(idf2.boilerhotwaters[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].nominal_thermal_efficiency, var_nominal_thermal_efficiency)
        self.assertEqual(idf2.boilerhotwaters[0].efficiency_curve_temperature_evaluation_variable, var_efficiency_curve_temperature_evaluation_variable)
        self.assertEqual(idf2.boilerhotwaters[0].normalized_boiler_efficiency_curve_name, var_normalized_boiler_efficiency_curve_name)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].design_water_outlet_temperature, var_design_water_outlet_temperature)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertEqual(idf2.boilerhotwaters[0].boiler_water_inlet_node_name, var_boiler_water_inlet_node_name)
        self.assertEqual(idf2.boilerhotwaters[0].boiler_water_outlet_node_name, var_boiler_water_outlet_node_name)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].water_outlet_upper_temperature_limit, var_water_outlet_upper_temperature_limit)
        self.assertEqual(idf2.boilerhotwaters[0].boiler_flow_mode, var_boiler_flow_mode)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].parasitic_electric_load, var_parasitic_electric_load)
        self.assertAlmostEqual(idf2.boilerhotwaters[0].sizing_factor, var_sizing_factor)