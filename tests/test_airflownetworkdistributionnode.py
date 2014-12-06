import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionNode

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionNode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributionnode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionNode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_component_name_or_node_name = "Component Name or Node Name"
        obj.component_name_or_node_name = var_component_name_or_node_name
        # alpha
        var_component_object_type_or_node_type = "AirLoopHVAC:ZoneMixer"
        obj.component_object_type_or_node_type = var_component_object_type_or_node_type
        # real
        var_node_height = 4.4
        obj.node_height = var_node_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributionnodes[0].name, var_name)
        self.assertEqual(idf2.airflownetworkdistributionnodes[0].component_name_or_node_name, var_component_name_or_node_name)
        self.assertEqual(idf2.airflownetworkdistributionnodes[0].component_object_type_or_node_type, var_component_object_type_or_node_type)
        self.assertAlmostEqual(idf2.airflownetworkdistributionnodes[0].node_height, var_node_height)