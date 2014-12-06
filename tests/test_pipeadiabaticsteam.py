import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import PipeAdiabaticSteam

log = logging.getLogger(__name__)

class TestPipeAdiabaticSteam(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipeadiabaticsteam(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipeAdiabaticSteam()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipeadiabaticsteams[0].name, var_name)
        self.assertEqual(idf2.pipeadiabaticsteams[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.pipeadiabaticsteams[0].outlet_node_name, var_outlet_node_name)