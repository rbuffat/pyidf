import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialRoofVegetation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMaterialRoofVegetation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialroofvegetation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialRoofVegetation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_height_of_plants = 0.50255
        obj.height_of_plants = var_height_of_plants
        # real
        var_leaf_area_index = 2.50055
        obj.leaf_area_index = var_leaf_area_index
        # real
        var_leaf_reflectivity = 0.275
        obj.leaf_reflectivity = var_leaf_reflectivity
        # real
        var_leaf_emissivity = 0.9
        obj.leaf_emissivity = var_leaf_emissivity
        # real
        var_minimum_stomatal_resistance = 175.0
        obj.minimum_stomatal_resistance = var_minimum_stomatal_resistance
        # alpha
        var_soil_layer_name = "Soil Layer Name"
        obj.soil_layer_name = var_soil_layer_name
        # alpha
        var_roughness = "VeryRough"
        obj.roughness = var_roughness
        # real
        var_thickness = 0.37505
        obj.thickness = var_thickness
        # real
        var_conductivity_of_dry_soil = 0.85
        obj.conductivity_of_dry_soil = var_conductivity_of_dry_soil
        # real
        var_density_of_dry_soil = 1150.0
        obj.density_of_dry_soil = var_density_of_dry_soil
        # real
        var_specific_heat_of_dry_soil = 1250.00005
        obj.specific_heat_of_dry_soil = var_specific_heat_of_dry_soil
        # real
        var_thermal_absorptance = 0.90005
        obj.thermal_absorptance = var_thermal_absorptance
        # real
        var_solar_absorptance = 0.65
        obj.solar_absorptance = var_solar_absorptance
        # real
        var_visible_absorptance = 0.75005
        obj.visible_absorptance = var_visible_absorptance
        # real
        var_saturation_volumetric_moisture_content_of_the_soil_layer = 0.30005
        obj.saturation_volumetric_moisture_content_of_the_soil_layer = var_saturation_volumetric_moisture_content_of_the_soil_layer
        # real
        var_residual_volumetric_moisture_content_of_the_soil_layer = 0.055
        obj.residual_volumetric_moisture_content_of_the_soil_layer = var_residual_volumetric_moisture_content_of_the_soil_layer
        # real
        var_initial_volumetric_moisture_content_of_the_soil_layer = 0.27505
        obj.initial_volumetric_moisture_content_of_the_soil_layer = var_initial_volumetric_moisture_content_of_the_soil_layer
        # alpha
        var_moisture_diffusion_calculation_method = "Simple"
        obj.moisture_diffusion_calculation_method = var_moisture_diffusion_calculation_method

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialroofvegetations[0].name, var_name)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].height_of_plants, var_height_of_plants)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].leaf_area_index, var_leaf_area_index)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].leaf_reflectivity, var_leaf_reflectivity)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].leaf_emissivity, var_leaf_emissivity)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].minimum_stomatal_resistance, var_minimum_stomatal_resistance)
        self.assertEqual(idf2.materialroofvegetations[0].soil_layer_name, var_soil_layer_name)
        self.assertEqual(idf2.materialroofvegetations[0].roughness, var_roughness)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].thickness, var_thickness)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].conductivity_of_dry_soil, var_conductivity_of_dry_soil)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].density_of_dry_soil, var_density_of_dry_soil)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].specific_heat_of_dry_soil, var_specific_heat_of_dry_soil)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].thermal_absorptance, var_thermal_absorptance)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].solar_absorptance, var_solar_absorptance)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].visible_absorptance, var_visible_absorptance)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].saturation_volumetric_moisture_content_of_the_soil_layer, var_saturation_volumetric_moisture_content_of_the_soil_layer)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].residual_volumetric_moisture_content_of_the_soil_layer, var_residual_volumetric_moisture_content_of_the_soil_layer)
        self.assertAlmostEqual(idf2.materialroofvegetations[0].initial_volumetric_moisture_content_of_the_soil_layer, var_initial_volumetric_moisture_content_of_the_soil_layer)
        self.assertEqual(idf2.materialroofvegetations[0].moisture_diffusion_calculation_method, var_moisture_diffusion_calculation_method)