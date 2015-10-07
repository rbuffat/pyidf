import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacUnitHeater

log = logging.getLogger(__name__)

class TestZoneHvacUnitHeater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacunitheater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacUnitHeater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # real
        var_maximum_supply_air_flow_rate = 0.0001
        obj.maximum_supply_air_flow_rate = var_maximum_supply_air_flow_rate
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Water"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_supply_air_fan_operation_during_no_heating = "Yes"
        obj.supply_air_fan_operation_during_no_heating = var_supply_air_fan_operation_during_no_heating
        # real
        var_maximum_hot_water_or_steam_flow_rate = 0.0001
        obj.maximum_hot_water_or_steam_flow_rate = var_maximum_hot_water_or_steam_flow_rate
        # real
        var_minimum_hot_water_or_steam_flow_rate = 0.0
        obj.minimum_hot_water_or_steam_flow_rate = var_minimum_hot_water_or_steam_flow_rate
        # real
        var_heating_convergence_tolerance = 0.0001
        obj.heating_convergence_tolerance = var_heating_convergence_tolerance
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacunitheaters[0].name, var_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacunitheaters[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertAlmostEqual(idf2.zonehvacunitheaters[0].maximum_supply_air_flow_rate, var_maximum_supply_air_flow_rate)
        self.assertEqual(idf2.zonehvacunitheaters[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacunitheaters[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].supply_air_fan_operation_during_no_heating, var_supply_air_fan_operation_during_no_heating)
        self.assertAlmostEqual(idf2.zonehvacunitheaters[0].maximum_hot_water_or_steam_flow_rate, var_maximum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacunitheaters[0].minimum_hot_water_or_steam_flow_rate, var_minimum_hot_water_or_steam_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacunitheaters[0].heating_convergence_tolerance, var_heating_convergence_tolerance)
        self.assertEqual(idf2.zonehvacunitheaters[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacunitheaters[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)