import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabManualGrid
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabManualGrid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabmanualgrid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabManualGrid()
        # real
        var_nx_number_of_cells_in_the_x_direction = 1.0
        obj.nx_number_of_cells_in_the_x_direction = var_nx_number_of_cells_in_the_x_direction
        # real
        var_ny_number_of_cells_in_the_y_direction = 1.0
        obj.ny_number_of_cells_in_the_y_direction = var_ny_number_of_cells_in_the_y_direction
        # real
        var_nz_number_of_cells_in_the_z_direction = 1.0
        obj.nz_number_of_cells_in_the_z_direction = var_nz_number_of_cells_in_the_z_direction
        # real
        var_ibox_x_direction_cell_indicator_of_slab_edge = 4.4
        obj.ibox_x_direction_cell_indicator_of_slab_edge = var_ibox_x_direction_cell_indicator_of_slab_edge
        # real
        var_jbox_y_direction_cell_indicator_of_slab_edge = 5.5
        obj.jbox_y_direction_cell_indicator_of_slab_edge = var_jbox_y_direction_cell_indicator_of_slab_edge

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabmanualgrids[0].nx_number_of_cells_in_the_x_direction, var_nx_number_of_cells_in_the_x_direction)
        self.assertAlmostEqual(idf2.groundheattransferslabmanualgrids[0].ny_number_of_cells_in_the_y_direction, var_ny_number_of_cells_in_the_y_direction)
        self.assertAlmostEqual(idf2.groundheattransferslabmanualgrids[0].nz_number_of_cells_in_the_z_direction, var_nz_number_of_cells_in_the_z_direction)
        self.assertAlmostEqual(idf2.groundheattransferslabmanualgrids[0].ibox_x_direction_cell_indicator_of_slab_edge, var_ibox_x_direction_cell_indicator_of_slab_edge)
        self.assertAlmostEqual(idf2.groundheattransferslabmanualgrids[0].jbox_y_direction_cell_indicator_of_slab_edge, var_jbox_y_direction_cell_indicator_of_slab_edge)