import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorCombustionTurbine
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorCombustionTurbine(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorcombustionturbine(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorCombustionTurbine()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_rated_power_output = 2.2
        obj.rated_power_output = var_rated_power_output
        # alpha
        var_electric_circuit_node_name = "Electric Circuit Node Name"
        obj.electric_circuit_node_name = var_electric_circuit_node_name
        # real
        var_minimum_part_load_ratio = 0.5
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.50005
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 6.6
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # object-list
        var_part_load_based_fuel_input_curve_name = "object-list|Part Load Based Fuel Input Curve Name"
        obj.part_load_based_fuel_input_curve_name = var_part_load_based_fuel_input_curve_name
        # object-list
        var_temperature_based_fuel_input_curve_name = "object-list|Temperature Based Fuel Input Curve Name"
        obj.temperature_based_fuel_input_curve_name = var_temperature_based_fuel_input_curve_name
        # object-list
        var_exhaust_flow_curve_name = "object-list|Exhaust Flow Curve Name"
        obj.exhaust_flow_curve_name = var_exhaust_flow_curve_name
        # object-list
        var_part_load_based_exhaust_temperature_curve_name = "object-list|Part Load Based Exhaust Temperature Curve Name"
        obj.part_load_based_exhaust_temperature_curve_name = var_part_load_based_exhaust_temperature_curve_name
        # object-list
        var_temperature_based_exhaust_temperature_curve_name = "object-list|Temperature Based Exhaust Temperature Curve Name"
        obj.temperature_based_exhaust_temperature_curve_name = var_temperature_based_exhaust_temperature_curve_name
        # object-list
        var_heat_recovery_lube_energy_curve_name = "object-list|Heat Recovery Lube Energy Curve Name"
        obj.heat_recovery_lube_energy_curve_name = var_heat_recovery_lube_energy_curve_name
        # real
        var_coefficient_1_of_ufactor_times_area_curve = 13.13
        obj.coefficient_1_of_ufactor_times_area_curve = var_coefficient_1_of_ufactor_times_area_curve
        # real
        var_coefficient_2_of_ufactor_times_area_curve = 2.0
        obj.coefficient_2_of_ufactor_times_area_curve = var_coefficient_2_of_ufactor_times_area_curve
        # real
        var_maximum_exhaust_flow_per_unit_of_power_output = 15.15
        obj.maximum_exhaust_flow_per_unit_of_power_output = var_maximum_exhaust_flow_per_unit_of_power_output
        # real
        var_design_minimum_exhaust_temperature = 16.16
        obj.design_minimum_exhaust_temperature = var_design_minimum_exhaust_temperature
        # real
        var_design_air_inlet_temperature = 17.17
        obj.design_air_inlet_temperature = var_design_air_inlet_temperature
        # real
        var_fuel_higher_heating_value = 18.18
        obj.fuel_higher_heating_value = var_fuel_higher_heating_value
        # real
        var_design_heat_recovery_water_flow_rate = 0.0
        obj.design_heat_recovery_water_flow_rate = var_design_heat_recovery_water_flow_rate
        # node
        var_heat_recovery_inlet_node_name = "node|Heat Recovery Inlet Node Name"
        obj.heat_recovery_inlet_node_name = var_heat_recovery_inlet_node_name
        # node
        var_heat_recovery_outlet_node_name = "node|Heat Recovery Outlet Node Name"
        obj.heat_recovery_outlet_node_name = var_heat_recovery_outlet_node_name
        # alpha
        var_fuel_type = "NaturalGas"
        obj.fuel_type = var_fuel_type
        # real
        var_heat_recovery_maximum_temperature = 50.0
        obj.heat_recovery_maximum_temperature = var_heat_recovery_maximum_temperature
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorcombustionturbines[0].name, var_name)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].rated_power_output, var_rated_power_output)
        self.assertEqual(idf2.generatorcombustionturbines[0].electric_circuit_node_name, var_electric_circuit_node_name)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertEqual(idf2.generatorcombustionturbines[0].part_load_based_fuel_input_curve_name, var_part_load_based_fuel_input_curve_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].temperature_based_fuel_input_curve_name, var_temperature_based_fuel_input_curve_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].exhaust_flow_curve_name, var_exhaust_flow_curve_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].part_load_based_exhaust_temperature_curve_name, var_part_load_based_exhaust_temperature_curve_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].temperature_based_exhaust_temperature_curve_name, var_temperature_based_exhaust_temperature_curve_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].heat_recovery_lube_energy_curve_name, var_heat_recovery_lube_energy_curve_name)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].coefficient_1_of_ufactor_times_area_curve, var_coefficient_1_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].coefficient_2_of_ufactor_times_area_curve, var_coefficient_2_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].maximum_exhaust_flow_per_unit_of_power_output, var_maximum_exhaust_flow_per_unit_of_power_output)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].design_minimum_exhaust_temperature, var_design_minimum_exhaust_temperature)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].design_air_inlet_temperature, var_design_air_inlet_temperature)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].fuel_higher_heating_value, var_fuel_higher_heating_value)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.generatorcombustionturbines[0].heat_recovery_inlet_node_name, var_heat_recovery_inlet_node_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].heat_recovery_outlet_node_name, var_heat_recovery_outlet_node_name)
        self.assertEqual(idf2.generatorcombustionturbines[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.generatorcombustionturbines[0].heat_recovery_maximum_temperature, var_heat_recovery_maximum_temperature)
        self.assertEqual(idf2.generatorcombustionturbines[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)