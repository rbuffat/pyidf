import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import GeometryTransform

log = logging.getLogger(__name__)

class TestGeometryTransform(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_geometrytransform(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeometryTransform()
        # alpha
        var_plane_of_transform = "XY"
        obj.plane_of_transform = var_plane_of_transform
        # real
        var_current_aspect_ratio = 0.0001
        obj.current_aspect_ratio = var_current_aspect_ratio
        # real
        var_new_aspect_ratio = 0.0001
        obj.new_aspect_ratio = var_new_aspect_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.geometrytransforms[0].plane_of_transform, var_plane_of_transform)
        self.assertAlmostEqual(idf2.geometrytransforms[0].current_aspect_ratio, var_current_aspect_ratio)
        self.assertAlmostEqual(idf2.geometrytransforms[0].new_aspect_ratio, var_new_aspect_ratio)