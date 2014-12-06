import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ThermostatSetpointDualSetpoint
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestThermostatSetpointDualSetpoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermostatsetpointdualsetpoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermostatSetpointDualSetpoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_heating_setpoint_temperature_schedule_name = "object-list|Heating Setpoint Temperature Schedule Name"
        obj.heating_setpoint_temperature_schedule_name = var_heating_setpoint_temperature_schedule_name
        # object-list
        var_cooling_setpoint_temperature_schedule_name = "object-list|Cooling Setpoint Temperature Schedule Name"
        obj.cooling_setpoint_temperature_schedule_name = var_cooling_setpoint_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermostatsetpointdualsetpoints[0].name, var_name)
        self.assertEqual(idf2.thermostatsetpointdualsetpoints[0].heating_setpoint_temperature_schedule_name, var_heating_setpoint_temperature_schedule_name)
        self.assertEqual(idf2.thermostatsetpointdualsetpoints[0].cooling_setpoint_temperature_schedule_name, var_cooling_setpoint_temperature_schedule_name)