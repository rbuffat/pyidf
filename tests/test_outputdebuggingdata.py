import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputDebuggingData
from pyidf import ValidationLevel
from pyidf.idf import IDF


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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.outputdebuggingdatas[0].report_debugging_data, var_report_debugging_data)
        self.assertAlmostEqual(idf2.outputdebuggingdatas[0].report_during_warmup, var_report_during_warmup)