import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementEquivAutoGrid

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementEquivAutoGrid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementequivautogrid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementEquivAutoGrid()
        # real
        var_clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain = 0.0
        obj.clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain = var_clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain
        # real
        var_slabdepth_thickness_of_the_floor_slab = 0.0
        obj.slabdepth_thickness_of_the_floor_slab = var_slabdepth_thickness_of_the_floor_slab
        # real
        var_basedepth_depth_of_the_basement_wall_below_grade = 0.0
        obj.basedepth_depth_of_the_basement_wall_below_grade = var_basedepth_depth_of_the_basement_wall_below_grade

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementequivautogrids[0].clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain, var_clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain)
        self.assertAlmostEqual(idf2.groundheattransferbasementequivautogrids[0].slabdepth_thickness_of_the_floor_slab, var_slabdepth_thickness_of_the_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementequivautogrids[0].basedepth_depth_of_the_basement_wall_below_grade, var_basedepth_depth_of_the_basement_wall_below_grade)