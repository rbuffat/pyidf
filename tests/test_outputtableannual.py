import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputTableAnnual

log = logging.getLogger(__name__)

class TestOutputTableAnnual(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputtableannual(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputTableAnnual()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_filter = "Filter"
        obj.filter = var_filter
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputtableannuals[0].name, var_name)
        self.assertEqual(idf2.outputtableannuals[0].filter, var_filter)
        self.assertEqual(idf2.outputtableannuals[0].schedule_name, var_schedule_name)