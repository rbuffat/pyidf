import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementBldgData

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementBldgData(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementbldgdata(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementBldgData()
        # real
        var_dwall_wall_thickness = 0.2
        obj.dwall_wall_thickness = var_dwall_wall_thickness
        # real
        var_dslab_floor_slab_thickness = 0.12505
        obj.dslab_floor_slab_thickness = var_dslab_floor_slab_thickness
        # real
        var_dgravxy_width_of_gravel_pit_beside_basement_wall = 0.0001
        obj.dgravxy_width_of_gravel_pit_beside_basement_wall = var_dgravxy_width_of_gravel_pit_beside_basement_wall
        # real
        var_dgravzn_gravel_depth_extending_above_the_floor_slab = 0.0001
        obj.dgravzn_gravel_depth_extending_above_the_floor_slab = var_dgravzn_gravel_depth_extending_above_the_floor_slab
        # real
        var_dgravzp_gravel_depth_below_the_floor_slab = 0.0001
        obj.dgravzp_gravel_depth_below_the_floor_slab = var_dgravzp_gravel_depth_below_the_floor_slab

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementbldgdatas[0].dwall_wall_thickness, var_dwall_wall_thickness)
        self.assertAlmostEqual(idf2.groundheattransferbasementbldgdatas[0].dslab_floor_slab_thickness, var_dslab_floor_slab_thickness)
        self.assertAlmostEqual(idf2.groundheattransferbasementbldgdatas[0].dgravxy_width_of_gravel_pit_beside_basement_wall, var_dgravxy_width_of_gravel_pit_beside_basement_wall)
        self.assertAlmostEqual(idf2.groundheattransferbasementbldgdatas[0].dgravzn_gravel_depth_extending_above_the_floor_slab, var_dgravzn_gravel_depth_extending_above_the_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementbldgdatas[0].dgravzp_gravel_depth_below_the_floor_slab, var_dgravzp_gravel_depth_below_the_floor_slab)