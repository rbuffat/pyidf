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
        # object-list
        var_scheduleweek_name_1 = "object-list|Schedule:Week Name 1"
        obj.scheduleweek_name_1 = var_scheduleweek_name_1
        # integer
        var_start_month_1 = 6
        obj.start_month_1 = var_start_month_1
        # integer
        var_start_day_1 = 16
        obj.start_day_1 = var_start_day_1
        # integer
        var_end_month_1 = 6
        obj.end_month_1 = var_end_month_1
        # integer
        var_end_day_1 = 16
        obj.end_day_1 = var_end_day_1
        # object-list
        var_scheduleweek_name_2 = "object-list|Schedule:Week Name 2"
        obj.scheduleweek_name_2 = var_scheduleweek_name_2
        # integer
        var_start_month_2 = 6
        obj.start_month_2 = var_start_month_2
        # integer
        var_start_day_2 = 16
        obj.start_day_2 = var_start_day_2
        # integer
        var_end_month_2 = 6
        obj.end_month_2 = var_end_month_2
        # integer
        var_end_day_2 = 16
        obj.end_day_2 = var_end_day_2
        # object-list
        var_scheduleweek_name_3 = "object-list|Schedule:Week Name 3"
        obj.scheduleweek_name_3 = var_scheduleweek_name_3
        # integer
        var_start_month_3 = 6
        obj.start_month_3 = var_start_month_3
        # integer
        var_start_day_3 = 16
        obj.start_day_3 = var_start_day_3
        # integer
        var_end_month_3 = 6
        obj.end_month_3 = var_end_month_3
        # integer
        var_end_day_3 = 16
        obj.end_day_3 = var_end_day_3
        # object-list
        var_scheduleweek_name_4 = "object-list|Schedule:Week Name 4"
        obj.scheduleweek_name_4 = var_scheduleweek_name_4
        # integer
        var_start_month_4 = 6
        obj.start_month_4 = var_start_month_4
        # integer
        var_start_day_4 = 16
        obj.start_day_4 = var_start_day_4
        # integer
        var_end_month_4 = 6
        obj.end_month_4 = var_end_month_4
        # integer
        var_end_day_4 = 16
        obj.end_day_4 = var_end_day_4
        # object-list
        var_scheduleweek_name_5 = "object-list|Schedule:Week Name 5"
        obj.scheduleweek_name_5 = var_scheduleweek_name_5
        # integer
        var_start_month_5 = 6
        obj.start_month_5 = var_start_month_5
        # integer
        var_start_day_5 = 16
        obj.start_day_5 = var_start_day_5
        # integer
        var_end_month_5 = 6
        obj.end_month_5 = var_end_month_5
        # integer
        var_end_day_5 = 16
        obj.end_day_5 = var_end_day_5
        # object-list
        var_scheduleweek_name_6 = "object-list|Schedule:Week Name 6"
        obj.scheduleweek_name_6 = var_scheduleweek_name_6
        # integer
        var_start_month_6 = 6
        obj.start_month_6 = var_start_month_6
        # integer
        var_start_day_6 = 16
        obj.start_day_6 = var_start_day_6
        # integer
        var_end_month_6 = 6
        obj.end_month_6 = var_end_month_6
        # integer
        var_end_day_6 = 16
        obj.end_day_6 = var_end_day_6
        # object-list
        var_scheduleweek_name_7 = "object-list|Schedule:Week Name 7"
        obj.scheduleweek_name_7 = var_scheduleweek_name_7
        # integer
        var_start_month_7 = 6
        obj.start_month_7 = var_start_month_7
        # integer
        var_start_day_7 = 16
        obj.start_day_7 = var_start_day_7
        # integer
        var_end_month_7 = 6
        obj.end_month_7 = var_end_month_7
        # integer
        var_end_day_7 = 16
        obj.end_day_7 = var_end_day_7
        # object-list
        var_scheduleweek_name_8 = "object-list|Schedule:Week Name 8"
        obj.scheduleweek_name_8 = var_scheduleweek_name_8
        # integer
        var_start_month_8 = 6
        obj.start_month_8 = var_start_month_8
        # integer
        var_start_day_8 = 16
        obj.start_day_8 = var_start_day_8
        # integer
        var_end_month_8 = 6
        obj.end_month_8 = var_end_month_8
        # integer
        var_end_day_8 = 16
        obj.end_day_8 = var_end_day_8
        # object-list
        var_scheduleweek_name_9 = "object-list|Schedule:Week Name 9"
        obj.scheduleweek_name_9 = var_scheduleweek_name_9
        # integer
        var_start_month_9 = 6
        obj.start_month_9 = var_start_month_9
        # integer
        var_start_day_9 = 16
        obj.start_day_9 = var_start_day_9
        # integer
        var_end_month_9 = 6
        obj.end_month_9 = var_end_month_9
        # integer
        var_end_day_9 = 16
        obj.end_day_9 = var_end_day_9
        # object-list
        var_scheduleweek_name_10 = "object-list|Schedule:Week Name 10"
        obj.scheduleweek_name_10 = var_scheduleweek_name_10
        # integer
        var_start_month_10 = 6
        obj.start_month_10 = var_start_month_10
        # integer
        var_start_day_10 = 16
        obj.start_day_10 = var_start_day_10
        # integer
        var_end_month_10 = 6
        obj.end_month_10 = var_end_month_10
        # integer
        var_end_day_10 = 16
        obj.end_day_10 = var_end_day_10
        # object-list
        var_scheduleweek_name_11 = "object-list|Schedule:Week Name 11"
        obj.scheduleweek_name_11 = var_scheduleweek_name_11
        # integer
        var_start_month_11 = 6
        obj.start_month_11 = var_start_month_11
        # integer
        var_start_day_11 = 16
        obj.start_day_11 = var_start_day_11
        # integer
        var_end_month_11 = 6
        obj.end_month_11 = var_end_month_11
        # integer
        var_end_day_11 = 16
        obj.end_day_11 = var_end_day_11
        # object-list
        var_scheduleweek_name_12 = "object-list|Schedule:Week Name 12"
        obj.scheduleweek_name_12 = var_scheduleweek_name_12
        # integer
        var_start_month_12 = 6
        obj.start_month_12 = var_start_month_12
        # integer
        var_start_day_12 = 16
        obj.start_day_12 = var_start_day_12
        # integer
        var_end_month_12 = 6
        obj.end_month_12 = var_end_month_12
        # integer
        var_end_day_12 = 16
        obj.end_day_12 = var_end_day_12
        # object-list
        var_scheduleweek_name_13 = "object-list|Schedule:Week Name 13"
        obj.scheduleweek_name_13 = var_scheduleweek_name_13
        # integer
        var_start_month_13 = 6
        obj.start_month_13 = var_start_month_13
        # integer
        var_start_day_13 = 16
        obj.start_day_13 = var_start_day_13
        # integer
        var_end_month_13 = 6
        obj.end_month_13 = var_end_month_13
        # integer
        var_end_day_13 = 16
        obj.end_day_13 = var_end_day_13
        # object-list
        var_scheduleweek_name_14 = "object-list|Schedule:Week Name 14"
        obj.scheduleweek_name_14 = var_scheduleweek_name_14
        # integer
        var_start_month_14 = 6
        obj.start_month_14 = var_start_month_14
        # integer
        var_start_day_14 = 16
        obj.start_day_14 = var_start_day_14
        # integer
        var_end_month_14 = 6
        obj.end_month_14 = var_end_month_14
        # integer
        var_end_day_14 = 16
        obj.end_day_14 = var_end_day_14
        # object-list
        var_scheduleweek_name_15 = "object-list|Schedule:Week Name 15"
        obj.scheduleweek_name_15 = var_scheduleweek_name_15
        # integer
        var_start_month_15 = 6
        obj.start_month_15 = var_start_month_15
        # integer
        var_start_day_15 = 16
        obj.start_day_15 = var_start_day_15
        # integer
        var_end_month_15 = 6
        obj.end_month_15 = var_end_month_15
        # integer
        var_end_day_15 = 16
        obj.end_day_15 = var_end_day_15
        # object-list
        var_scheduleweek_name_16 = "object-list|Schedule:Week Name 16"
        obj.scheduleweek_name_16 = var_scheduleweek_name_16
        # integer
        var_start_month_16 = 6
        obj.start_month_16 = var_start_month_16
        # integer
        var_start_day_16 = 16
        obj.start_day_16 = var_start_day_16
        # integer
        var_end_month_16 = 6
        obj.end_month_16 = var_end_month_16
        # integer
        var_end_day_16 = 16
        obj.end_day_16 = var_end_day_16
        # object-list
        var_scheduleweek_name_17 = "object-list|Schedule:Week Name 17"
        obj.scheduleweek_name_17 = var_scheduleweek_name_17
        # integer
        var_start_month_17 = 6
        obj.start_month_17 = var_start_month_17
        # integer
        var_start_day_17 = 16
        obj.start_day_17 = var_start_day_17
        # integer
        var_end_month_17 = 6
        obj.end_month_17 = var_end_month_17
        # integer
        var_end_day_17 = 16
        obj.end_day_17 = var_end_day_17
        # object-list
        var_scheduleweek_name_18 = "object-list|Schedule:Week Name 18"
        obj.scheduleweek_name_18 = var_scheduleweek_name_18
        # integer
        var_start_month_18 = 6
        obj.start_month_18 = var_start_month_18
        # integer
        var_start_day_18 = 16
        obj.start_day_18 = var_start_day_18
        # integer
        var_end_month_18 = 6
        obj.end_month_18 = var_end_month_18
        # integer
        var_end_day_18 = 16
        obj.end_day_18 = var_end_day_18
        # object-list
        var_scheduleweek_name_19 = "object-list|Schedule:Week Name 19"
        obj.scheduleweek_name_19 = var_scheduleweek_name_19
        # integer
        var_start_month_19 = 6
        obj.start_month_19 = var_start_month_19
        # integer
        var_start_day_19 = 16
        obj.start_day_19 = var_start_day_19
        # integer
        var_end_month_19 = 6
        obj.end_month_19 = var_end_month_19
        # integer
        var_end_day_19 = 16
        obj.end_day_19 = var_end_day_19
        # object-list
        var_scheduleweek_name_20 = "object-list|Schedule:Week Name 20"
        obj.scheduleweek_name_20 = var_scheduleweek_name_20
        # integer
        var_start_month_20 = 6
        obj.start_month_20 = var_start_month_20
        # integer
        var_start_day_20 = 16
        obj.start_day_20 = var_start_day_20
        # integer
        var_end_month_20 = 6
        obj.end_month_20 = var_end_month_20
        # integer
        var_end_day_20 = 16
        obj.end_day_20 = var_end_day_20
        # object-list
        var_scheduleweek_name_21 = "object-list|Schedule:Week Name 21"
        obj.scheduleweek_name_21 = var_scheduleweek_name_21
        # integer
        var_start_month_21 = 6
        obj.start_month_21 = var_start_month_21
        # integer
        var_start_day_21 = 16
        obj.start_day_21 = var_start_day_21
        # integer
        var_end_month_21 = 6
        obj.end_month_21 = var_end_month_21
        # integer
        var_end_day_21 = 16
        obj.end_day_21 = var_end_day_21
        # object-list
        var_scheduleweek_name_22 = "object-list|Schedule:Week Name 22"
        obj.scheduleweek_name_22 = var_scheduleweek_name_22
        # integer
        var_start_month_22 = 6
        obj.start_month_22 = var_start_month_22
        # integer
        var_start_day_22 = 16
        obj.start_day_22 = var_start_day_22
        # integer
        var_end_month_22 = 6
        obj.end_month_22 = var_end_month_22
        # integer
        var_end_day_22 = 16
        obj.end_day_22 = var_end_day_22
        # object-list
        var_scheduleweek_name_23 = "object-list|Schedule:Week Name 23"
        obj.scheduleweek_name_23 = var_scheduleweek_name_23
        # integer
        var_start_month_23 = 6
        obj.start_month_23 = var_start_month_23
        # integer
        var_start_day_23 = 16
        obj.start_day_23 = var_start_day_23
        # integer
        var_end_month_23 = 6
        obj.end_month_23 = var_end_month_23
        # integer
        var_end_day_23 = 16
        obj.end_day_23 = var_end_day_23
        # object-list
        var_scheduleweek_name_24 = "object-list|Schedule:Week Name 24"
        obj.scheduleweek_name_24 = var_scheduleweek_name_24
        # integer
        var_start_month_24 = 6
        obj.start_month_24 = var_start_month_24
        # integer
        var_start_day_24 = 16
        obj.start_day_24 = var_start_day_24
        # integer
        var_end_month_24 = 6
        obj.end_month_24 = var_end_month_24
        # integer
        var_end_day_24 = 16
        obj.end_day_24 = var_end_day_24
        # object-list
        var_scheduleweek_name_25 = "object-list|Schedule:Week Name 25"
        obj.scheduleweek_name_25 = var_scheduleweek_name_25
        # integer
        var_start_month_25 = 6
        obj.start_month_25 = var_start_month_25
        # integer
        var_start_day_25 = 16
        obj.start_day_25 = var_start_day_25
        # integer
        var_end_month_25 = 6
        obj.end_month_25 = var_end_month_25
        # integer
        var_end_day_25 = 16
        obj.end_day_25 = var_end_day_25
        # object-list
        var_scheduleweek_name_26 = "object-list|Schedule:Week Name 26"
        obj.scheduleweek_name_26 = var_scheduleweek_name_26
        # integer
        var_start_month_26 = 6
        obj.start_month_26 = var_start_month_26
        # integer
        var_start_day_26 = 16
        obj.start_day_26 = var_start_day_26
        # integer
        var_end_month_26 = 6
        obj.end_month_26 = var_end_month_26
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3
        # integer
        var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = 16
        obj.end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3 = var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduleyears[0].name, var_name)
        self.assertEqual(idf2.scheduleyears[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_1, var_scheduleweek_name_1)
        self.assertEqual(idf2.scheduleyears[0].start_month_1, var_start_month_1)
        self.assertEqual(idf2.scheduleyears[0].start_day_1, var_start_day_1)
        self.assertEqual(idf2.scheduleyears[0].end_month_1, var_end_month_1)
        self.assertEqual(idf2.scheduleyears[0].end_day_1, var_end_day_1)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_2, var_scheduleweek_name_2)
        self.assertEqual(idf2.scheduleyears[0].start_month_2, var_start_month_2)
        self.assertEqual(idf2.scheduleyears[0].start_day_2, var_start_day_2)
        self.assertEqual(idf2.scheduleyears[0].end_month_2, var_end_month_2)
        self.assertEqual(idf2.scheduleyears[0].end_day_2, var_end_day_2)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_3, var_scheduleweek_name_3)
        self.assertEqual(idf2.scheduleyears[0].start_month_3, var_start_month_3)
        self.assertEqual(idf2.scheduleyears[0].start_day_3, var_start_day_3)
        self.assertEqual(idf2.scheduleyears[0].end_month_3, var_end_month_3)
        self.assertEqual(idf2.scheduleyears[0].end_day_3, var_end_day_3)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_4, var_scheduleweek_name_4)
        self.assertEqual(idf2.scheduleyears[0].start_month_4, var_start_month_4)
        self.assertEqual(idf2.scheduleyears[0].start_day_4, var_start_day_4)
        self.assertEqual(idf2.scheduleyears[0].end_month_4, var_end_month_4)
        self.assertEqual(idf2.scheduleyears[0].end_day_4, var_end_day_4)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_5, var_scheduleweek_name_5)
        self.assertEqual(idf2.scheduleyears[0].start_month_5, var_start_month_5)
        self.assertEqual(idf2.scheduleyears[0].start_day_5, var_start_day_5)
        self.assertEqual(idf2.scheduleyears[0].end_month_5, var_end_month_5)
        self.assertEqual(idf2.scheduleyears[0].end_day_5, var_end_day_5)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_6, var_scheduleweek_name_6)
        self.assertEqual(idf2.scheduleyears[0].start_month_6, var_start_month_6)
        self.assertEqual(idf2.scheduleyears[0].start_day_6, var_start_day_6)
        self.assertEqual(idf2.scheduleyears[0].end_month_6, var_end_month_6)
        self.assertEqual(idf2.scheduleyears[0].end_day_6, var_end_day_6)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_7, var_scheduleweek_name_7)
        self.assertEqual(idf2.scheduleyears[0].start_month_7, var_start_month_7)
        self.assertEqual(idf2.scheduleyears[0].start_day_7, var_start_day_7)
        self.assertEqual(idf2.scheduleyears[0].end_month_7, var_end_month_7)
        self.assertEqual(idf2.scheduleyears[0].end_day_7, var_end_day_7)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_8, var_scheduleweek_name_8)
        self.assertEqual(idf2.scheduleyears[0].start_month_8, var_start_month_8)
        self.assertEqual(idf2.scheduleyears[0].start_day_8, var_start_day_8)
        self.assertEqual(idf2.scheduleyears[0].end_month_8, var_end_month_8)
        self.assertEqual(idf2.scheduleyears[0].end_day_8, var_end_day_8)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_9, var_scheduleweek_name_9)
        self.assertEqual(idf2.scheduleyears[0].start_month_9, var_start_month_9)
        self.assertEqual(idf2.scheduleyears[0].start_day_9, var_start_day_9)
        self.assertEqual(idf2.scheduleyears[0].end_month_9, var_end_month_9)
        self.assertEqual(idf2.scheduleyears[0].end_day_9, var_end_day_9)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_10, var_scheduleweek_name_10)
        self.assertEqual(idf2.scheduleyears[0].start_month_10, var_start_month_10)
        self.assertEqual(idf2.scheduleyears[0].start_day_10, var_start_day_10)
        self.assertEqual(idf2.scheduleyears[0].end_month_10, var_end_month_10)
        self.assertEqual(idf2.scheduleyears[0].end_day_10, var_end_day_10)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_11, var_scheduleweek_name_11)
        self.assertEqual(idf2.scheduleyears[0].start_month_11, var_start_month_11)
        self.assertEqual(idf2.scheduleyears[0].start_day_11, var_start_day_11)
        self.assertEqual(idf2.scheduleyears[0].end_month_11, var_end_month_11)
        self.assertEqual(idf2.scheduleyears[0].end_day_11, var_end_day_11)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_12, var_scheduleweek_name_12)
        self.assertEqual(idf2.scheduleyears[0].start_month_12, var_start_month_12)
        self.assertEqual(idf2.scheduleyears[0].start_day_12, var_start_day_12)
        self.assertEqual(idf2.scheduleyears[0].end_month_12, var_end_month_12)
        self.assertEqual(idf2.scheduleyears[0].end_day_12, var_end_day_12)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_13, var_scheduleweek_name_13)
        self.assertEqual(idf2.scheduleyears[0].start_month_13, var_start_month_13)
        self.assertEqual(idf2.scheduleyears[0].start_day_13, var_start_day_13)
        self.assertEqual(idf2.scheduleyears[0].end_month_13, var_end_month_13)
        self.assertEqual(idf2.scheduleyears[0].end_day_13, var_end_day_13)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_14, var_scheduleweek_name_14)
        self.assertEqual(idf2.scheduleyears[0].start_month_14, var_start_month_14)
        self.assertEqual(idf2.scheduleyears[0].start_day_14, var_start_day_14)
        self.assertEqual(idf2.scheduleyears[0].end_month_14, var_end_month_14)
        self.assertEqual(idf2.scheduleyears[0].end_day_14, var_end_day_14)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_15, var_scheduleweek_name_15)
        self.assertEqual(idf2.scheduleyears[0].start_month_15, var_start_month_15)
        self.assertEqual(idf2.scheduleyears[0].start_day_15, var_start_day_15)
        self.assertEqual(idf2.scheduleyears[0].end_month_15, var_end_month_15)
        self.assertEqual(idf2.scheduleyears[0].end_day_15, var_end_day_15)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_16, var_scheduleweek_name_16)
        self.assertEqual(idf2.scheduleyears[0].start_month_16, var_start_month_16)
        self.assertEqual(idf2.scheduleyears[0].start_day_16, var_start_day_16)
        self.assertEqual(idf2.scheduleyears[0].end_month_16, var_end_month_16)
        self.assertEqual(idf2.scheduleyears[0].end_day_16, var_end_day_16)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_17, var_scheduleweek_name_17)
        self.assertEqual(idf2.scheduleyears[0].start_month_17, var_start_month_17)
        self.assertEqual(idf2.scheduleyears[0].start_day_17, var_start_day_17)
        self.assertEqual(idf2.scheduleyears[0].end_month_17, var_end_month_17)
        self.assertEqual(idf2.scheduleyears[0].end_day_17, var_end_day_17)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_18, var_scheduleweek_name_18)
        self.assertEqual(idf2.scheduleyears[0].start_month_18, var_start_month_18)
        self.assertEqual(idf2.scheduleyears[0].start_day_18, var_start_day_18)
        self.assertEqual(idf2.scheduleyears[0].end_month_18, var_end_month_18)
        self.assertEqual(idf2.scheduleyears[0].end_day_18, var_end_day_18)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_19, var_scheduleweek_name_19)
        self.assertEqual(idf2.scheduleyears[0].start_month_19, var_start_month_19)
        self.assertEqual(idf2.scheduleyears[0].start_day_19, var_start_day_19)
        self.assertEqual(idf2.scheduleyears[0].end_month_19, var_end_month_19)
        self.assertEqual(idf2.scheduleyears[0].end_day_19, var_end_day_19)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_20, var_scheduleweek_name_20)
        self.assertEqual(idf2.scheduleyears[0].start_month_20, var_start_month_20)
        self.assertEqual(idf2.scheduleyears[0].start_day_20, var_start_day_20)
        self.assertEqual(idf2.scheduleyears[0].end_month_20, var_end_month_20)
        self.assertEqual(idf2.scheduleyears[0].end_day_20, var_end_day_20)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_21, var_scheduleweek_name_21)
        self.assertEqual(idf2.scheduleyears[0].start_month_21, var_start_month_21)
        self.assertEqual(idf2.scheduleyears[0].start_day_21, var_start_day_21)
        self.assertEqual(idf2.scheduleyears[0].end_month_21, var_end_month_21)
        self.assertEqual(idf2.scheduleyears[0].end_day_21, var_end_day_21)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_22, var_scheduleweek_name_22)
        self.assertEqual(idf2.scheduleyears[0].start_month_22, var_start_month_22)
        self.assertEqual(idf2.scheduleyears[0].start_day_22, var_start_day_22)
        self.assertEqual(idf2.scheduleyears[0].end_month_22, var_end_month_22)
        self.assertEqual(idf2.scheduleyears[0].end_day_22, var_end_day_22)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_23, var_scheduleweek_name_23)
        self.assertEqual(idf2.scheduleyears[0].start_month_23, var_start_month_23)
        self.assertEqual(idf2.scheduleyears[0].start_day_23, var_start_day_23)
        self.assertEqual(idf2.scheduleyears[0].end_month_23, var_end_month_23)
        self.assertEqual(idf2.scheduleyears[0].end_day_23, var_end_day_23)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_24, var_scheduleweek_name_24)
        self.assertEqual(idf2.scheduleyears[0].start_month_24, var_start_month_24)
        self.assertEqual(idf2.scheduleyears[0].start_day_24, var_start_day_24)
        self.assertEqual(idf2.scheduleyears[0].end_month_24, var_end_month_24)
        self.assertEqual(idf2.scheduleyears[0].end_day_24, var_end_day_24)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_25, var_scheduleweek_name_25)
        self.assertEqual(idf2.scheduleyears[0].start_month_25, var_start_month_25)
        self.assertEqual(idf2.scheduleyears[0].start_day_25, var_start_day_25)
        self.assertEqual(idf2.scheduleyears[0].end_month_25, var_end_month_25)
        self.assertEqual(idf2.scheduleyears[0].end_day_25, var_end_day_25)
        self.assertEqual(idf2.scheduleyears[0].scheduleweek_name_26, var_scheduleweek_name_26)
        self.assertEqual(idf2.scheduleyears[0].start_month_26, var_start_month_26)
        self.assertEqual(idf2.scheduleyears[0].start_day_26, var_start_day_26)
        self.assertEqual(idf2.scheduleyears[0].end_month_26, var_end_month_26)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)
        self.assertEqual(idf2.scheduleyears[0].end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3, var_end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3)