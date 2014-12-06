import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import FenestrationSurfaceDetailed
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFenestrationSurfaceDetailed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fenestrationsurfacedetailed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FenestrationSurfaceDetailed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_surface_type = "Window"
        obj.surface_type = var_surface_type
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_building_surface_name = "object-list|Building Surface Name"
        obj.building_surface_name = var_building_surface_name
        # object-list
        var_outside_boundary_condition_object = "object-list|Outside Boundary Condition Object"
        obj.outside_boundary_condition_object = var_outside_boundary_condition_object
        # real
        var_view_factor_to_ground = 0.5
        obj.view_factor_to_ground = var_view_factor_to_ground
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
        var_number_of_vertices = 3.5
        obj.number_of_vertices = var_number_of_vertices
        # real
        var_vertex_1_xcoordinate = 11.11
        obj.vertex_1_xcoordinate = var_vertex_1_xcoordinate
        # real
        var_vertex_1_ycoordinate = 12.12
        obj.vertex_1_ycoordinate = var_vertex_1_ycoordinate
        # real
        var_vertex_1_zcoordinate = 13.13
        obj.vertex_1_zcoordinate = var_vertex_1_zcoordinate
        # real
        var_vertex_2_xcoordinate = 14.14
        obj.vertex_2_xcoordinate = var_vertex_2_xcoordinate
        # real
        var_vertex_2_ycoordinate = 15.15
        obj.vertex_2_ycoordinate = var_vertex_2_ycoordinate
        # real
        var_vertex_2_zcoordinate = 16.16
        obj.vertex_2_zcoordinate = var_vertex_2_zcoordinate
        # real
        var_vertex_3_xcoordinate = 17.17
        obj.vertex_3_xcoordinate = var_vertex_3_xcoordinate
        # real
        var_vertex_3_ycoordinate = 18.18
        obj.vertex_3_ycoordinate = var_vertex_3_ycoordinate
        # real
        var_vertex_3_zcoordinate = 19.19
        obj.vertex_3_zcoordinate = var_vertex_3_zcoordinate
        # real
        var_vertex_4_xcoordinate = 20.2
        obj.vertex_4_xcoordinate = var_vertex_4_xcoordinate
        # real
        var_vertex_4_ycoordinate = 21.21
        obj.vertex_4_ycoordinate = var_vertex_4_ycoordinate
        # real
        var_vertex_4_zcoordinate = 22.22
        obj.vertex_4_zcoordinate = var_vertex_4_zcoordinate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].name, var_name)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].surface_type, var_surface_type)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].construction_name, var_construction_name)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].building_surface_name, var_building_surface_name)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].outside_boundary_condition_object, var_outside_boundary_condition_object)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].view_factor_to_ground, var_view_factor_to_ground)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].shading_control_name, var_shading_control_name)
        self.assertEqual(idf2.fenestrationsurfacedetaileds[0].frame_and_divider_name, var_frame_and_divider_name)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].multiplier, var_multiplier)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].number_of_vertices, var_number_of_vertices)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_1_xcoordinate, var_vertex_1_xcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_1_ycoordinate, var_vertex_1_ycoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_1_zcoordinate, var_vertex_1_zcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_2_xcoordinate, var_vertex_2_xcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_2_ycoordinate, var_vertex_2_ycoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_2_zcoordinate, var_vertex_2_zcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_3_xcoordinate, var_vertex_3_xcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_3_ycoordinate, var_vertex_3_ycoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_3_zcoordinate, var_vertex_3_zcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_4_xcoordinate, var_vertex_4_xcoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_4_ycoordinate, var_vertex_4_ycoordinate)
        self.assertAlmostEqual(idf2.fenestrationsurfacedetaileds[0].vertex_4_zcoordinate, var_vertex_4_zcoordinate)