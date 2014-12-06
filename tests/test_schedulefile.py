import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.schedules import ScheduleFile

log = logging.getLogger(__name__)

class TestScheduleFile(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_schedulefile(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleFile()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # alpha
        var_file_name = "File Name"
        obj.file_name = var_file_name
        # integer
        var_column_number = 1
        obj.column_number = var_column_number
        # integer
        var_rows_to_skip_at_top = 0
        obj.rows_to_skip_at_top = var_rows_to_skip_at_top
        # real
        var_number_of_hours_of_data = 8772.0
        obj.number_of_hours_of_data = var_number_of_hours_of_data
        # alpha
        var_column_separator = "Comma"
        obj.column_separator = var_column_separator
        # alpha
        var_interpolate_to_timestep = "Yes"
        obj.interpolate_to_timestep = var_interpolate_to_timestep
        # integer
        var_minutes_per_item = 30
        obj.minutes_per_item = var_minutes_per_item

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.schedulefiles[0].name, var_name)
        self.assertEqual(idf2.schedulefiles[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertEqual(idf2.schedulefiles[0].file_name, var_file_name)
        self.assertEqual(idf2.schedulefiles[0].column_number, var_column_number)
        self.assertEqual(idf2.schedulefiles[0].rows_to_skip_at_top, var_rows_to_skip_at_top)
        self.assertAlmostEqual(idf2.schedulefiles[0].number_of_hours_of_data, var_number_of_hours_of_data)
        self.assertEqual(idf2.schedulefiles[0].column_separator, var_column_separator)
        self.assertEqual(idf2.schedulefiles[0].interpolate_to_timestep, var_interpolate_to_timestep)
        self.assertEqual(idf2.schedulefiles[0].minutes_per_item, var_minutes_per_item)