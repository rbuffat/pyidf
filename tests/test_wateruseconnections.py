import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_systems import WaterUseConnections

log = logging.getLogger(__name__)

class TestWaterUseConnections(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_wateruseconnections(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterUseConnections()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # object-list
        var_reclamation_water_storage_tank_name = "object-list|Reclamation Water Storage Tank Name"
        obj.reclamation_water_storage_tank_name = var_reclamation_water_storage_tank_name
        # object-list
        var_hot_water_supply_temperature_schedule_name = "object-list|Hot Water Supply Temperature Schedule Name"
        obj.hot_water_supply_temperature_schedule_name = var_hot_water_supply_temperature_schedule_name
        # object-list
        var_cold_water_supply_temperature_schedule_name = "object-list|Cold Water Supply Temperature Schedule Name"
        obj.cold_water_supply_temperature_schedule_name = var_cold_water_supply_temperature_schedule_name
        # alpha
        var_drain_water_heat_exchanger_type = "None"
        obj.drain_water_heat_exchanger_type = var_drain_water_heat_exchanger_type
        # alpha
        var_drain_water_heat_exchanger_destination = "Plant"
        obj.drain_water_heat_exchanger_destination = var_drain_water_heat_exchanger_destination
        # real
        var_drain_water_heat_exchanger_ufactor_times_area = 0.0
        obj.drain_water_heat_exchanger_ufactor_times_area = var_drain_water_heat_exchanger_ufactor_times_area
        paras = []
        var_water_use_equipment_1_name = "object-list|Water Use Equipment 1 Name"
        paras.append(var_water_use_equipment_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.wateruseconnectionss[0].name, var_name)
        self.assertEqual(idf2.wateruseconnectionss[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.wateruseconnectionss[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.wateruseconnectionss[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.wateruseconnectionss[0].reclamation_water_storage_tank_name, var_reclamation_water_storage_tank_name)
        self.assertEqual(idf2.wateruseconnectionss[0].hot_water_supply_temperature_schedule_name, var_hot_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.wateruseconnectionss[0].cold_water_supply_temperature_schedule_name, var_cold_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.wateruseconnectionss[0].drain_water_heat_exchanger_type, var_drain_water_heat_exchanger_type)
        self.assertEqual(idf2.wateruseconnectionss[0].drain_water_heat_exchanger_destination, var_drain_water_heat_exchanger_destination)
        self.assertAlmostEqual(idf2.wateruseconnectionss[0].drain_water_heat_exchanger_ufactor_times_area, var_drain_water_heat_exchanger_ufactor_times_area)
        index = obj.extensible_field_index("Water Use Equipment 1 Name")
        self.assertEqual(idf2.wateruseconnectionss[0].extensibles[0][index], var_water_use_equipment_1_name)