import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabEquivalentSlab

log = logging.getLogger(__name__)

class TestGroundHeatTransferSlabEquivalentSlab(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabequivalentslab(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabEquivalentSlab()
        # real
        var_apratio_the_area_to_perimeter_ratio_for_this_slab = 11.75
        obj.apratio_the_area_to_perimeter_ratio_for_this_slab = var_apratio_the_area_to_perimeter_ratio_for_this_slab
        # real
        var_slabdepth_thickness_of_slab_on_grade = 2.2
        obj.slabdepth_thickness_of_slab_on_grade = var_slabdepth_thickness_of_slab_on_grade
        # real
        var_clearance_distance_from_edge_of_slab_to_domain_edge = 3.3
        obj.clearance_distance_from_edge_of_slab_to_domain_edge = var_clearance_distance_from_edge_of_slab_to_domain_edge
        # real
        var_zclearance_distance_from_bottom_of_slab_to_domain_bottom = 4.4
        obj.zclearance_distance_from_bottom_of_slab_to_domain_bottom = var_zclearance_distance_from_bottom_of_slab_to_domain_bottom

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabequivalentslabs[0].apratio_the_area_to_perimeter_ratio_for_this_slab, var_apratio_the_area_to_perimeter_ratio_for_this_slab)
        self.assertAlmostEqual(idf2.groundheattransferslabequivalentslabs[0].slabdepth_thickness_of_slab_on_grade, var_slabdepth_thickness_of_slab_on_grade)
        self.assertAlmostEqual(idf2.groundheattransferslabequivalentslabs[0].clearance_distance_from_edge_of_slab_to_domain_edge, var_clearance_distance_from_edge_of_slab_to_domain_edge)
        self.assertAlmostEqual(idf2.groundheattransferslabequivalentslabs[0].zclearance_distance_from_bottom_of_slab_to_domain_bottom, var_zclearance_distance_from_bottom_of_slab_to_domain_bottom)