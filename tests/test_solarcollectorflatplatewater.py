import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.solar_collectors import SolarCollectorFlatPlateWater

log = logging.getLogger(__name__)

class TestSolarCollectorFlatPlateWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorflatplatewater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorFlatPlateWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_solarcollectorperformance_name = "object-list|SolarCollectorPerformance Name"
        obj.solarcollectorperformance_name = var_solarcollectorperformance_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_maximum_flow_rate = 0.0001
        obj.maximum_flow_rate = var_maximum_flow_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorflatplatewaters[0].name, var_name)
        self.assertEqual(idf2.solarcollectorflatplatewaters[0].solarcollectorperformance_name, var_solarcollectorperformance_name)
        self.assertEqual(idf2.solarcollectorflatplatewaters[0].surface_name, var_surface_name)
        self.assertEqual(idf2.solarcollectorflatplatewaters[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.solarcollectorflatplatewaters[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.solarcollectorflatplatewaters[0].maximum_flow_rate, var_maximum_flow_rate)