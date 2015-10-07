import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import NodeList

log = logging.getLogger(__name__)

class TestNodeList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_nodelist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = NodeList()
        # node
        var_name = "node|Name"
        obj.name = var_name
        paras = []
        var_node_1_name = "node|Node 1 Name"
        paras.append(var_node_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.nodelists[0].name, var_name)
        index = obj.extensible_field_index("Node 1 Name")
        self.assertEqual(idf2.nodelists[0].extensibles[0][index], var_node_1_name)