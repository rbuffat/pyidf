import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_controls_and_thermostats import ThermostatSetpointSingleHeatingOrCooling

log = logging.getLogger(__name__)

class TestThermostatSetpointSingleHeatingOrCooling(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermostatsetpointsingleheatingorcooling(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermostatSetpointSingleHeatingOrCooling()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_setpoint_temperature_schedule_name = "object-list|Setpoint Temperature Schedule Name"
        obj.setpoint_temperature_schedule_name = var_setpoint_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermostatsetpointsingleheatingorcoolings[0].name, var_name)
        self.assertEqual(idf2.thermostatsetpointsingleheatingorcoolings[0].setpoint_temperature_schedule_name, var_setpoint_temperature_schedule_name)