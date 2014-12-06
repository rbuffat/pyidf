import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabBoundConds
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabBoundConds(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabboundconds(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabBoundConds()
        # alpha
        var_evtr_is_surface_evapotranspiration_modeled = "TRUE"
        obj.evtr_is_surface_evapotranspiration_modeled = var_evtr_is_surface_evapotranspiration_modeled
        # alpha
        var_fixbc_is_the_lower_boundary_at_a_fixed_temperature = "TRUE"
        obj.fixbc_is_the_lower_boundary_at_a_fixed_temperature = var_fixbc_is_the_lower_boundary_at_a_fixed_temperature
        # real
        var_tdeepin = 3.3
        obj.tdeepin = var_tdeepin
        # alpha
        var_usrhflag_is_the_ground_surface_h_specified_by_the_user = "TRUE"
        obj.usrhflag_is_the_ground_surface_h_specified_by_the_user = var_usrhflag_is_the_ground_surface_h_specified_by_the_user
        # real
        var_userh_user_specified_ground_surface_heat_transfer_coefficient = 5.5
        obj.userh_user_specified_ground_surface_heat_transfer_coefficient = var_userh_user_specified_ground_surface_heat_transfer_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheattransferslabboundcondss[0].evtr_is_surface_evapotranspiration_modeled, var_evtr_is_surface_evapotranspiration_modeled)
        self.assertEqual(idf2.groundheattransferslabboundcondss[0].fixbc_is_the_lower_boundary_at_a_fixed_temperature, var_fixbc_is_the_lower_boundary_at_a_fixed_temperature)
        self.assertAlmostEqual(idf2.groundheattransferslabboundcondss[0].tdeepin, var_tdeepin)
        self.assertEqual(idf2.groundheattransferslabboundcondss[0].usrhflag_is_the_ground_surface_h_specified_by_the_user, var_usrhflag_is_the_ground_surface_h_specified_by_the_user)
        self.assertAlmostEqual(idf2.groundheattransferslabboundcondss[0].userh_user_specified_ground_surface_heat_transfer_coefficient, var_userh_user_specified_ground_surface_heat_transfer_coefficient)