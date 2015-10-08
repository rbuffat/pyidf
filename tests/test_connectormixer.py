import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import ConnectorMixer

log = logging.getLogger(__name__)

class TestConnectorMixer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_connectormixer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConnectorMixer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_outlet_branch_name = "object-list|Outlet Branch Name"
        obj.outlet_branch_name = var_outlet_branch_name
        paras = []
        var_inlet_branch_name = "object-list|Inlet Branch Name"
        paras.append(var_inlet_branch_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.connectormixers[0].name, var_name)
        self.assertEqual(idf2.connectormixers[0].outlet_branch_name, var_outlet_branch_name)
        index = obj.extensible_field_index("Inlet Branch Name")
        self.assertEqual(idf2.connectormixers[0].extensibles[0][index], var_inlet_branch_name)