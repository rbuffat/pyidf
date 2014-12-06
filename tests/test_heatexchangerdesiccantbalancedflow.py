import os
import tempfile
import unittest
import pyidf
from pyidf.heat_recovery import HeatExchangerDesiccantBalancedFlow
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHeatExchangerDesiccantBalancedFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatexchangerdesiccantbalancedflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatExchangerDesiccantBalancedFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_regeneration_air_inlet_node_name = "node|Regeneration Air Inlet Node Name"
        obj.regeneration_air_inlet_node_name = var_regeneration_air_inlet_node_name
        # node
        var_regeneration_air_outlet_node_name = "node|Regeneration Air Outlet Node Name"
        obj.regeneration_air_outlet_node_name = var_regeneration_air_outlet_node_name
        # node
        var_process_air_inlet_node_name = "node|Process Air Inlet Node Name"
        obj.process_air_inlet_node_name = var_process_air_inlet_node_name
        # node
        var_process_air_outlet_node_name = "node|Process Air Outlet Node Name"
        obj.process_air_outlet_node_name = var_process_air_outlet_node_name
        # alpha
        var_heat_exchanger_performance_object_type = "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"
        obj.heat_exchanger_performance_object_type = var_heat_exchanger_performance_object_type
        # object-list
        var_heat_exchanger_performance_name = "object-list|Heat Exchanger Performance Name"
        obj.heat_exchanger_performance_name = var_heat_exchanger_performance_name
        # alpha
        var_economizer_lockout = "Yes"
        obj.economizer_lockout = var_economizer_lockout

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].name, var_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].regeneration_air_inlet_node_name, var_regeneration_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].regeneration_air_outlet_node_name, var_regeneration_air_outlet_node_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].process_air_inlet_node_name, var_process_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].process_air_outlet_node_name, var_process_air_outlet_node_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].heat_exchanger_performance_object_type, var_heat_exchanger_performance_object_type)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].heat_exchanger_performance_name, var_heat_exchanger_performance_name)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflows[0].economizer_lockout, var_economizer_lockout)