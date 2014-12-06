import os
import tempfile
import unittest
import pyidf
from pyidf.solar_collectors import SolarCollectorUnglazedTranspiredMultisystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSolarCollectorUnglazedTranspiredMultisystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorunglazedtranspiredmultisystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorUnglazedTranspiredMultisystem()
        # object-list
        var_solar_collector_name = "object-list|Solar Collector Name"
        obj.solar_collector_name = var_solar_collector_name
        paras = []
        var_outdoor_air_system_1_collector_inlet_node = "node|Outdoor Air System 1 Collector Inlet Node"
        paras.append(var_outdoor_air_system_1_collector_inlet_node)
        var_outdoor_air_system_1_collector_outlet_node = "node|Outdoor Air System 1 Collector Outlet Node"
        paras.append(var_outdoor_air_system_1_collector_outlet_node)
        var_outdoor_air_system_1_mixed_air_node = "node|Outdoor Air System 1 Mixed Air Node"
        paras.append(var_outdoor_air_system_1_mixed_air_node)
        var_outdoor_air_system_1_zone_node = "node|Outdoor Air System 1 Zone Node"
        paras.append(var_outdoor_air_system_1_zone_node)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorunglazedtranspiredmultisystems[0].solar_collector_name, var_solar_collector_name)
        index = obj.extensible_field_index("Outdoor Air System 1 Collector Inlet Node")
        self.assertEqual(idf2.solarcollectorunglazedtranspiredmultisystems[0].extensibles[0][index], var_outdoor_air_system_1_collector_inlet_node)
        index = obj.extensible_field_index("Outdoor Air System 1 Collector Outlet Node")
        self.assertEqual(idf2.solarcollectorunglazedtranspiredmultisystems[0].extensibles[0][index], var_outdoor_air_system_1_collector_outlet_node)
        index = obj.extensible_field_index("Outdoor Air System 1 Mixed Air Node")
        self.assertEqual(idf2.solarcollectorunglazedtranspiredmultisystems[0].extensibles[0][index], var_outdoor_air_system_1_mixed_air_node)
        index = obj.extensible_field_index("Outdoor Air System 1 Zone Node")
        self.assertEqual(idf2.solarcollectorunglazedtranspiredmultisystems[0].extensibles[0][index], var_outdoor_air_system_1_zone_node)