import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_controls_and_thermostats import ThermostatSetpointThermalComfortFangerDualSetpoint
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestThermostatSetpointThermalComfortFangerDualSetpoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermostatsetpointthermalcomfortfangerdualsetpoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermostatSetpointThermalComfortFangerDualSetpoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_fanger_thermal_comfort_heating_schedule_name = "object-list|Fanger Thermal Comfort Heating Schedule Name"
        obj.fanger_thermal_comfort_heating_schedule_name = var_fanger_thermal_comfort_heating_schedule_name
        # object-list
        var_fanger_thermal_comfort_cooling_schedule_name = "object-list|Fanger Thermal Comfort Cooling Schedule Name"
        obj.fanger_thermal_comfort_cooling_schedule_name = var_fanger_thermal_comfort_cooling_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermostatsetpointthermalcomfortfangerdualsetpoints[0].name, var_name)
        self.assertEqual(idf2.thermostatsetpointthermalcomfortfangerdualsetpoints[0].fanger_thermal_comfort_heating_schedule_name, var_fanger_thermal_comfort_heating_schedule_name)
        self.assertEqual(idf2.thermostatsetpointthermalcomfortfangerdualsetpoints[0].fanger_thermal_comfort_cooling_schedule_name, var_fanger_thermal_comfort_cooling_schedule_name)