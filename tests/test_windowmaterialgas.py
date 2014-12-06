import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialGas
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialGas(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialgas(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGas()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_gas_type = "Air"
        obj.gas_type = var_gas_type
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # real
        var_conductivity_coefficient_a = 4.4
        obj.conductivity_coefficient_a = var_conductivity_coefficient_a
        # real
        var_conductivity_coefficient_b = 5.5
        obj.conductivity_coefficient_b = var_conductivity_coefficient_b
        # real
        var_conductivity_coefficient_c = 6.6
        obj.conductivity_coefficient_c = var_conductivity_coefficient_c
        # real
        var_viscosity_coefficient_a = 0.0001
        obj.viscosity_coefficient_a = var_viscosity_coefficient_a
        # real
        var_viscosity_coefficient_b = 8.8
        obj.viscosity_coefficient_b = var_viscosity_coefficient_b
        # real
        var_viscosity_coefficient_c = 9.9
        obj.viscosity_coefficient_c = var_viscosity_coefficient_c
        # real
        var_specific_heat_coefficient_a = 0.0001
        obj.specific_heat_coefficient_a = var_specific_heat_coefficient_a
        # real
        var_specific_heat_coefficient_b = 11.11
        obj.specific_heat_coefficient_b = var_specific_heat_coefficient_b
        # real
        var_specific_heat_coefficient_c = 12.12
        obj.specific_heat_coefficient_c = var_specific_heat_coefficient_c
        # real
        var_molecular_weight = 110.0
        obj.molecular_weight = var_molecular_weight
        # real
        var_specific_heat_ratio = 14.14
        obj.specific_heat_ratio = var_specific_heat_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialgass[0].name, var_name)
        self.assertEqual(idf2.windowmaterialgass[0].gas_type, var_gas_type)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].conductivity_coefficient_a, var_conductivity_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].conductivity_coefficient_b, var_conductivity_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].conductivity_coefficient_c, var_conductivity_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].viscosity_coefficient_a, var_viscosity_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].viscosity_coefficient_b, var_viscosity_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].viscosity_coefficient_c, var_viscosity_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].specific_heat_coefficient_a, var_specific_heat_coefficient_a)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].specific_heat_coefficient_b, var_specific_heat_coefficient_b)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].specific_heat_coefficient_c, var_specific_heat_coefficient_c)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].molecular_weight, var_molecular_weight)
        self.assertAlmostEqual(idf2.windowmaterialgass[0].specific_heat_ratio, var_specific_heat_ratio)