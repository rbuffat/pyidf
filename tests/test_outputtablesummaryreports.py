import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputTableSummaryReports
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputTableSummaryReports(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputtablesummaryreports(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputTableSummaryReports()

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)