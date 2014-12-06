import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentLeakageRatio

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionComponentLeakageRatio(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentleakageratio(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentLeakageRatio()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_effective_leakage_ratio = 0.50005
        obj.effective_leakage_ratio = var_effective_leakage_ratio
        # real
        var_maximum_flow_rate = 0.0001
        obj.maximum_flow_rate = var_maximum_flow_rate
        # real
        var_reference_pressure_difference = 0.0001
        obj.reference_pressure_difference = var_reference_pressure_difference
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
        self.assertEqual(idf2.airflownetworkdistributioncomponentleakageratios[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleakageratios[0].effective_leakage_ratio, var_effective_leakage_ratio)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleakageratios[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleakageratios[0].reference_pressure_difference, var_reference_pressure_difference)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentleakageratios[0].air_mass_flow_exponent, var_air_mass_flow_exponent)