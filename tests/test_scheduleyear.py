import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.schedules import ScheduleYear

log = logging.getLogger(__name__)

class TestScheduleYear(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduleyear(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleYear()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        paras = []
        var_scheduleweek = "object-list|Schedule:Week"
        paras.append(var_scheduleweek)
        var_start_month = 6
        paras.append(var_start_month)
        var_start_day = 16
        paras.append(var_start_day)
        var_end_month = 6
        paras.append(var_end_month)
        var_end_day = 16
        paras.append(var_end_day)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduleyears[0].name, var_name)
        self.assertEqual(idf2.scheduleyears[0].schedule_type_limits_name, var_schedule_type_limits_name)
        index = obj.extensible_field_index("Schedule:Week")
        self.assertEqual(idf2.scheduleyears[0].extensibles[0][index], var_scheduleweek)
        index = obj.extensible_field_index("Start Month")
        self.assertEqual(idf2.scheduleyears[0].extensibles[0][index], var_start_month)
        index = obj.extensible_field_index("Start Day")
        self.assertEqual(idf2.scheduleyears[0].extensibles[0][index], var_start_day)
        index = obj.extensible_field_index("End Month")
        self.assertEqual(idf2.scheduleyears[0].extensibles[0][index], var_end_month)
        index = obj.extensible_field_index("End Day")
        self.assertEqual(idf2.scheduleyears[0].extensibles[0][index], var_end_day)