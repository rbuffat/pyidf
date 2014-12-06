import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.user_defined_hvac_and_plant_component_models import ZoneHvacForcedAirUserDefined

log = logging.getLogger(__name__)

class TestZoneHvacForcedAirUserDefined(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacforcedairuserdefined(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacForcedAirUserDefined()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_overall_model_simulation_program_calling_manager_name = "object-list|Overall Model Simulation Program Calling Manager Name"
        obj.overall_model_simulation_program_calling_manager_name = var_overall_model_simulation_program_calling_manager_name
        # object-list
        var_model_setup_and_sizing_program_calling_manager_name = "object-list|Model Setup and Sizing Program Calling Manager Name"
        obj.model_setup_and_sizing_program_calling_manager_name = var_model_setup_and_sizing_program_calling_manager_name
        # node
        var_primary_air_inlet_node_name = "node|Primary Air Inlet Node Name"
        obj.primary_air_inlet_node_name = var_primary_air_inlet_node_name
        # node
        var_primary_air_outlet_node_name = "node|Primary Air Outlet Node Name"
        obj.primary_air_outlet_node_name = var_primary_air_outlet_node_name
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name
        # node
        var_secondary_air_outlet_node_name = "node|Secondary Air Outlet Node Name"
        obj.secondary_air_outlet_node_name = var_secondary_air_outlet_node_name
        # integer
        var_number_of_plant_loop_connections = 1
        obj.number_of_plant_loop_connections = var_number_of_plant_loop_connections
        # node
        var_plant_connection_1_inlet_node_name = "node|Plant Connection 1 Inlet Node Name"
        obj.plant_connection_1_inlet_node_name = var_plant_connection_1_inlet_node_name
        # node
        var_plant_connection_1_outlet_node_name = "node|Plant Connection 1 Outlet Node Name"
        obj.plant_connection_1_outlet_node_name = var_plant_connection_1_outlet_node_name
        # node
        var_plant_connection_2_inlet_node_name = "node|Plant Connection 2 Inlet Node Name"
        obj.plant_connection_2_inlet_node_name = var_plant_connection_2_inlet_node_name
        # node
        var_plant_connection_2_outlet_node_name = "node|Plant Connection 2 Outlet Node Name"
        obj.plant_connection_2_outlet_node_name = var_plant_connection_2_outlet_node_name
        # node
        var_plant_connection_3_inlet_node_name = "node|Plant Connection 3 Inlet Node Name"
        obj.plant_connection_3_inlet_node_name = var_plant_connection_3_inlet_node_name
        # node
        var_plant_connection_3_outlet_node_name = "node|Plant Connection 3 Outlet Node Name"
        obj.plant_connection_3_outlet_node_name = var_plant_connection_3_outlet_node_name
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
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].name, var_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].overall_model_simulation_program_calling_manager_name, var_overall_model_simulation_program_calling_manager_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].model_setup_and_sizing_program_calling_manager_name, var_model_setup_and_sizing_program_calling_manager_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].primary_air_inlet_node_name, var_primary_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].primary_air_outlet_node_name, var_primary_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].secondary_air_outlet_node_name, var_secondary_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].number_of_plant_loop_connections, var_number_of_plant_loop_connections)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_1_inlet_node_name, var_plant_connection_1_inlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_1_outlet_node_name, var_plant_connection_1_outlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_2_inlet_node_name, var_plant_connection_2_inlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_2_outlet_node_name, var_plant_connection_2_outlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_3_inlet_node_name, var_plant_connection_3_inlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].plant_connection_3_outlet_node_name, var_plant_connection_3_outlet_node_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].supply_inlet_water_storage_tank_name, var_supply_inlet_water_storage_tank_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].collection_outlet_water_storage_tank_name, var_collection_outlet_water_storage_tank_name)
        self.assertEqual(idf2.zonehvacforcedairuserdefineds[0].ambient_zone_name, var_ambient_zone_name)