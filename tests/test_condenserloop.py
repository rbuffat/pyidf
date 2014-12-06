import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import CondenserLoop

log = logging.getLogger(__name__)

class TestCondenserLoop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_condenserloop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CondenserLoop()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fluid_type = "Water"
        obj.fluid_type = var_fluid_type
        # object-list
        var_user_defined_fluid_type = "object-list|User Defined Fluid Type"
        obj.user_defined_fluid_type = var_user_defined_fluid_type
        # object-list
        var_condenser_equipment_operation_scheme_name = "object-list|Condenser Equipment Operation Scheme Name"
        obj.condenser_equipment_operation_scheme_name = var_condenser_equipment_operation_scheme_name
        # node
        var_condenser_loop_temperature_setpoint_node_name = "node|Condenser Loop Temperature Setpoint Node Name"
        obj.condenser_loop_temperature_setpoint_node_name = var_condenser_loop_temperature_setpoint_node_name
        # real
        var_maximum_loop_temperature = 6.6
        obj.maximum_loop_temperature = var_maximum_loop_temperature
        # real
        var_minimum_loop_temperature = 7.7
        obj.minimum_loop_temperature = var_minimum_loop_temperature
        # real
        var_maximum_loop_flow_rate = 0.0001
        obj.maximum_loop_flow_rate = var_maximum_loop_flow_rate
        # real
        var_minimum_loop_flow_rate = 9.9
        obj.minimum_loop_flow_rate = var_minimum_loop_flow_rate
        # real
        var_condenser_loop_volume = 0.0
        obj.condenser_loop_volume = var_condenser_loop_volume
        # node
        var_condenser_side_inlet_node_name = "node|Condenser Side Inlet Node Name"
        obj.condenser_side_inlet_node_name = var_condenser_side_inlet_node_name
        # node
        var_condenser_side_outlet_node_name = "node|Condenser Side Outlet Node Name"
        obj.condenser_side_outlet_node_name = var_condenser_side_outlet_node_name
        # object-list
        var_condenser_side_branch_list_name = "object-list|Condenser Side Branch List Name"
        obj.condenser_side_branch_list_name = var_condenser_side_branch_list_name
        # object-list
        var_condenser_side_connector_list_name = "object-list|Condenser Side Connector List Name"
        obj.condenser_side_connector_list_name = var_condenser_side_connector_list_name
        # node
        var_demand_side_inlet_node_name = "node|Demand Side Inlet Node Name"
        obj.demand_side_inlet_node_name = var_demand_side_inlet_node_name
        # node
        var_demand_side_outlet_node_name = "node|Demand Side Outlet Node Name"
        obj.demand_side_outlet_node_name = var_demand_side_outlet_node_name
        # object-list
        var_condenser_demand_side_branch_list_name = "object-list|Condenser Demand Side Branch List Name"
        obj.condenser_demand_side_branch_list_name = var_condenser_demand_side_branch_list_name
        # object-list
        var_condenser_demand_side_connector_list_name = "object-list|Condenser Demand Side Connector List Name"
        obj.condenser_demand_side_connector_list_name = var_condenser_demand_side_connector_list_name
        # alpha
        var_load_distribution_scheme = "Optimal"
        obj.load_distribution_scheme = var_load_distribution_scheme
        # alpha
        var_pressure_simulation_type = "PumpPowerCorrection"
        obj.pressure_simulation_type = var_pressure_simulation_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.condenserloops[0].name, var_name)
        self.assertEqual(idf2.condenserloops[0].fluid_type, var_fluid_type)
        self.assertEqual(idf2.condenserloops[0].user_defined_fluid_type, var_user_defined_fluid_type)
        self.assertEqual(idf2.condenserloops[0].condenser_equipment_operation_scheme_name, var_condenser_equipment_operation_scheme_name)
        self.assertEqual(idf2.condenserloops[0].condenser_loop_temperature_setpoint_node_name, var_condenser_loop_temperature_setpoint_node_name)
        self.assertAlmostEqual(idf2.condenserloops[0].maximum_loop_temperature, var_maximum_loop_temperature)
        self.assertAlmostEqual(idf2.condenserloops[0].minimum_loop_temperature, var_minimum_loop_temperature)
        self.assertAlmostEqual(idf2.condenserloops[0].maximum_loop_flow_rate, var_maximum_loop_flow_rate)
        self.assertAlmostEqual(idf2.condenserloops[0].minimum_loop_flow_rate, var_minimum_loop_flow_rate)
        self.assertAlmostEqual(idf2.condenserloops[0].condenser_loop_volume, var_condenser_loop_volume)
        self.assertEqual(idf2.condenserloops[0].condenser_side_inlet_node_name, var_condenser_side_inlet_node_name)
        self.assertEqual(idf2.condenserloops[0].condenser_side_outlet_node_name, var_condenser_side_outlet_node_name)
        self.assertEqual(idf2.condenserloops[0].condenser_side_branch_list_name, var_condenser_side_branch_list_name)
        self.assertEqual(idf2.condenserloops[0].condenser_side_connector_list_name, var_condenser_side_connector_list_name)
        self.assertEqual(idf2.condenserloops[0].demand_side_inlet_node_name, var_demand_side_inlet_node_name)
        self.assertEqual(idf2.condenserloops[0].demand_side_outlet_node_name, var_demand_side_outlet_node_name)
        self.assertEqual(idf2.condenserloops[0].condenser_demand_side_branch_list_name, var_condenser_demand_side_branch_list_name)
        self.assertEqual(idf2.condenserloops[0].condenser_demand_side_connector_list_name, var_condenser_demand_side_connector_list_name)
        self.assertEqual(idf2.condenserloops[0].load_distribution_scheme, var_load_distribution_scheme)
        self.assertEqual(idf2.condenserloops[0].pressure_simulation_type, var_pressure_simulation_type)