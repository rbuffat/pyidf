import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleConstant
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleConstant(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduleconstant(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleConstant()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # real
        var_hourly_value = 3.3
        obj.hourly_value = var_hourly_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduleconstants[0].name, var_name)
        self.assertEqual(idf2.scheduleconstants[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertAlmostEqual(idf2.scheduleconstants[0].hourly_value, var_hourly_value)