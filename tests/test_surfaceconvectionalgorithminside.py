import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import SurfaceConvectionAlgorithmInside

log = logging.getLogger(__name__)

class TestSurfaceConvectionAlgorithmInside(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithminside(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmInside()
        # alpha
        var_algorithm = "Simple"
        obj.algorithm = var_algorithm

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithminsides[0].algorithm, var_algorithm)