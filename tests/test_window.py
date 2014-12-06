import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import Window

log = logging.getLogger(__name__)

class TestWindow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_window(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Window()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_building_surface_name = "object-list|Building Surface Name"
        obj.building_surface_name = var_building_surface_name
        # object-list
        var_shading_control_name = "object-list|Shading Control Name"
        obj.shading_control_name = var_shading_control_name
        # object-list
        var_frame_and_divider_name = "object-list|Frame and Divider Name"
        obj.frame_and_divider_name = var_frame_and_divider_name
        # real
        var_multiplier = 1.0
        obj.multiplier = var_multiplier
        # real
        var_starting_x_coordinate = 7.7
        obj.starting_x_coordinate = var_starting_x_coordinate
        # real
        var_starting_z_coordinate = 8.8
        obj.starting_z_coordinate = var_starting_z_coordinate
        # real
        var_length = 9.9
        obj.length = var_length
        # real
        var_height = 10.1
        obj.height = var_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windows[0].name, var_name)
        self.assertEqual(idf2.windows[0].construction_name, var_construction_name)
        self.assertEqual(idf2.windows[0].building_surface_name, var_building_surface_name)
        self.assertEqual(idf2.windows[0].shading_control_name, var_shading_control_name)
        self.assertEqual(idf2.windows[0].frame_and_divider_name, var_frame_and_divider_name)
        self.assertAlmostEqual(idf2.windows[0].multiplier, var_multiplier)
        self.assertAlmostEqual(idf2.windows[0].starting_x_coordinate, var_starting_x_coordinate)
        self.assertAlmostEqual(idf2.windows[0].starting_z_coordinate, var_starting_z_coordinate)
        self.assertAlmostEqual(idf2.windows[0].length, var_length)
        self.assertAlmostEqual(idf2.windows[0].height, var_height)