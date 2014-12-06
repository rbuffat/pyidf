import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelCellAirSupply
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelCellAirSupply(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellairsupply(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellAirSupply()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # object-list
        var_blower_power_curve_name = "object-list|Blower Power Curve Name"
        obj.blower_power_curve_name = var_blower_power_curve_name
        # real
        var_blower_heat_loss_factor = 0.5
        obj.blower_heat_loss_factor = var_blower_heat_loss_factor
        # alpha
        var_air_supply_rate_calculation_mode = "AirRatiobyStoics"
        obj.air_supply_rate_calculation_mode = var_air_supply_rate_calculation_mode
        # real
        var_stoichiometric_ratio = 6.6
        obj.stoichiometric_ratio = var_stoichiometric_ratio
        # object-list
        var_air_rate_function_of_electric_power_curve_name = "object-list|Air Rate Function of Electric Power Curve Name"
        obj.air_rate_function_of_electric_power_curve_name = var_air_rate_function_of_electric_power_curve_name
        # real
        var_air_rate_air_temperature_coefficient = 8.8
        obj.air_rate_air_temperature_coefficient = var_air_rate_air_temperature_coefficient
        # object-list
        var_air_rate_function_of_fuel_rate_curve_name = "object-list|Air Rate Function of Fuel Rate Curve Name"
        obj.air_rate_function_of_fuel_rate_curve_name = var_air_rate_function_of_fuel_rate_curve_name
        # alpha
        var_air_intake_heat_recovery_mode = "NoRecovery"
        obj.air_intake_heat_recovery_mode = var_air_intake_heat_recovery_mode
        # alpha
        var_air_supply_constituent_mode = "AmbientAir"
        obj.air_supply_constituent_mode = var_air_supply_constituent_mode
        # real
        var_number_of_userdefined_constituents = 5.0
        obj.number_of_userdefined_constituents = var_number_of_userdefined_constituents
        paras = []
        var_constituent_1_name = "CarbonDioxide"
        paras.append(var_constituent_1_name)
        var_molar_fraction_1 = 0.5
        paras.append(var_molar_fraction_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].blower_power_curve_name, var_blower_power_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelcellairsupplys[0].blower_heat_loss_factor, var_blower_heat_loss_factor)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_supply_rate_calculation_mode, var_air_supply_rate_calculation_mode)
        self.assertAlmostEqual(idf2.generatorfuelcellairsupplys[0].stoichiometric_ratio, var_stoichiometric_ratio)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_rate_function_of_electric_power_curve_name, var_air_rate_function_of_electric_power_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelcellairsupplys[0].air_rate_air_temperature_coefficient, var_air_rate_air_temperature_coefficient)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_rate_function_of_fuel_rate_curve_name, var_air_rate_function_of_fuel_rate_curve_name)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_intake_heat_recovery_mode, var_air_intake_heat_recovery_mode)
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].air_supply_constituent_mode, var_air_supply_constituent_mode)
        self.assertAlmostEqual(idf2.generatorfuelcellairsupplys[0].number_of_userdefined_constituents, var_number_of_userdefined_constituents)
        index = obj.extensible_field_index("Constituent 1 Name")
        self.assertEqual(idf2.generatorfuelcellairsupplys[0].extensibles[0][index], var_constituent_1_name)
        index = obj.extensible_field_index("Molar Fraction 1")
        self.assertAlmostEqual(idf2.generatorfuelcellairsupplys[0].extensibles[0][index], var_molar_fraction_1)