import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateThermostat

log = logging.getLogger(__name__)

class TestHvactemplateThermostat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatethermostat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateThermostat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_heating_setpoint_schedule_name = "object-list|Heating Setpoint Schedule Name"
        obj.heating_setpoint_schedule_name = var_heating_setpoint_schedule_name
        # real
        var_constant_heating_setpoint = 3.3
        obj.constant_heating_setpoint = var_constant_heating_setpoint
        # object-list
        var_cooling_setpoint_schedule_name = "object-list|Cooling Setpoint Schedule Name"
        obj.cooling_setpoint_schedule_name = var_cooling_setpoint_schedule_name
        # real
        var_constant_cooling_setpoint = 5.5
        obj.constant_cooling_setpoint = var_constant_cooling_setpoint

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatethermostats[0].name, var_name)
        self.assertEqual(idf2.hvactemplatethermostats[0].heating_setpoint_schedule_name, var_heating_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatethermostats[0].constant_heating_setpoint, var_constant_heating_setpoint)
        self.assertEqual(idf2.hvactemplatethermostats[0].cooling_setpoint_schedule_name, var_cooling_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatethermostats[0].constant_cooling_setpoint, var_constant_cooling_setpoint)