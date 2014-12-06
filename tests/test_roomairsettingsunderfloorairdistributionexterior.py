import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirSettingsUnderFloorAirDistributionExterior

log = logging.getLogger(__name__)

class TestRoomAirSettingsUnderFloorAirDistributionExterior(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingsunderfloorairdistributionexterior(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsUnderFloorAirDistributionExterior()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_number_of_diffusers_per_zone = 0.0001
        obj.number_of_diffusers_per_zone = var_number_of_diffusers_per_zone
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
        var_coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = 11.11
        obj.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = var_coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2
        # real
        var_coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = 12.12
        obj.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = var_coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2
        # real
        var_coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = 13.13
        obj.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = var_coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2
        # real
        var_coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = 14.14
        obj.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = var_coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2
        # real
        var_coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = 15.15
        obj.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = var_coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].number_of_diffusers_per_zone, var_number_of_diffusers_per_zone)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].power_per_plume, var_power_per_plume)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].design_effective_area_of_diffuser, var_design_effective_area_of_diffuser)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].diffuser_slot_angle_from_vertical, var_diffuser_slot_angle_from_vertical)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].thermostat_height, var_thermostat_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].comfort_height, var_comfort_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].temperature_difference_threshold_for_reporting, var_temperature_difference_threshold_for_reporting)
        self.assertEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].floor_diffuser_type, var_floor_diffuser_type)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].transition_height, var_transition_height)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2, var_coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2, var_coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2, var_coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2, var_coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2)
        self.assertAlmostEqual(idf2.roomairsettingsunderfloorairdistributionexteriors[0].coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2, var_coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2)