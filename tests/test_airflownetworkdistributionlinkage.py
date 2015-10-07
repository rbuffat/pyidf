import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionLinkage

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionLinkage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributionlinkage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionLinkage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_node_1_name = "object-list|Node 1 Name"
        obj.node_1_name = var_node_1_name
        # object-list
        var_node_2_name = "object-list|Node 2 Name"
        obj.node_2_name = var_node_2_name
        # object-list
        var_component_name = "object-list|Component Name"
        obj.component_name = var_component_name
        # object-list
        var_thermal_zone_name = "object-list|Thermal Zone Name"
        obj.thermal_zone_name = var_thermal_zone_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributionlinkages[0].name, var_name)
        self.assertEqual(idf2.airflownetworkdistributionlinkages[0].node_1_name, var_node_1_name)
        self.assertEqual(idf2.airflownetworkdistributionlinkages[0].node_2_name, var_node_2_name)
        self.assertEqual(idf2.airflownetworkdistributionlinkages[0].component_name, var_component_name)
        self.assertEqual(idf2.airflownetworkdistributionlinkages[0].thermal_zone_name, var_thermal_zone_name)