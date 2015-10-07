import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_equipment_connections import ZoneHvacEquipmentConnections

log = logging.getLogger(__name__)

class TestZoneHvacEquipmentConnections(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacequipmentconnections(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacEquipmentConnections()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_zone_conditioning_equipment_list_name = "object-list|Zone Conditioning Equipment List Name"
        obj.zone_conditioning_equipment_list_name = var_zone_conditioning_equipment_list_name
        # node
        var_zone_air_inlet_node_or_nodelist_name = "node|Zone Air Inlet Node or NodeList Name"
        obj.zone_air_inlet_node_or_nodelist_name = var_zone_air_inlet_node_or_nodelist_name
        # node
        var_zone_air_exhaust_node_or_nodelist_name = "node|Zone Air Exhaust Node or NodeList Name"
        obj.zone_air_exhaust_node_or_nodelist_name = var_zone_air_exhaust_node_or_nodelist_name
        # node
        var_zone_air_node_name = "node|Zone Air Node Name"
        obj.zone_air_node_name = var_zone_air_node_name
        # node
        var_zone_return_air_node_name = "node|Zone Return Air Node Name"
        obj.zone_return_air_node_name = var_zone_return_air_node_name
        # object-list
        var_zone_return_air_flow_rate_fraction_schedule_name = "object-list|Zone Return Air Flow Rate Fraction Schedule Name"
        obj.zone_return_air_flow_rate_fraction_schedule_name = var_zone_return_air_flow_rate_fraction_schedule_name
        # node
        var_zone_return_air_flow_rate_basis_node_or_nodelist_name = "node|Zone Return Air Flow Rate Basis Node or NodeList Name"
        obj.zone_return_air_flow_rate_basis_node_or_nodelist_name = var_zone_return_air_flow_rate_basis_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_conditioning_equipment_list_name, var_zone_conditioning_equipment_list_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_air_inlet_node_or_nodelist_name, var_zone_air_inlet_node_or_nodelist_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_air_exhaust_node_or_nodelist_name, var_zone_air_exhaust_node_or_nodelist_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_air_node_name, var_zone_air_node_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_return_air_node_name, var_zone_return_air_node_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_return_air_flow_rate_fraction_schedule_name, var_zone_return_air_flow_rate_fraction_schedule_name)
        self.assertEqual(idf2.zonehvacequipmentconnectionss[0].zone_return_air_flow_rate_basis_node_or_nodelist_name, var_zone_return_air_flow_rate_basis_node_or_nodelist_name)