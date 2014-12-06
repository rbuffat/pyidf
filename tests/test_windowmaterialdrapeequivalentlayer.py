import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialDrapeEquivalentLayer

log = logging.getLogger(__name__)

class TestWindowMaterialDrapeEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialdrapeequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialDrapeEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_drape_beambeam_solar_transmittance_at_normal_incidence = 0.1
        obj.drape_beambeam_solar_transmittance_at_normal_incidence = var_drape_beambeam_solar_transmittance_at_normal_incidence
        # real
        var_front_side_drape_beamdiffuse_solar_transmittance = 0.49995
        obj.front_side_drape_beamdiffuse_solar_transmittance = var_front_side_drape_beamdiffuse_solar_transmittance
        # real
        var_back_side_drape_beamdiffuse_solar_transmittance = 0.49995
        obj.back_side_drape_beamdiffuse_solar_transmittance = var_back_side_drape_beamdiffuse_solar_transmittance
        # real
        var_front_side_drape_beamdiffuse_solar_reflectance = 0.49995
        obj.front_side_drape_beamdiffuse_solar_reflectance = var_front_side_drape_beamdiffuse_solar_reflectance
        # real
        var_back_side_drape_beamdiffuse_solar_reflectance = 0.49995
        obj.back_side_drape_beamdiffuse_solar_reflectance = var_back_side_drape_beamdiffuse_solar_reflectance
        # real
        var_drape_beambeam_visible_transmittance = 0.49995
        obj.drape_beambeam_visible_transmittance = var_drape_beambeam_visible_transmittance
        # real
        var_drape_beamdiffuse_visible_transmittance = 0.49995
        obj.drape_beamdiffuse_visible_transmittance = var_drape_beamdiffuse_visible_transmittance
        # real
        var_drape_beamdiffuse_visible_reflectance = 0.49995
        obj.drape_beamdiffuse_visible_reflectance = var_drape_beamdiffuse_visible_reflectance
        # real
        var_drape_material_infrared_transmittance = 0.49995
        obj.drape_material_infrared_transmittance = var_drape_material_infrared_transmittance
        # real
        var_front_side_drape_material_infrared_emissivity = 0.5
        obj.front_side_drape_material_infrared_emissivity = var_front_side_drape_material_infrared_emissivity
        # real
        var_back_side_drape_material_infrared_emissivity = 0.5
        obj.back_side_drape_material_infrared_emissivity = var_back_side_drape_material_infrared_emissivity
        # real
        var_width_of_pleated_fabric = 0.0
        obj.width_of_pleated_fabric = var_width_of_pleated_fabric
        # real
        var_length_of_pleated_fabric = 0.0
        obj.length_of_pleated_fabric = var_length_of_pleated_fabric

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialdrapeequivalentlayers[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].drape_beambeam_solar_transmittance_at_normal_incidence, var_drape_beambeam_solar_transmittance_at_normal_incidence)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].front_side_drape_beamdiffuse_solar_transmittance, var_front_side_drape_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].back_side_drape_beamdiffuse_solar_transmittance, var_back_side_drape_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].front_side_drape_beamdiffuse_solar_reflectance, var_front_side_drape_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].back_side_drape_beamdiffuse_solar_reflectance, var_back_side_drape_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].drape_beambeam_visible_transmittance, var_drape_beambeam_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].drape_beamdiffuse_visible_transmittance, var_drape_beamdiffuse_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].drape_beamdiffuse_visible_reflectance, var_drape_beamdiffuse_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].drape_material_infrared_transmittance, var_drape_material_infrared_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].front_side_drape_material_infrared_emissivity, var_front_side_drape_material_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].back_side_drape_material_infrared_emissivity, var_back_side_drape_material_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].width_of_pleated_fabric, var_width_of_pleated_fabric)
        self.assertAlmostEqual(idf2.windowmaterialdrapeequivalentlayers[0].length_of_pleated_fabric, var_length_of_pleated_fabric)