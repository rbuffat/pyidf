import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialGapEquivalentLayer

log = logging.getLogger(__name__)

class TestWindowMaterialGapEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialgapequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGapEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_gas_type = "AIR"
        obj.gas_type = var_gas_type
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # alpha
        var_gap_vent_type = "Sealed"
        obj.gap_vent_type = var_gap_vent_type
        # real
        var_conductivity_coefficient_a = 5.5
        obj.conductivity_coefficient_a = var_conductivity_coefficient_a
        # real
        var_conductivity_coefficient_b = 6.6
        obj.conductivity_coefficient_b = var_conductivity_coefficient_b
        # real
        var_conductivity_coefficient_c = 7.7
        obj.conductivity_coefficient_c = var_conductivity_coefficient_c
        # real
        var_viscosity_coefficient_a = 0.0001
        obj.viscosity_coefficient_a = var_viscosity_coefficient_a
        # real
        var_viscosity_coefficient_b = 9.9
        obj.viscosity_coefficient_b = var_viscosity_coefficient_b
        # real
        var_viscosity_coefficient_c = 10.1
        obj.viscosity_coefficient_c = var_viscosity_coefficient_c
        # real
        var_specific_heat_coefficient_a = 0.0001
        obj.specific_heat_coefficient_a = var_specific_heat_coefficient_a
        # real
        var_specific_heat_coefficient_b = 12.12
        obj.specific_heat_coefficient_b = var_specific_heat_coefficient_b
        # real
        var_specific_heat_coefficient_c = 13.13
        obj.specific_heat_coefficient_c = var_specific_heat_coefficient_c
        # real
        var_molecular_weight = 110.0
        obj.molecular_weight = var_molecular_weight
        # real
        var_specific_heat_ratio = 15.15
        obj.specific_heat_ratio = var_specific_heat_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialgapequivalentlayers[0].name, var_name)
        self.assertEqual(idf2.windowmaterialgapequivalentlayers[0].gas_type, var_gas_type)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].thickness, var_thickness)
        self.assertEqual(idf2.windowmaterialgapequivalentlayers[0].gap_vent_type, var_gap_vent_type)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].conductivity_coefficient_a, var_conductivity_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].conductivity_coefficient_b, var_conductivity_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].conductivity_coefficient_c, var_conductivity_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].viscosity_coefficient_a, var_viscosity_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].viscosity_coefficient_b, var_viscosity_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].viscosity_coefficient_c, var_viscosity_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].specific_heat_coefficient_a, var_specific_heat_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].specific_heat_coefficient_b, var_specific_heat_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].specific_heat_coefficient_c, var_specific_heat_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].molecular_weight, var_molecular_weight)
        self.assertAlmostEqual(idf2.windowmaterialgapequivalentlayers[0].specific_heat_ratio, var_specific_heat_ratio)