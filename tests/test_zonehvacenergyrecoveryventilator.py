import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_forced_air_units import ZoneHvacEnergyRecoveryVentilator
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacEnergyRecoveryVentilator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacenergyrecoveryventilator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacEnergyRecoveryVentilator()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_heat_exchanger_name = "object-list|Heat Exchanger Name"
        obj.heat_exchanger_name = var_heat_exchanger_name
        # real
        var_supply_air_flow_rate = 0.0001
        obj.supply_air_flow_rate = var_supply_air_flow_rate
        # real
        var_exhaust_air_flow_rate = 0.0001
        obj.exhaust_air_flow_rate = var_exhaust_air_flow_rate
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # object-list
        var_exhaust_air_fan_name = "object-list|Exhaust Air Fan Name"
        obj.exhaust_air_fan_name = var_exhaust_air_fan_name
        # object-list
        var_controller_name = "object-list|Controller Name"
        obj.controller_name = var_controller_name
        # real
        var_ventilation_rate_per_unit_floor_area = 0.0
        obj.ventilation_rate_per_unit_floor_area = var_ventilation_rate_per_unit_floor_area
        # real
        var_ventilation_rate_per_occupant = 0.0
        obj.ventilation_rate_per_occupant = var_ventilation_rate_per_occupant
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].name, var_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].heat_exchanger_name, var_heat_exchanger_name)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilators[0].supply_air_flow_rate, var_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilators[0].exhaust_air_flow_rate, var_exhaust_air_flow_rate)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].exhaust_air_fan_name, var_exhaust_air_fan_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].controller_name, var_controller_name)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilators[0].ventilation_rate_per_unit_floor_area, var_ventilation_rate_per_unit_floor_area)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilators[0].ventilation_rate_per_occupant, var_ventilation_rate_per_occupant)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilators[0].availability_manager_list_name, var_availability_manager_list_name)