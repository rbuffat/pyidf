import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputMeterMeterFileOnly

log = logging.getLogger(__name__)

class TestOutputMeterMeterFileOnly(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputmetermeterfileonly(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputMeterMeterFileOnly()
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputmetermeterfileonlys[0].name, var_name)
        self.assertEqual(idf2.outputmetermeterfileonlys[0].reporting_frequency, var_reporting_frequency)