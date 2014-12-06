import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialComplexShade

log = logging.getLogger(__name__)

class TestWindowMaterialComplexShade(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialcomplexshade(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialComplexShade()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_layer_type = "Venetian"
        obj.layer_type = var_layer_type
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_ir_transmittance = 0.5
        obj.ir_transmittance = var_ir_transmittance
        # real
        var_front_emissivity = 0.5
        obj.front_emissivity = var_front_emissivity
        # real
        var_back_emissivity = 0.5
        obj.back_emissivity = var_back_emissivity
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
        # real
        var_front_opening_multiplier = 0.5
        obj.front_opening_multiplier = var_front_opening_multiplier
        # real
        var_slat_width = 0.0001
        obj.slat_width = var_slat_width
        # real
        var_slat_spacing = 0.0001
        obj.slat_spacing = var_slat_spacing
        # real
        var_slat_thickness = 0.0001
        obj.slat_thickness = var_slat_thickness
        # real
        var_slat_angle = 0.0
        obj.slat_angle = var_slat_angle
        # real
        var_slat_conductivity = 0.0001
        obj.slat_conductivity = var_slat_conductivity
        # real
        var_slat_curve = 0.0
        obj.slat_curve = var_slat_curve

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialcomplexshades[0].name, var_name)
        self.assertEqual(idf2.windowmaterialcomplexshades[0].layer_type, var_layer_type)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].ir_transmittance, var_ir_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].front_emissivity, var_front_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].back_emissivity, var_back_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].top_opening_multiplier, var_top_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].bottom_opening_multiplier, var_bottom_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].left_side_opening_multiplier, var_left_side_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].right_side_opening_multiplier, var_right_side_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].front_opening_multiplier, var_front_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_width, var_slat_width)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_spacing, var_slat_spacing)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_thickness, var_slat_thickness)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_angle, var_slat_angle)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_conductivity, var_slat_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialcomplexshades[0].slat_curve, var_slat_curve)