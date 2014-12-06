import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelCell
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelCell(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcell(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCell()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_power_module_name = "object-list|Power Module Name"
        obj.power_module_name = var_power_module_name
        # object-list
        var_air_supply_name = "object-list|Air Supply Name"
        obj.air_supply_name = var_air_supply_name
        # object-list
        var_fuel_supply_name = "object-list|Fuel Supply Name"
        obj.fuel_supply_name = var_fuel_supply_name
        # object-list
        var_water_supply_name = "object-list|Water Supply Name"
        obj.water_supply_name = var_water_supply_name
        # object-list
        var_auxiliary_heater_name = "object-list|Auxiliary Heater Name"
        obj.auxiliary_heater_name = var_auxiliary_heater_name
        # object-list
        var_heat_exchanger_name = "object-list|Heat Exchanger Name"
        obj.heat_exchanger_name = var_heat_exchanger_name
        # object-list
        var_electrical_storage_name = "object-list|Electrical Storage Name"
        obj.electrical_storage_name = var_electrical_storage_name
        # object-list
        var_inverter_name = "object-list|Inverter Name"
        obj.inverter_name = var_inverter_name
        # object-list
        var_stack_cooler_name = "object-list|Stack Cooler Name"
        obj.stack_cooler_name = var_stack_cooler_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcells[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcells[0].power_module_name, var_power_module_name)
        self.assertEqual(idf2.generatorfuelcells[0].air_supply_name, var_air_supply_name)
        self.assertEqual(idf2.generatorfuelcells[0].fuel_supply_name, var_fuel_supply_name)
        self.assertEqual(idf2.generatorfuelcells[0].water_supply_name, var_water_supply_name)
        self.assertEqual(idf2.generatorfuelcells[0].auxiliary_heater_name, var_auxiliary_heater_name)
        self.assertEqual(idf2.generatorfuelcells[0].heat_exchanger_name, var_heat_exchanger_name)
        self.assertEqual(idf2.generatorfuelcells[0].electrical_storage_name, var_electrical_storage_name)
        self.assertEqual(idf2.generatorfuelcells[0].inverter_name, var_inverter_name)
        self.assertEqual(idf2.generatorfuelcells[0].stack_cooler_name, var_stack_cooler_name)