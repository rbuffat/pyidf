import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateZoneVrf
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateZoneVrf(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonevrf(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneVrf()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_vrf_system_name = "object-list|Template VRF System Name"
        obj.template_vrf_system_name = var_template_vrf_system_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # real
        var_zone_cooling_sizing_factor = 0.0
        obj.zone_cooling_sizing_factor = var_zone_cooling_sizing_factor
        # real
        var_rated_total_heating_capacity_sizing_ratio = 1.0
        obj.rated_total_heating_capacity_sizing_ratio = var_rated_total_heating_capacity_sizing_ratio
        # real
        var_supply_air_flow_rate_during_cooling_operation = 0.0001
        obj.supply_air_flow_rate_during_cooling_operation = var_supply_air_flow_rate_during_cooling_operation
        # real
        var_supply_air_flow_rate_when_no_cooling_is_needed = 0.0
        obj.supply_air_flow_rate_when_no_cooling_is_needed = var_supply_air_flow_rate_when_no_cooling_is_needed
        # real
        var_supply_air_flow_rate_during_heating_operation = 0.0001
        obj.supply_air_flow_rate_during_heating_operation = var_supply_air_flow_rate_during_heating_operation
        # real
        var_supply_air_flow_rate_when_no_heating_is_needed = 0.0
        obj.supply_air_flow_rate_when_no_heating_is_needed = var_supply_air_flow_rate_when_no_heating_is_needed
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
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 15.15
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 16.16
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 17.17
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # object-list
        var_supply_fan_operating_mode_schedule_name = "object-list|Supply Fan Operating Mode Schedule Name"
        obj.supply_fan_operating_mode_schedule_name = var_supply_fan_operating_mode_schedule_name
        # alpha
        var_supply_air_fan_placement = "BlowThrough"
        obj.supply_air_fan_placement = var_supply_air_fan_placement
        # real
        var_supply_fan_total_efficiency = 0.50005
        obj.supply_fan_total_efficiency = var_supply_fan_total_efficiency
        # real
        var_supply_fan_delta_pressure = 0.0
        obj.supply_fan_delta_pressure = var_supply_fan_delta_pressure
        # real
        var_supply_fan_motor_efficiency = 0.50005
        obj.supply_fan_motor_efficiency = var_supply_fan_motor_efficiency
        # alpha
        var_cooling_coil_type = "VariableRefrigerantFlowDX"
        obj.cooling_coil_type = var_cooling_coil_type
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # real
        var_cooling_coil_gross_rated_total_capacity = 0.0001
        obj.cooling_coil_gross_rated_total_capacity = var_cooling_coil_gross_rated_total_capacity
        # real
        var_cooling_coil_gross_rated_sensible_heat_ratio = 0.75
        obj.cooling_coil_gross_rated_sensible_heat_ratio = var_cooling_coil_gross_rated_sensible_heat_ratio
        # alpha
        var_heat_pump_heating_coil_type = "VariableRefrigerantFlowDX"
        obj.heat_pump_heating_coil_type = var_heat_pump_heating_coil_type
        # object-list
        var_heat_pump_heating_coil_availability_schedule_name = "object-list|Heat Pump Heating Coil Availability Schedule Name"
        obj.heat_pump_heating_coil_availability_schedule_name = var_heat_pump_heating_coil_availability_schedule_name
        # real
        var_heat_pump_heating_coil_gross_rated_capacity = 0.0001
        obj.heat_pump_heating_coil_gross_rated_capacity = var_heat_pump_heating_coil_gross_rated_capacity
        # real
        var_zone_terminal_unit_on_parasitic_electric_energy_use = 0.0
        obj.zone_terminal_unit_on_parasitic_electric_energy_use = var_zone_terminal_unit_on_parasitic_electric_energy_use
        # real
        var_zone_terminal_unit_off_parasitic_electric_energy_use = 0.0
        obj.zone_terminal_unit_off_parasitic_electric_energy_use = var_zone_terminal_unit_off_parasitic_electric_energy_use
        # object-list
        var_dedicated_outdoor_air_system_name = "object-list|Dedicated Outdoor Air System Name"
        obj.dedicated_outdoor_air_system_name = var_dedicated_outdoor_air_system_name
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 37.37
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 38.38
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 40.4
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 41.41
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 44.44
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].template_vrf_system_name, var_template_vrf_system_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].rated_total_heating_capacity_sizing_ratio, var_rated_total_heating_capacity_sizing_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_air_flow_rate_during_cooling_operation, var_supply_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_air_flow_rate_when_no_cooling_is_needed, var_supply_air_flow_rate_when_no_cooling_is_needed)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_air_flow_rate_during_heating_operation, var_supply_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_air_flow_rate_when_no_heating_is_needed, var_supply_air_flow_rate_when_no_heating_is_needed)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_during_cooling_operation, var_outdoor_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_during_heating_operation, var_outdoor_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed, var_outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].supply_fan_operating_mode_schedule_name, var_supply_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].supply_air_fan_placement, var_supply_air_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].cooling_coil_gross_rated_total_capacity, var_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].cooling_coil_gross_rated_sensible_heat_ratio, var_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].heat_pump_heating_coil_type, var_heat_pump_heating_coil_type)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].heat_pump_heating_coil_availability_schedule_name, var_heat_pump_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].heat_pump_heating_coil_gross_rated_capacity, var_heat_pump_heating_coil_gross_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_terminal_unit_on_parasitic_electric_energy_use, var_zone_terminal_unit_on_parasitic_electric_energy_use)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_terminal_unit_off_parasitic_electric_energy_use, var_zone_terminal_unit_off_parasitic_electric_energy_use)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].dedicated_outdoor_air_system_name, var_dedicated_outdoor_air_system_name)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonevrfs[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevrfs[0].baseboard_heating_capacity, var_baseboard_heating_capacity)