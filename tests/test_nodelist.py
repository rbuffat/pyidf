import os
import tempfile
import unittest
import pyidf
from pyidf.node import NodeList
from pyidf import ValidationLevel
from pyidf.idf import IDF


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
        var_node_name = "node|Node Name"
        paras.append(var_node_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.nodelists[0].name, var_name)
        index = obj.extensible_field_index("Node Name")
        self.assertEqual(idf2.nodelists[0].extensibles[0][index], var_node_name)