import os
import tempfile
import unittest
import pyidf
from pyidf.fans import FanPerformanceNightVentilation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFanPerformanceNightVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fanperformancenightventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FanPerformanceNightVentilation()
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # real
        var_fan_total_efficiency = 0.50005
        obj.fan_total_efficiency = var_fan_total_efficiency
        # real
        var_pressure_rise = 3.3
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

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fanperformancenightventilations[0].fan_name, var_fan_name)
        self.assertAlmostEqual(idf2.fanperformancenightventilations[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.fanperformancenightventilations[0].pressure_rise, var_pressure_rise)
        self.assertAlmostEqual(idf2.fanperformancenightventilations[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertAlmostEqual(idf2.fanperformancenightventilations[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.fanperformancenightventilations[0].motor_in_airstream_fraction, var_motor_in_airstream_fraction)