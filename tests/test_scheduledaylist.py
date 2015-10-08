import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.schedules import ScheduleDayList

log = logging.getLogger(__name__)

class TestScheduleDayList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduledaylist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleDayList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # alpha
        var_interpolate_to_timestep = "Yes"
        obj.interpolate_to_timestep = var_interpolate_to_timestep
        # integer
        var_minutes_per_item = 30
        obj.minutes_per_item = var_minutes_per_item
        paras = []
        var_value = 5.5
        paras.append(var_value)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduledaylists[0].name, var_name)
        self.assertEqual(idf2.scheduledaylists[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertEqual(idf2.scheduledaylists[0].interpolate_to_timestep, var_interpolate_to_timestep)
        self.assertEqual(idf2.scheduledaylists[0].minutes_per_item, var_minutes_per_item)
        index = obj.extensible_field_index("Value")
        self.assertAlmostEqual(idf2.scheduledaylists[0].extensibles[0][index], var_value)