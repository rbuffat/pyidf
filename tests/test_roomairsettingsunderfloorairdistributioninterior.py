import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import RoomAirSettingsUnderFloorAirDistributionInterior
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRoomAirSettingsUnderFloorAirDistributionInterior(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingsunderfloorairdistributioninterior(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsUnderFloorAirDistributionInterior()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_number_of_diffusers = 0.0001
        obj.number_of_diffusers = var_number_of_diffusers
        # real
        var_power_per_plume = 0.0
        obj.power_per_plume = var_power_per_plume
        # real
        var_design_effective_area_of_diffuser = 0.0001
        obj.design_effective_area_of_diffuser = var_design_effective_area_of_diffuser
        # real
        var_diffuser_slot_angle_from_vertical = 45.0
        obj.diffuser_slot_angle_from_vertical = var_diffuser_slot_angle_from_vertical
        # real
        var_thermostat_height = 0.0001
        obj.thermostat_height = var_thermostat_height
        # real
        var_comfort_height = 0.0001
        obj.comfort_height = var_comfort_height
        # real
        var_temperature_difference_threshold_for_reporting = 0.0
        obj.temperature_difference_threshold_for_reporting = var_temperature_difference_threshold_for_reporting
        # alpha
        var_floor_diffuser_type = "Custom"
        obj.floor_diffuser_type = var_floor_diffuser_type
        # real
        var_transition_height = 0.0001
        obj.transition_height = var_transition_height
        # real
        var_coefficient_a = 11.11
        obj.coefficient_a = var_coefficient_a
        # real
        var_coefficient_b = 12.12
        obj.coefficient_b = var_coefficient_b
        # real
        var_coefficient_c = 13.13
        obj.coefficient_c = var_coefficient_c
        # real
        var_coefficient_d = 14.14
        obj.coefficient_d = var_coefficient_d
        # real
        var_coefficient_e = 15.15
        obj.coefficient_e = var_coefficient_e

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].number_of_diffusers, var_number_of_diffusers)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].power_per_plume, var_power_per_plume)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].design_effective_area_of_diffuser, var_design_effective_area_of_diffuser)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].diffuser_slot_angle_from_vertical, var_diffuser_slot_angle_from_vertical)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].thermostat_height, var_thermostat_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].comfort_height, var_comfort_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].temperature_difference_threshold_for_reporting, var_temperature_difference_threshold_for_reporting)
        self.assertEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].floor_diffuser_type, var_floor_diffuser_type)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].transition_height, var_transition_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].coefficient_a, var_coefficient_a)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].coefficient_b, var_coefficient_b)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].coefficient_c, var_coefficient_c)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].coefficient_d, var_coefficient_d)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributioninteriors[0].coefficient_e, var_coefficient_e)