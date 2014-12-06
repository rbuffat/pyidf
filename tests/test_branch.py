import os
import tempfile
import unittest
import pyidf
from pyidf.node import Branch
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestBranch(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_branch(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Branch()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_maximum_flow_rate = 0.0
        obj.maximum_flow_rate = var_maximum_flow_rate
        # object-list
        var_pressure_drop_curve_name = "object-list|Pressure Drop Curve Name"
        obj.pressure_drop_curve_name = var_pressure_drop_curve_name
        paras = []
        var_component_1_object_type = "Component 1 Object Type"
        paras.append(var_component_1_object_type)
        var_component_1_name = "Component 1 Name"
        paras.append(var_component_1_name)
        var_component_1_inlet_node_name = "node|Component 1 Inlet Node Name"
        paras.append(var_component_1_inlet_node_name)
        var_component_1_outlet_node_name = "node|Component 1 Outlet Node Name"
        paras.append(var_component_1_outlet_node_name)
        var_component_1_branch_control_type = "Component 1 Branch Control Type"
        paras.append(var_component_1_branch_control_type)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.branchs[0].name, var_name)
        self.assertAlmostEqual(idf2.branchs[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertEqual(idf2.branchs[0].pressure_drop_curve_name, var_pressure_drop_curve_name)
        index = obj.extensible_field_index("Component 1 Object Type")
        self.assertEqual(idf2.branchs[0].extensibles[0][index], var_component_1_object_type)
        index = obj.extensible_field_index("Component 1 Name")
        self.assertEqual(idf2.branchs[0].extensibles[0][index], var_component_1_name)
        index = obj.extensible_field_index("Component 1 Inlet Node Name")
        self.assertEqual(idf2.branchs[0].extensibles[0][index], var_component_1_inlet_node_name)
        index = obj.extensible_field_index("Component 1 Outlet Node Name")
        self.assertEqual(idf2.branchs[0].extensibles[0][index], var_component_1_outlet_node_name)
        index = obj.extensible_field_index("Component 1 Branch Control Type")
        self.assertEqual(idf2.branchs[0].extensibles[0][index], var_component_1_branch_control_type)