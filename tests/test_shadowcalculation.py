import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import ShadowCalculation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestShadowCalculation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadowcalculation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadowCalculation()
        # alpha
        var_calculation_method = "AverageOverDaysInFrequency"
        obj.calculation_method = var_calculation_method
        # integer
        var_calculation_frequency = 1
        obj.calculation_frequency = var_calculation_frequency
        # integer
        var_maximum_figures_in_shadow_overlap_calculations = 200
        obj.maximum_figures_in_shadow_overlap_calculations = var_maximum_figures_in_shadow_overlap_calculations
        # alpha
        var_polygon_clipping_algorithm = "ConvexWeilerAtherton"
        obj.polygon_clipping_algorithm = var_polygon_clipping_algorithm
        # alpha
        var_sky_diffuse_modeling_algorithm = "SimpleSkyDiffuseModeling"
        obj.sky_diffuse_modeling_algorithm = var_sky_diffuse_modeling_algorithm

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadowcalculations[0].calculation_method, var_calculation_method)
        self.assertEqual(idf2.shadowcalculations[0].calculation_frequency, var_calculation_frequency)
        self.assertEqual(idf2.shadowcalculations[0].maximum_figures_in_shadow_overlap_calculations, var_maximum_figures_in_shadow_overlap_calculations)
        self.assertEqual(idf2.shadowcalculations[0].polygon_clipping_algorithm, var_polygon_clipping_algorithm)
        self.assertEqual(idf2.shadowcalculations[0].sky_diffuse_modeling_algorithm, var_sky_diffuse_modeling_algorithm)