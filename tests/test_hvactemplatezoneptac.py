import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateZonePtac

log = logging.getLogger(__name__)

class TestHvactemplateZonePtac(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezoneptac(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZonePtac()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_cooling_supply_air_flow_rate = 0.0001
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate = 0.0001
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # real
        var_zone_cooling_sizing_factor = 0.0
        obj.zone_cooling_sizing_factor = var_zone_cooling_sizing_factor
        # alpha
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 9.9
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 10.1
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 11.11
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # object-list
        var_supply_fan_operating_mode_schedule_name = "object-list|Supply Fan Operating Mode Schedule Name"
        obj.supply_fan_operating_mode_schedule_name = var_supply_fan_operating_mode_schedule_name
        # alpha
        var_supply_fan_placement = "BlowThrough"
        obj.supply_fan_placement = var_supply_fan_placement
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
        var_cooling_coil_type = "SingleSpeedDX"
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
        # real
        var_cooling_coil_gross_rated_cooling_cop = 0.0001
        obj.cooling_coil_gross_rated_cooling_cop = var_cooling_coil_gross_rated_cooling_cop
        # alpha
        var_heating_coil_type = "Electric"
        obj.heating_coil_type = var_heating_coil_type
        # object-list
        var_heating_coil_availability_schedule_name = "object-list|Heating Coil Availability Schedule Name"
        obj.heating_coil_availability_schedule_name = var_heating_coil_availability_schedule_name
        # real
        var_heating_coil_capacity = 25.25
        obj.heating_coil_capacity = var_heating_coil_capacity
        # real
        var_gas_heating_coil_efficiency = 0.5
        obj.gas_heating_coil_efficiency = var_gas_heating_coil_efficiency
        # real
        var_gas_heating_coil_parasitic_electric_load = 0.0
        obj.gas_heating_coil_parasitic_electric_load = var_gas_heating_coil_parasitic_electric_load
        # object-list
        var_dedicated_outdoor_air_system_name = "object-list|Dedicated Outdoor Air System Name"
        obj.dedicated_outdoor_air_system_name = var_dedicated_outdoor_air_system_name
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 30.3
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 31.31
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 33.33
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 34.34
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 39.39
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].supply_fan_operating_mode_schedule_name, var_supply_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].supply_fan_placement, var_supply_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].cooling_coil_gross_rated_total_capacity, var_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].cooling_coil_gross_rated_sensible_heat_ratio, var_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].cooling_coil_gross_rated_cooling_cop, var_cooling_coil_gross_rated_cooling_cop)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].heating_coil_capacity, var_heating_coil_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].gas_heating_coil_efficiency, var_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].gas_heating_coil_parasitic_electric_load, var_gas_heating_coil_parasitic_electric_load)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].dedicated_outdoor_air_system_name, var_dedicated_outdoor_air_system_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezoneptacs[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezoneptacs[0].baseboard_heating_capacity, var_baseboard_heating_capacity)