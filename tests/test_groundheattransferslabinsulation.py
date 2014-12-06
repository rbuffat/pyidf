import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabInsulation

log = logging.getLogger(__name__)

class TestGroundHeatTransferSlabInsulation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabinsulation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabInsulation()
        # real
        var_rins_r_value_of_under_slab_insulation = 1.1
        obj.rins_r_value_of_under_slab_insulation = var_rins_r_value_of_under_slab_insulation
        # real
        var_dins_width_of_strip_of_under_slab_insulation = 2.2
        obj.dins_width_of_strip_of_under_slab_insulation = var_dins_width_of_strip_of_under_slab_insulation
        # real
        var_rvins_r_value_of_vertical_insulation = 3.3
        obj.rvins_r_value_of_vertical_insulation = var_rvins_r_value_of_vertical_insulation
        # real
        var_zvins_depth_of_vertical_insulation = 4.4
        obj.zvins_depth_of_vertical_insulation = var_zvins_depth_of_vertical_insulation
        # integer
        var_ivins_flag_is_there_vertical_insulation = 0
        obj.ivins_flag_is_there_vertical_insulation = var_ivins_flag_is_there_vertical_insulation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabinsulations[0].rins_r_value_of_under_slab_insulation, var_rins_r_value_of_under_slab_insulation)
        self.assertAlmostEqual(idf2.groundheattransferslabinsulations[0].dins_width_of_strip_of_under_slab_insulation, var_dins_width_of_strip_of_under_slab_insulation)
        self.assertAlmostEqual(idf2.groundheattransferslabinsulations[0].rvins_r_value_of_vertical_insulation, var_rvins_r_value_of_vertical_insulation)
        self.assertAlmostEqual(idf2.groundheattransferslabinsulations[0].zvins_depth_of_vertical_insulation, var_zvins_depth_of_vertical_insulation)
        self.assertEqual(idf2.groundheattransferslabinsulations[0].ivins_flag_is_there_vertical_insulation, var_ivins_flag_is_there_vertical_insulation)