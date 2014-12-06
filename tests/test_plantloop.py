import os
import tempfile
import unittest
import pyidf
from pyidf.plant import PlantLoop
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPlantLoop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantloop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantLoop()
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
        var_plant_equipment_operation_scheme_name = "object-list|Plant Equipment Operation Scheme Name"
        obj.plant_equipment_operation_scheme_name = var_plant_equipment_operation_scheme_name
        # node
        var_loop_temperature_setpoint_node_name = "node|Loop Temperature Setpoint Node Name"
        obj.loop_temperature_setpoint_node_name = var_loop_temperature_setpoint_node_name
        # real
        var_maximum_loop_temperature = 6.6
        obj.maximum_loop_temperature = var_maximum_loop_temperature
        # real
        var_minimum_loop_temperature = 7.7
        obj.minimum_loop_temperature = var_minimum_loop_temperature
        # real
        var_maximum_loop_flow_rate = 0.0
        obj.maximum_loop_flow_rate = var_maximum_loop_flow_rate
        # real
        var_minimum_loop_flow_rate = 9.9
        obj.minimum_loop_flow_rate = var_minimum_loop_flow_rate
        # real
        var_plant_loop_volume = 0.0
        obj.plant_loop_volume = var_plant_loop_volume
        # node
        var_plant_side_inlet_node_name = "node|Plant Side Inlet Node Name"
        obj.plant_side_inlet_node_name = var_plant_side_inlet_node_name
        # node
        var_plant_side_outlet_node_name = "node|Plant Side Outlet Node Name"
        obj.plant_side_outlet_node_name = var_plant_side_outlet_node_name
        # object-list
        var_plant_side_branch_list_name = "object-list|Plant Side Branch List Name"
        obj.plant_side_branch_list_name = var_plant_side_branch_list_name
        # object-list
        var_plant_side_connector_list_name = "object-list|Plant Side Connector List Name"
        obj.plant_side_connector_list_name = var_plant_side_connector_list_name
        # node
        var_demand_side_inlet_node_name = "node|Demand Side Inlet Node Name"
        obj.demand_side_inlet_node_name = var_demand_side_inlet_node_name
        # node
        var_demand_side_outlet_node_name = "node|Demand Side Outlet Node Name"
        obj.demand_side_outlet_node_name = var_demand_side_outlet_node_name
        # object-list
        var_demand_side_branch_list_name = "object-list|Demand Side Branch List Name"
        obj.demand_side_branch_list_name = var_demand_side_branch_list_name
        # object-list
        var_demand_side_connector_list_name = "object-list|Demand Side Connector List Name"
        obj.demand_side_connector_list_name = var_demand_side_connector_list_name
        # alpha
        var_load_distribution_scheme = "Optimal"
        obj.load_distribution_scheme = var_load_distribution_scheme
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # alpha
        var_plant_loop_demand_calculation_scheme = "SingleSetpoint"
        obj.plant_loop_demand_calculation_scheme = var_plant_loop_demand_calculation_scheme
        # alpha
        var_common_pipe_simulation = "CommonPipe"
        obj.common_pipe_simulation = var_common_pipe_simulation
        # alpha
        var_pressure_simulation_type = "PumpPowerCorrection"
        obj.pressure_simulation_type = var_pressure_simulation_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantloops[0].name, var_name)
        self.assertEqual(idf2.plantloops[0].fluid_type, var_fluid_type)
        self.assertEqual(idf2.plantloops[0].user_defined_fluid_type, var_user_defined_fluid_type)
        self.assertEqual(idf2.plantloops[0].plant_equipment_operation_scheme_name, var_plant_equipment_operation_scheme_name)
        self.assertEqual(idf2.plantloops[0].loop_temperature_setpoint_node_name, var_loop_temperature_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantloops[0].maximum_loop_temperature, var_maximum_loop_temperature)
        self.assertAlmostEqual(idf2.plantloops[0].minimum_loop_temperature, var_minimum_loop_temperature)
        self.assertAlmostEqual(idf2.plantloops[0].maximum_loop_flow_rate, var_maximum_loop_flow_rate)
        self.assertAlmostEqual(idf2.plantloops[0].minimum_loop_flow_rate, var_minimum_loop_flow_rate)
        self.assertAlmostEqual(idf2.plantloops[0].plant_loop_volume, var_plant_loop_volume)
        self.assertEqual(idf2.plantloops[0].plant_side_inlet_node_name, var_plant_side_inlet_node_name)
        self.assertEqual(idf2.plantloops[0].plant_side_outlet_node_name, var_plant_side_outlet_node_name)
        self.assertEqual(idf2.plantloops[0].plant_side_branch_list_name, var_plant_side_branch_list_name)
        self.assertEqual(idf2.plantloops[0].plant_side_connector_list_name, var_plant_side_connector_list_name)
        self.assertEqual(idf2.plantloops[0].demand_side_inlet_node_name, var_demand_side_inlet_node_name)
        self.assertEqual(idf2.plantloops[0].demand_side_outlet_node_name, var_demand_side_outlet_node_name)
        self.assertEqual(idf2.plantloops[0].demand_side_branch_list_name, var_demand_side_branch_list_name)
        self.assertEqual(idf2.plantloops[0].demand_side_connector_list_name, var_demand_side_connector_list_name)
        self.assertEqual(idf2.plantloops[0].load_distribution_scheme, var_load_distribution_scheme)
        self.assertEqual(idf2.plantloops[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.plantloops[0].plant_loop_demand_calculation_scheme, var_plant_loop_demand_calculation_scheme)
        self.assertEqual(idf2.plantloops[0].common_pipe_simulation, var_common_pipe_simulation)
        self.assertEqual(idf2.plantloops[0].pressure_simulation_type, var_pressure_simulation_type)