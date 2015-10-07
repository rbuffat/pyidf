import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundDomainBasement

log = logging.getLogger(__name__)

class TestSiteGroundDomainBasement(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegrounddomainbasement(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundDomainBasement()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_ground_domain_depth = 0.0001
        obj.ground_domain_depth = var_ground_domain_depth
        # real
        var_aspect_ratio = 3.3
        obj.aspect_ratio = var_aspect_ratio
        # real
        var_perimeter_offset = 0.0001
        obj.perimeter_offset = var_perimeter_offset
        # real
        var_soil_thermal_conductivity = 0.0001
        obj.soil_thermal_conductivity = var_soil_thermal_conductivity
        # real
        var_soil_density = 0.0001
        obj.soil_density = var_soil_density
        # real
        var_soil_specific_heat = 0.0001
        obj.soil_specific_heat = var_soil_specific_heat
        # real
        var_soil_moisture_content_volume_fraction = 50.0
        obj.soil_moisture_content_volume_fraction = var_soil_moisture_content_volume_fraction
        # real
        var_soil_moisture_content_volume_fraction_at_saturation = 50.0
        obj.soil_moisture_content_volume_fraction_at_saturation = var_soil_moisture_content_volume_fraction_at_saturation
        # alpha
        var_undisturbed_ground_temperature_model_type = "Site:GroundTemperature:Undisturbed:FiniteDifference"
        obj.undisturbed_ground_temperature_model_type = var_undisturbed_ground_temperature_model_type
        # object-list
        var_undisturbed_ground_temperature_model_name = "object-list|Undisturbed Ground Temperature Model Name"
        obj.undisturbed_ground_temperature_model_name = var_undisturbed_ground_temperature_model_name
        # real
        var_evapotranspiration_ground_cover_parameter = 0.75
        obj.evapotranspiration_ground_cover_parameter = var_evapotranspiration_ground_cover_parameter
        # object-list
        var_basement_floor_boundary_condition_model_name = "object-list|Basement Floor Boundary Condition Model Name"
        obj.basement_floor_boundary_condition_model_name = var_basement_floor_boundary_condition_model_name
        # alpha
        var_horizontal_insulation = "Yes"
        obj.horizontal_insulation = var_horizontal_insulation
        # object-list
        var_horizontal_insulation_material_name = "object-list|Horizontal Insulation Material Name"
        obj.horizontal_insulation_material_name = var_horizontal_insulation_material_name
        # alpha
        var_horizontal_insulation_extents = "Perimeter"
        obj.horizontal_insulation_extents = var_horizontal_insulation_extents
        # real
        var_perimeter_horizontal_insulation_width = 0.0001
        obj.perimeter_horizontal_insulation_width = var_perimeter_horizontal_insulation_width
        # real
        var_basement_wall_depth = 0.0001
        obj.basement_wall_depth = var_basement_wall_depth
        # object-list
        var_basement_wall_boundary_condition_model_name = "object-list|Basement Wall Boundary Condition Model Name"
        obj.basement_wall_boundary_condition_model_name = var_basement_wall_boundary_condition_model_name
        # alpha
        var_vertical_insulation = "Yes"
        obj.vertical_insulation = var_vertical_insulation
        # object-list
        var_basement_wall_vertical_insulation_material_name = "object-list|Basement Wall Vertical Insulation Material Name"
        obj.basement_wall_vertical_insulation_material_name = var_basement_wall_vertical_insulation_material_name
        # real
        var_vertical_insulation_depth = 0.0001
        obj.vertical_insulation_depth = var_vertical_insulation_depth
        # alpha
        var_simulation_timestep = "Timestep"
        obj.simulation_timestep = var_simulation_timestep
        # integer
        var_mesh_density_parameter = 2
        obj.mesh_density_parameter = var_mesh_density_parameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitegrounddomainbasements[0].name, var_name)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].ground_domain_depth, var_ground_domain_depth)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].aspect_ratio, var_aspect_ratio)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].perimeter_offset, var_perimeter_offset)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].soil_moisture_content_volume_fraction, var_soil_moisture_content_volume_fraction)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].soil_moisture_content_volume_fraction_at_saturation, var_soil_moisture_content_volume_fraction_at_saturation)
        self.assertEqual(idf2.sitegrounddomainbasements[0].undisturbed_ground_temperature_model_type, var_undisturbed_ground_temperature_model_type)
        self.assertEqual(idf2.sitegrounddomainbasements[0].undisturbed_ground_temperature_model_name, var_undisturbed_ground_temperature_model_name)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].evapotranspiration_ground_cover_parameter, var_evapotranspiration_ground_cover_parameter)
        self.assertEqual(idf2.sitegrounddomainbasements[0].basement_floor_boundary_condition_model_name, var_basement_floor_boundary_condition_model_name)
        self.assertEqual(idf2.sitegrounddomainbasements[0].horizontal_insulation, var_horizontal_insulation)
        self.assertEqual(idf2.sitegrounddomainbasements[0].horizontal_insulation_material_name, var_horizontal_insulation_material_name)
        self.assertEqual(idf2.sitegrounddomainbasements[0].horizontal_insulation_extents, var_horizontal_insulation_extents)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].perimeter_horizontal_insulation_width, var_perimeter_horizontal_insulation_width)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].basement_wall_depth, var_basement_wall_depth)
        self.assertEqual(idf2.sitegrounddomainbasements[0].basement_wall_boundary_condition_model_name, var_basement_wall_boundary_condition_model_name)
        self.assertEqual(idf2.sitegrounddomainbasements[0].vertical_insulation, var_vertical_insulation)
        self.assertEqual(idf2.sitegrounddomainbasements[0].basement_wall_vertical_insulation_material_name, var_basement_wall_vertical_insulation_material_name)
        self.assertAlmostEqual(idf2.sitegrounddomainbasements[0].vertical_insulation_depth, var_vertical_insulation_depth)
        self.assertEqual(idf2.sitegrounddomainbasements[0].simulation_timestep, var_simulation_timestep)
        self.assertEqual(idf2.sitegrounddomainbasements[0].mesh_density_parameter, var_mesh_density_parameter)