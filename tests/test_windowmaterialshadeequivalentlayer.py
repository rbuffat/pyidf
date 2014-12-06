import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialShadeEquivalentLayer

log = logging.getLogger(__name__)

class TestWindowMaterialShadeEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialshadeequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialShadeEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_shade_beambeam_solar_transmittance = 0.4
        obj.shade_beambeam_solar_transmittance = var_shade_beambeam_solar_transmittance
        # real
        var_front_side_shade_beamdiffuse_solar_transmittance = 0.49995
        obj.front_side_shade_beamdiffuse_solar_transmittance = var_front_side_shade_beamdiffuse_solar_transmittance
        # real
        var_back_side_shade_beamdiffuse_solar_transmittance = 0.49995
        obj.back_side_shade_beamdiffuse_solar_transmittance = var_back_side_shade_beamdiffuse_solar_transmittance
        # real
        var_front_side_shade_beamdiffuse_solar_reflectance = 0.49995
        obj.front_side_shade_beamdiffuse_solar_reflectance = var_front_side_shade_beamdiffuse_solar_reflectance
        # real
        var_back_side_shade_beamdiffuse_solar_reflectance = 0.49995
        obj.back_side_shade_beamdiffuse_solar_reflectance = var_back_side_shade_beamdiffuse_solar_reflectance
        # real
        var_shade_beambeam_visible_transmittance_at_normal_incidence = 0.49995
        obj.shade_beambeam_visible_transmittance_at_normal_incidence = var_shade_beambeam_visible_transmittance_at_normal_incidence
        # real
        var_shade_beamdiffuse_visible_transmittance_at_normal_incidence = 0.49995
        obj.shade_beamdiffuse_visible_transmittance_at_normal_incidence = var_shade_beamdiffuse_visible_transmittance_at_normal_incidence
        # real
        var_shade_beamdiffuse_visible_reflectance_at_normal_incidence = 0.49995
        obj.shade_beamdiffuse_visible_reflectance_at_normal_incidence = var_shade_beamdiffuse_visible_reflectance_at_normal_incidence
        # real
        var_shade_material_infrared_transmittance = 0.49995
        obj.shade_material_infrared_transmittance = var_shade_material_infrared_transmittance
        # real
        var_front_side_shade_material_infrared_emissivity = 0.5
        obj.front_side_shade_material_infrared_emissivity = var_front_side_shade_material_infrared_emissivity
        # real
        var_back_side_shade_material_infrared_emissivity = 0.5
        obj.back_side_shade_material_infrared_emissivity = var_back_side_shade_material_infrared_emissivity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialshadeequivalentlayers[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].shade_beambeam_solar_transmittance, var_shade_beambeam_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].front_side_shade_beamdiffuse_solar_transmittance, var_front_side_shade_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].back_side_shade_beamdiffuse_solar_transmittance, var_back_side_shade_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].front_side_shade_beamdiffuse_solar_reflectance, var_front_side_shade_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].back_side_shade_beamdiffuse_solar_reflectance, var_back_side_shade_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].shade_beambeam_visible_transmittance_at_normal_incidence, var_shade_beambeam_visible_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].shade_beamdiffuse_visible_transmittance_at_normal_incidence, var_shade_beamdiffuse_visible_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].shade_beamdiffuse_visible_reflectance_at_normal_incidence, var_shade_beamdiffuse_visible_reflectance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].shade_material_infrared_transmittance, var_shade_material_infrared_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].front_side_shade_material_infrared_emissivity, var_front_side_shade_material_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialshadeequivalentlayers[0].back_side_shade_material_infrared_emissivity, var_back_side_shade_material_infrared_emissivity)