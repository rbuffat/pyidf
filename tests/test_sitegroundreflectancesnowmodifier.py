import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteGroundReflectanceSnowModifier
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteGroundReflectanceSnowModifier(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundreflectancesnowmodifier(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundReflectanceSnowModifier()
        # real
        var_ground_reflected_solar_modifier = 0.0
        obj.ground_reflected_solar_modifier = var_ground_reflected_solar_modifier
        # real
        var_daylighting_ground_reflected_solar_modifier = 0.0
        obj.daylighting_ground_reflected_solar_modifier = var_daylighting_ground_reflected_solar_modifier

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sitegroundreflectancesnowmodifiers[0].ground_reflected_solar_modifier, var_ground_reflected_solar_modifier)
        self.assertAlmostEqual(idf2.sitegroundreflectancesnowmodifiers[0].daylighting_ground_reflected_solar_modifier, var_daylighting_ground_reflected_solar_modifier)