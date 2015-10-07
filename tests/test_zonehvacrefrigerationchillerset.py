import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import ZoneHvacRefrigerationChillerSet

log = logging.getLogger(__name__)

class TestZoneHvacRefrigerationChillerSet(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacrefrigerationchillerset(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacRefrigerationChillerSet()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        paras = []
        var_air_chiller_1_name = "object-list|Air Chiller 1 Name"
        paras.append(var_air_chiller_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].name, var_name)
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].air_outlet_node_name, var_air_outlet_node_name)
        index = obj.extensible_field_index("Air Chiller 1 Name")
        self.assertEqual(idf2.zonehvacrefrigerationchillersets[0].extensibles[0][index], var_air_chiller_1_name)