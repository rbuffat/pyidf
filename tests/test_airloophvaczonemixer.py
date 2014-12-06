import os
import tempfile
import unittest
import pyidf
from pyidf.air_distribution import AirLoopHvacZoneMixer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirLoopHvacZoneMixer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvaczonemixer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacZoneMixer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        paras = []
        var_inlet_1_node_name = "node|Inlet 1 Node Name"
        paras.append(var_inlet_1_node_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvaczonemixers[0].name, var_name)
        self.assertEqual(idf2.airloophvaczonemixers[0].outlet_node_name, var_outlet_node_name)
        index = obj.extensible_field_index("Inlet 1 Node Name")
        self.assertEqual(idf2.airloophvaczonemixers[0].extensibles[0][index], var_inlet_1_node_name)