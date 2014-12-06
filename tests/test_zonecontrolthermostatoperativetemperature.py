import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostatOperativeTemperature
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneControlThermostatOperativeTemperature(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolthermostatoperativetemperature(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlThermostatOperativeTemperature()
        # object-list
        var_thermostat_name = "object-list|Thermostat Name"
        obj.thermostat_name = var_thermostat_name
        # alpha
        var_radiative_fraction_input_mode = "Constant"
        obj.radiative_fraction_input_mode = var_radiative_fraction_input_mode
        # real
        var_fixed_radiative_fraction = 0.44995
        obj.fixed_radiative_fraction = var_fixed_radiative_fraction
        # object-list
        var_radiative_fraction_schedule_name = "object-list|Radiative Fraction Schedule Name"
        obj.radiative_fraction_schedule_name = var_radiative_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolthermostatoperativetemperatures[0].thermostat_name, var_thermostat_name)
        self.assertEqual(idf2.zonecontrolthermostatoperativetemperatures[0].radiative_fraction_input_mode, var_radiative_fraction_input_mode)
        self.assertAlmostEqual(idf2.zonecontrolthermostatoperativetemperatures[0].fixed_radiative_fraction, var_fixed_radiative_fraction)
        self.assertEqual(idf2.zonecontrolthermostatoperativetemperatures[0].radiative_fraction_schedule_name, var_radiative_fraction_schedule_name)