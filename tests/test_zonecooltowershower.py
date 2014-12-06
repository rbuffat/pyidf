import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneCoolTowerShower

log = logging.getLogger(__name__)

class TestZoneCoolTowerShower(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecooltowershower(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneCoolTowerShower()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_water_supply_storage_tank_name = "object-list|Water Supply Storage Tank Name"
        obj.water_supply_storage_tank_name = var_water_supply_storage_tank_name
        # alpha
        var_flow_control_type = "WaterFlowSchedule"
        obj.flow_control_type = var_flow_control_type
        # object-list
        var_pump_flow_rate_schedule_name = "object-list|Pump Flow Rate Schedule Name"
        obj.pump_flow_rate_schedule_name = var_pump_flow_rate_schedule_name
        # real
        var_maximum_water_flow_rate = 7.7
        obj.maximum_water_flow_rate = var_maximum_water_flow_rate
        # real
        var_effective_tower_height = 8.8
        obj.effective_tower_height = var_effective_tower_height
        # real
        var_airflow_outlet_area = 9.9
        obj.airflow_outlet_area = var_airflow_outlet_area
        # real
        var_maximum_air_flow_rate = 0.0
        obj.maximum_air_flow_rate = var_maximum_air_flow_rate
        # real
        var_minimum_indoor_temperature = 0.0
        obj.minimum_indoor_temperature = var_minimum_indoor_temperature
        # real
        var_fraction_of_water_loss = 0.5
        obj.fraction_of_water_loss = var_fraction_of_water_loss
        # real
        var_fraction_of_flow_schedule = 0.5
        obj.fraction_of_flow_schedule = var_fraction_of_flow_schedule
        # real
        var_rated_power_consumption = 14.14
        obj.rated_power_consumption = var_rated_power_consumption

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecooltowershowers[0].name, var_name)
        self.assertEqual(idf2.zonecooltowershowers[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonecooltowershowers[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonecooltowershowers[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)
        self.assertEqual(idf2.zonecooltowershowers[0].flow_control_type, var_flow_control_type)
        self.assertEqual(idf2.zonecooltowershowers[0].pump_flow_rate_schedule_name, var_pump_flow_rate_schedule_name)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].maximum_water_flow_rate, var_maximum_water_flow_rate)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].effective_tower_height, var_effective_tower_height)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].airflow_outlet_area, var_airflow_outlet_area)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].maximum_air_flow_rate, var_maximum_air_flow_rate)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].minimum_indoor_temperature, var_minimum_indoor_temperature)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].fraction_of_water_loss, var_fraction_of_water_loss)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].fraction_of_flow_schedule, var_fraction_of_flow_schedule)
        self.assertAlmostEqual(idf2.zonecooltowershowers[0].rated_power_consumption, var_rated_power_consumption)