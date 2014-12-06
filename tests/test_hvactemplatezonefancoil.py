import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateZoneFanCoil

log = logging.getLogger(__name__)

class TestHvactemplateZoneFanCoil(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonefancoil(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneFanCoil()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_supply_air_maximum_flow_rate = 3.3
        obj.supply_air_maximum_flow_rate = var_supply_air_maximum_flow_rate
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
        var_outdoor_air_flow_rate_per_person = 7.7
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 8.8
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 9.9
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # real
        var_supply_fan_total_efficiency = 0.50005
        obj.supply_fan_total_efficiency = var_supply_fan_total_efficiency
        # real
        var_supply_fan_delta_pressure = 0.0
        obj.supply_fan_delta_pressure = var_supply_fan_delta_pressure
        # real
        var_supply_fan_motor_efficiency = 0.50005
        obj.supply_fan_motor_efficiency = var_supply_fan_motor_efficiency
        # real
        var_supply_fan_motor_in_air_stream_fraction = 0.5
        obj.supply_fan_motor_in_air_stream_fraction = var_supply_fan_motor_in_air_stream_fraction
        # alpha
        var_cooling_coil_type = "ChilledWater"
        obj.cooling_coil_type = var_cooling_coil_type
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # real
        var_cooling_coil_design_setpoint = 17.17
        obj.cooling_coil_design_setpoint = var_cooling_coil_design_setpoint
        # alpha
        var_heating_coil_type = "HotWater"
        obj.heating_coil_type = var_heating_coil_type
        # object-list
        var_heating_coil_availability_schedule_name = "object-list|Heating Coil Availability Schedule Name"
        obj.heating_coil_availability_schedule_name = var_heating_coil_availability_schedule_name
        # real
        var_heating_coil_design_setpoint = 20.2
        obj.heating_coil_design_setpoint = var_heating_coil_design_setpoint
        # object-list
        var_dedicated_outdoor_air_system_name = "object-list|Dedicated Outdoor Air System Name"
        obj.dedicated_outdoor_air_system_name = var_dedicated_outdoor_air_system_name
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 23.23
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature_difference = 25.25
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name
        # alpha
        var_capacity_control_method = "ConstantFanVariableFlow"
        obj.capacity_control_method = var_capacity_control_method
        # real
        var_low_speed_supply_air_flow_ratio = 0.0001
        obj.low_speed_supply_air_flow_ratio = var_low_speed_supply_air_flow_ratio
        # real
        var_medium_speed_supply_air_flow_ratio = 0.0001
        obj.medium_speed_supply_air_flow_ratio = var_medium_speed_supply_air_flow_ratio
        # object-list
        var_outdoor_air_schedule_name = "object-list|Outdoor Air Schedule Name"
        obj.outdoor_air_schedule_name = var_outdoor_air_schedule_name
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 34.34
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].supply_air_maximum_flow_rate, var_supply_air_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].supply_fan_motor_in_air_stream_fraction, var_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].cooling_coil_design_setpoint, var_cooling_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].heating_coil_design_setpoint, var_heating_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].dedicated_outdoor_air_system_name, var_dedicated_outdoor_air_system_name)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].capacity_control_method, var_capacity_control_method)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].low_speed_supply_air_flow_ratio, var_low_speed_supply_air_flow_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].medium_speed_supply_air_flow_ratio, var_medium_speed_supply_air_flow_ratio)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].outdoor_air_schedule_name, var_outdoor_air_schedule_name)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonefancoils[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonefancoils[0].baseboard_heating_capacity, var_baseboard_heating_capacity)