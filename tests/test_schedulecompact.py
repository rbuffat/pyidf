import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleCompact
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleCompact(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_schedulecompact(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleCompact()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        paras = []
        var_field = "Field"
        paras.append(var_field)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.schedulecompacts[0].name, var_name)
        self.assertEqual(idf2.schedulecompacts[0].schedule_type_limits_name, var_schedule_type_limits_name)
        index = obj.extensible_field_index("Field")
        self.assertEqual(idf2.schedulecompacts[0].extensibles[0][index], var_field)