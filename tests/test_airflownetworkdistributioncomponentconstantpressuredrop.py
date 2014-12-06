import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentConstantPressureDrop

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionComponentConstantPressureDrop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentconstantpressuredrop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentConstantPressureDrop()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_pressure_difference_across_the_component = 0.0001
        obj.pressure_difference_across_the_component = var_pressure_difference_across_the_component

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentconstantpressuredrops[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentconstantpressuredrops[0].pressure_difference_across_the_component, var_pressure_difference_across_the_component)