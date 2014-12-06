import os
import tempfile
import unittest
import pyidf
from pyidf.solar_collectors import SolarCollectorIntegralCollectorStorage
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSolarCollectorIntegralCollectorStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorintegralcollectorstorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorIntegralCollectorStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_integralcollectorstorageparameters_name = "object-list|IntegralCollectorStorageParameters Name"
        obj.integralcollectorstorageparameters_name = var_integralcollectorstorageparameters_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_bottom_surface_boundary_conditions_type = "OtherSideConditionsModel"
        obj.bottom_surface_boundary_conditions_type = var_bottom_surface_boundary_conditions_type
        # alpha
        var_boundary_condition_model_name = "Boundary Condition Model Name"
        obj.boundary_condition_model_name = var_boundary_condition_model_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_maximum_flow_rate = 0.0001
        obj.maximum_flow_rate = var_maximum_flow_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].name, var_name)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].integralcollectorstorageparameters_name, var_integralcollectorstorageparameters_name)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].surface_name, var_surface_name)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].bottom_surface_boundary_conditions_type, var_bottom_surface_boundary_conditions_type)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].boundary_condition_model_name, var_boundary_condition_model_name)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.solarcollectorintegralcollectorstorages[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.solarcollectorintegralcollectorstorages[0].maximum_flow_rate, var_maximum_flow_rate)