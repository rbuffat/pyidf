import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.air_distribution import AirLoopHvacReturnPlenum

log = logging.getLogger(__name__)

class TestAirLoopHvacReturnPlenum(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacreturnplenum(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacReturnPlenum()
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
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # node
        var_induced_air_outlet_node_or_nodelist_name = "node|Induced Air Outlet Node or NodeList Name"
        obj.induced_air_outlet_node_or_nodelist_name = var_induced_air_outlet_node_or_nodelist_name
        paras = []
        var_inlet_1_node_name = "node|Inlet 1 Node Name"
        paras.append(var_inlet_1_node_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacreturnplenums[0].name, var_name)
        self.assertEqual(idf2.airloophvacreturnplenums[0].zone_name, var_zone_name)
        self.assertEqual(idf2.airloophvacreturnplenums[0].zone_node_name, var_zone_node_name)
        self.assertEqual(idf2.airloophvacreturnplenums[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.airloophvacreturnplenums[0].induced_air_outlet_node_or_nodelist_name, var_induced_air_outlet_node_or_nodelist_name)
        index = obj.extensible_field_index("Inlet 1 Node Name")
        self.assertEqual(idf2.airloophvacreturnplenums[0].extensibles[0][index], var_inlet_1_node_name)