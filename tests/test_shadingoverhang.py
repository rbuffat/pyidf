import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import ShadingOverhang
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestShadingOverhang(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadingoverhang(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadingOverhang()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_window_or_door_name = "object-list|Window or Door Name"
        obj.window_or_door_name = var_window_or_door_name
        # real
        var_height_above_window_or_door = 3.3
        obj.height_above_window_or_door = var_height_above_window_or_door
        # real
        var_tilt_angle_from_window_or_door = 90.0
        obj.tilt_angle_from_window_or_door = var_tilt_angle_from_window_or_door
        # real
        var_left_extension_from_window_or_door_width = 5.5
        obj.left_extension_from_window_or_door_width = var_left_extension_from_window_or_door_width
        # real
        var_right_extension_from_window_or_door_width = 6.6
        obj.right_extension_from_window_or_door_width = var_right_extension_from_window_or_door_width
        # real
        var_depth = 0.0
        obj.depth = var_depth

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadingoverhangs[0].name, var_name)
        self.assertEqual(idf2.shadingoverhangs[0].window_or_door_name, var_window_or_door_name)
        self.assertAlmostEqual(idf2.shadingoverhangs[0].height_above_window_or_door, var_height_above_window_or_door)
        self.assertAlmostEqual(idf2.shadingoverhangs[0].tilt_angle_from_window_or_door, var_tilt_angle_from_window_or_door)
        self.assertAlmostEqual(idf2.shadingoverhangs[0].left_extension_from_window_or_door_width, var_left_extension_from_window_or_door_width)
        self.assertAlmostEqual(idf2.shadingoverhangs[0].right_extension_from_window_or_door_width, var_right_extension_from_window_or_door_width)
        self.assertAlmostEqual(idf2.shadingoverhangs[0].depth, var_depth)