import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.air_distribution import AirLoopHvacReturnPath

log = logging.getLogger(__name__)

class TestAirLoopHvacReturnPath(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacreturnpath(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacReturnPath()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_return_air_path_outlet_node_name = "node|Return Air Path Outlet Node Name"
        obj.return_air_path_outlet_node_name = var_return_air_path_outlet_node_name
        paras = []
        var_component_1_object_type = "AirLoopHVAC:ZoneMixer"
        paras.append(var_component_1_object_type)
        var_component_1_name = "object-list|Component 1 Name"
        paras.append(var_component_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacreturnpaths[0].name, var_name)
        self.assertEqual(idf2.airloophvacreturnpaths[0].return_air_path_outlet_node_name, var_return_air_path_outlet_node_name)
        index = obj.extensible_field_index("Component 1 Object Type")
        self.assertEqual(idf2.airloophvacreturnpaths[0].extensibles[0][index], var_component_1_object_type)
        index = obj.extensible_field_index("Component 1 Name")
        self.assertEqual(idf2.airloophvacreturnpaths[0].extensibles[0][index], var_component_1_name)