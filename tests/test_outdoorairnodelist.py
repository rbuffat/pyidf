import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import OutdoorAirNodeList

log = logging.getLogger(__name__)

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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        index = obj.extensible_field_index("Node or NodeList Name 1")
        self.assertEqual(idf2.outdoorairnodelists[0].extensibles[0][index], var_node_or_nodelist_name_1)