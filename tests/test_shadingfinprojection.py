import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import ShadingFinProjection
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestShadingFinProjection(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadingfinprojection(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadingFinProjection()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_window_or_door_name = "object-list|Window or Door Name"
        obj.window_or_door_name = var_window_or_door_name
        # real
        var_left_extension_from_window_or_door = 3.3
        obj.left_extension_from_window_or_door = var_left_extension_from_window_or_door
        # real
        var_left_distance_above_top_of_window = 4.4
        obj.left_distance_above_top_of_window = var_left_distance_above_top_of_window
        # real
        var_left_distance_below_bottom_of_window = 5.5
        obj.left_distance_below_bottom_of_window = var_left_distance_below_bottom_of_window
        # real
        var_left_tilt_angle_from_window_or_door = 90.0
        obj.left_tilt_angle_from_window_or_door = var_left_tilt_angle_from_window_or_door
        # real
        var_left_depth_as_fraction_of_window_or_door_width = 0.0
        obj.left_depth_as_fraction_of_window_or_door_width = var_left_depth_as_fraction_of_window_or_door_width
        # real
        var_right_extension_from_window_or_door = 8.8
        obj.right_extension_from_window_or_door = var_right_extension_from_window_or_door
        # real
        var_right_distance_above_top_of_window = 9.9
        obj.right_distance_above_top_of_window = var_right_distance_above_top_of_window
        # real
        var_right_distance_below_bottom_of_window = 10.1
        obj.right_distance_below_bottom_of_window = var_right_distance_below_bottom_of_window
        # real
        var_right_tilt_angle_from_window_or_door = 90.0
        obj.right_tilt_angle_from_window_or_door = var_right_tilt_angle_from_window_or_door
        # real
        var_right_depth_as_fraction_of_window_or_door_width = 0.0
        obj.right_depth_as_fraction_of_window_or_door_width = var_right_depth_as_fraction_of_window_or_door_width

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadingfinprojections[0].name, var_name)
        self.assertEqual(idf2.shadingfinprojections[0].window_or_door_name, var_window_or_door_name)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].left_extension_from_window_or_door, var_left_extension_from_window_or_door)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].left_distance_above_top_of_window, var_left_distance_above_top_of_window)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].left_distance_below_bottom_of_window, var_left_distance_below_bottom_of_window)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].left_tilt_angle_from_window_or_door, var_left_tilt_angle_from_window_or_door)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].left_depth_as_fraction_of_window_or_door_width, var_left_depth_as_fraction_of_window_or_door_width)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].right_extension_from_window_or_door, var_right_extension_from_window_or_door)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].right_distance_above_top_of_window, var_right_distance_above_top_of_window)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].right_distance_below_bottom_of_window, var_right_distance_below_bottom_of_window)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].right_tilt_angle_from_window_or_door, var_right_tilt_angle_from_window_or_door)
        self.assertAlmostEqual(idf2.shadingfinprojections[0].right_depth_as_fraction_of_window_or_door_width, var_right_depth_as_fraction_of_window_or_door_width)