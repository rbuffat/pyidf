import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementAutoGrid

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementAutoGrid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementautogrid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementAutoGrid()
        # real
        var_clearance_distance_from_outside_of_wall_to_edge_ = 0.0
        obj.clearance_distance_from_outside_of_wall_to_edge_ = var_clearance_distance_from_outside_of_wall_to_edge_
        # real
        var_slabx_x_dimension_of_the_building_slab = 30.0
        obj.slabx_x_dimension_of_the_building_slab = var_slabx_x_dimension_of_the_building_slab
        # real
        var_slaby_y_dimension_of_the_building_slab = 30.0
        obj.slaby_y_dimension_of_the_building_slab = var_slaby_y_dimension_of_the_building_slab
        # real
        var_concagheight_height_of_the_foundation_wall_above_grade = 0.0
        obj.concagheight_height_of_the_foundation_wall_above_grade = var_concagheight_height_of_the_foundation_wall_above_grade
        # real
        var_slabdepth_thickness_of_the_floor_slab = 5.5
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
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].clearance_distance_from_outside_of_wall_to_edge_, var_clearance_distance_from_outside_of_wall_to_edge_)
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].slabx_x_dimension_of_the_building_slab, var_slabx_x_dimension_of_the_building_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].slaby_y_dimension_of_the_building_slab, var_slaby_y_dimension_of_the_building_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].concagheight_height_of_the_foundation_wall_above_grade, var_concagheight_height_of_the_foundation_wall_above_grade)
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].slabdepth_thickness_of_the_floor_slab, var_slabdepth_thickness_of_the_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementautogrids[0].basedepth_depth_of_the_basement_wall_below_grade, var_basedepth_depth_of_the_basement_wall_below_grade)