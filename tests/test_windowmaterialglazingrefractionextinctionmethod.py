import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialGlazingRefractionExtinctionMethod

log = logging.getLogger(__name__)

class TestWindowMaterialGlazingRefractionExtinctionMethod(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialglazingrefractionextinctionmethod(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGlazingRefractionExtinctionMethod()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # real
        var_solar_index_of_refraction = 1.0001
        obj.solar_index_of_refraction = var_solar_index_of_refraction
        # real
        var_solar_extinction_coefficient = 0.0001
        obj.solar_extinction_coefficient = var_solar_extinction_coefficient
        # real
        var_visible_index_of_refraction = 1.0001
        obj.visible_index_of_refraction = var_visible_index_of_refraction
        # real
        var_visible_extinction_coefficient = 0.0001
        obj.visible_extinction_coefficient = var_visible_extinction_coefficient
        # real
        var_infrared_transmittance_at_normal_incidence = 0.49995
        obj.infrared_transmittance_at_normal_incidence = var_infrared_transmittance_at_normal_incidence
        # real
        var_infrared_hemispherical_emissivity = 0.5
        obj.infrared_hemispherical_emissivity = var_infrared_hemispherical_emissivity
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_dirt_correction_factor_for_solar_and_visible_transmittance = 0.50005
        obj.dirt_correction_factor_for_solar_and_visible_transmittance = var_dirt_correction_factor_for_solar_and_visible_transmittance
        # alpha
        var_solar_diffusing = "No"
        obj.solar_diffusing = var_solar_diffusing

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].solar_index_of_refraction, var_solar_index_of_refraction)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].solar_extinction_coefficient, var_solar_extinction_coefficient)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].visible_index_of_refraction, var_visible_index_of_refraction)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].visible_extinction_coefficient, var_visible_extinction_coefficient)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].infrared_transmittance_at_normal_incidence, var_infrared_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].infrared_hemispherical_emissivity, var_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].dirt_correction_factor_for_solar_and_visible_transmittance, var_dirt_correction_factor_for_solar_and_visible_transmittance)
        self.assertEqual(idf2.windowmaterialglazingrefractionextinctionmethods[0].solar_diffusing, var_solar_diffusing)