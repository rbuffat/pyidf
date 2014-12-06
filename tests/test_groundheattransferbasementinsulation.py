import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementInsulation

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementInsulation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementinsulation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementInsulation()
        # real
        var_rext_r_value_of_any_exterior_insulation = 0.0001
        obj.rext_r_value_of_any_exterior_insulation = var_rext_r_value_of_any_exterior_insulation
        # alpha
        var_insfull_flag_is_the_wall_fully_insulated = "TRUE"
        obj.insfull_flag_is_the_wall_fully_insulated = var_insfull_flag_is_the_wall_fully_insulated

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementinsulations[0].rext_r_value_of_any_exterior_insulation, var_rext_r_value_of_any_exterior_insulation)
        self.assertEqual(idf2.groundheattransferbasementinsulations[0].insfull_flag_is_the_wall_fully_insulated, var_insfull_flag_is_the_wall_fully_insulated)