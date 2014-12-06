import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneVentilationDesignFlowRate

log = logging.getLogger(__name__)

class TestZoneVentilationDesignFlowRate(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneventilationdesignflowrate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneVentilationDesignFlowRate()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # alpha
        var_design_flow_rate_calculation_method = "Flow/Zone"
        obj.design_flow_rate_calculation_method = var_design_flow_rate_calculation_method
        # real
        var_design_flow_rate = 0.0
        obj.design_flow_rate = var_design_flow_rate
        # real
        var_flow_rate_per_zone_floor_area = 0.0
        obj.flow_rate_per_zone_floor_area = var_flow_rate_per_zone_floor_area
        # real
        var_flow_rate_per_person = 0.0
        obj.flow_rate_per_person = var_flow_rate_per_person
        # real
        var_air_changes_per_hour = 0.0
        obj.air_changes_per_hour = var_air_changes_per_hour
        # alpha
        var_ventilation_type = "Natural"
        obj.ventilation_type = var_ventilation_type
        # real
        var_fan_pressure_rise = 0.0
        obj.fan_pressure_rise = var_fan_pressure_rise
        # real
        var_fan_total_efficiency = 0.0001
        obj.fan_total_efficiency = var_fan_total_efficiency
        # real
        var_constant_term_coefficient = 12.12
        obj.constant_term_coefficient = var_constant_term_coefficient
        # real
        var_temperature_term_coefficient = 13.13
        obj.temperature_term_coefficient = var_temperature_term_coefficient
        # real
        var_velocity_term_coefficient = 14.14
        obj.velocity_term_coefficient = var_velocity_term_coefficient
        # real
        var_velocity_squared_term_coefficient = 15.15
        obj.velocity_squared_term_coefficient = var_velocity_squared_term_coefficient
        # real
        var_minimum_indoor_temperature = 0.0
        obj.minimum_indoor_temperature = var_minimum_indoor_temperature
        # object-list
        var_minimum_indoor_temperature_schedule_name = "object-list|Minimum Indoor Temperature Schedule Name"
        obj.minimum_indoor_temperature_schedule_name = var_minimum_indoor_temperature_schedule_name
        # real
        var_maximum_indoor_temperature = 0.0
        obj.maximum_indoor_temperature = var_maximum_indoor_temperature
        # object-list
        var_maximum_indoor_temperature_schedule_name = "object-list|Maximum Indoor Temperature Schedule Name"
        obj.maximum_indoor_temperature_schedule_name = var_maximum_indoor_temperature_schedule_name
        # real
        var_delta_temperature = -100.0
        obj.delta_temperature = var_delta_temperature
        # object-list
        var_delta_temperature_schedule_name = "object-list|Delta Temperature Schedule Name"
        obj.delta_temperature_schedule_name = var_delta_temperature_schedule_name
        # real
        var_minimum_outdoor_temperature = 0.0
        obj.minimum_outdoor_temperature = var_minimum_outdoor_temperature
        # object-list
        var_minimum_outdoor_temperature_schedule_name = "object-list|Minimum Outdoor Temperature Schedule Name"
        obj.minimum_outdoor_temperature_schedule_name = var_minimum_outdoor_temperature_schedule_name
        # real
        var_maximum_outdoor_temperature = 0.0
        obj.maximum_outdoor_temperature = var_maximum_outdoor_temperature
        # object-list
        var_maximum_outdoor_temperature_schedule_name = "object-list|Maximum Outdoor Temperature Schedule Name"
        obj.maximum_outdoor_temperature_schedule_name = var_maximum_outdoor_temperature_schedule_name
        # real
        var_maximum_wind_speed = 20.0
        obj.maximum_wind_speed = var_maximum_wind_speed

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].name, var_name)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].design_flow_rate_calculation_method, var_design_flow_rate_calculation_method)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].flow_rate_per_zone_floor_area, var_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].flow_rate_per_person, var_flow_rate_per_person)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].air_changes_per_hour, var_air_changes_per_hour)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].ventilation_type, var_ventilation_type)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].fan_pressure_rise, var_fan_pressure_rise)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].constant_term_coefficient, var_constant_term_coefficient)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].temperature_term_coefficient, var_temperature_term_coefficient)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].velocity_term_coefficient, var_velocity_term_coefficient)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].velocity_squared_term_coefficient, var_velocity_squared_term_coefficient)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].minimum_indoor_temperature, var_minimum_indoor_temperature)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].minimum_indoor_temperature_schedule_name, var_minimum_indoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].maximum_indoor_temperature, var_maximum_indoor_temperature)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].maximum_indoor_temperature_schedule_name, var_maximum_indoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].delta_temperature, var_delta_temperature)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].delta_temperature_schedule_name, var_delta_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].minimum_outdoor_temperature, var_minimum_outdoor_temperature)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].minimum_outdoor_temperature_schedule_name, var_minimum_outdoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].maximum_outdoor_temperature, var_maximum_outdoor_temperature)
        self.assertEqual(idf2.zoneventilationdesignflowrates[0].maximum_outdoor_temperature_schedule_name, var_maximum_outdoor_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zoneventilationdesignflowrates[0].maximum_wind_speed, var_maximum_wind_speed)