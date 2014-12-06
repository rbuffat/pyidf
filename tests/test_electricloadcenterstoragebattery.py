import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import ElectricLoadCenterStorageBattery

log = logging.getLogger(__name__)

class TestElectricLoadCenterStorageBattery(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterstoragebattery(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterStorageBattery()
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
        var_radiative_fraction = 0.5
        obj.radiative_fraction = var_radiative_fraction
        # integer
        var_number_of_battery_modules_in_parallel = 1
        obj.number_of_battery_modules_in_parallel = var_number_of_battery_modules_in_parallel
        # integer
        var_number_of_battery_modules_in_series = 1
        obj.number_of_battery_modules_in_series = var_number_of_battery_modules_in_series
        # real
        var_maximum_module_capacity = 0.0
        obj.maximum_module_capacity = var_maximum_module_capacity
        # real
        var_initial_fractional_state_of_charge = 0.5
        obj.initial_fractional_state_of_charge = var_initial_fractional_state_of_charge
        # real
        var_fraction_of_available_charge_capacity = 0.5
        obj.fraction_of_available_charge_capacity = var_fraction_of_available_charge_capacity
        # real
        var_change_rate_from_bound_charge_to_available_charge = 0.0
        obj.change_rate_from_bound_charge_to_available_charge = var_change_rate_from_bound_charge_to_available_charge
        # real
        var_fully_charged_module_open_circuit_voltage = 0.0
        obj.fully_charged_module_open_circuit_voltage = var_fully_charged_module_open_circuit_voltage
        # real
        var_fully_discharged_module_open_circuit_voltage = 0.0
        obj.fully_discharged_module_open_circuit_voltage = var_fully_discharged_module_open_circuit_voltage
        # object-list
        var_voltage_change_curve_name_for_charging = "object-list|Voltage Change Curve Name for Charging"
        obj.voltage_change_curve_name_for_charging = var_voltage_change_curve_name_for_charging
        # object-list
        var_voltage_change_curve_name_for_discharging = "object-list|Voltage Change Curve Name for Discharging"
        obj.voltage_change_curve_name_for_discharging = var_voltage_change_curve_name_for_discharging
        # real
        var_module_internal_electrical_resistance = 0.0
        obj.module_internal_electrical_resistance = var_module_internal_electrical_resistance
        # real
        var_maximum_module_discharging_current = 0.0
        obj.maximum_module_discharging_current = var_maximum_module_discharging_current
        # real
        var_module_cutoff_voltage = 0.0
        obj.module_cutoff_voltage = var_module_cutoff_voltage
        # real
        var_module_charge_rate_limit = 0.0
        obj.module_charge_rate_limit = var_module_charge_rate_limit
        # alpha
        var_battery_life_calculation = "Yes"
        obj.battery_life_calculation = var_battery_life_calculation
        # integer
        var_number_of_cycle_bins = 5
        obj.number_of_cycle_bins = var_number_of_cycle_bins
        # object-list
        var_battery_life_curve_name = "object-list|Battery Life Curve Name"
        obj.battery_life_curve_name = var_battery_life_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].radiative_fraction, var_radiative_fraction)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].number_of_battery_modules_in_parallel, var_number_of_battery_modules_in_parallel)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].number_of_battery_modules_in_series, var_number_of_battery_modules_in_series)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].maximum_module_capacity, var_maximum_module_capacity)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].initial_fractional_state_of_charge, var_initial_fractional_state_of_charge)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].fraction_of_available_charge_capacity, var_fraction_of_available_charge_capacity)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].change_rate_from_bound_charge_to_available_charge, var_change_rate_from_bound_charge_to_available_charge)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].fully_charged_module_open_circuit_voltage, var_fully_charged_module_open_circuit_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].fully_discharged_module_open_circuit_voltage, var_fully_discharged_module_open_circuit_voltage)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].voltage_change_curve_name_for_charging, var_voltage_change_curve_name_for_charging)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].voltage_change_curve_name_for_discharging, var_voltage_change_curve_name_for_discharging)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].module_internal_electrical_resistance, var_module_internal_electrical_resistance)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].maximum_module_discharging_current, var_maximum_module_discharging_current)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].module_cutoff_voltage, var_module_cutoff_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterstoragebatterys[0].module_charge_rate_limit, var_module_charge_rate_limit)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].battery_life_calculation, var_battery_life_calculation)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].number_of_cycle_bins, var_number_of_cycle_bins)
        self.assertEqual(idf2.electricloadcenterstoragebatterys[0].battery_life_curve_name, var_battery_life_curve_name)