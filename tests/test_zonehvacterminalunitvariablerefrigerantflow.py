import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacTerminalUnitVariableRefrigerantFlow

log = logging.getLogger(__name__)

class TestZoneHvacTerminalUnitVariableRefrigerantFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacterminalunitvariablerefrigerantflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacTerminalUnitVariableRefrigerantFlow()
        # alpha
        var_zone_terminal_unit_name = "Zone Terminal Unit Name"
        obj.zone_terminal_unit_name = var_zone_terminal_unit_name
        # object-list
        var_terminal_unit_availability_schedule = "object-list|Terminal Unit Availability Schedule"
        obj.terminal_unit_availability_schedule = var_terminal_unit_availability_schedule
        # node
        var_terminal_unit_air_inlet_node_name = "node|Terminal Unit Air Inlet Node Name"
        obj.terminal_unit_air_inlet_node_name = var_terminal_unit_air_inlet_node_name
        # node
        var_terminal_unit_air_outlet_node_name = "node|Terminal Unit Air Outlet Node Name"
        obj.terminal_unit_air_outlet_node_name = var_terminal_unit_air_outlet_node_name
        # real
        var_cooling_supply_air_flow_rate = 0.0001
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_no_cooling_supply_air_flow_rate = 0.0
        obj.no_cooling_supply_air_flow_rate = var_no_cooling_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate = 0.0001
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_no_heating_supply_air_flow_rate = 0.0
        obj.no_heating_supply_air_flow_rate = var_no_heating_supply_air_flow_rate
        # real
        var_cooling_outdoor_air_flow_rate = 0.0
        obj.cooling_outdoor_air_flow_rate = var_cooling_outdoor_air_flow_rate
        # real
        var_heating_outdoor_air_flow_rate = 0.0
        obj.heating_outdoor_air_flow_rate = var_heating_outdoor_air_flow_rate
        # real
        var_no_load_outdoor_air_flow_rate = 0.0
        obj.no_load_outdoor_air_flow_rate = var_no_load_outdoor_air_flow_rate
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_supply_air_fan_placement = "BlowThrough"
        obj.supply_air_fan_placement = var_supply_air_fan_placement
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_object_name = "object-list|Supply Air Fan Object Name"
        obj.supply_air_fan_object_name = var_supply_air_fan_object_name
        # alpha
        var_outside_air_mixer_object_type = "OutdoorAir:Mixer"
        obj.outside_air_mixer_object_type = var_outside_air_mixer_object_type
        # object-list
        var_outside_air_mixer_object_name = "object-list|Outside Air Mixer Object Name"
        obj.outside_air_mixer_object_name = var_outside_air_mixer_object_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:VariableRefrigerantFlow"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_object_name = "object-list|Cooling Coil Object Name"
        obj.cooling_coil_object_name = var_cooling_coil_object_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:DX:VariableRefrigerantFlow"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_object_name = "object-list|Heating Coil Object Name"
        obj.heating_coil_object_name = var_heating_coil_object_name
        # real
        var_zone_terminal_unit_on_parasitic_electric_energy_use = 0.0
        obj.zone_terminal_unit_on_parasitic_electric_energy_use = var_zone_terminal_unit_on_parasitic_electric_energy_use
        # real
        var_zone_terminal_unit_off_parasitic_electric_energy_use = 0.0
        obj.zone_terminal_unit_off_parasitic_electric_energy_use = var_zone_terminal_unit_off_parasitic_electric_energy_use
        # real
        var_rated_heating_capacity_sizing_ratio = 1.0
        obj.rated_heating_capacity_sizing_ratio = var_rated_heating_capacity_sizing_ratio
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
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].zone_terminal_unit_name, var_zone_terminal_unit_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].terminal_unit_availability_schedule, var_terminal_unit_availability_schedule)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].terminal_unit_air_inlet_node_name, var_terminal_unit_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].terminal_unit_air_outlet_node_name, var_terminal_unit_air_outlet_node_name)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].no_cooling_supply_air_flow_rate, var_no_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].no_heating_supply_air_flow_rate, var_no_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].cooling_outdoor_air_flow_rate, var_cooling_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].heating_outdoor_air_flow_rate, var_heating_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].no_load_outdoor_air_flow_rate, var_no_load_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].supply_air_fan_placement, var_supply_air_fan_placement)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].supply_air_fan_object_name, var_supply_air_fan_object_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].outside_air_mixer_object_type, var_outside_air_mixer_object_type)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].outside_air_mixer_object_name, var_outside_air_mixer_object_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].cooling_coil_object_name, var_cooling_coil_object_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].heating_coil_object_name, var_heating_coil_object_name)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].zone_terminal_unit_on_parasitic_electric_energy_use, var_zone_terminal_unit_on_parasitic_electric_energy_use)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].zone_terminal_unit_off_parasitic_electric_energy_use, var_zone_terminal_unit_off_parasitic_electric_energy_use)
        self.assertAlmostEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].rated_heating_capacity_sizing_ratio, var_rated_heating_capacity_sizing_ratio)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacterminalunitvariablerefrigerantflows[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)