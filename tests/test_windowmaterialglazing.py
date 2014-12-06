import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowMaterialGlazing
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowMaterialGlazing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialglazing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGlazing()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_optical_data_type = "SpectralAverage"
        obj.optical_data_type = var_optical_data_type
        # alpha
        var_window_glass_spectral_data_set_name = "Window Glass Spectral Data Set Name"
        obj.window_glass_spectral_data_set_name = var_window_glass_spectral_data_set_name
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # real
        var_solar_transmittance_at_normal_incidence = 0.5
        obj.solar_transmittance_at_normal_incidence = var_solar_transmittance_at_normal_incidence
        # real
        var_front_side_solar_reflectance_at_normal_incidence = 0.5
        obj.front_side_solar_reflectance_at_normal_incidence = var_front_side_solar_reflectance_at_normal_incidence
        # real
        var_back_side_solar_reflectance_at_normal_incidence = 0.5
        obj.back_side_solar_reflectance_at_normal_incidence = var_back_side_solar_reflectance_at_normal_incidence
        # real
        var_visible_transmittance_at_normal_incidence = 0.5
        obj.visible_transmittance_at_normal_incidence = var_visible_transmittance_at_normal_incidence
        # real
        var_front_side_visible_reflectance_at_normal_incidence = 0.5
        obj.front_side_visible_reflectance_at_normal_incidence = var_front_side_visible_reflectance_at_normal_incidence
        # real
        var_back_side_visible_reflectance_at_normal_incidence = 0.5
        obj.back_side_visible_reflectance_at_normal_incidence = var_back_side_visible_reflectance_at_normal_incidence
        # real
        var_infrared_transmittance_at_normal_incidence = 0.5
        obj.infrared_transmittance_at_normal_incidence = var_infrared_transmittance_at_normal_incidence
        # real
        var_front_side_infrared_hemispherical_emissivity = 0.5
        obj.front_side_infrared_hemispherical_emissivity = var_front_side_infrared_hemispherical_emissivity
        # real
        var_back_side_infrared_hemispherical_emissivity = 0.5
        obj.back_side_infrared_hemispherical_emissivity = var_back_side_infrared_hemispherical_emissivity
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_dirt_correction_factor_for_solar_and_visible_transmittance = 0.50005
        obj.dirt_correction_factor_for_solar_and_visible_transmittance = var_dirt_correction_factor_for_solar_and_visible_transmittance
        # alpha
        var_solar_diffusing = "No"
        obj.solar_diffusing = var_solar_diffusing
        # real
        var_youngs_modulus = 0.0001
        obj.youngs_modulus = var_youngs_modulus
        # real
        var_poissons_ratio = 0.5
        obj.poissons_ratio = var_poissons_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialglazings[0].name, var_name)
        self.assertEqual(idf2.windowmaterialglazings[0].optical_data_type, var_optical_data_type)
        self.assertEqual(idf2.windowmaterialglazings[0].window_glass_spectral_data_set_name, var_window_glass_spectral_data_set_name)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].solar_transmittance_at_normal_incidence, var_solar_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].front_side_solar_reflectance_at_normal_incidence, var_front_side_solar_reflectance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].back_side_solar_reflectance_at_normal_incidence, var_back_side_solar_reflectance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].visible_transmittance_at_normal_incidence, var_visible_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].front_side_visible_reflectance_at_normal_incidence, var_front_side_visible_reflectance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].back_side_visible_reflectance_at_normal_incidence, var_back_side_visible_reflectance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].infrared_transmittance_at_normal_incidence, var_infrared_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].front_side_infrared_hemispherical_emissivity, var_front_side_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].back_side_infrared_hemispherical_emissivity, var_back_side_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].dirt_correction_factor_for_solar_and_visible_transmittance, var_dirt_correction_factor_for_solar_and_visible_transmittance)
        self.assertEqual(idf2.windowmaterialglazings[0].solar_diffusing, var_solar_diffusing)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].youngs_modulus, var_youngs_modulus)
        self.assertAlmostEqual(idf2.windowmaterialglazings[0].poissons_ratio, var_poissons_ratio)