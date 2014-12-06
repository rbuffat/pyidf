import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ThermostatSetpointThermalComfortFangerSingleHeating
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestThermostatSetpointThermalComfortFangerSingleHeating(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermostatsetpointthermalcomfortfangersingleheating(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermostatSetpointThermalComfortFangerSingleHeating()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_fanger_thermal_comfort_schedule_name = "object-list|Fanger Thermal Comfort Schedule Name"
        obj.fanger_thermal_comfort_schedule_name = var_fanger_thermal_comfort_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermostatsetpointthermalcomfortfangersingleheatings[0].name, var_name)
        self.assertEqual(idf2.thermostatsetpointthermalcomfortfangersingleheatings[0].fanger_thermal_comfort_schedule_name, var_fanger_thermal_comfort_schedule_name)