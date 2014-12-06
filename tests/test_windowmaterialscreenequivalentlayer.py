import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialScreenEquivalentLayer

log = logging.getLogger(__name__)

class TestWindowMaterialScreenEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialscreenequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialScreenEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_screen_beambeam_solar_transmittance = 0.49995
        obj.screen_beambeam_solar_transmittance = var_screen_beambeam_solar_transmittance
        # real
        var_screen_beamdiffuse_solar_transmittance = 0.49995
        obj.screen_beamdiffuse_solar_transmittance = var_screen_beamdiffuse_solar_transmittance
        # real
        var_screen_beamdiffuse_solar_reflectance = 0.49995
        obj.screen_beamdiffuse_solar_reflectance = var_screen_beamdiffuse_solar_reflectance
        # real
        var_screen_beambeam_visible_transmittance = 0.49995
        obj.screen_beambeam_visible_transmittance = var_screen_beambeam_visible_transmittance
        # real
        var_screen_beamdiffuse_visible_transmittance = 0.49995
        obj.screen_beamdiffuse_visible_transmittance = var_screen_beamdiffuse_visible_transmittance
        # real
        var_screen_beamdiffuse_visible_reflectance = 0.49995
        obj.screen_beamdiffuse_visible_reflectance = var_screen_beamdiffuse_visible_reflectance
        # real
        var_screen_infrared_transmittance = 0.49995
        obj.screen_infrared_transmittance = var_screen_infrared_transmittance
        # real
        var_screen_infrared_emissivity = 0.5
        obj.screen_infrared_emissivity = var_screen_infrared_emissivity
        # real
        var_screen_wire_spacing = 0.0001
        obj.screen_wire_spacing = var_screen_wire_spacing
        # real
        var_screen_wire_diameter = 0.0001
        obj.screen_wire_diameter = var_screen_wire_diameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialscreenequivalentlayers[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beambeam_solar_transmittance, var_screen_beambeam_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beamdiffuse_solar_transmittance, var_screen_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beamdiffuse_solar_reflectance, var_screen_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beambeam_visible_transmittance, var_screen_beambeam_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beamdiffuse_visible_transmittance, var_screen_beamdiffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_beamdiffuse_visible_reflectance, var_screen_beamdiffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_infrared_transmittance, var_screen_infrared_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_infrared_emissivity, var_screen_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_wire_spacing, var_screen_wire_spacing)
        self.assertAlmostEqual(idf2.windowmaterialscreenequivalentlayers[0].screen_wire_diameter, var_screen_wire_diameter)