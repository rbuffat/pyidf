import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateZonePthp
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateZonePthp(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonepthp(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZonePthp()
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
        var_cooling_coil_gross_rated_cop = 0.0001
        obj.cooling_coil_gross_rated_cop = var_cooling_coil_gross_rated_cop
        # alpha
        var_heat_pump_heating_coil_type = "SingleSpeedDXHeatPump"
        obj.heat_pump_heating_coil_type = var_heat_pump_heating_coil_type
        # object-list
        var_heat_pump_heating_coil_availability_schedule_name = "object-list|Heat Pump Heating Coil Availability Schedule Name"
        obj.heat_pump_heating_coil_availability_schedule_name = var_heat_pump_heating_coil_availability_schedule_name
        # real
        var_heat_pump_heating_coil_gross_rated_capacity = 0.0001
        obj.heat_pump_heating_coil_gross_rated_capacity = var_heat_pump_heating_coil_gross_rated_capacity
        # real
        var_heat_pump_heating_coil_gross_rated_cop = 0.0001
        obj.heat_pump_heating_coil_gross_rated_cop = var_heat_pump_heating_coil_gross_rated_cop
        # real
        var_heat_pump_heating_minimum_outdoor_drybulb_temperature = -20.0
        obj.heat_pump_heating_minimum_outdoor_drybulb_temperature = var_heat_pump_heating_minimum_outdoor_drybulb_temperature
        # real
        var_heat_pump_defrost_maximum_outdoor_drybulb_temperature = 3.61
        obj.heat_pump_defrost_maximum_outdoor_drybulb_temperature = var_heat_pump_defrost_maximum_outdoor_drybulb_temperature
        # alpha
        var_heat_pump_defrost_strategy = "ReverseCycle"
        obj.heat_pump_defrost_strategy = var_heat_pump_defrost_strategy
        # alpha
        var_heat_pump_defrost_control = "Timed"
        obj.heat_pump_defrost_control = var_heat_pump_defrost_control
        # real
        var_heat_pump_defrost_time_period_fraction = 0.0
        obj.heat_pump_defrost_time_period_fraction = var_heat_pump_defrost_time_period_fraction
        # alpha
        var_supplemental_heating_coil_type = "Electric"
        obj.supplemental_heating_coil_type = var_supplemental_heating_coil_type
        # object-list
        var_supplemental_heating_coil_availability_schedule_name = "object-list|Supplemental Heating Coil Availability Schedule Name"
        obj.supplemental_heating_coil_availability_schedule_name = var_supplemental_heating_coil_availability_schedule_name
        # real
        var_supplemental_heating_coil_capacity = 34.34
        obj.supplemental_heating_coil_capacity = var_supplemental_heating_coil_capacity
        # real
        var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature = 21.0
        obj.supplemental_heating_coil_maximum_outdoor_drybulb_temperature = var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature
        # real
        var_supplemental_gas_heating_coil_efficiency = 0.5
        obj.supplemental_gas_heating_coil_efficiency = var_supplemental_gas_heating_coil_efficiency
        # real
        var_supplemental_gas_heating_coil_parasitic_electric_load = 0.0
        obj.supplemental_gas_heating_coil_parasitic_electric_load = var_supplemental_gas_heating_coil_parasitic_electric_load
        # object-list
        var_dedicated_outdoor_air_system_name = "object-list|Dedicated Outdoor Air System Name"
        obj.dedicated_outdoor_air_system_name = var_dedicated_outdoor_air_system_name
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 40.4
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 41.41
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 43.43
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 44.44
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
        var_baseboard_heating_capacity = 49.49
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonepthps[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertEqual(idf2.hvactemplatezonepthps[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonepthps[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].supply_fan_operating_mode_schedule_name, var_supply_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].supply_fan_placement, var_supply_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertEqual(idf2.hvactemplatezonepthps[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatezonepthps[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].cooling_coil_gross_rated_total_capacity, var_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].cooling_coil_gross_rated_sensible_heat_ratio, var_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].cooling_coil_gross_rated_cop, var_cooling_coil_gross_rated_cop)
        self.assertEqual(idf2.hvactemplatezonepthps[0].heat_pump_heating_coil_type, var_heat_pump_heating_coil_type)
        self.assertEqual(idf2.hvactemplatezonepthps[0].heat_pump_heating_coil_availability_schedule_name, var_heat_pump_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heat_pump_heating_coil_gross_rated_capacity, var_heat_pump_heating_coil_gross_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heat_pump_heating_coil_gross_rated_cop, var_heat_pump_heating_coil_gross_rated_cop)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heat_pump_heating_minimum_outdoor_drybulb_temperature, var_heat_pump_heating_minimum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heat_pump_defrost_maximum_outdoor_drybulb_temperature, var_heat_pump_defrost_maximum_outdoor_drybulb_temperature)
        self.assertEqual(idf2.hvactemplatezonepthps[0].heat_pump_defrost_strategy, var_heat_pump_defrost_strategy)
        self.assertEqual(idf2.hvactemplatezonepthps[0].heat_pump_defrost_control, var_heat_pump_defrost_control)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].heat_pump_defrost_time_period_fraction, var_heat_pump_defrost_time_period_fraction)
        self.assertEqual(idf2.hvactemplatezonepthps[0].supplemental_heating_coil_type, var_supplemental_heating_coil_type)
        self.assertEqual(idf2.hvactemplatezonepthps[0].supplemental_heating_coil_availability_schedule_name, var_supplemental_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supplemental_heating_coil_capacity, var_supplemental_heating_coil_capacity)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supplemental_heating_coil_maximum_outdoor_drybulb_temperature, var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supplemental_gas_heating_coil_efficiency, var_supplemental_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].supplemental_gas_heating_coil_parasitic_electric_load, var_supplemental_gas_heating_coil_parasitic_electric_load)
        self.assertEqual(idf2.hvactemplatezonepthps[0].dedicated_outdoor_air_system_name, var_dedicated_outdoor_air_system_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonepthps[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonepthps[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)
        self.assertEqual(idf2.hvactemplatezonepthps[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonepthps[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonepthps[0].baseboard_heating_capacity, var_baseboard_heating_capacity)