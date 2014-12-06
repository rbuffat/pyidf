import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import OutputIlluminanceMap
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputIlluminanceMap(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputilluminancemap(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputIlluminanceMap()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_z_height = 3.3
        obj.z_height = var_z_height
        # real
        var_x_minimum_coordinate = 4.4
        obj.x_minimum_coordinate = var_x_minimum_coordinate
        # real
        var_x_maximum_coordinate = 5.5
        obj.x_maximum_coordinate = var_x_maximum_coordinate
        # integer
        var_number_of_x_grid_points = 1
        obj.number_of_x_grid_points = var_number_of_x_grid_points
        # real
        var_y_minimum_coordinate = 7.7
        obj.y_minimum_coordinate = var_y_minimum_coordinate
        # real
        var_y_maximum_coordinate = 8.8
        obj.y_maximum_coordinate = var_y_maximum_coordinate
        # integer
        var_number_of_y_grid_points = 1
        obj.number_of_y_grid_points = var_number_of_y_grid_points

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputilluminancemaps[0].name, var_name)
        self.assertEqual(idf2.outputilluminancemaps[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.outputilluminancemaps[0].z_height, var_z_height)
        self.assertAlmostEqual(idf2.outputilluminancemaps[0].x_minimum_coordinate, var_x_minimum_coordinate)
        self.assertAlmostEqual(idf2.outputilluminancemaps[0].x_maximum_coordinate, var_x_maximum_coordinate)
        self.assertEqual(idf2.outputilluminancemaps[0].number_of_x_grid_points, var_number_of_x_grid_points)
        self.assertAlmostEqual(idf2.outputilluminancemaps[0].y_minimum_coordinate, var_y_minimum_coordinate)
        self.assertAlmostEqual(idf2.outputilluminancemaps[0].y_maximum_coordinate, var_y_maximum_coordinate)
        self.assertEqual(idf2.outputilluminancemaps[0].number_of_y_grid_points, var_number_of_y_grid_points)