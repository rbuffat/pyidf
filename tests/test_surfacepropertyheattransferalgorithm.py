import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfacePropertyHeatTransferAlgorithm

log = logging.getLogger(__name__)

class TestSurfacePropertyHeatTransferAlgorithm(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyheattransferalgorithm(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyHeatTransferAlgorithm()
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_algorithm = "ConductionTransferFunction"
        obj.algorithm = var_algorithm

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithms[0].surface_name, var_surface_name)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithms[0].algorithm, var_algorithm)