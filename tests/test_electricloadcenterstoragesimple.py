import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import ElectricLoadCenterStorageSimple

log = logging.getLogger(__name__)

class TestElectricLoadCenterStorageSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterstoragesimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterStorageSimple()
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
        var_radiative_fraction_for_zone_heat_gains = 0.5
        obj.radiative_fraction_for_zone_heat_gains = var_radiative_fraction_for_zone_heat_gains
        # real
        var_nominal_energetic_efficiency_for_charging = 0.5
        obj.nominal_energetic_efficiency_for_charging = var_nominal_energetic_efficiency_for_charging
        # real
        var_nominal_discharging_energetic_efficiency = 0.5
        obj.nominal_discharging_energetic_efficiency = var_nominal_discharging_energetic_efficiency
        # real
        var_maximum_storage_capacity = 7.7
        obj.maximum_storage_capacity = var_maximum_storage_capacity
        # real
        var_maximum_power_for_discharging = 8.8
        obj.maximum_power_for_discharging = var_maximum_power_for_discharging
        # real
        var_maximum_power_for_charging = 9.9
        obj.maximum_power_for_charging = var_maximum_power_for_charging
        # real
        var_initial_state_of_charge = 10.1
        obj.initial_state_of_charge = var_initial_state_of_charge

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterstoragesimples[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterstoragesimples[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcenterstoragesimples[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].radiative_fraction_for_zone_heat_gains, var_radiative_fraction_for_zone_heat_gains)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].nominal_energetic_efficiency_for_charging, var_nominal_energetic_efficiency_for_charging)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].nominal_discharging_energetic_efficiency, var_nominal_discharging_energetic_efficiency)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].maximum_storage_capacity, var_maximum_storage_capacity)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].maximum_power_for_discharging, var_maximum_power_for_discharging)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].maximum_power_for_charging, var_maximum_power_for_charging)
        self.assertAlmostEqual(idf2.electricloadcenterstoragesimples[0].initial_state_of_charge, var_initial_state_of_charge)