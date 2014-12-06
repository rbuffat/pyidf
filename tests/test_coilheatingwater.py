import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingWater

log = logging.getLogger(__name__)

class TestCoilHeatingWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingwater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_ufactor_times_area_value = 3.3
        obj.ufactor_times_area_value = var_ufactor_times_area_value
        # real
        var_maximum_water_flow_rate = 4.4
        obj.maximum_water_flow_rate = var_maximum_water_flow_rate
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
        var_performance_input_method = "UFactorTimesAreaAndDesignWaterFlowRate"
        obj.performance_input_method = var_performance_input_method
        # real
        var_rated_capacity = 0.0
        obj.rated_capacity = var_rated_capacity
        # real
        var_rated_inlet_water_temperature = 11.11
        obj.rated_inlet_water_temperature = var_rated_inlet_water_temperature
        # real
        var_rated_inlet_air_temperature = 12.12
        obj.rated_inlet_air_temperature = var_rated_inlet_air_temperature
        # real
        var_rated_outlet_water_temperature = 13.13
        obj.rated_outlet_water_temperature = var_rated_outlet_water_temperature
        # real
        var_rated_outlet_air_temperature = 14.14
        obj.rated_outlet_air_temperature = var_rated_outlet_air_temperature
        # real
        var_rated_ratio_for_air_and_water_convection = 0.0001
        obj.rated_ratio_for_air_and_water_convection = var_rated_ratio_for_air_and_water_convection

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingwaters[0].name, var_name)
        self.assertEqual(idf2.coilheatingwaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].ufactor_times_area_value, var_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].maximum_water_flow_rate, var_maximum_water_flow_rate)
        self.assertEqual(idf2.coilheatingwaters[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilheatingwaters[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilheatingwaters[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingwaters[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingwaters[0].performance_input_method, var_performance_input_method)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_capacity, var_rated_capacity)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_inlet_water_temperature, var_rated_inlet_water_temperature)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_inlet_air_temperature, var_rated_inlet_air_temperature)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_outlet_water_temperature, var_rated_outlet_water_temperature)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_outlet_air_temperature, var_rated_outlet_air_temperature)
        self.assertAlmostEqual(idf2.coilheatingwaters[0].rated_ratio_for_air_and_water_convection, var_rated_ratio_for_air_and_water_convection)