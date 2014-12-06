import os
import tempfile
import unittest
import pyidf
from pyidf.node import OutdoorAirNodeList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutdoorAirNodeList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outdoorairnodelist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutdoorAirNodeList()
        paras = []
        var_node_or_nodelist_name_1 = "node|Node or NodeList Name 1"
        paras.append(var_node_or_nodelist_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        index = obj.extensible_field_index("Node or NodeList Name 1")
        self.assertEqual(idf2.outdoorairnodelists[0].extensibles[0][index], var_node_or_nodelist_name_1)