import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfacePropertyHeatTransferAlgorithmConstruction
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfacePropertyHeatTransferAlgorithmConstruction(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyheattransferalgorithmconstruction(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyHeatTransferAlgorithmConstruction()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_algorithm = "ConductionTransferFunction"
        obj.algorithm = var_algorithm
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmconstructions[0].name, var_name)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmconstructions[0].algorithm, var_algorithm)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmconstructions[0].construction_name, var_construction_name)