import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import DesignSpecificationZoneAirDistribution

log = logging.getLogger(__name__)

class TestDesignSpecificationZoneAirDistribution(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_designspecificationzoneairdistribution(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DesignSpecificationZoneAirDistribution()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_zone_air_distribution_effectiveness_in_cooling_mode = 0.0001
        obj.zone_air_distribution_effectiveness_in_cooling_mode = var_zone_air_distribution_effectiveness_in_cooling_mode
        # real
        var_zone_air_distribution_effectiveness_in_heating_mode = 0.0001
        obj.zone_air_distribution_effectiveness_in_heating_mode = var_zone_air_distribution_effectiveness_in_heating_mode
        # object-list
        var_zone_air_distribution_effectiveness_schedule_name = "object-list|Zone Air Distribution Effectiveness Schedule Name"
        obj.zone_air_distribution_effectiveness_schedule_name = var_zone_air_distribution_effectiveness_schedule_name
        # real
        var_zone_secondary_recirculation_fraction = 0.0
        obj.zone_secondary_recirculation_fraction = var_zone_secondary_recirculation_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.designspecificationzoneairdistributions[0].name, var_name)
        self.assertAlmostEqual(idf2.designspecificationzoneairdistributions[0].zone_air_distribution_effectiveness_in_cooling_mode, var_zone_air_distribution_effectiveness_in_cooling_mode)
        self.assertAlmostEqual(idf2.designspecificationzoneairdistributions[0].zone_air_distribution_effectiveness_in_heating_mode, var_zone_air_distribution_effectiveness_in_heating_mode)
        self.assertEqual(idf2.designspecificationzoneairdistributions[0].zone_air_distribution_effectiveness_schedule_name, var_zone_air_distribution_effectiveness_schedule_name)
        self.assertAlmostEqual(idf2.designspecificationzoneairdistributions[0].zone_secondary_recirculation_fraction, var_zone_secondary_recirculation_fraction)