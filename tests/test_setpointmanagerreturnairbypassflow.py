import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerReturnAirBypassFlow

log = logging.getLogger(__name__)

class TestSetpointManagerReturnAirBypassFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerreturnairbypassflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerReturnAirBypassFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Flow"
        obj.control_variable = var_control_variable
        # object-list
        var_hvac_air_loop_name = "object-list|HVAC Air Loop Name"
        obj.hvac_air_loop_name = var_hvac_air_loop_name
        # object-list
        var_temperature_setpoint_schedule_name = "object-list|Temperature Setpoint Schedule Name"
        obj.temperature_setpoint_schedule_name = var_temperature_setpoint_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagerreturnairbypassflows[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerreturnairbypassflows[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerreturnairbypassflows[0].hvac_air_loop_name, var_hvac_air_loop_name)
        self.assertEqual(idf2.setpointmanagerreturnairbypassflows[0].temperature_setpoint_schedule_name, var_temperature_setpoint_schedule_name)