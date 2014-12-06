import os
import tempfile
import unittest
import pyidf
from pyidf.air_distribution import AirLoopHvacSupplyPlenum
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirLoopHvacSupplyPlenum(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacsupplyplenum(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacSupplyPlenum()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # node
        var_zone_node_name = "node|Zone Node Name"
        obj.zone_node_name = var_zone_node_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        paras = []
        var_outlet_node_name = "node|Outlet Node Name"
        paras.append(var_outlet_node_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacsupplyplenums[0].name, var_name)
        self.assertEqual(idf2.airloophvacsupplyplenums[0].zone_name, var_zone_name)
        self.assertEqual(idf2.airloophvacsupplyplenums[0].zone_node_name, var_zone_node_name)
        self.assertEqual(idf2.airloophvacsupplyplenums[0].inlet_node_name, var_inlet_node_name)
        index = obj.extensible_field_index("Outlet Node Name")
        self.assertEqual(idf2.airloophvacsupplyplenums[0].extensibles[0][index], var_outlet_node_name)