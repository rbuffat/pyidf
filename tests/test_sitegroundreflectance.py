import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteGroundReflectance
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteGroundReflectance(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundreflectance(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundReflectance()
        # real
        var_january_ground_reflectance = 0.5
        obj.january_ground_reflectance = var_january_ground_reflectance
        # real
        var_february_ground_reflectance = 0.5
        obj.february_ground_reflectance = var_february_ground_reflectance
        # real
        var_march_ground_reflectance = 0.5
        obj.march_ground_reflectance = var_march_ground_reflectance
        # real
        var_april_ground_reflectance = 0.5
        obj.april_ground_reflectance = var_april_ground_reflectance
        # real
        var_may_ground_reflectance = 0.5
        obj.may_ground_reflectance = var_may_ground_reflectance
        # real
        var_june_ground_reflectance = 0.5
        obj.june_ground_reflectance = var_june_ground_reflectance
        # real
        var_july_ground_reflectance = 0.5
        obj.july_ground_reflectance = var_july_ground_reflectance
        # real
        var_august_ground_reflectance = 0.5
        obj.august_ground_reflectance = var_august_ground_reflectance
        # real
        var_september_ground_reflectance = 0.5
        obj.september_ground_reflectance = var_september_ground_reflectance
        # real
        var_october_ground_reflectance = 0.5
        obj.october_ground_reflectance = var_october_ground_reflectance
        # real
        var_november_ground_reflectance = 0.5
        obj.november_ground_reflectance = var_november_ground_reflectance
        # real
        var_december_ground_reflectance = 0.5
        obj.december_ground_reflectance = var_december_ground_reflectance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].january_ground_reflectance, var_january_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].february_ground_reflectance, var_february_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].march_ground_reflectance, var_march_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].april_ground_reflectance, var_april_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].may_ground_reflectance, var_may_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].june_ground_reflectance, var_june_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].july_ground_reflectance, var_july_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].august_ground_reflectance, var_august_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].september_ground_reflectance, var_september_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].october_ground_reflectance, var_october_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].november_ground_reflectance, var_november_ground_reflectance)
        self.assertAlmostEqual(idf2.sitegroundreflectances[0].december_ground_reflectance, var_december_ground_reflectance)