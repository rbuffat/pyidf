import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabAutoGrid
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabAutoGrid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabautogrid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabAutoGrid()
        # real
        var_slabx_x_dimension_of_the_building_slab = 6.0
        obj.slabx_x_dimension_of_the_building_slab = var_slabx_x_dimension_of_the_building_slab
        # real
        var_slaby_y_dimension_of_the_building_slab = 6.0
        obj.slaby_y_dimension_of_the_building_slab = var_slaby_y_dimension_of_the_building_slab
        # real
        var_slabdepth_thickness_of_slab_on_grade = 3.3
        obj.slabdepth_thickness_of_slab_on_grade = var_slabdepth_thickness_of_slab_on_grade
        # real
        var_clearance_distance_from_edge_of_slab_to_domain_edge = 4.4
        obj.clearance_distance_from_edge_of_slab_to_domain_edge = var_clearance_distance_from_edge_of_slab_to_domain_edge
        # real
        var_zclearance_distance_from_bottom_of_slab_to_domain_bottom = 5.5
        obj.zclearance_distance_from_bottom_of_slab_to_domain_bottom = var_zclearance_distance_from_bottom_of_slab_to_domain_bottom

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabautogrids[0].slabx_x_dimension_of_the_building_slab, var_slabx_x_dimension_of_the_building_slab)
        self.assertAlmostEqual(idf2.groundheattransferslabautogrids[0].slaby_y_dimension_of_the_building_slab, var_slaby_y_dimension_of_the_building_slab)
        self.assertAlmostEqual(idf2.groundheattransferslabautogrids[0].slabdepth_thickness_of_slab_on_grade, var_slabdepth_thickness_of_slab_on_grade)
        self.assertAlmostEqual(idf2.groundheattransferslabautogrids[0].clearance_distance_from_edge_of_slab_to_domain_edge, var_clearance_distance_from_edge_of_slab_to_domain_edge)
        self.assertAlmostEqual(idf2.groundheattransferslabautogrids[0].zclearance_distance_from_bottom_of_slab_to_domain_bottom, var_zclearance_distance_from_bottom_of_slab_to_domain_bottom)