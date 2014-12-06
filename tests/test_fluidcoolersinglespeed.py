import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import FluidCoolerSingleSpeed

log = logging.getLogger(__name__)

class TestFluidCoolerSingleSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidcoolersinglespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidCoolerSingleSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # alpha
        var_performance_input_method = "UFactorTimesAreaAndDesignWaterFlowRate"
        obj.performance_input_method = var_performance_input_method
        # real
        var_design_air_flow_rate_ufactor_times_area_value = 1050000.00005
        obj.design_air_flow_rate_ufactor_times_area_value = var_design_air_flow_rate_ufactor_times_area_value
        # real
        var_nominal_capacity = 0.0001
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_design_entering_water_temperature = 0.0001
        obj.design_entering_water_temperature = var_design_entering_water_temperature
        # real
        var_design_entering_air_temperature = 0.0001
        obj.design_entering_air_temperature = var_design_entering_air_temperature
        # real
        var_design_entering_air_wetbulb_temperature = 0.0001
        obj.design_entering_air_wetbulb_temperature = var_design_entering_air_wetbulb_temperature
        # real
        var_design_water_flow_rate = 0.0001
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_design_air_flow_rate = 0.0001
        obj.design_air_flow_rate = var_design_air_flow_rate
        # real
        var_design_air_flow_rate_fan_power = 0.0001
        obj.design_air_flow_rate_fan_power = var_design_air_flow_rate_fan_power
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidcoolersinglespeeds[0].name, var_name)
        self.assertEqual(idf2.fluidcoolersinglespeeds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.fluidcoolersinglespeeds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.fluidcoolersinglespeeds[0].performance_input_method, var_performance_input_method)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_air_flow_rate_ufactor_times_area_value, var_design_air_flow_rate_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_entering_water_temperature, var_design_entering_water_temperature)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_entering_air_temperature, var_design_entering_air_temperature)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_entering_air_wetbulb_temperature, var_design_entering_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_air_flow_rate, var_design_air_flow_rate)
        self.assertAlmostEqual(idf2.fluidcoolersinglespeeds[0].design_air_flow_rate_fan_power, var_design_air_flow_rate_fan_power)
        self.assertEqual(idf2.fluidcoolersinglespeeds[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)