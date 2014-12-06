import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorMicroTurbine
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorMicroTurbine(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatormicroturbine(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorMicroTurbine()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_reference_electrical_power_output = 0.0001
        obj.reference_electrical_power_output = var_reference_electrical_power_output
        # real
        var_minimum_full_load_electrical_power_output = 0.0
        obj.minimum_full_load_electrical_power_output = var_minimum_full_load_electrical_power_output
        # real
        var_maximum_full_load_electrical_power_output = 0.0001
        obj.maximum_full_load_electrical_power_output = var_maximum_full_load_electrical_power_output
        # real
        var_reference_electrical_efficiency_using_lower_heating_value = 0.50005
        obj.reference_electrical_efficiency_using_lower_heating_value = var_reference_electrical_efficiency_using_lower_heating_value
        # real
        var_reference_combustion_air_inlet_temperature = 6.6
        obj.reference_combustion_air_inlet_temperature = var_reference_combustion_air_inlet_temperature
        # real
        var_reference_combustion_air_inlet_humidity_ratio = 0.0001
        obj.reference_combustion_air_inlet_humidity_ratio = var_reference_combustion_air_inlet_humidity_ratio
        # real
        var_reference_elevation = -300.0
        obj.reference_elevation = var_reference_elevation
        # object-list
        var_electrical_power_function_of_temperature_and_elevation_curve_name = "object-list|Electrical Power Function of Temperature and Elevation Curve Name"
        obj.electrical_power_function_of_temperature_and_elevation_curve_name = var_electrical_power_function_of_temperature_and_elevation_curve_name
        # object-list
        var_electrical_efficiency_function_of_temperature_curve_name = "object-list|Electrical Efficiency Function of Temperature Curve Name"
        obj.electrical_efficiency_function_of_temperature_curve_name = var_electrical_efficiency_function_of_temperature_curve_name
        # object-list
        var_electrical_efficiency_function_of_part_load_ratio_curve_name = "object-list|Electrical Efficiency Function of Part Load Ratio Curve Name"
        obj.electrical_efficiency_function_of_part_load_ratio_curve_name = var_electrical_efficiency_function_of_part_load_ratio_curve_name
        # alpha
        var_fuel_type = "NaturalGas"
        obj.fuel_type = var_fuel_type
        # real
        var_fuel_higher_heating_value = 0.0001
        obj.fuel_higher_heating_value = var_fuel_higher_heating_value
        # real
        var_fuel_lower_heating_value = 0.0001
        obj.fuel_lower_heating_value = var_fuel_lower_heating_value
        # real
        var_standby_power = 0.0
        obj.standby_power = var_standby_power
        # real
        var_ancillary_power = 0.0
        obj.ancillary_power = var_ancillary_power
        # object-list
        var_ancillary_power_function_of_fuel_input_curve_name = "object-list|Ancillary Power Function of Fuel Input Curve Name"
        obj.ancillary_power_function_of_fuel_input_curve_name = var_ancillary_power_function_of_fuel_input_curve_name
        # node
        var_heat_recovery_water_inlet_node_name = "node|Heat Recovery Water Inlet Node Name"
        obj.heat_recovery_water_inlet_node_name = var_heat_recovery_water_inlet_node_name
        # node
        var_heat_recovery_water_outlet_node_name = "node|Heat Recovery Water Outlet Node Name"
        obj.heat_recovery_water_outlet_node_name = var_heat_recovery_water_outlet_node_name
        # real
        var_reference_thermal_efficiency_using_lower_heat_value = 0.5
        obj.reference_thermal_efficiency_using_lower_heat_value = var_reference_thermal_efficiency_using_lower_heat_value
        # real
        var_reference_inlet_water_temperature = 21.21
        obj.reference_inlet_water_temperature = var_reference_inlet_water_temperature
        # alpha
        var_heat_recovery_water_flow_operating_mode = "PlantControl"
        obj.heat_recovery_water_flow_operating_mode = var_heat_recovery_water_flow_operating_mode
        # real
        var_reference_heat_recovery_water_flow_rate = 0.0001
        obj.reference_heat_recovery_water_flow_rate = var_reference_heat_recovery_water_flow_rate
        # object-list
        var_heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name = "object-list|Heat Recovery Water Flow Rate Function of Temperature and Power Curve Name"
        obj.heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name = var_heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name
        # object-list
        var_thermal_efficiency_function_of_temperature_and_elevation_curve_name = "object-list|Thermal Efficiency Function of Temperature and Elevation Curve Name"
        obj.thermal_efficiency_function_of_temperature_and_elevation_curve_name = var_thermal_efficiency_function_of_temperature_and_elevation_curve_name
        # object-list
        var_heat_recovery_rate_function_of_part_load_ratio_curve_name = "object-list|Heat Recovery Rate Function of Part Load Ratio Curve Name"
        obj.heat_recovery_rate_function_of_part_load_ratio_curve_name = var_heat_recovery_rate_function_of_part_load_ratio_curve_name
        # object-list
        var_heat_recovery_rate_function_of_inlet_water_temperature_curve_name = "object-list|Heat Recovery Rate Function of Inlet Water Temperature Curve Name"
        obj.heat_recovery_rate_function_of_inlet_water_temperature_curve_name = var_heat_recovery_rate_function_of_inlet_water_temperature_curve_name
        # object-list
        var_heat_recovery_rate_function_of_water_flow_rate_curve_name = "object-list|Heat Recovery Rate Function of Water Flow Rate Curve Name"
        obj.heat_recovery_rate_function_of_water_flow_rate_curve_name = var_heat_recovery_rate_function_of_water_flow_rate_curve_name
        # real
        var_minimum_heat_recovery_water_flow_rate = 0.0
        obj.minimum_heat_recovery_water_flow_rate = var_minimum_heat_recovery_water_flow_rate
        # real
        var_maximum_heat_recovery_water_flow_rate = 0.0
        obj.maximum_heat_recovery_water_flow_rate = var_maximum_heat_recovery_water_flow_rate
        # real
        var_maximum_heat_recovery_water_temperature = 31.31
        obj.maximum_heat_recovery_water_temperature = var_maximum_heat_recovery_water_temperature
        # node
        var_combustion_air_inlet_node_name = "node|Combustion Air Inlet Node Name"
        obj.combustion_air_inlet_node_name = var_combustion_air_inlet_node_name
        # node
        var_combustion_air_outlet_node_name = "node|Combustion Air Outlet Node Name"
        obj.combustion_air_outlet_node_name = var_combustion_air_outlet_node_name
        # real
        var_reference_exhaust_air_mass_flow_rate = 0.0001
        obj.reference_exhaust_air_mass_flow_rate = var_reference_exhaust_air_mass_flow_rate
        # object-list
        var_exhaust_air_flow_rate_function_of_temperature_curve_name = "object-list|Exhaust Air Flow Rate Function of Temperature Curve Name"
        obj.exhaust_air_flow_rate_function_of_temperature_curve_name = var_exhaust_air_flow_rate_function_of_temperature_curve_name
        # object-list
        var_exhaust_air_flow_rate_function_of_part_load_ratio_curve_name = "object-list|Exhaust Air Flow Rate Function of Part Load Ratio Curve Name"
        obj.exhaust_air_flow_rate_function_of_part_load_ratio_curve_name = var_exhaust_air_flow_rate_function_of_part_load_ratio_curve_name
        # real
        var_nominal_exhaust_air_outlet_temperature = 37.37
        obj.nominal_exhaust_air_outlet_temperature = var_nominal_exhaust_air_outlet_temperature
        # object-list
        var_exhaust_air_temperature_function_of_temperature_curve_name = "object-list|Exhaust Air Temperature Function of Temperature Curve Name"
        obj.exhaust_air_temperature_function_of_temperature_curve_name = var_exhaust_air_temperature_function_of_temperature_curve_name
        # object-list
        var_exhaust_air_temperature_function_of_part_load_ratio_curve_name = "object-list|Exhaust Air Temperature Function of Part Load Ratio Curve Name"
        obj.exhaust_air_temperature_function_of_part_load_ratio_curve_name = var_exhaust_air_temperature_function_of_part_load_ratio_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatormicroturbines[0].name, var_name)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_electrical_power_output, var_reference_electrical_power_output)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].minimum_full_load_electrical_power_output, var_minimum_full_load_electrical_power_output)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].maximum_full_load_electrical_power_output, var_maximum_full_load_electrical_power_output)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_electrical_efficiency_using_lower_heating_value, var_reference_electrical_efficiency_using_lower_heating_value)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_combustion_air_inlet_temperature, var_reference_combustion_air_inlet_temperature)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_combustion_air_inlet_humidity_ratio, var_reference_combustion_air_inlet_humidity_ratio)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_elevation, var_reference_elevation)
        self.assertEqual(idf2.generatormicroturbines[0].electrical_power_function_of_temperature_and_elevation_curve_name, var_electrical_power_function_of_temperature_and_elevation_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].electrical_efficiency_function_of_temperature_curve_name, var_electrical_efficiency_function_of_temperature_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].electrical_efficiency_function_of_part_load_ratio_curve_name, var_electrical_efficiency_function_of_part_load_ratio_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].fuel_higher_heating_value, var_fuel_higher_heating_value)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].fuel_lower_heating_value, var_fuel_lower_heating_value)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].standby_power, var_standby_power)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].ancillary_power, var_ancillary_power)
        self.assertEqual(idf2.generatormicroturbines[0].ancillary_power_function_of_fuel_input_curve_name, var_ancillary_power_function_of_fuel_input_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_water_inlet_node_name, var_heat_recovery_water_inlet_node_name)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_water_outlet_node_name, var_heat_recovery_water_outlet_node_name)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_thermal_efficiency_using_lower_heat_value, var_reference_thermal_efficiency_using_lower_heat_value)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_inlet_water_temperature, var_reference_inlet_water_temperature)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_water_flow_operating_mode, var_heat_recovery_water_flow_operating_mode)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_heat_recovery_water_flow_rate, var_reference_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name, var_heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].thermal_efficiency_function_of_temperature_and_elevation_curve_name, var_thermal_efficiency_function_of_temperature_and_elevation_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_rate_function_of_part_load_ratio_curve_name, var_heat_recovery_rate_function_of_part_load_ratio_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_rate_function_of_inlet_water_temperature_curve_name, var_heat_recovery_rate_function_of_inlet_water_temperature_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].heat_recovery_rate_function_of_water_flow_rate_curve_name, var_heat_recovery_rate_function_of_water_flow_rate_curve_name)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].minimum_heat_recovery_water_flow_rate, var_minimum_heat_recovery_water_flow_rate)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].maximum_heat_recovery_water_flow_rate, var_maximum_heat_recovery_water_flow_rate)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].maximum_heat_recovery_water_temperature, var_maximum_heat_recovery_water_temperature)
        self.assertEqual(idf2.generatormicroturbines[0].combustion_air_inlet_node_name, var_combustion_air_inlet_node_name)
        self.assertEqual(idf2.generatormicroturbines[0].combustion_air_outlet_node_name, var_combustion_air_outlet_node_name)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].reference_exhaust_air_mass_flow_rate, var_reference_exhaust_air_mass_flow_rate)
        self.assertEqual(idf2.generatormicroturbines[0].exhaust_air_flow_rate_function_of_temperature_curve_name, var_exhaust_air_flow_rate_function_of_temperature_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].exhaust_air_flow_rate_function_of_part_load_ratio_curve_name, var_exhaust_air_flow_rate_function_of_part_load_ratio_curve_name)
        self.assertAlmostEqual(idf2.generatormicroturbines[0].nominal_exhaust_air_outlet_temperature, var_nominal_exhaust_air_outlet_temperature)
        self.assertEqual(idf2.generatormicroturbines[0].exhaust_air_temperature_function_of_temperature_curve_name, var_exhaust_air_temperature_function_of_temperature_curve_name)
        self.assertEqual(idf2.generatormicroturbines[0].exhaust_air_temperature_function_of_part_load_ratio_curve_name, var_exhaust_air_temperature_function_of_part_load_ratio_curve_name)