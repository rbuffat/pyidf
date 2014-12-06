import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleDayHourly
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleDayHourly(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduledayhourly(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleDayHourly()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_type_limits_name = "object-list|Schedule Type Limits Name"
        obj.schedule_type_limits_name = var_schedule_type_limits_name
        # real
        var_hour_1 = 3.3
        obj.hour_1 = var_hour_1
        # real
        var_hour_2 = 4.4
        obj.hour_2 = var_hour_2
        # real
        var_hour_3 = 5.5
        obj.hour_3 = var_hour_3
        # real
        var_hour_4 = 6.6
        obj.hour_4 = var_hour_4
        # real
        var_hour_5 = 7.7
        obj.hour_5 = var_hour_5
        # real
        var_hour_6 = 8.8
        obj.hour_6 = var_hour_6
        # real
        var_hour_7 = 9.9
        obj.hour_7 = var_hour_7
        # real
        var_hour_8 = 10.1
        obj.hour_8 = var_hour_8
        # real
        var_hour_9 = 11.11
        obj.hour_9 = var_hour_9
        # real
        var_hour_10 = 12.12
        obj.hour_10 = var_hour_10
        # real
        var_hour_11 = 13.13
        obj.hour_11 = var_hour_11
        # real
        var_hour_12 = 14.14
        obj.hour_12 = var_hour_12
        # real
        var_hour_13 = 15.15
        obj.hour_13 = var_hour_13
        # real
        var_hour_14 = 16.16
        obj.hour_14 = var_hour_14
        # real
        var_hour_15 = 17.17
        obj.hour_15 = var_hour_15
        # real
        var_hour_16 = 18.18
        obj.hour_16 = var_hour_16
        # real
        var_hour_17 = 19.19
        obj.hour_17 = var_hour_17
        # real
        var_hour_18 = 20.2
        obj.hour_18 = var_hour_18
        # real
        var_hour_19 = 21.21
        obj.hour_19 = var_hour_19
        # real
        var_hour_20 = 22.22
        obj.hour_20 = var_hour_20
        # real
        var_hour_21 = 23.23
        obj.hour_21 = var_hour_21
        # real
        var_hour_22 = 24.24
        obj.hour_22 = var_hour_22
        # real
        var_hour_23 = 25.25
        obj.hour_23 = var_hour_23
        # real
        var_hour_24 = 26.26
        obj.hour_24 = var_hour_24

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduledayhourlys[0].name, var_name)
        self.assertEqual(idf2.scheduledayhourlys[0].schedule_type_limits_name, var_schedule_type_limits_name)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_1, var_hour_1)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_2, var_hour_2)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_3, var_hour_3)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_4, var_hour_4)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_5, var_hour_5)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_6, var_hour_6)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_7, var_hour_7)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_8, var_hour_8)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_9, var_hour_9)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_10, var_hour_10)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_11, var_hour_11)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_12, var_hour_12)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_13, var_hour_13)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_14, var_hour_14)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_15, var_hour_15)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_16, var_hour_16)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_17, var_hour_17)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_18, var_hour_18)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_19, var_hour_19)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_20, var_hour_20)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_21, var_hour_21)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_22, var_hour_22)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_23, var_hour_23)
        self.assertAlmostEqual(idf2.scheduledayhourlys[0].hour_24, var_hour_24)