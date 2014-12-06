import os
import tempfile
import unittest
import pyidf
from pyidf.schedules import ScheduleTypeLimits
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestScheduleTypeLimits(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_scheduletypelimits(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ScheduleTypeLimits()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_lower_limit_value = 2.2
        obj.lower_limit_value = var_lower_limit_value
        # real
        var_upper_limit_value = 3.3
        obj.upper_limit_value = var_upper_limit_value
        # alpha
        var_numeric_type = "Continuous"
        obj.numeric_type = var_numeric_type
        # alpha
        var_unit_type = "Dimensionless"
        obj.unit_type = var_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.scheduletypelimitss[0].name, var_name)
        self.assertAlmostEqual(idf2.scheduletypelimitss[0].lower_limit_value, var_lower_limit_value)
        self.assertAlmostEqual(idf2.scheduletypelimitss[0].upper_limit_value, var_upper_limit_value)
        self.assertEqual(idf2.scheduletypelimitss[0].numeric_type, var_numeric_type)
        self.assertEqual(idf2.scheduletypelimitss[0].unit_type, var_unit_type)