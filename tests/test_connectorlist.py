import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import ConnectorList

log = logging.getLogger(__name__)

class TestConnectorList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_connectorlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConnectorList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_connector_1_object_type = "Connector:Splitter"
        obj.connector_1_object_type = var_connector_1_object_type
        # alpha
        var_connector_1_name = "Connector 1 Name"
        obj.connector_1_name = var_connector_1_name
        # alpha
        var_connector_2_object_type = "Connector:Splitter"
        obj.connector_2_object_type = var_connector_2_object_type
        # alpha
        var_connector_2_name = "Connector 2 Name"
        obj.connector_2_name = var_connector_2_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.connectorlists[0].name, var_name)
        self.assertEqual(idf2.connectorlists[0].connector_1_object_type, var_connector_1_object_type)
        self.assertEqual(idf2.connectorlists[0].connector_1_name, var_connector_1_name)
        self.assertEqual(idf2.connectorlists[0].connector_2_object_type, var_connector_2_object_type)
        self.assertEqual(idf2.connectorlists[0].connector_2_name, var_connector_2_name)