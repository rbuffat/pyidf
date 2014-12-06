import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentLeak

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionComponentLeak(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentleak(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentLeak()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_air_mass_flow_coefficient = 0.0001
        obj.air_mass_flow_coefficient = var_air_mass_flow_coefficient
        # real
        var_air_mass_flow_exponent = 0.75
        obj.air_mass_flow_exponent = var_air_mass_flow_exponent

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentleaks[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleaks[0].air_mass_flow_coefficient, var_air_mass_flow_coefficient)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleaks[0].air_mass_flow_exponent, var_air_mass_flow_exponent)