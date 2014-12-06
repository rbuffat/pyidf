import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialGlazingGroupThermochromic
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialGlazingGroupThermochromic(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialglazinggroupthermochromic(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGlazingGroupThermochromic()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_optical_data_temperature_1 = 2.2
        paras.append(var_optical_data_temperature_1)
        var_window_material_glazing_name_1 = "object-list|Window Material Glazing Name 1"
        paras.append(var_window_material_glazing_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialglazinggroupthermochromics[0].name, var_name)
        index = obj.extensible_field_index("Optical Data Temperature 1")
        self.assertAlmostEqual(idf2.windowmaterialglazinggroupthermochromics[0].extensibles[0][index], var_optical_data_temperature_1)
        index = obj.extensible_field_index("Window Material Glazing Name 1")
        self.assertEqual(idf2.windowmaterialglazinggroupthermochromics[0].extensibles[0][index], var_window_material_glazing_name_1)