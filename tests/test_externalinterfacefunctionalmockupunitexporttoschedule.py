import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitExportToSchedule

log = logging.getLogger(__name__)

class TestExternalInterfaceFunctionalMockupUnitExportToSchedule(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitexporttoschedule(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitExportToSchedule()
        # alpha
        var_schedule_name = "Schedule Name"
        obj.schedule_name = var_schedule_name
        # object-list
        var_schedule_type_limits_names = "object-list|Schedule Type Limits Names"
        obj.schedule_type_limits_names = var_schedule_type_limits_names
        # alpha
        var_fmu_variable_name = "FMU Variable Name"
        obj.fmu_variable_name = var_fmu_variable_name
        # real
        var_initial_value = 4.4
        obj.initial_value = var_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoschedules[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoschedules[0].schedule_type_limits_names, var_schedule_type_limits_names)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexporttoschedules[0].fmu_variable_name, var_fmu_variable_name)
        self.assertAlmostEqual(idf2.externalinterfacefunctionalmockupunitexporttoschedules[0].initial_value, var_initial_value)