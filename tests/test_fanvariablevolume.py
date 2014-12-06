import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.fans import FanVariableVolume

log = logging.getLogger(__name__)

class TestFanVariableVolume(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fanvariablevolume(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FanVariableVolume()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_fan_total_efficiency = 0.50005
        obj.fan_total_efficiency = var_fan_total_efficiency
        # real
        var_pressure_rise = 4.4
        obj.pressure_rise = var_pressure_rise
        # real
        var_maximum_flow_rate = 0.0
        obj.maximum_flow_rate = var_maximum_flow_rate
        # alpha
        var_fan_power_minimum_flow_rate_input_method = "Fraction"
        obj.fan_power_minimum_flow_rate_input_method = var_fan_power_minimum_flow_rate_input_method
        # real
        var_fan_power_minimum_flow_fraction = 0.5
        obj.fan_power_minimum_flow_fraction = var_fan_power_minimum_flow_fraction
        # real
        var_fan_power_minimum_air_flow_rate = 0.0
        obj.fan_power_minimum_air_flow_rate = var_fan_power_minimum_air_flow_rate
        # real
        var_motor_efficiency = 0.50005
        obj.motor_efficiency = var_motor_efficiency
        # real
        var_motor_in_airstream_fraction = 0.5
        obj.motor_in_airstream_fraction = var_motor_in_airstream_fraction
        # real
        var_fan_power_coefficient_1 = 11.11
        obj.fan_power_coefficient_1 = var_fan_power_coefficient_1
        # real
        var_fan_power_coefficient_2 = 12.12
        obj.fan_power_coefficient_2 = var_fan_power_coefficient_2
        # real
        var_fan_power_coefficient_3 = 13.13
        obj.fan_power_coefficient_3 = var_fan_power_coefficient_3
        # real
        var_fan_power_coefficient_4 = 14.14
        obj.fan_power_coefficient_4 = var_fan_power_coefficient_4
        # real
        var_fan_power_coefficient_5 = 15.15
        obj.fan_power_coefficient_5 = var_fan_power_coefficient_5
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fanvariablevolumes[0].name, var_name)
        self.assertEqual(idf2.fanvariablevolumes[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].pressure_rise, var_pressure_rise)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertEqual(idf2.fanvariablevolumes[0].fan_power_minimum_flow_rate_input_method, var_fan_power_minimum_flow_rate_input_method)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_minimum_flow_fraction, var_fan_power_minimum_flow_fraction)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_minimum_air_flow_rate, var_fan_power_minimum_air_flow_rate)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].motor_in_airstream_fraction, var_motor_in_airstream_fraction)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_coefficient_1, var_fan_power_coefficient_1)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_coefficient_2, var_fan_power_coefficient_2)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_coefficient_3, var_fan_power_coefficient_3)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_coefficient_4, var_fan_power_coefficient_4)
        self.assertAlmostEqual(idf2.fanvariablevolumes[0].fan_power_coefficient_5, var_fan_power_coefficient_5)
        self.assertEqual(idf2.fanvariablevolumes[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.fanvariablevolumes[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.fanvariablevolumes[0].enduse_subcategory, var_enduse_subcategory)