import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacWaterToAirHeatPump

log = logging.getLogger(__name__)

class TestZoneHvacWaterToAirHeatPump(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacwatertoairheatpump(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacWaterToAirHeatPump()
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
        var_heating_coil_object_type = "Coil:Heating:WaterToAirHeatPump:EquationFit"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:WaterToAirHeatPump:EquationFit"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # real
        var_maximum_cycling_rate = 2.5
        obj.maximum_cycling_rate = var_maximum_cycling_rate
        # real
        var_heat_pump_time_constant = 250.0
        obj.heat_pump_time_constant = var_heat_pump_time_constant
        # real
        var_fraction_of_oncycle_power_use = 0.025
        obj.fraction_of_oncycle_power_use = var_fraction_of_oncycle_power_use
        # real
        var_heat_pump_fan_delay_time = 0.0
        obj.heat_pump_fan_delay_time = var_heat_pump_fan_delay_time
        # alpha
        var_supplemental_heating_coil_object_type = "Coil:Heating:Gas"
        obj.supplemental_heating_coil_object_type = var_supplemental_heating_coil_object_type
        # object-list
        var_supplemental_heating_coil_name = "object-list|Supplemental Heating Coil Name"
        obj.supplemental_heating_coil_name = var_supplemental_heating_coil_name
        # real
        var_maximum_supply_air_temperature_from_supplemental_heater = 25.25
        obj.maximum_supply_air_temperature_from_supplemental_heater = var_maximum_supply_air_temperature_from_supplemental_heater
        # real
        var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = 21.0
        obj.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation
        # node
        var_outdoor_drybulb_temperature_sensor_node_name = "node|Outdoor Dry-Bulb Temperature Sensor Node Name"
        obj.outdoor_drybulb_temperature_sensor_node_name = var_outdoor_drybulb_temperature_sensor_node_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # alpha
        var_heat_pump_coil_water_flow_mode = "Constant"
        obj.heat_pump_coil_water_flow_mode = var_heat_pump_coil_water_flow_mode
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
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].name, var_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_air_mixer_object_type, var_outdoor_air_mixer_object_type)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_air_mixer_name, var_outdoor_air_mixer_name)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_flow_rate_during_cooling_operation, var_supply_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_flow_rate_during_heating_operation, var_supply_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_flow_rate_when_no_cooling_or_heating_is_needed, var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_air_flow_rate_during_cooling_operation, var_outdoor_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_air_flow_rate_during_heating_operation, var_outdoor_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed, var_outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].cooling_coil_name, var_cooling_coil_name)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].maximum_cycling_rate, var_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].heat_pump_time_constant, var_heat_pump_time_constant)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].fraction_of_oncycle_power_use, var_fraction_of_oncycle_power_use)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].heat_pump_fan_delay_time, var_heat_pump_fan_delay_time)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].supplemental_heating_coil_object_type, var_supplemental_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].supplemental_heating_coil_name, var_supplemental_heating_coil_name)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].maximum_supply_air_temperature_from_supplemental_heater, var_maximum_supply_air_temperature_from_supplemental_heater)
        self.assertAlmostEqual(idf2.zonehvacwatertoairheatpumps[0].maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation, var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].outdoor_drybulb_temperature_sensor_node_name, var_outdoor_drybulb_temperature_sensor_node_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].heat_pump_coil_water_flow_mode, var_heat_pump_coil_water_flow_mode)
        self.assertEqual(idf2.zonehvacwatertoairheatpumps[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)