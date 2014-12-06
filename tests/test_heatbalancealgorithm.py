import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import HeatBalanceAlgorithm

log = logging.getLogger(__name__)

class TestHeatBalanceAlgorithm(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatbalancealgorithm(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatBalanceAlgorithm()
        # alpha
        var_algorithm = "ConductionTransferFunction"
        obj.algorithm = var_algorithm
        # real
        var_surface_temperature_upper_limit = 200.0
        obj.surface_temperature_upper_limit = var_surface_temperature_upper_limit
        # real
        var_minimum_surface_convection_heat_transfer_coefficient_value = 0.0001
        obj.minimum_surface_convection_heat_transfer_coefficient_value = var_minimum_surface_convection_heat_transfer_coefficient_value
        # real
        var_maximum_surface_convection_heat_transfer_coefficient_value = 1.0
        obj.maximum_surface_convection_heat_transfer_coefficient_value = var_maximum_surface_convection_heat_transfer_coefficient_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatbalancealgorithms[0].algorithm, var_algorithm)
        self.assertAlmostEqual(idf2.heatbalancealgorithms[0].surface_temperature_upper_limit, var_surface_temperature_upper_limit)
        self.assertAlmostEqual(idf2.heatbalancealgorithms[0].minimum_surface_convection_heat_transfer_coefficient_value, var_minimum_surface_convection_heat_transfer_coefficient_value)
        self.assertAlmostEqual(idf2.heatbalancealgorithms[0].maximum_surface_convection_heat_transfer_coefficient_value, var_maximum_surface_convection_heat_transfer_coefficient_value)