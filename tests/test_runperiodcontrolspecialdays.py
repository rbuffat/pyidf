import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import RunPeriodControlSpecialDays
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRunPeriodControlSpecialDays(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_runperiodcontrolspecialdays(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RunPeriodControlSpecialDays()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_start_date = "Start Date"
        obj.start_date = var_start_date
        # real
        var_duration = 183.5
        obj.duration = var_duration
        # alpha
        var_special_day_type = "Holiday"
        obj.special_day_type = var_special_day_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.runperiodcontrolspecialdayss[0].name, var_name)
        self.assertEqual(idf2.runperiodcontrolspecialdayss[0].start_date, var_start_date)
        self.assertAlmostEqual(idf2.runperiodcontrolspecialdayss[0].duration, var_duration)
        self.assertEqual(idf2.runperiodcontrolspecialdayss[0].special_day_type, var_special_day_type)