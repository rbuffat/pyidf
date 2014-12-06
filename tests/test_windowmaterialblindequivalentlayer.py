import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialBlindEquivalentLayer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialBlindEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialblindequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialBlindEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_slat_orientation = "Horizontal"
        obj.slat_orientation = var_slat_orientation
        # real
        var_slat_width = 0.01255
        obj.slat_width = var_slat_width
        # real
        var_slat_separation = 0.01255
        obj.slat_separation = var_slat_separation
        # real
        var_slat_crown = 0.00078
        obj.slat_crown = var_slat_crown
        # real
        var_slat_angle = 90.0
        obj.slat_angle = var_slat_angle
        # real
        var_front_side_slat_beamdiffuse_solar_transmittance = 0.49995
        obj.front_side_slat_beamdiffuse_solar_transmittance = var_front_side_slat_beamdiffuse_solar_transmittance
        # real
        var_back_side_slat_beamdiffuse_solar_transmittance = 0.49995
        obj.back_side_slat_beamdiffuse_solar_transmittance = var_back_side_slat_beamdiffuse_solar_transmittance
        # real
        var_front_side_slat_beamdiffuse_solar_reflectance = 0.49995
        obj.front_side_slat_beamdiffuse_solar_reflectance = var_front_side_slat_beamdiffuse_solar_reflectance
        # real
        var_back_side_slat_beamdiffuse_solar_reflectance = 0.49995
        obj.back_side_slat_beamdiffuse_solar_reflectance = var_back_side_slat_beamdiffuse_solar_reflectance
        # real
        var_front_side_slat_beamdiffuse_visible_transmittance = 0.49995
        obj.front_side_slat_beamdiffuse_visible_transmittance = var_front_side_slat_beamdiffuse_visible_transmittance
        # real
        var_back_side_slat_beamdiffuse_visible_transmittance = 0.49995
        obj.back_side_slat_beamdiffuse_visible_transmittance = var_back_side_slat_beamdiffuse_visible_transmittance
        # real
        var_front_side_slat_beamdiffuse_visible_reflectance = 0.49995
        obj.front_side_slat_beamdiffuse_visible_reflectance = var_front_side_slat_beamdiffuse_visible_reflectance
        # real
        var_back_side_slat_beamdiffuse_visible_reflectance = 0.49995
        obj.back_side_slat_beamdiffuse_visible_reflectance = var_back_side_slat_beamdiffuse_visible_reflectance
        # real
        var_slat_diffusediffuse_solar_transmittance = 0.49995
        obj.slat_diffusediffuse_solar_transmittance = var_slat_diffusediffuse_solar_transmittance
        # real
        var_front_side_slat_diffusediffuse_solar_reflectance = 0.49995
        obj.front_side_slat_diffusediffuse_solar_reflectance = var_front_side_slat_diffusediffuse_solar_reflectance
        # real
        var_back_side_slat_diffusediffuse_solar_reflectance = 0.49995
        obj.back_side_slat_diffusediffuse_solar_reflectance = var_back_side_slat_diffusediffuse_solar_reflectance
        # real
        var_slat_diffusediffuse_visible_transmittance = 0.49995
        obj.slat_diffusediffuse_visible_transmittance = var_slat_diffusediffuse_visible_transmittance
        # real
        var_front_side_slat_diffusediffuse_visible_reflectance = 0.49995
        obj.front_side_slat_diffusediffuse_visible_reflectance = var_front_side_slat_diffusediffuse_visible_reflectance
        # real
        var_back_side_slat_diffusediffuse_visible_reflectance = 0.49995
        obj.back_side_slat_diffusediffuse_visible_reflectance = var_back_side_slat_diffusediffuse_visible_reflectance
        # real
        var_slat_infrared_transmittance = 0.49995
        obj.slat_infrared_transmittance = var_slat_infrared_transmittance
        # real
        var_front_side_slat_infrared_emissivity = 0.49995
        obj.front_side_slat_infrared_emissivity = var_front_side_slat_infrared_emissivity
        # real
        var_back_side_slat_infrared_emissivity = 0.49995
        obj.back_side_slat_infrared_emissivity = var_back_side_slat_infrared_emissivity
        # alpha
        var_slat_angle_control = "FixedSlatAngle"
        obj.slat_angle_control = var_slat_angle_control

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialblindequivalentlayers[0].name, var_name)
        self.assertEqual(idf2.windowmaterialblindequivalentlayers[0].slat_orientation, var_slat_orientation)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_width, var_slat_width)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_separation, var_slat_separation)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_crown, var_slat_crown)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_angle, var_slat_angle)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_beamdiffuse_solar_transmittance, var_front_side_slat_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_beamdiffuse_solar_transmittance, var_back_side_slat_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_beamdiffuse_solar_reflectance, var_front_side_slat_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_beamdiffuse_solar_reflectance, var_back_side_slat_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_beamdiffuse_visible_transmittance, var_front_side_slat_beamdiffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_beamdiffuse_visible_transmittance, var_back_side_slat_beamdiffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_beamdiffuse_visible_reflectance, var_front_side_slat_beamdiffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_beamdiffuse_visible_reflectance, var_back_side_slat_beamdiffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_diffusediffuse_solar_transmittance, var_slat_diffusediffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_diffusediffuse_solar_reflectance, var_front_side_slat_diffusediffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_diffusediffuse_solar_reflectance, var_back_side_slat_diffusediffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_diffusediffuse_visible_transmittance, var_slat_diffusediffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_diffusediffuse_visible_reflectance, var_front_side_slat_diffusediffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_diffusediffuse_visible_reflectance, var_back_side_slat_diffusediffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].slat_infrared_transmittance, var_slat_infrared_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].front_side_slat_infrared_emissivity, var_front_side_slat_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialblindequivalentlayers[0].back_side_slat_infrared_emissivity, var_back_side_slat_infrared_emissivity)
        self.assertEqual(idf2.windowmaterialblindequivalentlayers[0].slat_angle_control, var_slat_angle_control)