import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.schedules import ScheduleWeekCompact

log = logging.getLogger(__name__)

class TestScheduleWeekCompact(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduleweekcompact(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleWeekCompact()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_daytype_list_1 = "AllDays"
        paras.append(var_daytype_list_1)
        var_scheduleday_name_1 = "object-list|Schedule:Day Name 1"
        paras.append(var_scheduleday_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduleweekcompacts[0].name, var_name)
        index = obj.extensible_field_index("DayType List 1")
        self.assertEqual(idf2.scheduleweekcompacts[0].extensibles[0][index], var_daytype_list_1)
        index = obj.extensible_field_index("Schedule:Day Name 1")
        self.assertEqual(idf2.scheduleweekcompacts[0].extensibles[0][index], var_scheduleday_name_1)