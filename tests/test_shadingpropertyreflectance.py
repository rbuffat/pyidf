import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import ShadingPropertyReflectance
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestShadingPropertyReflectance(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadingpropertyreflectance(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadingPropertyReflectance()
        # object-list
        var_shading_surface_name = "object-list|Shading Surface Name"
        obj.shading_surface_name = var_shading_surface_name
        # real
        var_diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = 0.5
        obj.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = var_diffuse_solar_reflectance_of_unglazed_part_of_shading_surface
        # real
        var_diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = 0.5
        obj.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = var_diffuse_visible_reflectance_of_unglazed_part_of_shading_surface
        # real
        var_fraction_of_shading_surface_that_is_glazed = 0.5
        obj.fraction_of_shading_surface_that_is_glazed = var_fraction_of_shading_surface_that_is_glazed
        # alpha
        var_glazing_construction_name = "Glazing Construction Name"
        obj.glazing_construction_name = var_glazing_construction_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadingpropertyreflectances[0].shading_surface_name, var_shading_surface_name)
        self.assertAlmostEqual(idf2.shadingpropertyreflectances[0].diffuse_solar_reflectance_of_unglazed_part_of_shading_surface, var_diffuse_solar_reflectance_of_unglazed_part_of_shading_surface)
        self.assertAlmostEqual(idf2.shadingpropertyreflectances[0].diffuse_visible_reflectance_of_unglazed_part_of_shading_surface, var_diffuse_visible_reflectance_of_unglazed_part_of_shading_surface)
        self.assertAlmostEqual(idf2.shadingpropertyreflectances[0].fraction_of_shading_surface_that_is_glazed, var_fraction_of_shading_surface_that_is_glazed)
        self.assertEqual(idf2.shadingpropertyreflectances[0].glazing_construction_name, var_glazing_construction_name)