import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import Material

log = logging.getLogger(__name__)

class TestMaterial(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_material(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Material()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_roughness = "VeryRough"
        obj.roughness = var_roughness
        # real
        var_thickness = 1.50005
        obj.thickness = var_thickness
        # real
        var_conductivity = 0.0001
        obj.conductivity = var_conductivity
        # real
        var_density = 0.0001
        obj.density = var_density
        # real
        var_specific_heat = 100.0
        obj.specific_heat = var_specific_heat
        # real
        var_thermal_absorptance = 0.500045
        obj.thermal_absorptance = var_thermal_absorptance
        # real
        var_solar_absorptance = 0.5
        obj.solar_absorptance = var_solar_absorptance
        # real
        var_visible_absorptance = 0.5
        obj.visible_absorptance = var_visible_absorptance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materials[0].name, var_name)
        self.assertEqual(idf2.materials[0].roughness, var_roughness)
        self.assertAlmostEqual(idf2.materials[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.materials[0].conductivity, var_conductivity)
        self.assertAlmostEqual(idf2.materials[0].density, var_density)
        self.assertAlmostEqual(idf2.materials[0].specific_heat, var_specific_heat)
        self.assertAlmostEqual(idf2.materials[0].thermal_absorptance, var_thermal_absorptance)
        self.assertAlmostEqual(idf2.materials[0].solar_absorptance, var_solar_absorptance)
        self.assertAlmostEqual(idf2.materials[0].visible_absorptance, var_visible_absorptance)