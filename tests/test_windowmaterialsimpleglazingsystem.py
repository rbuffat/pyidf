import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialSimpleGlazingSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialSimpleGlazingSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialsimpleglazingsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialSimpleGlazingSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_ufactor = 3.50005
        obj.ufactor = var_ufactor
        # real
        var_solar_heat_gain_coefficient = 0.5
        obj.solar_heat_gain_coefficient = var_solar_heat_gain_coefficient
        # real
        var_visible_transmittance = 0.5
        obj.visible_transmittance = var_visible_transmittance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialsimpleglazingsystems[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialsimpleglazingsystems[0].ufactor, var_ufactor)
        self.assertAlmostEqual(idf2.windowmaterialsimpleglazingsystems[0].solar_heat_gain_coefficient, var_solar_heat_gain_coefficient)
        self.assertAlmostEqual(idf2.windowmaterialsimpleglazingsystems[0].visible_transmittance, var_visible_transmittance)