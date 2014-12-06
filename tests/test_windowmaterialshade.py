import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialShade

log = logging.getLogger(__name__)

class TestWindowMaterialShade(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialshade(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialShade()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_solar_transmittance = 0.49995
        obj.solar_transmittance = var_solar_transmittance
        # real
        var_solar_reflectance = 0.49995
        obj.solar_reflectance = var_solar_reflectance
        # real
        var_visible_transmittance = 0.49995
        obj.visible_transmittance = var_visible_transmittance
        # real
        var_visible_reflectance = 0.49995
        obj.visible_reflectance = var_visible_reflectance
        # real
        var_infrared_hemispherical_emissivity = 0.5
        obj.infrared_hemispherical_emissivity = var_infrared_hemispherical_emissivity
        # real
        var_infrared_transmittance = 0.49995
        obj.infrared_transmittance = var_infrared_transmittance
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_shade_to_glass_distance = 0.5005
        obj.shade_to_glass_distance = var_shade_to_glass_distance
        # real
        var_top_opening_multiplier = 0.5
        obj.top_opening_multiplier = var_top_opening_multiplier
        # real
        var_bottom_opening_multiplier = 0.5
        obj.bottom_opening_multiplier = var_bottom_opening_multiplier
        # real
        var_leftside_opening_multiplier = 0.5
        obj.leftside_opening_multiplier = var_leftside_opening_multiplier
        # real
        var_rightside_opening_multiplier = 0.5
        obj.rightside_opening_multiplier = var_rightside_opening_multiplier
        # real
        var_airflow_permeability = 0.4
        obj.airflow_permeability = var_airflow_permeability

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialshades[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].solar_transmittance, var_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].solar_reflectance, var_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].visible_transmittance, var_visible_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].visible_reflectance, var_visible_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].infrared_hemispherical_emissivity, var_infrared_hemispherical_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].infrared_transmittance, var_infrared_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].shade_to_glass_distance, var_shade_to_glass_distance)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].top_opening_multiplier, var_top_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].bottom_opening_multiplier, var_bottom_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].leftside_opening_multiplier, var_leftside_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].rightside_opening_multiplier, var_rightside_opening_multiplier)
        self.assertAlmostEqual(idf2.windowmaterialshades[0].airflow_permeability, var_airflow_permeability)