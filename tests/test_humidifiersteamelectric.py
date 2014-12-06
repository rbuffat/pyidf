import os
import tempfile
import unittest
import pyidf
from pyidf.humidifiers_and_dehumidifiers import HumidifierSteamElectric
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHumidifierSteamElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_humidifiersteamelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HumidifierSteamElectric()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_rated_capacity = 0.0
        obj.rated_capacity = var_rated_capacity
        # real
        var_rated_power = 0.0
        obj.rated_power = var_rated_power
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_standby_power = 0.0
        obj.standby_power = var_standby_power
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_water_storage_tank_name = "object-list|Water Storage Tank Name"
        obj.water_storage_tank_name = var_water_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.humidifiersteamelectrics[0].name, var_name)
        self.assertEqual(idf2.humidifiersteamelectrics[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.humidifiersteamelectrics[0].rated_capacity, var_rated_capacity)
        self.assertAlmostEqual(idf2.humidifiersteamelectrics[0].rated_power, var_rated_power)
        self.assertAlmostEqual(idf2.humidifiersteamelectrics[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.humidifiersteamelectrics[0].standby_power, var_standby_power)
        self.assertEqual(idf2.humidifiersteamelectrics[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.humidifiersteamelectrics[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.humidifiersteamelectrics[0].water_storage_tank_name, var_water_storage_tank_name)