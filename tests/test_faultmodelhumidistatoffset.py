import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.operational_faults import FaultModelHumidistatOffset

log = logging.getLogger(__name__)

class TestFaultModelHumidistatOffset(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelhumidistatoffset(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelHumidistatOffset()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_humidistat_name = "object-list|Humidistat Name"
        obj.humidistat_name = var_humidistat_name
        # alpha
        var_humidistat_offset_type = "ThermostatOffsetIndependent"
        obj.humidistat_offset_type = var_humidistat_offset_type
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_severity_schedule_name = "object-list|Severity Schedule Name"
        obj.severity_schedule_name = var_severity_schedule_name
        # real
        var_reference_humidistat_offset = 0.0
        obj.reference_humidistat_offset = var_reference_humidistat_offset
        # object-list
        var_related_thermostat_offset_fault_name = "object-list|Related Thermostat Offset Fault Name"
        obj.related_thermostat_offset_fault_name = var_related_thermostat_offset_fault_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].name, var_name)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].humidistat_name, var_humidistat_name)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].humidistat_offset_type, var_humidistat_offset_type)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].severity_schedule_name, var_severity_schedule_name)
        self.assertAlmostEqual(idf2.faultmodelhumidistatoffsets[0].reference_humidistat_offset, var_reference_humidistat_offset)
        self.assertEqual(idf2.faultmodelhumidistatoffsets[0].related_thermostat_offset_fault_name, var_related_thermostat_offset_fault_name)