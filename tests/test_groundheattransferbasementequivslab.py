import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementEquivSlab
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferBasementEquivSlab(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementequivslab(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementEquivSlab()
        # real
        var_apratio_the_area_to_perimeter_ratio_for_this_slab = 0.0001
        obj.apratio_the_area_to_perimeter_ratio_for_this_slab = var_apratio_the_area_to_perimeter_ratio_for_this_slab
        # alpha
        var_equivsizing_flag = "TRUE"
        obj.equivsizing_flag = var_equivsizing_flag

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementequivslabs[0].apratio_the_area_to_perimeter_ratio_for_this_slab, var_apratio_the_area_to_perimeter_ratio_for_this_slab)
        self.assertEqual(idf2.groundheattransferbasementequivslabs[0].equivsizing_flag, var_equivsizing_flag)