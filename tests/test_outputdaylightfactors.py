import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import OutputDaylightFactors
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputDaylightFactors(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputdaylightfactors(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputDaylightFactors()
        # alpha
        var_reporting_days = "SizingDays"
        obj.reporting_days = var_reporting_days

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputdaylightfactorss[0].reporting_days, var_reporting_days)