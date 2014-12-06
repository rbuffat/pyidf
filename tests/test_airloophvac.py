import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.air_distribution import AirLoopHvac

log = logging.getLogger(__name__)

class TestAirLoopHvac(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvac(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvac()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_controller_list_name = "object-list|Controller List Name"
        obj.controller_list_name = var_controller_list_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # real
        var_design_supply_air_flow_rate = 4.4
        obj.design_supply_air_flow_rate = var_design_supply_air_flow_rate
        # object-list
        var_branch_list_name = "object-list|Branch List Name"
        obj.branch_list_name = var_branch_list_name
        # object-list
        var_connector_list_name = "object-list|Connector List Name"
        obj.connector_list_name = var_connector_list_name
        # node
        var_supply_side_inlet_node_name = "node|Supply Side Inlet Node Name"
        obj.supply_side_inlet_node_name = var_supply_side_inlet_node_name
        # node
        var_demand_side_outlet_node_name = "node|Demand Side Outlet Node Name"
        obj.demand_side_outlet_node_name = var_demand_side_outlet_node_name
        # node
        var_demand_side_inlet_node_names = "node|Demand Side Inlet Node Names"
        obj.demand_side_inlet_node_names = var_demand_side_inlet_node_names
        # node
        var_supply_side_outlet_node_names = "node|Supply Side Outlet Node Names"
        obj.supply_side_outlet_node_names = var_supply_side_outlet_node_names

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacs[0].name, var_name)
        self.assertEqual(idf2.airloophvacs[0].controller_list_name, var_controller_list_name)
        self.assertEqual(idf2.airloophvacs[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertAlmostEqual(idf2.airloophvacs[0].design_supply_air_flow_rate, var_design_supply_air_flow_rate)
        self.assertEqual(idf2.airloophvacs[0].branch_list_name, var_branch_list_name)
        self.assertEqual(idf2.airloophvacs[0].connector_list_name, var_connector_list_name)
        self.assertEqual(idf2.airloophvacs[0].supply_side_inlet_node_name, var_supply_side_inlet_node_name)
        self.assertEqual(idf2.airloophvacs[0].demand_side_outlet_node_name, var_demand_side_outlet_node_name)
        self.assertEqual(idf2.airloophvacs[0].demand_side_inlet_node_names, var_demand_side_inlet_node_names)
        self.assertEqual(idf2.airloophvacs[0].supply_side_outlet_node_names, var_supply_side_outlet_node_names)