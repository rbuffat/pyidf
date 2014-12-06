import os
import tempfile
import unittest
import pyidf
from pyidf.fans import FanConstantVolume
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFanConstantVolume(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fanconstantvolume(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FanConstantVolume()
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
        # real
        var_motor_efficiency = 0.50005
        obj.motor_efficiency = var_motor_efficiency
        # real
        var_motor_in_airstream_fraction = 0.5
        obj.motor_in_airstream_fraction = var_motor_in_airstream_fraction
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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fanconstantvolumes[0].name, var_name)
        self.assertEqual(idf2.fanconstantvolumes[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.fanconstantvolumes[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.fanconstantvolumes[0].pressure_rise, var_pressure_rise)
        self.assertAlmostEqual(idf2.fanconstantvolumes[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertAlmostEqual(idf2.fanconstantvolumes[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.fanconstantvolumes[0].motor_in_airstream_fraction, var_motor_in_airstream_fraction)
        self.assertEqual(idf2.fanconstantvolumes[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.fanconstantvolumes[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.fanconstantvolumes[0].enduse_subcategory, var_enduse_subcategory)