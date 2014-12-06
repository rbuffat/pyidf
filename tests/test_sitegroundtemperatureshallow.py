import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteGroundTemperatureShallow
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteGroundTemperatureShallow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperatureshallow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureShallow()
        # real
        var_january_surface_ground_temperature = 1.1
        obj.january_surface_ground_temperature = var_january_surface_ground_temperature
        # real
        var_february_surface_ground_temperature = 2.2
        obj.february_surface_ground_temperature = var_february_surface_ground_temperature
        # real
        var_march_surface_ground_temperature = 3.3
        obj.march_surface_ground_temperature = var_march_surface_ground_temperature
        # real
        var_april_surface_ground_temperature = 4.4
        obj.april_surface_ground_temperature = var_april_surface_ground_temperature
        # real
        var_may_surface_ground_temperature = 5.5
        obj.may_surface_ground_temperature = var_may_surface_ground_temperature
        # real
        var_june_surface_ground_temperature = 6.6
        obj.june_surface_ground_temperature = var_june_surface_ground_temperature
        # real
        var_july_surface_ground_temperature = 7.7
        obj.july_surface_ground_temperature = var_july_surface_ground_temperature
        # real
        var_august_surface_ground_temperature = 8.8
        obj.august_surface_ground_temperature = var_august_surface_ground_temperature
        # real
        var_september_surface_ground_temperature = 9.9
        obj.september_surface_ground_temperature = var_september_surface_ground_temperature
        # real
        var_october_surface_ground_temperature = 10.1
        obj.october_surface_ground_temperature = var_october_surface_ground_temperature
        # real
        var_november_surface_ground_temperature = 11.11
        obj.november_surface_ground_temperature = var_november_surface_ground_temperature
        # real
        var_december_surface_ground_temperature = 12.12
        obj.december_surface_ground_temperature = var_december_surface_ground_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].january_surface_ground_temperature, var_january_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].february_surface_ground_temperature, var_february_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].march_surface_ground_temperature, var_march_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].april_surface_ground_temperature, var_april_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].may_surface_ground_temperature, var_may_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].june_surface_ground_temperature, var_june_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].july_surface_ground_temperature, var_july_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].august_surface_ground_temperature, var_august_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].september_surface_ground_temperature, var_september_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].october_surface_ground_temperature, var_october_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].november_surface_ground_temperature, var_november_surface_ground_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureshallows[0].december_surface_ground_temperature, var_december_surface_ground_temperature)