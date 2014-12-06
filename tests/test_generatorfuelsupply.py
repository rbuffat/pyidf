import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelSupply
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelSupply(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelsupply(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelSupply()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fuel_temperature_modeling_mode = "TemperatureFromAirNode"
        obj.fuel_temperature_modeling_mode = var_fuel_temperature_modeling_mode
        # node
        var_fuel_temperature_reference_node_name = "node|Fuel Temperature Reference Node Name"
        obj.fuel_temperature_reference_node_name = var_fuel_temperature_reference_node_name
        # alpha
        var_fuel_temperature_schedule_name = "Fuel Temperature Schedule Name"
        obj.fuel_temperature_schedule_name = var_fuel_temperature_schedule_name
        # object-list
        var_compressor_power_function_of_fuel_rate_curve_name = "object-list|Compressor Power Function of Fuel Rate Curve Name"
        obj.compressor_power_function_of_fuel_rate_curve_name = var_compressor_power_function_of_fuel_rate_curve_name
        # real
        var_compressor_heat_loss_factor = 0.5
        obj.compressor_heat_loss_factor = var_compressor_heat_loss_factor
        # alpha
        var_fuel_type = "GaseousConstituents"
        obj.fuel_type = var_fuel_type
        # real
        var_liquid_generic_fuel_lower_heating_value = 8.8
        obj.liquid_generic_fuel_lower_heating_value = var_liquid_generic_fuel_lower_heating_value
        # real
        var_liquid_generic_fuel_higher_heating_value = 9.9
        obj.liquid_generic_fuel_higher_heating_value = var_liquid_generic_fuel_higher_heating_value
        # real
        var_liquid_generic_fuel_molecular_weight = 10.1
        obj.liquid_generic_fuel_molecular_weight = var_liquid_generic_fuel_molecular_weight
        # real
        var_liquid_generic_fuel_co2_emission_factor = 11.11
        obj.liquid_generic_fuel_co2_emission_factor = var_liquid_generic_fuel_co2_emission_factor
        # real
        var_number_of_constituents_in_gaseous_constituent_fuel_supply = 6.0
        obj.number_of_constituents_in_gaseous_constituent_fuel_supply = var_number_of_constituents_in_gaseous_constituent_fuel_supply
        # alpha
        var_constituent_1_name = "CarbonDioxide"
        obj.constituent_1_name = var_constituent_1_name
        # real
        var_constituent_1_molar_fraction = 0.5
        obj.constituent_1_molar_fraction = var_constituent_1_molar_fraction
        # alpha
        var_constituent_2_name = "CarbonDioxide"
        obj.constituent_2_name = var_constituent_2_name
        # real
        var_constituent_2_molar_fraction = 0.5
        obj.constituent_2_molar_fraction = var_constituent_2_molar_fraction
        # alpha
        var_constituent_3_name = "CarbonDioxide"
        obj.constituent_3_name = var_constituent_3_name
        # real
        var_constituent_3_molar_fraction = 0.5
        obj.constituent_3_molar_fraction = var_constituent_3_molar_fraction
        # alpha
        var_constituent_4_name = "CarbonDioxide"
        obj.constituent_4_name = var_constituent_4_name
        # real
        var_constituent_4_molar_fraction = 0.5
        obj.constituent_4_molar_fraction = var_constituent_4_molar_fraction
        # alpha
        var_constituent_5_name = "CarbonDioxide"
        obj.constituent_5_name = var_constituent_5_name
        # real
        var_constituent_5_molar_fraction = 0.5
        obj.constituent_5_molar_fraction = var_constituent_5_molar_fraction
        # alpha
        var_constituent_6_name = "CarbonDioxide"
        obj.constituent_6_name = var_constituent_6_name
        # real
        var_constituent_6_molar_fraction = 0.5
        obj.constituent_6_molar_fraction = var_constituent_6_molar_fraction
        # alpha
        var_constituent_7_name = "Hydrogen"
        obj.constituent_7_name = var_constituent_7_name
        # real
        var_constituent_7_molar_fraction = 0.5
        obj.constituent_7_molar_fraction = var_constituent_7_molar_fraction
        # alpha
        var_constituent_8_name = "CarbonDioxide"
        obj.constituent_8_name = var_constituent_8_name
        # real
        var_constituent_8_molar_fraction = 0.5
        obj.constituent_8_molar_fraction = var_constituent_8_molar_fraction
        # alpha
        var_constituent_9_name = "CarbonDioxide"
        obj.constituent_9_name = var_constituent_9_name
        # real
        var_constituent_9_molar_fraction = 0.5
        obj.constituent_9_molar_fraction = var_constituent_9_molar_fraction
        # alpha
        var_constituent_10_name = "CarbonDioxide"
        obj.constituent_10_name = var_constituent_10_name
        # real
        var_constituent_10_molar_fraction = 0.5
        obj.constituent_10_molar_fraction = var_constituent_10_molar_fraction
        # alpha
        var_constituent_11_name = "CarbonDioxide"
        obj.constituent_11_name = var_constituent_11_name
        # real
        var_constituent_11_molar_fraction = 0.5
        obj.constituent_11_molar_fraction = var_constituent_11_molar_fraction
        # alpha
        var_constituent_12_name = "CarbonDioxide"
        obj.constituent_12_name = var_constituent_12_name
        # real
        var_constituent_12_molar_fraction = 0.5
        obj.constituent_12_molar_fraction = var_constituent_12_molar_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelsupplys[0].name, var_name)
        self.assertEqual(idf2.generatorfuelsupplys[0].fuel_temperature_modeling_mode, var_fuel_temperature_modeling_mode)
        self.assertEqual(idf2.generatorfuelsupplys[0].fuel_temperature_reference_node_name, var_fuel_temperature_reference_node_name)
        self.assertEqual(idf2.generatorfuelsupplys[0].fuel_temperature_schedule_name, var_fuel_temperature_schedule_name)
        self.assertEqual(idf2.generatorfuelsupplys[0].compressor_power_function_of_fuel_rate_curve_name, var_compressor_power_function_of_fuel_rate_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].compressor_heat_loss_factor, var_compressor_heat_loss_factor)
        self.assertEqual(idf2.generatorfuelsupplys[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].liquid_generic_fuel_lower_heating_value, var_liquid_generic_fuel_lower_heating_value)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].liquid_generic_fuel_higher_heating_value, var_liquid_generic_fuel_higher_heating_value)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].liquid_generic_fuel_molecular_weight, var_liquid_generic_fuel_molecular_weight)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].liquid_generic_fuel_co2_emission_factor, var_liquid_generic_fuel_co2_emission_factor)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].number_of_constituents_in_gaseous_constituent_fuel_supply, var_number_of_constituents_in_gaseous_constituent_fuel_supply)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_1_name, var_constituent_1_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_1_molar_fraction, var_constituent_1_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_2_name, var_constituent_2_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_2_molar_fraction, var_constituent_2_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_3_name, var_constituent_3_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_3_molar_fraction, var_constituent_3_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_4_name, var_constituent_4_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_4_molar_fraction, var_constituent_4_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_5_name, var_constituent_5_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_5_molar_fraction, var_constituent_5_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_6_name, var_constituent_6_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_6_molar_fraction, var_constituent_6_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_7_name, var_constituent_7_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_7_molar_fraction, var_constituent_7_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_8_name, var_constituent_8_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_8_molar_fraction, var_constituent_8_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_9_name, var_constituent_9_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_9_molar_fraction, var_constituent_9_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_10_name, var_constituent_10_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_10_molar_fraction, var_constituent_10_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_11_name, var_constituent_11_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_11_molar_fraction, var_constituent_11_molar_fraction)
        self.assertEqual(idf2.generatorfuelsupplys[0].constituent_12_name, var_constituent_12_name)
        self.assertAlmostEqual(idf2.generatorfuelsupplys[0].constituent_12_molar_fraction, var_constituent_12_molar_fraction)