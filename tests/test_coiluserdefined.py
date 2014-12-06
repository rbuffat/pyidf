import os
import tempfile
import unittest
import pyidf
from pyidf.user_defined_hvac_and_plant_component_models import CoilUserDefined
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilUserDefined(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coiluserdefined(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilUserDefined()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_overall_model_simulation_program_calling_manager_name = "object-list|Overall Model Simulation Program Calling Manager Name"
        obj.overall_model_simulation_program_calling_manager_name = var_overall_model_simulation_program_calling_manager_name
        # object-list
        var_model_setup_and_sizing_program_calling_manager_name = "object-list|Model Setup and Sizing Program Calling Manager Name"
        obj.model_setup_and_sizing_program_calling_manager_name = var_model_setup_and_sizing_program_calling_manager_name
        # integer
        var_number_of_air_connections = 1
        obj.number_of_air_connections = var_number_of_air_connections
        # node
        var_air_connection_1_inlet_node_name = "node|Air Connection 1 Inlet Node Name"
        obj.air_connection_1_inlet_node_name = var_air_connection_1_inlet_node_name
        # node
        var_air_connection_1_outlet_node_name = "node|Air Connection 1 Outlet Node Name"
        obj.air_connection_1_outlet_node_name = var_air_connection_1_outlet_node_name
        # node
        var_air_connection_2_inlet_node_name = "node|Air Connection 2 Inlet Node Name"
        obj.air_connection_2_inlet_node_name = var_air_connection_2_inlet_node_name
        # node
        var_air_connection_2_outlet_node_name = "node|Air Connection 2 Outlet Node Name"
        obj.air_connection_2_outlet_node_name = var_air_connection_2_outlet_node_name
        # alpha
        var_plant_connection_is_used = "Yes"
        obj.plant_connection_is_used = var_plant_connection_is_used
        # node
        var_plant_connection_inlet_node_name = "node|Plant Connection Inlet Node Name"
        obj.plant_connection_inlet_node_name = var_plant_connection_inlet_node_name
        # node
        var_plant_connection_outlet_node_name = "node|Plant Connection Outlet Node Name"
        obj.plant_connection_outlet_node_name = var_plant_connection_outlet_node_name
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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coiluserdefineds[0].name, var_name)
        self.assertEqual(idf2.coiluserdefineds[0].overall_model_simulation_program_calling_manager_name, var_overall_model_simulation_program_calling_manager_name)
        self.assertEqual(idf2.coiluserdefineds[0].model_setup_and_sizing_program_calling_manager_name, var_model_setup_and_sizing_program_calling_manager_name)
        self.assertEqual(idf2.coiluserdefineds[0].number_of_air_connections, var_number_of_air_connections)
        self.assertEqual(idf2.coiluserdefineds[0].air_connection_1_inlet_node_name, var_air_connection_1_inlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].air_connection_1_outlet_node_name, var_air_connection_1_outlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].air_connection_2_inlet_node_name, var_air_connection_2_inlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].air_connection_2_outlet_node_name, var_air_connection_2_outlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].plant_connection_is_used, var_plant_connection_is_used)
        self.assertEqual(idf2.coiluserdefineds[0].plant_connection_inlet_node_name, var_plant_connection_inlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].plant_connection_outlet_node_name, var_plant_connection_outlet_node_name)
        self.assertEqual(idf2.coiluserdefineds[0].supply_inlet_water_storage_tank_name, var_supply_inlet_water_storage_tank_name)
        self.assertEqual(idf2.coiluserdefineds[0].collection_outlet_water_storage_tank_name, var_collection_outlet_water_storage_tank_name)
        self.assertEqual(idf2.coiluserdefineds[0].ambient_zone_name, var_ambient_zone_name)