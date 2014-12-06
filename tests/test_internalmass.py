import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import InternalMass
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestInternalMass(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_internalmass(self):

        pyidf.validation_level = ValidationLevel.error

        obj = InternalMass()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_surface_area = 0.0001
        obj.surface_area = var_surface_area

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.internalmasss[0].name, var_name)
        self.assertEqual(idf2.internalmasss[0].construction_name, var_construction_name)
        self.assertEqual(idf2.internalmasss[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.internalmasss[0].surface_area, var_surface_area)