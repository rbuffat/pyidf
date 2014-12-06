import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilCoolingWater
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilCoolingWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingwater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_design_water_flow_rate = 0.0
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_design_air_flow_rate = 0.0
        obj.design_air_flow_rate = var_design_air_flow_rate
        # real
        var_design_inlet_water_temperature = 0.0001
        obj.design_inlet_water_temperature = var_design_inlet_water_temperature
        # real
        var_design_inlet_air_temperature = 0.0001
        obj.design_inlet_air_temperature = var_design_inlet_air_temperature
        # real
        var_design_outlet_air_temperature = 0.0001
        obj.design_outlet_air_temperature = var_design_outlet_air_temperature
        # real
        var_design_inlet_air_humidity_ratio = 0.0
        obj.design_inlet_air_humidity_ratio = var_design_inlet_air_humidity_ratio
        # real
        var_design_outlet_air_humidity_ratio = 0.0
        obj.design_outlet_air_humidity_ratio = var_design_outlet_air_humidity_ratio
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_type_of_analysis = "SimpleAnalysis"
        obj.type_of_analysis = var_type_of_analysis
        # alpha
        var_heat_exchanger_configuration = "CrossFlow"
        obj.heat_exchanger_configuration = var_heat_exchanger_configuration
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingwaters[0].name, var_name)
        self.assertEqual(idf2.coilcoolingwaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_air_flow_rate, var_design_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_inlet_water_temperature, var_design_inlet_water_temperature)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_inlet_air_temperature, var_design_inlet_air_temperature)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_outlet_air_temperature, var_design_outlet_air_temperature)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_inlet_air_humidity_ratio, var_design_inlet_air_humidity_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwaters[0].design_outlet_air_humidity_ratio, var_design_outlet_air_humidity_ratio)
        self.assertEqual(idf2.coilcoolingwaters[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwaters[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwaters[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwaters[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwaters[0].type_of_analysis, var_type_of_analysis)
        self.assertEqual(idf2.coilcoolingwaters[0].heat_exchanger_configuration, var_heat_exchanger_configuration)
        self.assertEqual(idf2.coilcoolingwaters[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)