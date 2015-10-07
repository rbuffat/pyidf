import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.humidifiers_and_dehumidifiers import HumidifierSteamGas

log = logging.getLogger(__name__)

class TestHumidifierSteamGas(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_humidifiersteamgas(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HumidifierSteamGas()
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
        var_rated_gas_use_rate = 0.0
        obj.rated_gas_use_rate = var_rated_gas_use_rate
        # real
        var_thermal_efficiency = 0.50005
        obj.thermal_efficiency = var_thermal_efficiency
        # object-list
        var_thermal_efficiency_modifier_curve_name = "object-list|Thermal Efficiency Modifier Curve Name"
        obj.thermal_efficiency_modifier_curve_name = var_thermal_efficiency_modifier_curve_name
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_auxiliary_electric_power = 0.0
        obj.auxiliary_electric_power = var_auxiliary_electric_power
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_water_storage_tank_name = "object-list|Water Storage Tank Name"
        obj.water_storage_tank_name = var_water_storage_tank_name
        # alpha
        var_inlet_water_temperature_option = "FixedInletWaterTemperature"
        obj.inlet_water_temperature_option = var_inlet_water_temperature_option

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.humidifiersteamgass[0].name, var_name)
        self.assertEqual(idf2.humidifiersteamgass[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.humidifiersteamgass[0].rated_capacity, var_rated_capacity)
        self.assertAlmostEqual(idf2.humidifiersteamgass[0].rated_gas_use_rate, var_rated_gas_use_rate)
        self.assertAlmostEqual(idf2.humidifiersteamgass[0].thermal_efficiency, var_thermal_efficiency)
        self.assertEqual(idf2.humidifiersteamgass[0].thermal_efficiency_modifier_curve_name, var_thermal_efficiency_modifier_curve_name)
        self.assertAlmostEqual(idf2.humidifiersteamgass[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.humidifiersteamgass[0].auxiliary_electric_power, var_auxiliary_electric_power)
        self.assertEqual(idf2.humidifiersteamgass[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.humidifiersteamgass[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.humidifiersteamgass[0].water_storage_tank_name, var_water_storage_tank_name)
        self.assertEqual(idf2.humidifiersteamgass[0].inlet_water_temperature_option, var_inlet_water_temperature_option)