import os
import tempfile
import unittest
import pyidf
from pyidf.air_distribution import AirLoopHvacSupplyPath
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirLoopHvacSupplyPath(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacsupplypath(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacSupplyPath()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_supply_air_path_inlet_node_name = "node|Supply Air Path Inlet Node Name"
        obj.supply_air_path_inlet_node_name = var_supply_air_path_inlet_node_name
        paras = []
        var_component_1_object_type = "AirLoopHVAC:ZoneSplitter"
        paras.append(var_component_1_object_type)
        var_component_1_name = "object-list|Component 1 Name"
        paras.append(var_component_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacsupplypaths[0].name, var_name)
        self.assertEqual(idf2.airloophvacsupplypaths[0].supply_air_path_inlet_node_name, var_supply_air_path_inlet_node_name)
        index = obj.extensible_field_index("Component 1 Object Type")
        self.assertEqual(idf2.airloophvacsupplypaths[0].extensibles[0][index], var_component_1_object_type)
        index = obj.extensible_field_index("Component 1 Name")
        self.assertEqual(idf2.airloophvacsupplypaths[0].extensibles[0][index], var_component_1_name)