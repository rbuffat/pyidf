import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationCase
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationCase(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcase(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCase()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_rated_ambient_temperature = 0.0001
        obj.rated_ambient_temperature = var_rated_ambient_temperature
        # real
        var_rated_ambient_relative_humidity = 50.0
        obj.rated_ambient_relative_humidity = var_rated_ambient_relative_humidity
        # real
        var_rated_total_cooling_capacity_per_unit_length = 0.0001
        obj.rated_total_cooling_capacity_per_unit_length = var_rated_total_cooling_capacity_per_unit_length
        # real
        var_rated_latent_heat_ratio = 0.5
        obj.rated_latent_heat_ratio = var_rated_latent_heat_ratio
        # real
        var_rated_runtime_fraction = 0.50005
        obj.rated_runtime_fraction = var_rated_runtime_fraction
        # real
        var_case_length = 0.0001
        obj.case_length = var_case_length
        # real
        var_case_operating_temperature = 19.9999
        obj.case_operating_temperature = var_case_operating_temperature
        # alpha
        var_latent_case_credit_curve_type = "CaseTemperatureMethod"
        obj.latent_case_credit_curve_type = var_latent_case_credit_curve_type
        # object-list
        var_latent_case_credit_curve_name = "object-list|Latent Case Credit Curve Name"
        obj.latent_case_credit_curve_name = var_latent_case_credit_curve_name
        # real
        var_standard_case_fan_power_per_unit_length = 0.0
        obj.standard_case_fan_power_per_unit_length = var_standard_case_fan_power_per_unit_length
        # real
        var_operating_case_fan_power_per_unit_length = 0.0
        obj.operating_case_fan_power_per_unit_length = var_operating_case_fan_power_per_unit_length
        # real
        var_standard_case_lighting_power_per_unit_length = 15.15
        obj.standard_case_lighting_power_per_unit_length = var_standard_case_lighting_power_per_unit_length
        # real
        var_installed_case_lighting_power_per_unit_length = 16.16
        obj.installed_case_lighting_power_per_unit_length = var_installed_case_lighting_power_per_unit_length
        # object-list
        var_case_lighting_schedule_name = "object-list|Case Lighting Schedule Name"
        obj.case_lighting_schedule_name = var_case_lighting_schedule_name
        # real
        var_fraction_of_lighting_energy_to_case = 0.5
        obj.fraction_of_lighting_energy_to_case = var_fraction_of_lighting_energy_to_case
        # real
        var_case_antisweat_heater_power_per_unit_length = 0.0
        obj.case_antisweat_heater_power_per_unit_length = var_case_antisweat_heater_power_per_unit_length
        # real
        var_minimum_antisweat_heater_power_per_unit_length = 0.0
        obj.minimum_antisweat_heater_power_per_unit_length = var_minimum_antisweat_heater_power_per_unit_length
        # alpha
        var_antisweat_heater_control_type = "None"
        obj.antisweat_heater_control_type = var_antisweat_heater_control_type
        # real
        var_humidity_at_zero_antisweat_heater_energy = 22.22
        obj.humidity_at_zero_antisweat_heater_energy = var_humidity_at_zero_antisweat_heater_energy
        # real
        var_case_height = 0.0
        obj.case_height = var_case_height
        # real
        var_fraction_of_antisweat_heater_energy_to_case = 0.5
        obj.fraction_of_antisweat_heater_energy_to_case = var_fraction_of_antisweat_heater_energy_to_case
        # real
        var_case_defrost_power_per_unit_length = 0.0
        obj.case_defrost_power_per_unit_length = var_case_defrost_power_per_unit_length
        # alpha
        var_case_defrost_type = "None"
        obj.case_defrost_type = var_case_defrost_type
        # object-list
        var_case_defrost_schedule_name = "object-list|Case Defrost Schedule Name"
        obj.case_defrost_schedule_name = var_case_defrost_schedule_name
        # object-list
        var_case_defrost_dripdown_schedule_name = "object-list|Case Defrost Drip-Down Schedule Name"
        obj.case_defrost_dripdown_schedule_name = var_case_defrost_dripdown_schedule_name
        # alpha
        var_defrost_energy_correction_curve_type = "None"
        obj.defrost_energy_correction_curve_type = var_defrost_energy_correction_curve_type
        # object-list
        var_defrost_energy_correction_curve_name = "object-list|Defrost Energy Correction Curve Name"
        obj.defrost_energy_correction_curve_name = var_defrost_energy_correction_curve_name
        # real
        var_under_case_hvac_return_air_fraction = 0.5
        obj.under_case_hvac_return_air_fraction = var_under_case_hvac_return_air_fraction
        # object-list
        var_refrigerated_case_restocking_schedule_name = "object-list|Refrigerated Case Restocking Schedule Name"
        obj.refrigerated_case_restocking_schedule_name = var_refrigerated_case_restocking_schedule_name
        # object-list
        var_case_credit_fraction_schedule_name = "object-list|Case Credit Fraction Schedule Name"
        obj.case_credit_fraction_schedule_name = var_case_credit_fraction_schedule_name
        # real
        var_design_evaporator_temperature_or_brine_inlet_temperature = -15.0
        obj.design_evaporator_temperature_or_brine_inlet_temperature = var_design_evaporator_temperature_or_brine_inlet_temperature
        # real
        var_average_refrigerant_charge_inventory = 35.35
        obj.average_refrigerant_charge_inventory = var_average_refrigerant_charge_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcases[0].name, var_name)
        self.assertEqual(idf2.refrigerationcases[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.refrigerationcases[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.refrigerationcases[0].rated_ambient_temperature, var_rated_ambient_temperature)
        self.assertAlmostEqual(idf2.refrigerationcases[0].rated_ambient_relative_humidity, var_rated_ambient_relative_humidity)
        self.assertAlmostEqual(idf2.refrigerationcases[0].rated_total_cooling_capacity_per_unit_length, var_rated_total_cooling_capacity_per_unit_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].rated_latent_heat_ratio, var_rated_latent_heat_ratio)
        self.assertAlmostEqual(idf2.refrigerationcases[0].rated_runtime_fraction, var_rated_runtime_fraction)
        self.assertAlmostEqual(idf2.refrigerationcases[0].case_length, var_case_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].case_operating_temperature, var_case_operating_temperature)
        self.assertEqual(idf2.refrigerationcases[0].latent_case_credit_curve_type, var_latent_case_credit_curve_type)
        self.assertEqual(idf2.refrigerationcases[0].latent_case_credit_curve_name, var_latent_case_credit_curve_name)
        self.assertAlmostEqual(idf2.refrigerationcases[0].standard_case_fan_power_per_unit_length, var_standard_case_fan_power_per_unit_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].operating_case_fan_power_per_unit_length, var_operating_case_fan_power_per_unit_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].standard_case_lighting_power_per_unit_length, var_standard_case_lighting_power_per_unit_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].installed_case_lighting_power_per_unit_length, var_installed_case_lighting_power_per_unit_length)
        self.assertEqual(idf2.refrigerationcases[0].case_lighting_schedule_name, var_case_lighting_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationcases[0].fraction_of_lighting_energy_to_case, var_fraction_of_lighting_energy_to_case)
        self.assertAlmostEqual(idf2.refrigerationcases[0].case_antisweat_heater_power_per_unit_length, var_case_antisweat_heater_power_per_unit_length)
        self.assertAlmostEqual(idf2.refrigerationcases[0].minimum_antisweat_heater_power_per_unit_length, var_minimum_antisweat_heater_power_per_unit_length)
        self.assertEqual(idf2.refrigerationcases[0].antisweat_heater_control_type, var_antisweat_heater_control_type)
        self.assertAlmostEqual(idf2.refrigerationcases[0].humidity_at_zero_antisweat_heater_energy, var_humidity_at_zero_antisweat_heater_energy)
        self.assertAlmostEqual(idf2.refrigerationcases[0].case_height, var_case_height)
        self.assertAlmostEqual(idf2.refrigerationcases[0].fraction_of_antisweat_heater_energy_to_case, var_fraction_of_antisweat_heater_energy_to_case)
        self.assertAlmostEqual(idf2.refrigerationcases[0].case_defrost_power_per_unit_length, var_case_defrost_power_per_unit_length)
        self.assertEqual(idf2.refrigerationcases[0].case_defrost_type, var_case_defrost_type)
        self.assertEqual(idf2.refrigerationcases[0].case_defrost_schedule_name, var_case_defrost_schedule_name)
        self.assertEqual(idf2.refrigerationcases[0].case_defrost_dripdown_schedule_name, var_case_defrost_dripdown_schedule_name)
        self.assertEqual(idf2.refrigerationcases[0].defrost_energy_correction_curve_type, var_defrost_energy_correction_curve_type)
        self.assertEqual(idf2.refrigerationcases[0].defrost_energy_correction_curve_name, var_defrost_energy_correction_curve_name)
        self.assertAlmostEqual(idf2.refrigerationcases[0].under_case_hvac_return_air_fraction, var_under_case_hvac_return_air_fraction)
        self.assertEqual(idf2.refrigerationcases[0].refrigerated_case_restocking_schedule_name, var_refrigerated_case_restocking_schedule_name)
        self.assertEqual(idf2.refrigerationcases[0].case_credit_fraction_schedule_name, var_case_credit_fraction_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationcases[0].design_evaporator_temperature_or_brine_inlet_temperature, var_design_evaporator_temperature_or_brine_inlet_temperature)
        self.assertAlmostEqual(idf2.refrigerationcases[0].average_refrigerant_charge_inventory, var_average_refrigerant_charge_inventory)