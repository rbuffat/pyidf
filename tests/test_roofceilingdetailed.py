import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import RoofCeilingDetailed

log = logging.getLogger(__name__)

class TestRoofCeilingDetailed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roofceilingdetailed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoofCeilingDetailed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # alpha
        var_outside_boundary_condition = "Adiabatic"
        obj.outside_boundary_condition = var_outside_boundary_condition
        # object-list
        var_outside_boundary_condition_object = "object-list|Outside Boundary Condition Object"
        obj.outside_boundary_condition_object = var_outside_boundary_condition_object
        # alpha
        var_sun_exposure = "SunExposed"
        obj.sun_exposure = var_sun_exposure
        # alpha
        var_wind_exposure = "WindExposed"
        obj.wind_exposure = var_wind_exposure
        # real
        var_view_factor_to_ground = 0.5
        obj.view_factor_to_ground = var_view_factor_to_ground
        # real
        var_number_of_vertices = 3.0
        obj.number_of_vertices = var_number_of_vertices
        paras = []
        var_vertex_1_xcoordinate = 10.1
        paras.append(var_vertex_1_xcoordinate)
        var_vertex_1_ycoordinate = 11.11
        paras.append(var_vertex_1_ycoordinate)
        var_vertex_1_zcoordinate = 12.12
        paras.append(var_vertex_1_zcoordinate)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roofceilingdetaileds[0].name, var_name)
        self.assertEqual(idf2.roofceilingdetaileds[0].construction_name, var_construction_name)
        self.assertEqual(idf2.roofceilingdetaileds[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roofceilingdetaileds[0].outside_boundary_condition, var_outside_boundary_condition)
        self.assertEqual(idf2.roofceilingdetaileds[0].outside_boundary_condition_object, var_outside_boundary_condition_object)
        self.assertEqual(idf2.roofceilingdetaileds[0].sun_exposure, var_sun_exposure)
        self.assertEqual(idf2.roofceilingdetaileds[0].wind_exposure, var_wind_exposure)
        self.assertAlmostEqual(idf2.roofceilingdetaileds[0].view_factor_to_ground, var_view_factor_to_ground)
        self.assertAlmostEqual(idf2.roofceilingdetaileds[0].number_of_vertices, var_number_of_vertices)
        index = obj.extensible_field_index("Vertex 1 X-coordinate")
        self.assertAlmostEqual(idf2.roofceilingdetaileds[0].extensibles[0][index], var_vertex_1_xcoordinate)
        index = obj.extensible_field_index("Vertex 1 Y-coordinate")
        self.assertAlmostEqual(idf2.roofceilingdetaileds[0].extensibles[0][index], var_vertex_1_ycoordinate)
        index = obj.extensible_field_index("Vertex 1 Z-coordinate")
        self.assertAlmostEqual(idf2.roofceilingdetaileds[0].extensibles[0][index], var_vertex_1_zcoordinate)