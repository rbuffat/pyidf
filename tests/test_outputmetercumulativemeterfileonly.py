import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputMeterCumulativeMeterFileOnly
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputMeterCumulativeMeterFileOnly(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputmetercumulativemeterfileonly(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputMeterCumulativeMeterFileOnly()
        # external-list
        var_name = "external-list|Name"
        obj.name = var_name
        # alpha
        var_reporting_frequency = "Timestep"
        obj.reporting_frequency = var_reporting_frequency

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputmetercumulativemeterfileonlys[0].name, var_name)
        self.assertEqual(idf2.outputmetercumulativemeterfileonlys[0].reporting_frequency, var_reporting_frequency)