import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerNightCycle

log = logging.getLogger(__name__)

class TestAvailabilityManagerNightCycle(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagernightcycle(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerNightCycle()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_applicability_schedule_name = "object-list|Applicability Schedule Name"
        obj.applicability_schedule_name = var_applicability_schedule_name
        # object-list
        var_fan_schedule_name = "object-list|Fan Schedule Name"
        obj.fan_schedule_name = var_fan_schedule_name
        # alpha
        var_control_type = "StayOff"
        obj.control_type = var_control_type
        # real
        var_thermostat_tolerance = 5.5
        obj.thermostat_tolerance = var_thermostat_tolerance
        # real
        var_cycling_run_time = 6.6
        obj.cycling_run_time = var_cycling_run_time
        # object-list
        var_control_zone_name = "object-list|Control Zone Name"
        obj.control_zone_name = var_control_zone_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagernightcycles[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagernightcycles[0].applicability_schedule_name, var_applicability_schedule_name)
        self.assertEqual(idf2.availabilitymanagernightcycles[0].fan_schedule_name, var_fan_schedule_name)
        self.assertEqual(idf2.availabilitymanagernightcycles[0].control_type, var_control_type)
        self.assertAlmostEqual(idf2.availabilitymanagernightcycles[0].thermostat_tolerance, var_thermostat_tolerance)
        self.assertAlmostEqual(idf2.availabilitymanagernightcycles[0].cycling_run_time, var_cycling_run_time)
        self.assertEqual(idf2.availabilitymanagernightcycles[0].control_zone_name, var_control_zone_name)