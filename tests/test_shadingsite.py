import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import ShadingSite
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestShadingSite(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadingsite(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadingSite()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_azimuth_angle = 180.0
        obj.azimuth_angle = var_azimuth_angle
        # real
        var_tilt_angle = 90.0
        obj.tilt_angle = var_tilt_angle
        # real
        var_starting_x_coordinate = 4.4
        obj.starting_x_coordinate = var_starting_x_coordinate
        # real
        var_starting_y_coordinate = 5.5
        obj.starting_y_coordinate = var_starting_y_coordinate
        # real
        var_starting_z_coordinate = 6.6
        obj.starting_z_coordinate = var_starting_z_coordinate
        # real
        var_length = 7.7
        obj.length = var_length
        # real
        var_height = 8.8
        obj.height = var_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadingsites[0].name, var_name)
        self.assertAlmostEqual(idf2.shadingsites[0].azimuth_angle, var_azimuth_angle)
        self.assertAlmostEqual(idf2.shadingsites[0].tilt_angle, var_tilt_angle)
        self.assertAlmostEqual(idf2.shadingsites[0].starting_x_coordinate, var_starting_x_coordinate)
        self.assertAlmostEqual(idf2.shadingsites[0].starting_y_coordinate, var_starting_y_coordinate)
        self.assertAlmostEqual(idf2.shadingsites[0].starting_z_coordinate, var_starting_z_coordinate)
        self.assertAlmostEqual(idf2.shadingsites[0].length, var_length)
        self.assertAlmostEqual(idf2.shadingsites[0].height, var_height)