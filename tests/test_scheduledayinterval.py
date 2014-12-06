import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleDayInterval
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleDayInterval(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduledayinterval(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleDayInterval()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # alpha
        var_interpolate_to_timestep = "Yes"
        obj.interpolate_to_timestep = var_interpolate_to_timestep
        paras = []
        var_time_1 = "Time 1"
        paras.append(var_time_1)
        var_value_until_time_1 = 5.5
        paras.append(var_value_until_time_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduledayintervals[0].name, var_name)
        self.assertEqual(idf2.scheduledayintervals[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertEqual(idf2.scheduledayintervals[0].interpolate_to_timestep, var_interpolate_to_timestep)
        index = obj.extensible_field_index("Time 1")
        self.assertEqual(idf2.scheduledayintervals[0].extensibles[0][index], var_time_1)
        index = obj.extensible_field_index("Value Until Time 1")
        self.assertAlmostEqual(idf2.scheduledayintervals[0].extensibles[0][index], var_value_until_time_1)