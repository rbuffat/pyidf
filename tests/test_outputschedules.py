import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputSchedules

log = logging.getLogger(__name__)

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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputscheduless[0].key_field, var_key_field)