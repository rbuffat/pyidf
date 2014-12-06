import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementSimParameters
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferBasementSimParameters(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementsimparameters(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementSimParameters()
        # real
        var_f_multiplier_for_the_adi_solution = 0.50005
        obj.f_multiplier_for_the_adi_solution = var_f_multiplier_for_the_adi_solution
        # real
        var_iyrs_maximum_number_of_yearly_iterations = 0.0
        obj.iyrs_maximum_number_of_yearly_iterations = var_iyrs_maximum_number_of_yearly_iterations

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementsimparameterss[0].f_multiplier_for_the_adi_solution, var_f_multiplier_for_the_adi_solution)
        self.assertAlmostEqual(idf2.groundheattransferbasementsimparameterss[0].iyrs_maximum_number_of_yearly_iterations, var_iyrs_maximum_number_of_yearly_iterations)