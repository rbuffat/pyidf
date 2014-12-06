import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundTemperatureBuildingSurface

log = logging.getLogger(__name__)

class TestSiteGroundTemperatureBuildingSurface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperaturebuildingsurface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureBuildingSurface()
        # real
        var_january_ground_temperature = 1.1
        obj.january_ground_temperature = var_january_ground_temperature
        # real
        var_february_ground_temperature = 2.2
        obj.february_ground_temperature = var_february_ground_temperature
        # real
        var_march_ground_temperature = 3.3
        obj.march_ground_temperature = var_march_ground_temperature
        # real
        var_april_ground_temperature = 4.4
        obj.april_ground_temperature = var_april_ground_temperature
        # real
        var_may_ground_temperature = 5.5
        obj.may_ground_temperature = var_may_ground_temperature
        # real
        var_june_ground_temperature = 6.6
        obj.june_ground_temperature = var_june_ground_temperature
        # real
        var_july_ground_temperature = 7.7
        obj.july_ground_temperature = var_july_ground_temperature
        # real
        var_august_ground_temperature = 8.8
        obj.august_ground_temperature = var_august_ground_temperature
        # real
        var_september_ground_temperature = 9.9
        obj.september_ground_temperature = var_september_ground_temperature
        # real
        var_october_ground_temperature = 10.1
        obj.october_ground_temperature = var_october_ground_temperature
        # real
        var_november_ground_temperature = 11.11
        obj.november_ground_temperature = var_november_ground_temperature
        # real
        var_december_ground_temperature = 12.12
        obj.december_ground_temperature = var_december_ground_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].january_ground_temperature, var_january_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].february_ground_temperature, var_february_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].march_ground_temperature, var_march_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].april_ground_temperature, var_april_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].may_ground_temperature, var_may_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].june_ground_temperature, var_june_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].july_ground_temperature, var_july_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].august_ground_temperature, var_august_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].september_ground_temperature, var_september_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].october_ground_temperature, var_october_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].november_ground_temperature, var_november_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperaturebuildingsurfaces[0].december_ground_temperature, var_december_ground_temperature)