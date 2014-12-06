import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import DesignSpecificationOutdoorAir

log = logging.getLogger(__name__)

class TestDesignSpecificationOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_designspecificationoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DesignSpecificationOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_per_person = 0.0
        obj.outdoor_air_flow_per_person = var_outdoor_air_flow_per_person
        # real
        var_outdoor_air_flow_per_zone_floor_area = 0.0
        obj.outdoor_air_flow_per_zone_floor_area = var_outdoor_air_flow_per_zone_floor_area
        # real
        var_outdoor_air_flow_per_zone = 0.0
        obj.outdoor_air_flow_per_zone = var_outdoor_air_flow_per_zone
        # real
        var_outdoor_air_flow_air_changes_per_hour = 0.0
        obj.outdoor_air_flow_air_changes_per_hour = var_outdoor_air_flow_air_changes_per_hour
        # object-list
        var_outdoor_air_flow_rate_fraction_schedule_name = "object-list|Outdoor Air Flow Rate Fraction Schedule Name"
        obj.outdoor_air_flow_rate_fraction_schedule_name = var_outdoor_air_flow_rate_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.designspecificationoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_flow_per_person, var_outdoor_air_flow_per_person)
        self.assertAlmostEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_flow_per_zone_floor_area, var_outdoor_air_flow_per_zone_floor_area)
        self.assertAlmostEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_flow_per_zone, var_outdoor_air_flow_per_zone)
        self.assertAlmostEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_flow_air_changes_per_hour, var_outdoor_air_flow_air_changes_per_hour)
        self.assertEqual(idf2.designspecificationoutdoorairs[0].outdoor_air_flow_rate_fraction_schedule_name, var_outdoor_air_flow_rate_fraction_schedule_name)