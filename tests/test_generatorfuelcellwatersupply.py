import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelCellWaterSupply
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelCellWaterSupply(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellwatersupply(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellWaterSupply()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_reformer_water_flow_rate_function_of_fuel_rate_curve_name = "object-list|Reformer Water Flow Rate Function of Fuel Rate Curve Name"
        obj.reformer_water_flow_rate_function_of_fuel_rate_curve_name = var_reformer_water_flow_rate_function_of_fuel_rate_curve_name
        # object-list
        var_reformer_water_pump_power_function_of_fuel_rate_curve_name = "object-list|Reformer Water Pump Power Function of Fuel Rate Curve Name"
        obj.reformer_water_pump_power_function_of_fuel_rate_curve_name = var_reformer_water_pump_power_function_of_fuel_rate_curve_name
        # real
        var_pump_heat_loss_factor = 4.4
        obj.pump_heat_loss_factor = var_pump_heat_loss_factor
        # alpha
        var_water_temperature_modeling_mode = "TemperatureFromAirNode"
        obj.water_temperature_modeling_mode = var_water_temperature_modeling_mode
        # node
        var_water_temperature_reference_node_name = "node|Water Temperature Reference Node Name"
        obj.water_temperature_reference_node_name = var_water_temperature_reference_node_name
        # object-list
        var_water_temperature_schedule_name = "object-list|Water Temperature Schedule Name"
        obj.water_temperature_schedule_name = var_water_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].reformer_water_flow_rate_function_of_fuel_rate_curve_name, var_reformer_water_flow_rate_function_of_fuel_rate_curve_name)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].reformer_water_pump_power_function_of_fuel_rate_curve_name, var_reformer_water_pump_power_function_of_fuel_rate_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelcellwatersupplys[0].pump_heat_loss_factor, var_pump_heat_loss_factor)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].water_temperature_modeling_mode, var_water_temperature_modeling_mode)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].water_temperature_reference_node_name, var_water_temperature_reference_node_name)
        self.assertEqual(idf2.generatorfuelcellwatersupplys[0].water_temperature_schedule_name, var_water_temperature_schedule_name)