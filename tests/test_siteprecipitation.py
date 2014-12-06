import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SitePrecipitation

log = logging.getLogger(__name__)

class TestSitePrecipitation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_siteprecipitation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SitePrecipitation()
        # alpha
        var_precipitation_model_type = "ScheduleAndDesignLevel"
        obj.precipitation_model_type = var_precipitation_model_type
        # real
        var_design_level_for_total_annual_precipitation = 2.2
        obj.design_level_for_total_annual_precipitation = var_design_level_for_total_annual_precipitation
        # object-list
        var_precipitation_rates_schedule_name = "object-list|Precipitation Rates Schedule Name"
        obj.precipitation_rates_schedule_name = var_precipitation_rates_schedule_name
        # real
        var_average_total_annual_precipitation = 0.0
        obj.average_total_annual_precipitation = var_average_total_annual_precipitation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.siteprecipitations[0].precipitation_model_type, var_precipitation_model_type)
        self.assertAlmostEqual(idf2.siteprecipitations[0].design_level_for_total_annual_precipitation, var_design_level_for_total_annual_precipitation)
        self.assertEqual(idf2.siteprecipitations[0].precipitation_rates_schedule_name, var_precipitation_rates_schedule_name)
        self.assertAlmostEqual(idf2.siteprecipitations[0].average_total_annual_precipitation, var_average_total_annual_precipitation)