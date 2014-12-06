import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputEnvironmentalImpactFactors
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputEnvironmentalImpactFactors(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputenvironmentalimpactfactors(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputEnvironmentalImpactFactors()
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
        self.assertEqual(idf2.outputenvironmentalimpactfactorss[0].reporting_frequency, var_reporting_frequency)