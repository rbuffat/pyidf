import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import SurfaceConvectionAlgorithmOutside
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfaceConvectionAlgorithmOutside(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithmoutside(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmOutside()
        # alpha
        var_algorithm = "SimpleCombined"
        obj.algorithm = var_algorithm

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsides[0].algorithm, var_algorithm)