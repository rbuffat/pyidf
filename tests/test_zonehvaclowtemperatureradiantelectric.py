import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_radiative import ZoneHvacLowTemperatureRadiantElectric

log = logging.getLogger(__name__)

class TestZoneHvacLowTemperatureRadiantElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvaclowtemperatureradiantelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacLowTemperatureRadiantElectric()
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
        var_surface_name_or_radiant_surface_group_name = "object-list|Surface Name or Radiant Surface Group Name"
        obj.surface_name_or_radiant_surface_group_name = var_surface_name_or_radiant_surface_group_name
        # alpha
        var_heating_design_capacity_method = "HeatingDesignCapacity"
        obj.heating_design_capacity_method = var_heating_design_capacity_method
        # real
        var_heating_design_capacity = 0.0
        obj.heating_design_capacity = var_heating_design_capacity
        # real
        var_heating_design_capacity_per_floor_area = 0.0
        obj.heating_design_capacity_per_floor_area = var_heating_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_heating_design_capacity = 0.0
        obj.fraction_of_autosized_heating_design_capacity = var_fraction_of_autosized_heating_design_capacity
        # alpha
        var_temperature_control_type = "MeanAirTemperature"
        obj.temperature_control_type = var_temperature_control_type
        # real
        var_heating_throttling_range = 0.0
        obj.heating_throttling_range = var_heating_throttling_range
        # object-list
        var_heating_setpoint_temperature_schedule_name = "object-list|Heating Setpoint Temperature Schedule Name"
        obj.heating_setpoint_temperature_schedule_name = var_heating_setpoint_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].name, var_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].surface_name_or_radiant_surface_group_name, var_surface_name_or_radiant_surface_group_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].temperature_control_type, var_temperature_control_type)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].heating_throttling_range, var_heating_throttling_range)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantelectrics[0].heating_setpoint_temperature_schedule_name, var_heating_setpoint_temperature_schedule_name)