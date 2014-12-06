import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import GlobalGeometryRules

log = logging.getLogger(__name__)

class TestGlobalGeometryRules(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_globalgeometryrules(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GlobalGeometryRules()
        # alpha
        var_starting_vertex_position = "UpperLeftCorner"
        obj.starting_vertex_position = var_starting_vertex_position
        # alpha
        var_vertex_entry_direction = "Counterclockwise"
        obj.vertex_entry_direction = var_vertex_entry_direction
        # alpha
        var_coordinate_system = "Relative"
        obj.coordinate_system = var_coordinate_system
        # alpha
        var_daylighting_reference_point_coordinate_system = "Relative"
        obj.daylighting_reference_point_coordinate_system = var_daylighting_reference_point_coordinate_system
        # alpha
        var_rectangular_surface_coordinate_system = "Relative"
        obj.rectangular_surface_coordinate_system = var_rectangular_surface_coordinate_system

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.globalgeometryruless[0].starting_vertex_position, var_starting_vertex_position)
        self.assertEqual(idf2.globalgeometryruless[0].vertex_entry_direction, var_vertex_entry_direction)
        self.assertEqual(idf2.globalgeometryruless[0].coordinate_system, var_coordinate_system)
        self.assertEqual(idf2.globalgeometryruless[0].daylighting_reference_point_coordinate_system, var_daylighting_reference_point_coordinate_system)
        self.assertEqual(idf2.globalgeometryruless[0].rectangular_surface_coordinate_system, var_rectangular_surface_coordinate_system)