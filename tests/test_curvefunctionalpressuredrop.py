import os
import tempfile
import unittest
import pyidf
from pyidf.performance_curves import CurveFunctionalPressureDrop
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCurveFunctionalPressureDrop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvefunctionalpressuredrop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveFunctionalPressureDrop()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_diameter = 0.0001
        obj.diameter = var_diameter
        # real
        var_minor_loss_coefficient = 0.0001
        obj.minor_loss_coefficient = var_minor_loss_coefficient
        # real
        var_length = 0.0001
        obj.length = var_length
        # real
        var_roughness = 0.0001
        obj.roughness = var_roughness
        # real
        var_fixed_friction_factor = 0.0001
        obj.fixed_friction_factor = var_fixed_friction_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvefunctionalpressuredrops[0].name, var_name)
        self.assertAlmostEqual(idf2.curvefunctionalpressuredrops[0].diameter, var_diameter)
        self.assertAlmostEqual(idf2.curvefunctionalpressuredrops[0].minor_loss_coefficient, var_minor_loss_coefficient)
        self.assertAlmostEqual(idf2.curvefunctionalpressuredrops[0].length, var_length)
        self.assertAlmostEqual(idf2.curvefunctionalpressuredrops[0].roughness, var_roughness)
        self.assertAlmostEqual(idf2.curvefunctionalpressuredrops[0].fixed_friction_factor, var_fixed_friction_factor)