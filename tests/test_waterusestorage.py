import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_systems import WaterUseStorage

log = logging.getLogger(__name__)

class TestWaterUseStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterusestorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterUseStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_water_quality_subcategory = "Water Quality Subcategory"
        obj.water_quality_subcategory = var_water_quality_subcategory
        # real
        var_maximum_capacity = 3.3
        obj.maximum_capacity = var_maximum_capacity
        # real
        var_initial_volume = 4.4
        obj.initial_volume = var_initial_volume
        # real
        var_design_in_flow_rate = 5.5
        obj.design_in_flow_rate = var_design_in_flow_rate
        # real
        var_design_out_flow_rate = 6.6
        obj.design_out_flow_rate = var_design_out_flow_rate
        # object-list
        var_overflow_destination = "object-list|Overflow Destination"
        obj.overflow_destination = var_overflow_destination
        # alpha
        var_type_of_supply_controlled_by_float_valve = "None"
        obj.type_of_supply_controlled_by_float_valve = var_type_of_supply_controlled_by_float_valve
        # real
        var_float_valve_on_capacity = 9.9
        obj.float_valve_on_capacity = var_float_valve_on_capacity
        # real
        var_float_valve_off_capacity = 10.1
        obj.float_valve_off_capacity = var_float_valve_off_capacity
        # real
        var_backup_mains_capacity = 11.11
        obj.backup_mains_capacity = var_backup_mains_capacity
        # object-list
        var_other_tank_name = "object-list|Other Tank Name"
        obj.other_tank_name = var_other_tank_name
        # alpha
        var_water_thermal_mode = "ScheduledTemperature"
        obj.water_thermal_mode = var_water_thermal_mode
        # object-list
        var_water_temperature_schedule_name = "object-list|Water Temperature Schedule Name"
        obj.water_temperature_schedule_name = var_water_temperature_schedule_name
        # alpha
        var_ambient_temperature_indicator = "Schedule"
        obj.ambient_temperature_indicator = var_ambient_temperature_indicator
        # object-list
        var_ambient_temperature_schedule_name = "object-list|Ambient Temperature Schedule Name"
        obj.ambient_temperature_schedule_name = var_ambient_temperature_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_tank_surface_area = 18.18
        obj.tank_surface_area = var_tank_surface_area
        # real
        var_tank_u_value = 19.19
        obj.tank_u_value = var_tank_u_value
        # object-list
        var_tank_outside_surface_material_name = "object-list|Tank Outside Surface Material Name"
        obj.tank_outside_surface_material_name = var_tank_outside_surface_material_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterusestorages[0].name, var_name)
        self.assertEqual(idf2.waterusestorages[0].water_quality_subcategory, var_water_quality_subcategory)
        self.assertAlmostEqual(idf2.waterusestorages[0].maximum_capacity, var_maximum_capacity)
        self.assertAlmostEqual(idf2.waterusestorages[0].initial_volume, var_initial_volume)
        self.assertAlmostEqual(idf2.waterusestorages[0].design_in_flow_rate, var_design_in_flow_rate)
        self.assertAlmostEqual(idf2.waterusestorages[0].design_out_flow_rate, var_design_out_flow_rate)
        self.assertEqual(idf2.waterusestorages[0].overflow_destination, var_overflow_destination)
        self.assertEqual(idf2.waterusestorages[0].type_of_supply_controlled_by_float_valve, var_type_of_supply_controlled_by_float_valve)
        self.assertAlmostEqual(idf2.waterusestorages[0].float_valve_on_capacity, var_float_valve_on_capacity)
        self.assertAlmostEqual(idf2.waterusestorages[0].float_valve_off_capacity, var_float_valve_off_capacity)
        self.assertAlmostEqual(idf2.waterusestorages[0].backup_mains_capacity, var_backup_mains_capacity)
        self.assertEqual(idf2.waterusestorages[0].other_tank_name, var_other_tank_name)
        self.assertEqual(idf2.waterusestorages[0].water_thermal_mode, var_water_thermal_mode)
        self.assertEqual(idf2.waterusestorages[0].water_temperature_schedule_name, var_water_temperature_schedule_name)
        self.assertEqual(idf2.waterusestorages[0].ambient_temperature_indicator, var_ambient_temperature_indicator)
        self.assertEqual(idf2.waterusestorages[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.waterusestorages[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.waterusestorages[0].tank_surface_area, var_tank_surface_area)
        self.assertAlmostEqual(idf2.waterusestorages[0].tank_u_value, var_tank_u_value)
        self.assertEqual(idf2.waterusestorages[0].tank_outside_surface_material_name, var_tank_outside_surface_material_name)