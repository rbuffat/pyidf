import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import RunPeriodControlDaylightSavingTime
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRunPeriodControlDaylightSavingTime(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_runperiodcontroldaylightsavingtime(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RunPeriodControlDaylightSavingTime()
        # alpha
        var_start_date = "Start Date"
        obj.start_date = var_start_date
        # alpha
        var_end_date = "End Date"
        obj.end_date = var_end_date

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.runperiodcontroldaylightsavingtimes[0].start_date, var_start_date)
        self.assertEqual(idf2.runperiodcontroldaylightsavingtimes[0].end_date, var_end_date)