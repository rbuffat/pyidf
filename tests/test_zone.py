import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import Zone
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZone(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zone(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Zone()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_direction_of_relative_north = 2.2
        obj.direction_of_relative_north = var_direction_of_relative_north
        # real
        var_x_origin = 3.3
        obj.x_origin = var_x_origin
        # real
        var_y_origin = 4.4
        obj.y_origin = var_y_origin
        # real
        var_z_origin = 5.5
        obj.z_origin = var_z_origin
        # integer
        var_type = 1
        obj.type = var_type
        # integer
        var_multiplier = 1
        obj.multiplier = var_multiplier
        # real
        var_ceiling_height = 8.8
        obj.ceiling_height = var_ceiling_height
        # real
        var_volume = 9.9
        obj.volume = var_volume
        # real
        var_floor_area = 10.1
        obj.floor_area = var_floor_area
        # alpha
        var_zone_inside_convection_algorithm = "Simple"
        obj.zone_inside_convection_algorithm = var_zone_inside_convection_algorithm
        # alpha
        var_zone_outside_convection_algorithm = "SimpleCombined"
        obj.zone_outside_convection_algorithm = var_zone_outside_convection_algorithm
        # alpha
        var_part_of_total_floor_area = "Yes"
        obj.part_of_total_floor_area = var_part_of_total_floor_area

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zones[0].name, var_name)
        self.assertAlmostEqual(idf2.zones[0].direction_of_relative_north, var_direction_of_relative_north)
        self.assertAlmostEqual(idf2.zones[0].x_origin, var_x_origin)
        self.assertAlmostEqual(idf2.zones[0].y_origin, var_y_origin)
        self.assertAlmostEqual(idf2.zones[0].z_origin, var_z_origin)
        self.assertEqual(idf2.zones[0].type, var_type)
        self.assertEqual(idf2.zones[0].multiplier, var_multiplier)
        self.assertAlmostEqual(idf2.zones[0].ceiling_height, var_ceiling_height)
        self.assertAlmostEqual(idf2.zones[0].volume, var_volume)
        self.assertAlmostEqual(idf2.zones[0].floor_area, var_floor_area)
        self.assertEqual(idf2.zones[0].zone_inside_convection_algorithm, var_zone_inside_convection_algorithm)
        self.assertEqual(idf2.zones[0].zone_outside_convection_algorithm, var_zone_outside_convection_algorithm)
        self.assertEqual(idf2.zones[0].part_of_total_floor_area, var_part_of_total_floor_area)