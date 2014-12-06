import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import SurfaceConvectionAlgorithmInside
from pyidf import ValidationLevel
from pyidf.idf import IDF


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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithminsides[0].algorithm, var_algorithm)