import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import DaylightingDelightComplexFenestration
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDaylightingDelightComplexFenestration(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdelightcomplexfenestration(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDelightComplexFenestration()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_complex_fenestration_type = "Complex Fenestration Type"
        obj.complex_fenestration_type = var_complex_fenestration_type
        # object-list
        var_building_surface_name = "object-list|Building Surface Name"
        obj.building_surface_name = var_building_surface_name
        # object-list
        var_window_name = "object-list|Window Name"
        obj.window_name = var_window_name
        # real
        var_fenestration_rotation = 5.5
        obj.fenestration_rotation = var_fenestration_rotation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdelightcomplexfenestrations[0].name, var_name)
        self.assertEqual(idf2.daylightingdelightcomplexfenestrations[0].complex_fenestration_type, var_complex_fenestration_type)
        self.assertEqual(idf2.daylightingdelightcomplexfenestrations[0].building_surface_name, var_building_surface_name)
        self.assertEqual(idf2.daylightingdelightcomplexfenestrations[0].window_name, var_window_name)
        self.assertAlmostEqual(idf2.daylightingdelightcomplexfenestrations[0].fenestration_rotation, var_fenestration_rotation)