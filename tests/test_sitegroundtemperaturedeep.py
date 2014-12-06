import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundTemperatureDeep

log = logging.getLogger(__name__)

class TestSiteGroundTemperatureDeep(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperaturedeep(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureDeep()
        # real
        var_january_deep_ground_temperature = 1.1
        obj.january_deep_ground_temperature = var_january_deep_ground_temperature
        # real
        var_february_deep_ground_temperature = 2.2
        obj.february_deep_ground_temperature = var_february_deep_ground_temperature
        # real
        var_march_deep_ground_temperature = 3.3
        obj.march_deep_ground_temperature = var_march_deep_ground_temperature
        # real
        var_april_deep_ground_temperature = 4.4
        obj.april_deep_ground_temperature = var_april_deep_ground_temperature
        # real
        var_may_deep_ground_temperature = 5.5
        obj.may_deep_ground_temperature = var_may_deep_ground_temperature
        # real
        var_june_deep_ground_temperature = 6.6
        obj.june_deep_ground_temperature = var_june_deep_ground_temperature
        # real
        var_july_deep_ground_temperature = 7.7
        obj.july_deep_ground_temperature = var_july_deep_ground_temperature
        # real
        var_august_deep_ground_temperature = 8.8
        obj.august_deep_ground_temperature = var_august_deep_ground_temperature
        # real
        var_september_deep_ground_temperature = 9.9
        obj.september_deep_ground_temperature = var_september_deep_ground_temperature
        # real
        var_october_deep_ground_temperature = 10.1
        obj.october_deep_ground_temperature = var_october_deep_ground_temperature
        # real
        var_november_deep_ground_temperature = 11.11
        obj.november_deep_ground_temperature = var_november_deep_ground_temperature
        # real
        var_december_deep_ground_temperature = 12.12
        obj.december_deep_ground_temperature = var_december_deep_ground_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].january_deep_ground_temperature, var_january_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].february_deep_ground_temperature, var_february_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].march_deep_ground_temperature, var_march_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].april_deep_ground_temperature, var_april_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].may_deep_ground_temperature, var_may_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].june_deep_ground_temperature, var_june_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].july_deep_ground_temperature, var_july_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].august_deep_ground_temperature, var_august_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].september_deep_ground_temperature, var_september_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].october_deep_ground_temperature, var_october_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].november_deep_ground_temperature, var_november_deep_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturedeeps[0].december_deep_ground_temperature, var_december_deep_ground_temperature)