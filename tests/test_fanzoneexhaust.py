import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.fans import FanZoneExhaust

log = logging.getLogger(__name__)

class TestFanZoneExhaust(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fanzoneexhaust(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FanZoneExhaust()
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
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # object-list
        var_flow_fraction_schedule_name = "object-list|Flow Fraction Schedule Name"
        obj.flow_fraction_schedule_name = var_flow_fraction_schedule_name
        # alpha
        var_system_availability_manager_coupling_mode = "Coupled"
        obj.system_availability_manager_coupling_mode = var_system_availability_manager_coupling_mode
        # object-list
        var_minimum_zone_temperature_limit_schedule_name = "object-list|Minimum Zone Temperature Limit Schedule Name"
        obj.minimum_zone_temperature_limit_schedule_name = var_minimum_zone_temperature_limit_schedule_name
        # object-list
        var_balanced_exhaust_fraction_schedule_name = "object-list|Balanced Exhaust Fraction Schedule Name"
        obj.balanced_exhaust_fraction_schedule_name = var_balanced_exhaust_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fanzoneexhausts[0].name, var_name)
        self.assertEqual(idf2.fanzoneexhausts[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.fanzoneexhausts[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.fanzoneexhausts[0].pressure_rise, var_pressure_rise)
        self.assertAlmostEqual(idf2.fanzoneexhausts[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertEqual(idf2.fanzoneexhausts[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.fanzoneexhausts[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.fanzoneexhausts[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.fanzoneexhausts[0].flow_fraction_schedule_name, var_flow_fraction_schedule_name)
        self.assertEqual(idf2.fanzoneexhausts[0].system_availability_manager_coupling_mode, var_system_availability_manager_coupling_mode)
        self.assertEqual(idf2.fanzoneexhausts[0].minimum_zone_temperature_limit_schedule_name, var_minimum_zone_temperature_limit_schedule_name)
        self.assertEqual(idf2.fanzoneexhausts[0].balanced_exhaust_fraction_schedule_name, var_balanced_exhaust_fraction_schedule_name)