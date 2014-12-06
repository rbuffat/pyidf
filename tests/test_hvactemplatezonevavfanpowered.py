import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateZoneVavFanPowered

log = logging.getLogger(__name__)

class TestHvactemplateZoneVavFanPowered(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonevavfanpowered(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneVavFanPowered()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_vav_system_name = "object-list|Template VAV System Name"
        obj.template_vav_system_name = var_template_vav_system_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_primary_supply_air_maximum_flow_rate = 4.4
        obj.primary_supply_air_maximum_flow_rate = var_primary_supply_air_maximum_flow_rate
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # real
        var_zone_cooling_sizing_factor = 0.0
        obj.zone_cooling_sizing_factor = var_zone_cooling_sizing_factor
        # real
        var_primary_supply_air_minimum_flow_fraction = 0.5
        obj.primary_supply_air_minimum_flow_fraction = var_primary_supply_air_minimum_flow_fraction
        # real
        var_secondary_supply_air_maximum_flow_rate = 8.8
        obj.secondary_supply_air_maximum_flow_rate = var_secondary_supply_air_maximum_flow_rate
        # alpha
        var_flow_type = "Series"
        obj.flow_type = var_flow_type
        # real
        var_parallel_fan_on_flow_fraction = 10.1
        obj.parallel_fan_on_flow_fraction = var_parallel_fan_on_flow_fraction
        # alpha
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 12.12
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 13.13
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 14.14
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # alpha
        var_reheat_coil_type = "HotWater"
        obj.reheat_coil_type = var_reheat_coil_type
        # object-list
        var_reheat_coil_availability_schedule_name = "object-list|Reheat Coil Availability Schedule Name"
        obj.reheat_coil_availability_schedule_name = var_reheat_coil_availability_schedule_name
        # real
        var_fan_total_efficiency = 0.50005
        obj.fan_total_efficiency = var_fan_total_efficiency
        # real
        var_fan_delta_pressure = 0.0
        obj.fan_delta_pressure = var_fan_delta_pressure
        # real
        var_fan_motor_efficiency = 0.50005
        obj.fan_motor_efficiency = var_fan_motor_efficiency
        # object-list
        var_supply_plenum_name = "object-list|Supply Plenum Name"
        obj.supply_plenum_name = var_supply_plenum_name
        # object-list
        var_return_plenum_name = "object-list|Return Plenum Name"
        obj.return_plenum_name = var_return_plenum_name
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 24.24
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 26.26
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 27.27
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 29.29
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 30.3
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # object-list
        var_zone_piu_fan_schedule_name = "object-list|Zone PIU Fan Schedule Name"
        obj.zone_piu_fan_schedule_name = var_zone_piu_fan_schedule_name
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].template_vav_system_name, var_template_vav_system_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].primary_supply_air_maximum_flow_rate, var_primary_supply_air_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].primary_supply_air_minimum_flow_fraction, var_primary_supply_air_minimum_flow_fraction)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].secondary_supply_air_maximum_flow_rate, var_secondary_supply_air_maximum_flow_rate)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].flow_type, var_flow_type)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].parallel_fan_on_flow_fraction, var_parallel_fan_on_flow_fraction)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].reheat_coil_type, var_reheat_coil_type)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].reheat_coil_availability_schedule_name, var_reheat_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].fan_delta_pressure, var_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].fan_motor_efficiency, var_fan_motor_efficiency)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].supply_plenum_name, var_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].baseboard_heating_capacity, var_baseboard_heating_capacity)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].zone_piu_fan_schedule_name, var_zone_piu_fan_schedule_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezonevavfanpowereds[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)