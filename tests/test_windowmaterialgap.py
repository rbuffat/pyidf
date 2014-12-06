import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialGap
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialGap(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialgap(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGap()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_thickness = 2.2
        obj.thickness = var_thickness
        # object-list
        var_gas_or_gas_mixture = "object-list|Gas (or Gas Mixture)"
        obj.gas_or_gas_mixture = var_gas_or_gas_mixture
        # real
        var_pressure = 4.4
        obj.pressure = var_pressure
        # object-list
        var_deflection_state = "object-list|Deflection State"
        obj.deflection_state = var_deflection_state
        # object-list
        var_support_pillar = "object-list|Support Pillar"
        obj.support_pillar = var_support_pillar

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialgaps[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialgaps[0].thickness, var_thickness)
        self.assertEqual(idf2.windowmaterialgaps[0].gas_or_gas_mixture, var_gas_or_gas_mixture)
        self.assertAlmostEqual(idf2.windowmaterialgaps[0].pressure, var_pressure)
        self.assertEqual(idf2.windowmaterialgaps[0].deflection_state, var_deflection_state)
        self.assertEqual(idf2.windowmaterialgaps[0].support_pillar, var_support_pillar)