import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorMicroChp
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorMicroChp(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatormicrochp(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorMicroChp()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_performance_parameters_name = "object-list|Performance Parameters Name"
        obj.performance_parameters_name = var_performance_parameters_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # node
        var_cooling_water_inlet_node_name = "node|Cooling Water Inlet Node Name"
        obj.cooling_water_inlet_node_name = var_cooling_water_inlet_node_name
        # node
        var_cooling_water_outlet_node_name = "node|Cooling Water Outlet Node Name"
        obj.cooling_water_outlet_node_name = var_cooling_water_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_generator_fuel_supply_name = "object-list|Generator Fuel Supply Name"
        obj.generator_fuel_supply_name = var_generator_fuel_supply_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatormicrochps[0].name, var_name)
        self.assertEqual(idf2.generatormicrochps[0].performance_parameters_name, var_performance_parameters_name)
        self.assertEqual(idf2.generatormicrochps[0].zone_name, var_zone_name)
        self.assertEqual(idf2.generatormicrochps[0].cooling_water_inlet_node_name, var_cooling_water_inlet_node_name)
        self.assertEqual(idf2.generatormicrochps[0].cooling_water_outlet_node_name, var_cooling_water_outlet_node_name)
        self.assertEqual(idf2.generatormicrochps[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.generatormicrochps[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.generatormicrochps[0].generator_fuel_supply_name, var_generator_fuel_supply_name)
        self.assertEqual(idf2.generatormicrochps[0].availability_schedule_name, var_availability_schedule_name)