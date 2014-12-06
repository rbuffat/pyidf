import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import ThermalStorageIceSimple

log = logging.getLogger(__name__)

class TestThermalStorageIceSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermalstorageicesimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermalStorageIceSimple()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_ice_storage_type = "IceOnCoilInternal"
        obj.ice_storage_type = var_ice_storage_type
        # real
        var_capacity = 3.3
        obj.capacity = var_capacity
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermalstorageicesimples[0].name, var_name)
        self.assertEqual(idf2.thermalstorageicesimples[0].ice_storage_type, var_ice_storage_type)
        self.assertAlmostEqual(idf2.thermalstorageicesimples[0].capacity, var_capacity)
        self.assertEqual(idf2.thermalstorageicesimples[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.thermalstorageicesimples[0].outlet_node_name, var_outlet_node_name)