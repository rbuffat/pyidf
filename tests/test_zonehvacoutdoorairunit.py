import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_forced_air_units import ZoneHvacOutdoorAirUnit
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacOutdoorAirUnit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacoutdoorairunit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacOutdoorAirUnit()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_outdoor_air_flow_rate = 0.0001
        obj.outdoor_air_flow_rate = var_outdoor_air_flow_rate
        # object-list
        var_outdoor_air_schedule_name = "object-list|Outdoor Air Schedule Name"
        obj.outdoor_air_schedule_name = var_outdoor_air_schedule_name
        # object-list
        var_supply_fan_name = "object-list|Supply Fan Name"
        obj.supply_fan_name = var_supply_fan_name
        # alpha
        var_supply_fan_placement = "BlowThrough"
        obj.supply_fan_placement = var_supply_fan_placement
        # object-list
        var_exhaust_fan_name = "object-list|Exhaust Fan Name"
        obj.exhaust_fan_name = var_exhaust_fan_name
        # real
        var_exhaust_air_flow_rate = 9.9
        obj.exhaust_air_flow_rate = var_exhaust_air_flow_rate
        # object-list
        var_exhaust_air_schedule_name = "object-list|Exhaust Air Schedule Name"
        obj.exhaust_air_schedule_name = var_exhaust_air_schedule_name
        # alpha
        var_unit_control_type = "NeutralControl"
        obj.unit_control_type = var_unit_control_type
        # object-list
        var_high_air_control_temperature_schedule_name = "object-list|High Air Control Temperature Schedule Name"
        obj.high_air_control_temperature_schedule_name = var_high_air_control_temperature_schedule_name
        # object-list
        var_low_air_control_temperature_schedule_name = "object-list|Low Air Control Temperature Schedule Name"
        obj.low_air_control_temperature_schedule_name = var_low_air_control_temperature_schedule_name
        # node
        var_outdoor_air_node_name = "node|Outdoor Air Node Name"
        obj.outdoor_air_node_name = var_outdoor_air_node_name
        # node
        var_airoutlet_node_name = "node|AirOutlet Node Name"
        obj.airoutlet_node_name = var_airoutlet_node_name
        # node
        var_airinlet_node_name = "node|AirInlet Node Name"
        obj.airinlet_node_name = var_airinlet_node_name
        # node
        var_supply_fanoutlet_node_name = "node|Supply FanOutlet Node Name"
        obj.supply_fanoutlet_node_name = var_supply_fanoutlet_node_name
        # object-list
        var_outdoor_air_unit_list_name = "object-list|Outdoor Air Unit List Name"
        obj.outdoor_air_unit_list_name = var_outdoor_air_unit_list_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].name, var_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonehvacoutdoorairunits[0].outdoor_air_flow_rate, var_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].outdoor_air_schedule_name, var_outdoor_air_schedule_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].supply_fan_name, var_supply_fan_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].supply_fan_placement, var_supply_fan_placement)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].exhaust_fan_name, var_exhaust_fan_name)
        self.assertAlmostEqual(idf2.zonehvacoutdoorairunits[0].exhaust_air_flow_rate, var_exhaust_air_flow_rate)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].exhaust_air_schedule_name, var_exhaust_air_schedule_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].unit_control_type, var_unit_control_type)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].high_air_control_temperature_schedule_name, var_high_air_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].low_air_control_temperature_schedule_name, var_low_air_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].outdoor_air_node_name, var_outdoor_air_node_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].airoutlet_node_name, var_airoutlet_node_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].airinlet_node_name, var_airinlet_node_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].supply_fanoutlet_node_name, var_supply_fanoutlet_node_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].outdoor_air_unit_list_name, var_outdoor_air_unit_list_name)
        self.assertEqual(idf2.zonehvacoutdoorairunits[0].availability_manager_list_name, var_availability_manager_list_name)