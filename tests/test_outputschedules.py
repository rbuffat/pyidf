import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputSchedules
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputSchedules(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputschedules(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputSchedules()
        # alpha
        var_key_field = "Hourly"
        obj.key_field = var_key_field

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputscheduless[0].key_field, var_key_field)