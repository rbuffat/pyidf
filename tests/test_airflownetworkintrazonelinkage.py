import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkIntraZoneLinkage

log = logging.getLogger(__name__)

class TestAirflowNetworkIntraZoneLinkage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkintrazonelinkage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkIntraZoneLinkage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_node_1_name = "Node 1 Name"
        obj.node_1_name = var_node_1_name
        # alpha
        var_node_2_name = "Node 2 Name"
        obj.node_2_name = var_node_2_name
        # object-list
        var_component_name = "object-list|Component Name"
        obj.component_name = var_component_name
        # object-list
        var_airflownetworkmultizonesurface_name = "object-list|AirflowNetwork:MultiZone:Surface Name"
        obj.airflownetworkmultizonesurface_name = var_airflownetworkmultizonesurface_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkintrazonelinkages[0].name, var_name)
        self.assertEqual(idf2.airflownetworkintrazonelinkages[0].node_1_name, var_node_1_name)
        self.assertEqual(idf2.airflownetworkintrazonelinkages[0].node_2_name, var_node_2_name)
        self.assertEqual(idf2.airflownetworkintrazonelinkages[0].component_name, var_component_name)
        self.assertEqual(idf2.airflownetworkintrazonelinkages[0].airflownetworkmultizonesurface_name, var_airflownetworkmultizonesurface_name)