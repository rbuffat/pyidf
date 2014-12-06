import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_forced_air_units import ZoneHvacPackagedTerminalHeatPump
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacPackagedTerminalHeatPump(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacpackagedterminalheatpump(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacPackagedTerminalHeatPump()
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
        var_outdoor_air_mixer_object_type = "OutdoorAir:Mixer"
        obj.outdoor_air_mixer_object_type = var_outdoor_air_mixer_object_type
        # object-list
        var_outdoor_air_mixer_name = "object-list|Outdoor Air Mixer Name"
        obj.outdoor_air_mixer_name = var_outdoor_air_mixer_name
        # real
        var_supply_air_flow_rate_during_cooling_operation = 0.0001
        obj.supply_air_flow_rate_during_cooling_operation = var_supply_air_flow_rate_during_cooling_operation
        # real
        var_supply_air_flow_rate_during_heating_operation = 0.0001
        obj.supply_air_flow_rate_during_heating_operation = var_supply_air_flow_rate_during_heating_operation
        # real
        var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed = 0.0
        obj.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed
        # real
        var_outdoor_air_flow_rate_during_cooling_operation = 0.0
        obj.outdoor_air_flow_rate_during_cooling_operation = var_outdoor_air_flow_rate_during_cooling_operation
        # real
        var_outdoor_air_flow_rate_during_heating_operation = 0.0
        obj.outdoor_air_flow_rate_during_heating_operation = var_outdoor_air_flow_rate_during_heating_operation
        # real
        var_outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = 0.0
        obj.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = var_outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:DX:SingleSpeed"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_heating_convergence_tolerance = 0.0001
        obj.heating_convergence_tolerance = var_heating_convergence_tolerance
        # real
        var_minimum_outdoor_drybulb_temperature_for_compressor_operation = -20.0
        obj.minimum_outdoor_drybulb_temperature_for_compressor_operation = var_minimum_outdoor_drybulb_temperature_for_compressor_operation
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # real
        var_cooling_convergence_tolerance = 0.0001
        obj.cooling_convergence_tolerance = var_cooling_convergence_tolerance
        # alpha
        var_supplemental_heating_coil_object_type = "Coil:Heating:Gas"
        obj.supplemental_heating_coil_object_type = var_supplemental_heating_coil_object_type
        # object-list
        var_supplemental_heating_coil_name = "object-list|Supplemental Heating Coil Name"
        obj.supplemental_heating_coil_name = var_supplemental_heating_coil_name
        # real
        var_maximum_supply_air_temperature_from_supplemental_heater = 24.24
        obj.maximum_supply_air_temperature_from_supplemental_heater = var_maximum_supply_air_temperature_from_supplemental_heater
        # real
        var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = 21.0
        obj.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].name, var_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].outdoor_air_mixer_object_type, var_outdoor_air_mixer_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].outdoor_air_mixer_name, var_outdoor_air_mixer_name)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_flow_rate_during_cooling_operation, var_supply_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_flow_rate_during_heating_operation, var_supply_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_flow_rate_when_no_cooling_or_heating_is_needed, var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].outdoor_air_flow_rate_during_cooling_operation, var_outdoor_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].outdoor_air_flow_rate_during_heating_operation, var_outdoor_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed, var_outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].heating_convergence_tolerance, var_heating_convergence_tolerance)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].minimum_outdoor_drybulb_temperature_for_compressor_operation, var_minimum_outdoor_drybulb_temperature_for_compressor_operation)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].cooling_coil_name, var_cooling_coil_name)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].cooling_convergence_tolerance, var_cooling_convergence_tolerance)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].supplemental_heating_coil_object_type, var_supplemental_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].supplemental_heating_coil_name, var_supplemental_heating_coil_name)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].maximum_supply_air_temperature_from_supplemental_heater, var_maximum_supply_air_temperature_from_supplemental_heater)
        self.assertAlmostEqual(idf2.zonehvacpackagedterminalheatpumps[0].maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation, var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacpackagedterminalheatpumps[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)