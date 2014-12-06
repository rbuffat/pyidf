import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_forced_air_units import ZoneHvacEvaporativeCoolerUnit
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacEvaporativeCoolerUnit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacevaporativecoolerunit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacEvaporativeCoolerUnit()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name
        # node
        var_cooler_outlet_node_name = "node|Cooler Outlet Node Name"
        obj.cooler_outlet_node_name = var_cooler_outlet_node_name
        # node
        var_zone_relief_air_node_name = "node|Zone Relief Air Node Name"
        obj.zone_relief_air_node_name = var_zone_relief_air_node_name
        # alpha
        var_supply_air_fan_object_type = "Fan:ConstantVolume"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # real
        var_design_supply_air_flow_rate = 0.0001
        obj.design_supply_air_flow_rate = var_design_supply_air_flow_rate
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # alpha
        var_cooler_unit_control_method = "ZoneTemperatureDeadbandOnOffCycling"
        obj.cooler_unit_control_method = var_cooler_unit_control_method
        # real
        var_throttling_range_temperature_difference = 0.0001
        obj.throttling_range_temperature_difference = var_throttling_range_temperature_difference
        # real
        var_cooling_load_control_threshold_heat_transfer_rate = 0.0001
        obj.cooling_load_control_threshold_heat_transfer_rate = var_cooling_load_control_threshold_heat_transfer_rate
        # alpha
        var_first_evaporative_cooler_object_type = "EvaporativeCooler:Direct:CelDekPad"
        obj.first_evaporative_cooler_object_type = var_first_evaporative_cooler_object_type
        # object-list
        var_first_evaporative_cooler_object_name = "object-list|First Evaporative Cooler Object Name"
        obj.first_evaporative_cooler_object_name = var_first_evaporative_cooler_object_name
        # alpha
        var_second_evaporative_cooler_object_type = "EvaporativeCooler:Direct:CelDekPad"
        obj.second_evaporative_cooler_object_type = var_second_evaporative_cooler_object_type
        # object-list
        var_second_evaporative_cooler_name = "object-list|Second Evaporative Cooler Name"
        obj.second_evaporative_cooler_name = var_second_evaporative_cooler_name
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].name, var_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].cooler_outlet_node_name, var_cooler_outlet_node_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].zone_relief_air_node_name, var_zone_relief_air_node_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertAlmostEqual(idf2.zonehvacevaporativecoolerunits[0].design_supply_air_flow_rate, var_design_supply_air_flow_rate)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].cooler_unit_control_method, var_cooler_unit_control_method)
        self.assertAlmostEqual(idf2.zonehvacevaporativecoolerunits[0].throttling_range_temperature_difference, var_throttling_range_temperature_difference)
        self.assertAlmostEqual(idf2.zonehvacevaporativecoolerunits[0].cooling_load_control_threshold_heat_transfer_rate, var_cooling_load_control_threshold_heat_transfer_rate)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].first_evaporative_cooler_object_type, var_first_evaporative_cooler_object_type)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].first_evaporative_cooler_object_name, var_first_evaporative_cooler_object_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].second_evaporative_cooler_object_type, var_second_evaporative_cooler_object_type)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].second_evaporative_cooler_name, var_second_evaporative_cooler_name)
        self.assertEqual(idf2.zonehvacevaporativecoolerunits[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)