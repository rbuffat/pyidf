import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import BoilerSteam

log = logging.getLogger(__name__)

class TestBoilerSteam(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_boilersteam(self):

        pyidf.validation_level = ValidationLevel.error

        obj = BoilerSteam()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
        # real
        var_maximum_operating_pressure = 3.3
        obj.maximum_operating_pressure = var_maximum_operating_pressure
        # real
        var_theoretical_efficiency = 0.5
        obj.theoretical_efficiency = var_theoretical_efficiency
        # real
        var_design_outlet_steam_temperature = 5.5
        obj.design_outlet_steam_temperature = var_design_outlet_steam_temperature
        # real
        var_nominal_capacity = 6.6
        obj.nominal_capacity = var_nominal_capacity
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
        var_coefficient_1_of_fuel_use_function_of_part_load_ratio_curve = 10.1
        obj.coefficient_1_of_fuel_use_function_of_part_load_ratio_curve = var_coefficient_1_of_fuel_use_function_of_part_load_ratio_curve
        # real
        var_coefficient_2_of_fuel_use_function_of_part_load_ratio_curve = 11.11
        obj.coefficient_2_of_fuel_use_function_of_part_load_ratio_curve = var_coefficient_2_of_fuel_use_function_of_part_load_ratio_curve
        # real
        var_coefficient_3_of_fuel_use_function_of_part_load_ratio_curve = 12.12
        obj.coefficient_3_of_fuel_use_function_of_part_load_ratio_curve = var_coefficient_3_of_fuel_use_function_of_part_load_ratio_curve
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_steam_outlet_node_name = "node|Steam Outlet Node Name"
        obj.steam_outlet_node_name = var_steam_outlet_node_name
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
        self.assertEqual(idf2.boilersteams[0].name, var_name)
        self.assertEqual(idf2.boilersteams[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.boilersteams[0].maximum_operating_pressure, var_maximum_operating_pressure)
        self.assertAlmostEqual(idf2.boilersteams[0].theoretical_efficiency, var_theoretical_efficiency)
        self.assertAlmostEqual(idf2.boilersteams[0].design_outlet_steam_temperature, var_design_outlet_steam_temperature)
        self.assertAlmostEqual(idf2.boilersteams[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.boilersteams[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.boilersteams[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.boilersteams[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.boilersteams[0].coefficient_1_of_fuel_use_function_of_part_load_ratio_curve, var_coefficient_1_of_fuel_use_function_of_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.boilersteams[0].coefficient_2_of_fuel_use_function_of_part_load_ratio_curve, var_coefficient_2_of_fuel_use_function_of_part_load_ratio_curve)
        self.assertAlmostEqual(idf2.boilersteams[0].coefficient_3_of_fuel_use_function_of_part_load_ratio_curve, var_coefficient_3_of_fuel_use_function_of_part_load_ratio_curve)
        self.assertEqual(idf2.boilersteams[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.boilersteams[0].steam_outlet_node_name, var_steam_outlet_node_name)
        self.assertAlmostEqual(idf2.boilersteams[0].sizing_factor, var_sizing_factor)