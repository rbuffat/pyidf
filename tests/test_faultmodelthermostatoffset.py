import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.operational_faults import FaultModelThermostatOffset

log = logging.getLogger(__name__)

class TestFaultModelThermostatOffset(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelthermostatoffset(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelThermostatOffset()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_thermostat_name = "object-list|Thermostat Name"
        obj.thermostat_name = var_thermostat_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_severity_schedule_name = "object-list|Severity Schedule Name"
        obj.severity_schedule_name = var_severity_schedule_name
        # real
        var_reference_thermostat_offset = 0.0
        obj.reference_thermostat_offset = var_reference_thermostat_offset

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelthermostatoffsets[0].name, var_name)
        self.assertEqual(idf2.faultmodelthermostatoffsets[0].thermostat_name, var_thermostat_name)
        self.assertEqual(idf2.faultmodelthermostatoffsets[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelthermostatoffsets[0].severity_schedule_name, var_severity_schedule_name)
        self.assertAlmostEqual(idf2.faultmodelthermostatoffsets[0].reference_thermostat_offset, var_reference_thermostat_offset)