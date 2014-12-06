import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowGapSupportPillar

log = logging.getLogger(__name__)

class TestWindowGapSupportPillar(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowgapsupportpillar(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowGapSupportPillar()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_spacing = 0.0001
        obj.spacing = var_spacing
        # real
        var_radius = 0.0001
        obj.radius = var_radius

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowgapsupportpillars[0].name, var_name)
        self.assertAlmostEqual(idf2.windowgapsupportpillars[0].spacing, var_spacing)
        self.assertAlmostEqual(idf2.windowgapsupportpillars[0].radius, var_radius)