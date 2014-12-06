import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorInternalCombustionEngine
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorInternalCombustionEngine(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorinternalcombustionengine(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorInternalCombustionEngine()
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
        var_shaft_power_curve_name = "object-list|Shaft Power Curve Name"
        obj.shaft_power_curve_name = var_shaft_power_curve_name
        # object-list
        var_jacket_heat_recovery_curve_name = "object-list|Jacket Heat Recovery Curve Name"
        obj.jacket_heat_recovery_curve_name = var_jacket_heat_recovery_curve_name
        # object-list
        var_lube_heat_recovery_curve_name = "object-list|Lube Heat Recovery Curve Name"
        obj.lube_heat_recovery_curve_name = var_lube_heat_recovery_curve_name
        # object-list
        var_total_exhaust_energy_curve_name = "object-list|Total Exhaust Energy Curve Name"
        obj.total_exhaust_energy_curve_name = var_total_exhaust_energy_curve_name
        # object-list
        var_exhaust_temperature_curve_name = "object-list|Exhaust Temperature Curve Name"
        obj.exhaust_temperature_curve_name = var_exhaust_temperature_curve_name
        # real
        var_coefficient_1_of_ufactor_times_area_curve = 12.12
        obj.coefficient_1_of_ufactor_times_area_curve = var_coefficient_1_of_ufactor_times_area_curve
        # real
        var_coefficient_2_of_ufactor_times_area_curve = 2.0
        obj.coefficient_2_of_ufactor_times_area_curve = var_coefficient_2_of_ufactor_times_area_curve
        # real
        var_maximum_exhaust_flow_per_unit_of_power_output = 14.14
        obj.maximum_exhaust_flow_per_unit_of_power_output = var_maximum_exhaust_flow_per_unit_of_power_output
        # real
        var_design_minimum_exhaust_temperature = 15.15
        obj.design_minimum_exhaust_temperature = var_design_minimum_exhaust_temperature
        # real
        var_fuel_higher_heating_value = 16.16
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

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].name, var_name)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].rated_power_output, var_rated_power_output)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].electric_circuit_node_name, var_electric_circuit_node_name)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].shaft_power_curve_name, var_shaft_power_curve_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].jacket_heat_recovery_curve_name, var_jacket_heat_recovery_curve_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].lube_heat_recovery_curve_name, var_lube_heat_recovery_curve_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].total_exhaust_energy_curve_name, var_total_exhaust_energy_curve_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].exhaust_temperature_curve_name, var_exhaust_temperature_curve_name)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].coefficient_1_of_ufactor_times_area_curve, var_coefficient_1_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].coefficient_2_of_ufactor_times_area_curve, var_coefficient_2_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].maximum_exhaust_flow_per_unit_of_power_output, var_maximum_exhaust_flow_per_unit_of_power_output)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].design_minimum_exhaust_temperature, var_design_minimum_exhaust_temperature)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].fuel_higher_heating_value, var_fuel_higher_heating_value)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].heat_recovery_inlet_node_name, var_heat_recovery_inlet_node_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].heat_recovery_outlet_node_name, var_heat_recovery_outlet_node_name)
        self.assertEqual(idf2.generatorinternalcombustionengines[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.generatorinternalcombustionengines[0].heat_recovery_maximum_temperature, var_heat_recovery_maximum_temperature)