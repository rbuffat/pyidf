import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import ZoneAirHeatBalanceAlgorithm

log = logging.getLogger(__name__)

class TestZoneAirHeatBalanceAlgorithm(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneairheatbalancealgorithm(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneAirHeatBalanceAlgorithm()
        # alpha
        var_algorithm = "ThirdOrderBackwardDifference"
        obj.algorithm = var_algorithm

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneairheatbalancealgorithms[0].algorithm, var_algorithm)