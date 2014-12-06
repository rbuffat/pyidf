import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialBlind

log = logging.getLogger(__name__)

class TestWindowMaterialBlind(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialblind(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialBlind()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_slat_orientation = "Horizontal"
        obj.slat_orientation = var_slat_orientation
        # real
        var_slat_width = 0.50005
        obj.slat_width = var_slat_width
        # real
        var_slat_separation = 0.50005
        obj.slat_separation = var_slat_separation
        # real
        var_slat_thickness = 0.05005
        obj.slat_thickness = var_slat_thickness
        # real
        var_slat_angle = 90.0
        obj.slat_angle = var_slat_angle
        # real
        var_slat_conductivity = 0.0001
        obj.slat_conductivity = var_slat_conductivity
        # real
        var_slat_beam_solar_transmittance = 0.49995
        obj.slat_beam_solar_transmittance = var_slat_beam_solar_transmittance
        # real
        var_front_side_slat_beam_solar_reflectance = 0.49995
        obj.front_side_slat_beam_solar_reflectance = var_front_side_slat_beam_solar_reflectance
        # real
        var_back_side_slat_beam_solar_reflectance = 0.49995
        obj.back_side_slat_beam_solar_reflectance = var_back_side_slat_beam_solar_reflectance
        # real
        var_slat_diffuse_solar_transmittance = 0.49995
        obj.slat_diffuse_solar_transmittance = var_slat_diffuse_solar_transmittance
        # real
        var_front_side_slat_diffuse_solar_reflectance = 0.49995
        obj.front_side_slat_diffuse_solar_reflectance = var_front_side_slat_diffuse_solar_reflectance
        # real
        var_back_side_slat_diffuse_solar_reflectance = 0.49995
        obj.back_side_slat_diffuse_solar_reflectance = var_back_side_slat_diffuse_solar_reflectance
        # real
        var_slat_beam_visible_transmittance = 0.49995
        obj.slat_beam_visible_transmittance = var_slat_beam_visible_transmittance
        # real
        var_front_side_slat_beam_visible_reflectance = 0.49995
        obj.front_side_slat_beam_visible_reflectance = var_front_side_slat_beam_visible_reflectance
        # real
        var_back_side_slat_beam_visible_reflectance = 0.49995
        obj.back_side_slat_beam_visible_reflectance = var_back_side_slat_beam_visible_reflectance
        # real
        var_slat_diffuse_visible_transmittance = 0.49995
        obj.slat_diffuse_visible_transmittance = var_slat_diffuse_visible_transmittance
        # real
        var_front_side_slat_diffuse_visible_reflectance = 0.49995
        obj.front_side_slat_diffuse_visible_reflectance = var_front_side_slat_diffuse_visible_reflectance
        # real
        var_back_side_slat_diffuse_visible_reflectance = 0.49995
        obj.back_side_slat_diffuse_visible_reflectance = var_back_side_slat_diffuse_visible_reflectance
        # real
        var_slat_infrared_hemispherical_transmittance = 0.49995
        obj.slat_infrared_hemispherical_transmittance = var_slat_infrared_hemispherical_transmittance
        # real
        var_front_side_slat_infrared_hemispherical_emissivity = 0.49995
        obj.front_side_slat_infrared_hemispherical_emissivity = var_front_side_slat_infrared_hemispherical_emissivity
        # real
        var_back_side_slat_infrared_hemispherical_emissivity = 0.49995
        obj.back_side_slat_infrared_hemispherical_emissivity = var_back_side_slat_infrared_hemispherical_emissivity
        # real
        var_blind_to_glass_distance = 0.505
        obj.blind_to_glass_distance = var_blind_to_glass_distance
        # real
        var_blind_top_opening_multiplier = 0.5
        obj.blind_top_opening_multiplier = var_blind_top_opening_multiplier
        # real
        var_blind_bottom_opening_multiplier = 0.5
        obj.blind_bottom_opening_multiplier = var_blind_bottom_opening_multiplier
        # real
        var_blind_left_side_opening_multiplier = 0.5
        obj.blind_left_side_opening_multiplier = var_blind_left_side_opening_multiplier
        # real
        var_blind_right_side_opening_multiplier = 0.5
        obj.blind_right_side_opening_multiplier = var_blind_right_side_opening_multiplier
        # real
        var_minimum_slat_angle = 90.0
        obj.minimum_slat_angle = var_minimum_slat_angle
        # real
        var_maximum_slat_angle = 90.0
        obj.maximum_slat_angle = var_maximum_slat_angle

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialblinds[0].name, var_name)
        self.assertEqual(idf2.windowmaterialblinds[0].slat_orientation, var_slat_orientation)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_width, var_slat_width)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_separation, var_slat_separation)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_thickness, var_slat_thickness)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_angle, var_slat_angle)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_conductivity, var_slat_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_beam_solar_transmittance, var_slat_beam_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].front_side_slat_beam_solar_reflectance, var_front_side_slat_beam_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].back_side_slat_beam_solar_reflectance, var_back_side_slat_beam_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_diffuse_solar_transmittance, var_slat_diffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].front_side_slat_diffuse_solar_reflectance, var_front_side_slat_diffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].back_side_slat_diffuse_solar_reflectance, var_back_side_slat_diffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_beam_visible_transmittance, var_slat_beam_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].front_side_slat_beam_visible_reflectance, var_front_side_slat_beam_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].back_side_slat_beam_visible_reflectance, var_back_side_slat_beam_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_diffuse_visible_transmittance, var_slat_diffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].front_side_slat_diffuse_visible_reflectance, var_front_side_slat_diffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].back_side_slat_diffuse_visible_reflectance, var_back_side_slat_diffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].slat_infrared_hemispherical_transmittance, var_slat_infrared_hemispherical_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].front_side_slat_infrared_hemispherical_emissivity, var_front_side_slat_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].back_side_slat_infrared_hemispherical_emissivity, var_back_side_slat_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].blind_to_glass_distance, var_blind_to_glass_distance)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].blind_top_opening_multiplier, var_blind_top_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].blind_bottom_opening_multiplier, var_blind_bottom_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].blind_left_side_opening_multiplier, var_blind_left_side_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].blind_right_side_opening_multiplier, var_blind_right_side_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].minimum_slat_angle, var_minimum_slat_angle)
        self.assertAlmostEqual(idf2.windowmaterialblinds[0].maximum_slat_angle, var_maximum_slat_angle)