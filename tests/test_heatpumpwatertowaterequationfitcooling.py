import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import HeatPumpWaterToWaterEquationFitCooling

log = logging.getLogger(__name__)

class TestHeatPumpWaterToWaterEquationFitCooling(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatpumpwatertowaterequationfitcooling(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatPumpWaterToWaterEquationFitCooling()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_source_side_inlet_node_name = "node|Source Side Inlet Node Name"
        obj.source_side_inlet_node_name = var_source_side_inlet_node_name
        # node
        var_source_side_outlet_node_name = "node|Source Side Outlet Node Name"
        obj.source_side_outlet_node_name = var_source_side_outlet_node_name
        # node
        var_load_side_inlet_node_name = "node|Load Side Inlet Node Name"
        obj.load_side_inlet_node_name = var_load_side_inlet_node_name
        # node
        var_load_side_outlet_node_name = "node|Load Side Outlet Node Name"
        obj.load_side_outlet_node_name = var_load_side_outlet_node_name
        # real
        var_rated_load_side_flow_rate = 0.0001
        obj.rated_load_side_flow_rate = var_rated_load_side_flow_rate
        # real
        var_rated_source_side_flow_rate = 0.0001
        obj.rated_source_side_flow_rate = var_rated_source_side_flow_rate
        # real
        var_rated_cooling_capacity = 0.0001
        obj.rated_cooling_capacity = var_rated_cooling_capacity
        # real
        var_rated_cooling_power_consumption = 0.0001
        obj.rated_cooling_power_consumption = var_rated_cooling_power_consumption
        # real
        var_cooling_capacity_coefficient_1 = 10.1
        obj.cooling_capacity_coefficient_1 = var_cooling_capacity_coefficient_1
        # real
        var_cooling_capacity_coefficient_2 = 11.11
        obj.cooling_capacity_coefficient_2 = var_cooling_capacity_coefficient_2
        # real
        var_cooling_capacity_coefficient_3 = 12.12
        obj.cooling_capacity_coefficient_3 = var_cooling_capacity_coefficient_3
        # real
        var_cooling_capacity_coefficient_4 = 13.13
        obj.cooling_capacity_coefficient_4 = var_cooling_capacity_coefficient_4
        # real
        var_cooling_capacity_coefficient_5 = 14.14
        obj.cooling_capacity_coefficient_5 = var_cooling_capacity_coefficient_5
        # real
        var_cooling_compressor_power_coefficient_1 = 15.15
        obj.cooling_compressor_power_coefficient_1 = var_cooling_compressor_power_coefficient_1
        # real
        var_cooling_compressor_power_coefficient_2 = 16.16
        obj.cooling_compressor_power_coefficient_2 = var_cooling_compressor_power_coefficient_2
        # real
        var_cooling_compressor_power_coefficient_3 = 17.17
        obj.cooling_compressor_power_coefficient_3 = var_cooling_compressor_power_coefficient_3
        # real
        var_cooling_compressor_power_coefficient_4 = 18.18
        obj.cooling_compressor_power_coefficient_4 = var_cooling_compressor_power_coefficient_4
        # real
        var_cooling_compressor_power_coefficient_5 = 19.19
        obj.cooling_compressor_power_coefficient_5 = var_cooling_compressor_power_coefficient_5

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].name, var_name)
        self.assertEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].load_side_inlet_node_name, var_load_side_inlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].load_side_outlet_node_name, var_load_side_outlet_node_name)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].rated_load_side_flow_rate, var_rated_load_side_flow_rate)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].rated_source_side_flow_rate, var_rated_source_side_flow_rate)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].rated_cooling_capacity, var_rated_cooling_capacity)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].rated_cooling_power_consumption, var_rated_cooling_power_consumption)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_capacity_coefficient_1, var_cooling_capacity_coefficient_1)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_capacity_coefficient_2, var_cooling_capacity_coefficient_2)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_capacity_coefficient_3, var_cooling_capacity_coefficient_3)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_capacity_coefficient_4, var_cooling_capacity_coefficient_4)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_capacity_coefficient_5, var_cooling_capacity_coefficient_5)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_compressor_power_coefficient_1, var_cooling_compressor_power_coefficient_1)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_compressor_power_coefficient_2, var_cooling_compressor_power_coefficient_2)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_compressor_power_coefficient_3, var_cooling_compressor_power_coefficient_3)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_compressor_power_coefficient_4, var_cooling_compressor_power_coefficient_4)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterequationfitcoolings[0].cooling_compressor_power_coefficient_5, var_cooling_compressor_power_coefficient_5)