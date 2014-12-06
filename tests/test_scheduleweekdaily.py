import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleWeekDaily
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleWeekDaily(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduleweekdaily(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleWeekDaily()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_sunday_scheduleday_name = "object-list|Sunday Schedule:Day Name"
        obj.sunday_scheduleday_name = var_sunday_scheduleday_name
        # object-list
        var_monday_scheduleday_name = "object-list|Monday Schedule:Day Name"
        obj.monday_scheduleday_name = var_monday_scheduleday_name
        # object-list
        var_tuesday_scheduleday_name = "object-list|Tuesday Schedule:Day Name"
        obj.tuesday_scheduleday_name = var_tuesday_scheduleday_name
        # object-list
        var_wednesday_scheduleday_name = "object-list|Wednesday Schedule:Day Name"
        obj.wednesday_scheduleday_name = var_wednesday_scheduleday_name
        # object-list
        var_thursday_scheduleday_name = "object-list|Thursday Schedule:Day Name"
        obj.thursday_scheduleday_name = var_thursday_scheduleday_name
        # object-list
        var_friday_scheduleday_name = "object-list|Friday Schedule:Day Name"
        obj.friday_scheduleday_name = var_friday_scheduleday_name
        # object-list
        var_saturday_scheduleday_name = "object-list|Saturday Schedule:Day Name"
        obj.saturday_scheduleday_name = var_saturday_scheduleday_name
        # object-list
        var_holiday_scheduleday_name = "object-list|Holiday Schedule:Day Name"
        obj.holiday_scheduleday_name = var_holiday_scheduleday_name
        # object-list
        var_summerdesignday_scheduleday_name = "object-list|SummerDesignDay Schedule:Day Name"
        obj.summerdesignday_scheduleday_name = var_summerdesignday_scheduleday_name
        # object-list
        var_winterdesignday_scheduleday_name = "object-list|WinterDesignDay Schedule:Day Name"
        obj.winterdesignday_scheduleday_name = var_winterdesignday_scheduleday_name
        # object-list
        var_customday1_scheduleday_name = "object-list|CustomDay1 Schedule:Day Name"
        obj.customday1_scheduleday_name = var_customday1_scheduleday_name
        # object-list
        var_customday2_scheduleday_name = "object-list|CustomDay2 Schedule:Day Name"
        obj.customday2_scheduleday_name = var_customday2_scheduleday_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduleweekdailys[0].name, var_name)
        self.assertEqual(idf2.scheduleweekdailys[0].sunday_scheduleday_name, var_sunday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].monday_scheduleday_name, var_monday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].tuesday_scheduleday_name, var_tuesday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].wednesday_scheduleday_name, var_wednesday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].thursday_scheduleday_name, var_thursday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].friday_scheduleday_name, var_friday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].saturday_scheduleday_name, var_saturday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].holiday_scheduleday_name, var_holiday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].summerdesignday_scheduleday_name, var_summerdesignday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].winterdesignday_scheduleday_name, var_winterdesignday_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].customday1_scheduleday_name, var_customday1_scheduleday_name)
        self.assertEqual(idf2.scheduleweekdailys[0].customday2_scheduleday_name, var_customday2_scheduleday_name)