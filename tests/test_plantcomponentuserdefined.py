import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.user_defined_hvac_and_plant_component_models import PlantComponentUserDefined

log = logging.getLogger(__name__)

class TestPlantComponentUserDefined(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantcomponentuserdefined(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantComponentUserDefined()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_main_model_program_calling_manager_name = "object-list|Main Model Program Calling Manager Name"
        obj.main_model_program_calling_manager_name = var_main_model_program_calling_manager_name
        # integer
        var_number_of_plant_loop_connections = 2
        obj.number_of_plant_loop_connections = var_number_of_plant_loop_connections
        # node
        var_plant_connection_1_inlet_node_name = "node|Plant Connection 1 Inlet Node Name"
        obj.plant_connection_1_inlet_node_name = var_plant_connection_1_inlet_node_name
        # node
        var_plant_connection_1_outlet_node_name = "node|Plant Connection 1 Outlet Node Name"
        obj.plant_connection_1_outlet_node_name = var_plant_connection_1_outlet_node_name
        # alpha
        var_plant_connection_1_loading_mode = "DemandsLoad"
        obj.plant_connection_1_loading_mode = var_plant_connection_1_loading_mode
        # alpha
        var_plant_connection_1_loop_flow_request_mode = "NeedsFlowIfLoopOn"
        obj.plant_connection_1_loop_flow_request_mode = var_plant_connection_1_loop_flow_request_mode
        # object-list
        var_plant_connection_1_initialization_program_calling_manager_name = "object-list|Plant Connection 1 Initialization Program Calling Manager Name"
        obj.plant_connection_1_initialization_program_calling_manager_name = var_plant_connection_1_initialization_program_calling_manager_name
        # object-list
        var_plant_connection_1_simulation_program_calling_manager_name = "object-list|Plant Connection 1 Simulation Program Calling Manager Name"
        obj.plant_connection_1_simulation_program_calling_manager_name = var_plant_connection_1_simulation_program_calling_manager_name
        # node
        var_plant_connection_2_inlet_node_name = "node|Plant Connection 2 Inlet Node Name"
        obj.plant_connection_2_inlet_node_name = var_plant_connection_2_inlet_node_name
        # node
        var_plant_connection_2_outlet_node_name = "node|Plant Connection 2 Outlet Node Name"
        obj.plant_connection_2_outlet_node_name = var_plant_connection_2_outlet_node_name
        # alpha
        var_plant_connection_2_loading_mode = "DemandsLoad"
        obj.plant_connection_2_loading_mode = var_plant_connection_2_loading_mode
        # alpha
        var_plant_connection_2_loop_flow_request_mode = "NeedsFlowIfLoopOn"
        obj.plant_connection_2_loop_flow_request_mode = var_plant_connection_2_loop_flow_request_mode
        # object-list
        var_plant_connection_2_initialization_program_calling_manager_name = "object-list|Plant Connection 2 Initialization Program Calling Manager Name"
        obj.plant_connection_2_initialization_program_calling_manager_name = var_plant_connection_2_initialization_program_calling_manager_name
        # object-list
        var_plant_connection_2_simulation_program_calling_manager_name = "object-list|Plant Connection 2 Simulation Program Calling Manager Name"
        obj.plant_connection_2_simulation_program_calling_manager_name = var_plant_connection_2_simulation_program_calling_manager_name
        # node
        var_plant_connection_3_inlet_node_name = "node|Plant Connection 3 Inlet Node Name"
        obj.plant_connection_3_inlet_node_name = var_plant_connection_3_inlet_node_name
        # node
        var_plant_connection_3_outlet_node_name = "node|Plant Connection 3 Outlet Node Name"
        obj.plant_connection_3_outlet_node_name = var_plant_connection_3_outlet_node_name
        # alpha
        var_plant_connection_3_loading_mode = "DemandsLoad"
        obj.plant_connection_3_loading_mode = var_plant_connection_3_loading_mode
        # alpha
        var_plant_connection_3_loop_flow_request_mode = "NeedsFlowIfLoopOn"
        obj.plant_connection_3_loop_flow_request_mode = var_plant_connection_3_loop_flow_request_mode
        # object-list
        var_plant_connection_3_initialization_program_calling_manager_name = "object-list|Plant Connection 3 Initialization Program Calling Manager Name"
        obj.plant_connection_3_initialization_program_calling_manager_name = var_plant_connection_3_initialization_program_calling_manager_name
        # object-list
        var_plant_connection_3_simulation_program_calling_manager_name = "object-list|Plant Connection 3 Simulation Program Calling Manager Name"
        obj.plant_connection_3_simulation_program_calling_manager_name = var_plant_connection_3_simulation_program_calling_manager_name
        # node
        var_plant_connection_4_inlet_node_name = "node|Plant Connection 4 Inlet Node Name"
        obj.plant_connection_4_inlet_node_name = var_plant_connection_4_inlet_node_name
        # node
        var_plant_connection_4_outlet_node_name = "node|Plant Connection 4 Outlet Node Name"
        obj.plant_connection_4_outlet_node_name = var_plant_connection_4_outlet_node_name
        # alpha
        var_plant_connection_4_loading_mode = "DemandsLoad"
        obj.plant_connection_4_loading_mode = var_plant_connection_4_loading_mode
        # alpha
        var_plant_connection_4_loop_flow_request_mode = "NeedsFlowIfLoopOn"
        obj.plant_connection_4_loop_flow_request_mode = var_plant_connection_4_loop_flow_request_mode
        # object-list
        var_plant_connection_4_initialization_program_calling_manager_name = "object-list|Plant Connection 4 Initialization Program Calling Manager Name"
        obj.plant_connection_4_initialization_program_calling_manager_name = var_plant_connection_4_initialization_program_calling_manager_name
        # object-list
        var_plant_connection_4_simulation_program_calling_manager_name = "object-list|Plant Connection 4 Simulation Program Calling Manager Name"
        obj.plant_connection_4_simulation_program_calling_manager_name = var_plant_connection_4_simulation_program_calling_manager_name
        # node
        var_air_connection_inlet_node_name = "node|Air Connection Inlet Node Name"
        obj.air_connection_inlet_node_name = var_air_connection_inlet_node_name
        # node
        var_air_connection_outlet_node_name = "node|Air Connection Outlet Node Name"
        obj.air_connection_outlet_node_name = var_air_connection_outlet_node_name
        # object-list
        var_supply_inlet_water_storage_tank_name = "object-list|Supply Inlet Water Storage Tank Name"
        obj.supply_inlet_water_storage_tank_name = var_supply_inlet_water_storage_tank_name
        # object-list
        var_collection_outlet_water_storage_tank_name = "object-list|Collection Outlet Water Storage Tank Name"
        obj.collection_outlet_water_storage_tank_name = var_collection_outlet_water_storage_tank_name
        # object-list
        var_ambient_zone_name = "object-list|Ambient Zone Name"
        obj.ambient_zone_name = var_ambient_zone_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].name, var_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].main_model_program_calling_manager_name, var_main_model_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].number_of_plant_loop_connections, var_number_of_plant_loop_connections)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_inlet_node_name, var_plant_connection_1_inlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_outlet_node_name, var_plant_connection_1_outlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_loading_mode, var_plant_connection_1_loading_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_loop_flow_request_mode, var_plant_connection_1_loop_flow_request_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_initialization_program_calling_manager_name, var_plant_connection_1_initialization_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_1_simulation_program_calling_manager_name, var_plant_connection_1_simulation_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_inlet_node_name, var_plant_connection_2_inlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_outlet_node_name, var_plant_connection_2_outlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_loading_mode, var_plant_connection_2_loading_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_loop_flow_request_mode, var_plant_connection_2_loop_flow_request_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_initialization_program_calling_manager_name, var_plant_connection_2_initialization_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_2_simulation_program_calling_manager_name, var_plant_connection_2_simulation_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_inlet_node_name, var_plant_connection_3_inlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_outlet_node_name, var_plant_connection_3_outlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_loading_mode, var_plant_connection_3_loading_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_loop_flow_request_mode, var_plant_connection_3_loop_flow_request_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_initialization_program_calling_manager_name, var_plant_connection_3_initialization_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_3_simulation_program_calling_manager_name, var_plant_connection_3_simulation_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_inlet_node_name, var_plant_connection_4_inlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_outlet_node_name, var_plant_connection_4_outlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_loading_mode, var_plant_connection_4_loading_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_loop_flow_request_mode, var_plant_connection_4_loop_flow_request_mode)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_initialization_program_calling_manager_name, var_plant_connection_4_initialization_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].plant_connection_4_simulation_program_calling_manager_name, var_plant_connection_4_simulation_program_calling_manager_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].air_connection_inlet_node_name, var_air_connection_inlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].air_connection_outlet_node_name, var_air_connection_outlet_node_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].supply_inlet_water_storage_tank_name, var_supply_inlet_water_storage_tank_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].collection_outlet_water_storage_tank_name, var_collection_outlet_water_storage_tank_name)
        self.assertEqual(idf2.plantcomponentuserdefineds[0].ambient_zone_name, var_ambient_zone_name)