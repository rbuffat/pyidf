import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneInfiltrationDesignFlowRate

log = logging.getLogger(__name__)

class TestZoneInfiltrationDesignFlowRate(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneinfiltrationdesignflowrate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneInfiltrationDesignFlowRate()
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
        var_flow_per_zone_floor_area = 0.0
        obj.flow_per_zone_floor_area = var_flow_per_zone_floor_area
        # real
        var_flow_per_exterior_surface_area = 0.0
        obj.flow_per_exterior_surface_area = var_flow_per_exterior_surface_area
        # real
        var_air_changes_per_hour = 0.0
        obj.air_changes_per_hour = var_air_changes_per_hour
        # real
        var_constant_term_coefficient = 9.9
        obj.constant_term_coefficient = var_constant_term_coefficient
        # real
        var_temperature_term_coefficient = 10.1
        obj.temperature_term_coefficient = var_temperature_term_coefficient
        # real
        var_velocity_term_coefficient = 11.11
        obj.velocity_term_coefficient = var_velocity_term_coefficient
        # real
        var_velocity_squared_term_coefficient = 12.12
        obj.velocity_squared_term_coefficient = var_velocity_squared_term_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneinfiltrationdesignflowrates[0].name, var_name)
        self.assertEqual(idf2.zoneinfiltrationdesignflowrates[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.zoneinfiltrationdesignflowrates[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.zoneinfiltrationdesignflowrates[0].design_flow_rate_calculation_method, var_design_flow_rate_calculation_method)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].flow_per_zone_floor_area, var_flow_per_zone_floor_area)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].flow_per_exterior_surface_area, var_flow_per_exterior_surface_area)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].air_changes_per_hour, var_air_changes_per_hour)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].constant_term_coefficient, var_constant_term_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].temperature_term_coefficient, var_temperature_term_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].velocity_term_coefficient, var_velocity_term_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationdesignflowrates[0].velocity_squared_term_coefficient, var_velocity_squared_term_coefficient)