import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import DaylightingDeviceShelf
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDaylightingDeviceShelf(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdeviceshelf(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDeviceShelf()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_window_name = "object-list|Window Name"
        obj.window_name = var_window_name
        # object-list
        var_inside_shelf_name = "object-list|Inside Shelf Name"
        obj.inside_shelf_name = var_inside_shelf_name
        # object-list
        var_outside_shelf_name = "object-list|Outside Shelf Name"
        obj.outside_shelf_name = var_outside_shelf_name
        # object-list
        var_outside_shelf_construction_name = "object-list|Outside Shelf Construction Name"
        obj.outside_shelf_construction_name = var_outside_shelf_construction_name
        # real
        var_view_factor_to_outside_shelf = 0.5
        obj.view_factor_to_outside_shelf = var_view_factor_to_outside_shelf

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdeviceshelfs[0].name, var_name)
        self.assertEqual(idf2.daylightingdeviceshelfs[0].window_name, var_window_name)
        self.assertEqual(idf2.daylightingdeviceshelfs[0].inside_shelf_name, var_inside_shelf_name)
        self.assertEqual(idf2.daylightingdeviceshelfs[0].outside_shelf_name, var_outside_shelf_name)
        self.assertEqual(idf2.daylightingdeviceshelfs[0].outside_shelf_construction_name, var_outside_shelf_construction_name)
        self.assertAlmostEqual(idf2.daylightingdeviceshelfs[0].view_factor_to_outside_shelf, var_view_factor_to_outside_shelf)