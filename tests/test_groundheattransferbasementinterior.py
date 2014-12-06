import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementInterior
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferBasementInterior(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementinterior(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementInterior()
        # alpha
        var_cond_flag_is_the_basement_conditioned = "TRUE"
        obj.cond_flag_is_the_basement_conditioned = var_cond_flag_is_the_basement_conditioned
        # real
        var_hin_downward_convection_only_heat_transfer_coefficient = 0.0001
        obj.hin_downward_convection_only_heat_transfer_coefficient = var_hin_downward_convection_only_heat_transfer_coefficient
        # real
        var_hin_upward_convection_only_heat_transfer_coefficient = 0.0001
        obj.hin_upward_convection_only_heat_transfer_coefficient = var_hin_upward_convection_only_heat_transfer_coefficient
        # real
        var_hin_horizontal_convection_only_heat_transfer_coefficient = 0.0001
        obj.hin_horizontal_convection_only_heat_transfer_coefficient = var_hin_horizontal_convection_only_heat_transfer_coefficient
        # real
        var_hin_downward_combined_convection_and_radiation_heat_transfer_coefficient = 0.0001
        obj.hin_downward_combined_convection_and_radiation_heat_transfer_coefficient = var_hin_downward_combined_convection_and_radiation_heat_transfer_coefficient
        # real
        var_hin_upward_combined_convection_and_radiation_heat_transfer_coefficient = 0.0001
        obj.hin_upward_combined_convection_and_radiation_heat_transfer_coefficient = var_hin_upward_combined_convection_and_radiation_heat_transfer_coefficient
        # real
        var_hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient = 0.0001
        obj.hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient = var_hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheattransferbasementinteriors[0].cond_flag_is_the_basement_conditioned, var_cond_flag_is_the_basement_conditioned)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_downward_convection_only_heat_transfer_coefficient, var_hin_downward_convection_only_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_upward_convection_only_heat_transfer_coefficient, var_hin_upward_convection_only_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_horizontal_convection_only_heat_transfer_coefficient, var_hin_horizontal_convection_only_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_downward_combined_convection_and_radiation_heat_transfer_coefficient, var_hin_downward_combined_convection_and_radiation_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_upward_combined_convection_and_radiation_heat_transfer_coefficient, var_hin_upward_combined_convection_and_radiation_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.groundheattransferbasementinteriors[0].hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient, var_hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient)