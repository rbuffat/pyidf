import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfacePropertyHeatTransferAlgorithmMultipleSurface

log = logging.getLogger(__name__)

class TestSurfacePropertyHeatTransferAlgorithmMultipleSurface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyheattransferalgorithmmultiplesurface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyHeatTransferAlgorithmMultipleSurface()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_surface_type = "AllExteriorSurfaces"
        obj.surface_type = var_surface_type
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
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmmultiplesurfaces[0].name, var_name)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmmultiplesurfaces[0].surface_type, var_surface_type)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmmultiplesurfaces[0].algorithm, var_algorithm)