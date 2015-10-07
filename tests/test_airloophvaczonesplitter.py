import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.air_distribution import AirLoopHvacZoneSplitter

log = logging.getLogger(__name__)

class TestAirLoopHvacZoneSplitter(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvaczonesplitter(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacZoneSplitter()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        paras = []
        var_outlet_1_node_name = "node|Outlet 1 Node Name"
        paras.append(var_outlet_1_node_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvaczonesplitters[0].name, var_name)
        self.assertEqual(idf2.airloophvaczonesplitters[0].inlet_node_name, var_inlet_node_name)
        index = obj.extensible_field_index("Outlet 1 Node Name")
        self.assertEqual(idf2.airloophvaczonesplitters[0].extensibles[0][index], var_outlet_1_node_name)