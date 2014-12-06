import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.external_interface import ExternalInterfaceSchedule

log = logging.getLogger(__name__)

class TestExternalInterfaceSchedule(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfaceschedule(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceSchedule()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # real
        var_initial_value = 3.3
        obj.initial_value = var_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfaceschedules[0].name, var_name)
        self.assertEqual(idf2.externalinterfaceschedules[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertAlmostEqual(idf2.externalinterfaceschedules[0].initial_value, var_initial_value)