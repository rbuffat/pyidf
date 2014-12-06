import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneMixing

log = logging.getLogger(__name__)

class TestZoneMixing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonemixing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneMixing()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
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
        # object-list
        var_source_zone_name = "object-list|Source Zone Name"
        obj.source_zone_name = var_source_zone_name
        # real
        var_delta_temperature = 10.1
        obj.delta_temperature = var_delta_temperature
        # object-list
        var_delta_temperature_schedule_name = "object-list|Delta Temperature Schedule Name"
        obj.delta_temperature_schedule_name = var_delta_temperature_schedule_name
        # object-list
        var_minimum_zone_temperature_schedule_name = "object-list|Minimum Zone Temperature Schedule Name"
        obj.minimum_zone_temperature_schedule_name = var_minimum_zone_temperature_schedule_name
        # object-list
        var_maximum_zone_temperature_schedule_name = "object-list|Maximum Zone Temperature Schedule Name"
        obj.maximum_zone_temperature_schedule_name = var_maximum_zone_temperature_schedule_name
        # object-list
        var_minimum_source_zone_temperature_schedule_name = "object-list|Minimum Source Zone Temperature Schedule Name"
        obj.minimum_source_zone_temperature_schedule_name = var_minimum_source_zone_temperature_schedule_name
        # object-list
        var_maximum_source_zone_temperature_schedule_name = "object-list|Maximum Source Zone Temperature Schedule Name"
        obj.maximum_source_zone_temperature_schedule_name = var_maximum_source_zone_temperature_schedule_name
        # object-list
        var_minimum_outdoor_temperature_schedule_name = "object-list|Minimum Outdoor Temperature Schedule Name"
        obj.minimum_outdoor_temperature_schedule_name = var_minimum_outdoor_temperature_schedule_name
        # object-list
        var_maximum_outdoor_temperature_schedule_name = "object-list|Maximum Outdoor Temperature Schedule Name"
        obj.maximum_outdoor_temperature_schedule_name = var_maximum_outdoor_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonemixings[0].name, var_name)
        self.assertEqual(idf2.zonemixings[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonemixings[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.zonemixings[0].design_flow_rate_calculation_method, var_design_flow_rate_calculation_method)
        self.assertAlmostEqual(idf2.zonemixings[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.zonemixings[0].flow_rate_per_zone_floor_area, var_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.zonemixings[0].flow_rate_per_person, var_flow_rate_per_person)
        self.assertAlmostEqual(idf2.zonemixings[0].air_changes_per_hour, var_air_changes_per_hour)
        self.assertEqual(idf2.zonemixings[0].source_zone_name, var_source_zone_name)
        self.assertAlmostEqual(idf2.zonemixings[0].delta_temperature, var_delta_temperature)
        self.assertEqual(idf2.zonemixings[0].delta_temperature_schedule_name, var_delta_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].minimum_zone_temperature_schedule_name, var_minimum_zone_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].maximum_zone_temperature_schedule_name, var_maximum_zone_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].minimum_source_zone_temperature_schedule_name, var_minimum_source_zone_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].maximum_source_zone_temperature_schedule_name, var_maximum_source_zone_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].minimum_outdoor_temperature_schedule_name, var_minimum_outdoor_temperature_schedule_name)
        self.assertEqual(idf2.zonemixings[0].maximum_outdoor_temperature_schedule_name, var_maximum_outdoor_temperature_schedule_name)