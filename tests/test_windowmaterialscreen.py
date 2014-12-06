import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialScreen
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialScreen(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialscreen(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialScreen()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_reflected_beam_transmittance_accounting_method = "DoNotModel"
        obj.reflected_beam_transmittance_accounting_method = var_reflected_beam_transmittance_accounting_method
        # real
        var_diffuse_solar_reflectance = 0.49995
        obj.diffuse_solar_reflectance = var_diffuse_solar_reflectance
        # real
        var_diffuse_visible_reflectance = 0.49995
        obj.diffuse_visible_reflectance = var_diffuse_visible_reflectance
        # real
        var_thermal_hemispherical_emissivity = 0.5
        obj.thermal_hemispherical_emissivity = var_thermal_hemispherical_emissivity
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_screen_material_spacing = 0.0001
        obj.screen_material_spacing = var_screen_material_spacing
        # real
        var_screen_material_diameter = 0.0001
        obj.screen_material_diameter = var_screen_material_diameter
        # real
        var_screen_to_glass_distance = 0.5005
        obj.screen_to_glass_distance = var_screen_to_glass_distance
        # real
        var_top_opening_multiplier = 0.5
        obj.top_opening_multiplier = var_top_opening_multiplier
        # real
        var_bottom_opening_multiplier = 0.5
        obj.bottom_opening_multiplier = var_bottom_opening_multiplier
        # real
        var_left_side_opening_multiplier = 0.5
        obj.left_side_opening_multiplier = var_left_side_opening_multiplier
        # real
        var_right_side_opening_multiplier = 0.5
        obj.right_side_opening_multiplier = var_right_side_opening_multiplier
        # integer
        var_angle_of_resolution_for_screen_transmittance_output_map = 0
        obj.angle_of_resolution_for_screen_transmittance_output_map = var_angle_of_resolution_for_screen_transmittance_output_map

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialscreens[0].name, var_name)
        self.assertEqual(idf2.windowmaterialscreens[0].reflected_beam_transmittance_accounting_method, var_reflected_beam_transmittance_accounting_method)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].diffuse_solar_reflectance, var_diffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].diffuse_visible_reflectance, var_diffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].thermal_hemispherical_emissivity, var_thermal_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].screen_material_spacing, var_screen_material_spacing)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].screen_material_diameter, var_screen_material_diameter)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].screen_to_glass_distance, var_screen_to_glass_distance)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].top_opening_multiplier, var_top_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].bottom_opening_multiplier, var_bottom_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].left_side_opening_multiplier, var_left_side_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialscreens[0].right_side_opening_multiplier, var_right_side_opening_multiplier)
        self.assertEqual(idf2.windowmaterialscreens[0].angle_of_resolution_for_screen_transmittance_output_map, var_angle_of_resolution_for_screen_transmittance_output_map)