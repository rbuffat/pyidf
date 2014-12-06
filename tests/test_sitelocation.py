import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteLocation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteLocation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitelocation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteLocation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_latitude = 0.0
        obj.latitude = var_latitude
        # real
        var_longitude = 0.0
        obj.longitude = var_longitude
        # real
        var_time_zone = 1.0
        obj.time_zone = var_time_zone
        # real
        var_elevation = 4299.99995
        obj.elevation = var_elevation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitelocations[0].name, var_name)
        self.assertAlmostEqual(idf2.sitelocations[0].latitude, var_latitude)
        self.assertAlmostEqual(idf2.sitelocations[0].longitude, var_longitude)
        self.assertAlmostEqual(idf2.sitelocations[0].time_zone, var_time_zone)
        self.assertAlmostEqual(idf2.sitelocations[0].elevation, var_elevation)