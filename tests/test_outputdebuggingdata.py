import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputDebuggingData

log = logging.getLogger(__name__)

class TestOutputDebuggingData(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputdebuggingdata(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputDebuggingData()
        # real
        var_report_debugging_data = 1.1
        obj.report_debugging_data = var_report_debugging_data
        # real
        var_report_during_warmup = 2.2
        obj.report_during_warmup = var_report_during_warmup

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.outputdebuggingdatas[0].report_debugging_data, var_report_debugging_data)
        self.assertAlmostEqual(idf2.outputdebuggingdatas[0].report_during_warmup, var_report_during_warmup)