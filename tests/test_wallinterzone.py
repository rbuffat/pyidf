import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import WallInterzone

log = logging.getLogger(__name__)

class TestWallInterzone(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_wallinterzone(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WallInterzone()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_outside_boundary_condition_object = "object-list|Outside Boundary Condition Object"
        obj.outside_boundary_condition_object = var_outside_boundary_condition_object
        # real
        var_azimuth_angle = 180.0
        obj.azimuth_angle = var_azimuth_angle
        # real
        var_tilt_angle = 90.0
        obj.tilt_angle = var_tilt_angle
        # real
        var_starting_x_coordinate = 7.7
        obj.starting_x_coordinate = var_starting_x_coordinate
        # real
        var_starting_y_coordinate = 8.8
        obj.starting_y_coordinate = var_starting_y_coordinate
        # real
        var_starting_z_coordinate = 9.9
        obj.starting_z_coordinate = var_starting_z_coordinate
        # real
        var_length = 10.1
        obj.length = var_length
        # real
        var_height = 11.11
        obj.height = var_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.wallinterzones[0].name, var_name)
        self.assertEqual(idf2.wallinterzones[0].construction_name, var_construction_name)
        self.assertEqual(idf2.wallinterzones[0].zone_name, var_zone_name)
        self.assertEqual(idf2.wallinterzones[0].outside_boundary_condition_object, var_outside_boundary_condition_object)
        self.assertAlmostEqual(idf2.wallinterzones[0].azimuth_angle, var_azimuth_angle)
        self.assertAlmostEqual(idf2.wallinterzones[0].tilt_angle, var_tilt_angle)
        self.assertAlmostEqual(idf2.wallinterzones[0].starting_x_coordinate, var_starting_x_coordinate)
        self.assertAlmostEqual(idf2.wallinterzones[0].starting_y_coordinate, var_starting_y_coordinate)
        self.assertAlmostEqual(idf2.wallinterzones[0].starting_z_coordinate, var_starting_z_coordinate)
        self.assertAlmostEqual(idf2.wallinterzones[0].length, var_length)
        self.assertAlmostEqual(idf2.wallinterzones[0].height, var_height)