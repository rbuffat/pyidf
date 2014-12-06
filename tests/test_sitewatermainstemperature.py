import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteWaterMainsTemperature

log = logging.getLogger(__name__)

class TestSiteWaterMainsTemperature(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitewatermainstemperature(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteWaterMainsTemperature()
        # alpha
        var_calculation_method = "Schedule"
        obj.calculation_method = var_calculation_method
        # object-list
        var_temperature_schedule_name = "object-list|Temperature Schedule Name"
        obj.temperature_schedule_name = var_temperature_schedule_name
        # real
        var_annual_average_outdoor_air_temperature = 3.3
        obj.annual_average_outdoor_air_temperature = var_annual_average_outdoor_air_temperature
        # real
        var_maximum_difference_in_monthly_average_outdoor_air_temperatures = 0.0
        obj.maximum_difference_in_monthly_average_outdoor_air_temperatures = var_maximum_difference_in_monthly_average_outdoor_air_temperatures

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitewatermainstemperatures[0].calculation_method, var_calculation_method)
        self.assertEqual(idf2.sitewatermainstemperatures[0].temperature_schedule_name, var_temperature_schedule_name)
        self.assertAlmostEqual(idf2.sitewatermainstemperatures[0].annual_average_outdoor_air_temperature, var_annual_average_outdoor_air_temperature)
        self.assertAlmostEqual(idf2.sitewatermainstemperatures[0].maximum_difference_in_monthly_average_outdoor_air_temperatures, var_maximum_difference_in_monthly_average_outdoor_air_temperatures)