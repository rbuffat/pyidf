import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import WindowPropertyFrameAndDivider
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowPropertyFrameAndDivider(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowpropertyframeanddivider(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowPropertyFrameAndDivider()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_frame_width = 0.5
        obj.frame_width = var_frame_width
        # real
        var_frame_outside_projection = 0.25
        obj.frame_outside_projection = var_frame_outside_projection
        # real
        var_frame_inside_projection = 0.25
        obj.frame_inside_projection = var_frame_inside_projection
        # real
        var_frame_conductance = 0.0
        obj.frame_conductance = var_frame_conductance
        # real
        var_ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = 2.00005
        obj.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = var_ratio_of_frameedge_glass_conductance_to_centerofglass_conductance
        # real
        var_frame_solar_absorptance = 0.5
        obj.frame_solar_absorptance = var_frame_solar_absorptance
        # real
        var_frame_visible_absorptance = 0.5
        obj.frame_visible_absorptance = var_frame_visible_absorptance
        # real
        var_frame_thermal_hemispherical_emissivity = 0.0001
        obj.frame_thermal_hemispherical_emissivity = var_frame_thermal_hemispherical_emissivity
        # alpha
        var_divider_type = "DividedLite"
        obj.divider_type = var_divider_type
        # real
        var_divider_width = 0.25
        obj.divider_width = var_divider_width
        # real
        var_number_of_horizontal_dividers = 0.0
        obj.number_of_horizontal_dividers = var_number_of_horizontal_dividers
        # real
        var_number_of_vertical_dividers = 0.0
        obj.number_of_vertical_dividers = var_number_of_vertical_dividers
        # real
        var_divider_outside_projection = 0.25
        obj.divider_outside_projection = var_divider_outside_projection
        # real
        var_divider_inside_projection = 0.25
        obj.divider_inside_projection = var_divider_inside_projection
        # real
        var_divider_conductance = 0.0
        obj.divider_conductance = var_divider_conductance
        # real
        var_ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = 2.00005
        obj.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = var_ratio_of_divideredge_glass_conductance_to_centerofglass_conductance
        # real
        var_divider_solar_absorptance = 0.5
        obj.divider_solar_absorptance = var_divider_solar_absorptance
        # real
        var_divider_visible_absorptance = 0.5
        obj.divider_visible_absorptance = var_divider_visible_absorptance
        # real
        var_divider_thermal_hemispherical_emissivity = 0.5
        obj.divider_thermal_hemispherical_emissivity = var_divider_thermal_hemispherical_emissivity
        # real
        var_outside_reveal_solar_absorptance = 0.5
        obj.outside_reveal_solar_absorptance = var_outside_reveal_solar_absorptance
        # real
        var_inside_sill_depth = 1.0
        obj.inside_sill_depth = var_inside_sill_depth
        # real
        var_inside_sill_solar_absorptance = 0.5
        obj.inside_sill_solar_absorptance = var_inside_sill_solar_absorptance
        # real
        var_inside_reveal_depth = 1.0
        obj.inside_reveal_depth = var_inside_reveal_depth
        # real
        var_inside_reveal_solar_absorptance = 0.5
        obj.inside_reveal_solar_absorptance = var_inside_reveal_solar_absorptance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowpropertyframeanddividers[0].name, var_name)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_width, var_frame_width)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_outside_projection, var_frame_outside_projection)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_inside_projection, var_frame_inside_projection)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_conductance, var_frame_conductance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].ratio_of_frameedge_glass_conductance_to_centerofglass_conductance, var_ratio_of_frameedge_glass_conductance_to_centerofglass_conductance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_solar_absorptance, var_frame_solar_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_visible_absorptance, var_frame_visible_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].frame_thermal_hemispherical_emissivity, var_frame_thermal_hemispherical_emissivity)
        self.assertEqual(idf2.windowpropertyframeanddividers[0].divider_type, var_divider_type)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_width, var_divider_width)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].number_of_horizontal_dividers, var_number_of_horizontal_dividers)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].number_of_vertical_dividers, var_number_of_vertical_dividers)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_outside_projection, var_divider_outside_projection)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_inside_projection, var_divider_inside_projection)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_conductance, var_divider_conductance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].ratio_of_divideredge_glass_conductance_to_centerofglass_conductance, var_ratio_of_divideredge_glass_conductance_to_centerofglass_conductance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_solar_absorptance, var_divider_solar_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_visible_absorptance, var_divider_visible_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].divider_thermal_hemispherical_emissivity, var_divider_thermal_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].outside_reveal_solar_absorptance, var_outside_reveal_solar_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].inside_sill_depth, var_inside_sill_depth)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].inside_sill_solar_absorptance, var_inside_sill_solar_absorptance)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].inside_reveal_depth, var_inside_reveal_depth)
        self.assertAlmostEqual(idf2.windowpropertyframeanddividers[0].inside_reveal_solar_absorptance, var_inside_reveal_solar_absorptance)