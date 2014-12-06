import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import HeatBalanceSettingsConductionFiniteDifference
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHeatBalanceSettingsConductionFiniteDifference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatbalancesettingsconductionfinitedifference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatBalanceSettingsConductionFiniteDifference()
        # alpha
        var_difference_scheme = "CrankNicholsonSecondOrder"
        obj.difference_scheme = var_difference_scheme
        # real
        var_space_discretization_constant = 2.2
        obj.space_discretization_constant = var_space_discretization_constant
        # real
        var_relaxation_factor = 0.505
        obj.relaxation_factor = var_relaxation_factor
        # real
        var_inside_face_surface_temperature_convergence_criteria = 0.00500005
        obj.inside_face_surface_temperature_convergence_criteria = var_inside_face_surface_temperature_convergence_criteria

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatbalancesettingsconductionfinitedifferences[0].difference_scheme, var_difference_scheme)
        self.assertAlmostEqual(idf2.heatbalancesettingsconductionfinitedifferences[0].space_discretization_constant, var_space_discretization_constant)
        self.assertAlmostEqual(idf2.heatbalancesettingsconductionfinitedifferences[0].relaxation_factor, var_relaxation_factor)
        self.assertAlmostEqual(idf2.heatbalancesettingsconductionfinitedifferences[0].inside_face_surface_temperature_convergence_criteria, var_inside_face_surface_temperature_convergence_criteria)