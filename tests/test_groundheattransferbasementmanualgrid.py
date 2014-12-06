import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementManualGrid

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementManualGrid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementmanualgrid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementManualGrid()
        # real
        var_nx_number_of_cells_in_the_x_direction_20 = 1.0
        obj.nx_number_of_cells_in_the_x_direction_20 = var_nx_number_of_cells_in_the_x_direction_20
        # real
        var_ny_number_of_cells_in_the_y_direction_20 = 1.0
        obj.ny_number_of_cells_in_the_y_direction_20 = var_ny_number_of_cells_in_the_y_direction_20
        # real
        var_nzag_number_of_cells_in_the_z_direction_above_grade_4_always = 1.0
        obj.nzag_number_of_cells_in_the_z_direction_above_grade_4_always = var_nzag_number_of_cells_in_the_z_direction_above_grade_4_always
        # real
        var_nzbg_number_of_cells_in_z_direction_below_grade_1035 = 1.0
        obj.nzbg_number_of_cells_in_z_direction_below_grade_1035 = var_nzbg_number_of_cells_in_z_direction_below_grade_1035
        # real
        var_ibase_x_direction_cell_indicator_of_slab_edge_520 = 5.5
        obj.ibase_x_direction_cell_indicator_of_slab_edge_520 = var_ibase_x_direction_cell_indicator_of_slab_edge_520
        # real
        var_jbase_y_direction_cell_indicator_of_slab_edge_520 = 6.6
        obj.jbase_y_direction_cell_indicator_of_slab_edge_520 = var_jbase_y_direction_cell_indicator_of_slab_edge_520
        # real
        var_kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520 = 7.7
        obj.kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520 = var_kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].nx_number_of_cells_in_the_x_direction_20, var_nx_number_of_cells_in_the_x_direction_20)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].ny_number_of_cells_in_the_y_direction_20, var_ny_number_of_cells_in_the_y_direction_20)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].nzag_number_of_cells_in_the_z_direction_above_grade_4_always, var_nzag_number_of_cells_in_the_z_direction_above_grade_4_always)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].nzbg_number_of_cells_in_z_direction_below_grade_1035, var_nzbg_number_of_cells_in_z_direction_below_grade_1035)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].ibase_x_direction_cell_indicator_of_slab_edge_520, var_ibase_x_direction_cell_indicator_of_slab_edge_520)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].jbase_y_direction_cell_indicator_of_slab_edge_520, var_jbase_y_direction_cell_indicator_of_slab_edge_520)
        self.assertAlmostEqual(idf2.groundheattransferbasementmanualgrids[0].kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520, var_kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520)