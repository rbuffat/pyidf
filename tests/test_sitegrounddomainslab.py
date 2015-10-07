import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundDomainSlab

log = logging.getLogger(__name__)

class TestSiteGroundDomainSlab(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegrounddomainslab(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundDomainSlab()
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
        var_slab_boundary_condition_model_name = "object-list|Slab Boundary Condition Model Name"
        obj.slab_boundary_condition_model_name = var_slab_boundary_condition_model_name
        # alpha
        var_slab_location = "InGrade"
        obj.slab_location = var_slab_location
        # object-list
        var_slab_material_name = "object-list|Slab Material Name"
        obj.slab_material_name = var_slab_material_name
        # alpha
        var_horizontal_insulation = "Yes"
        obj.horizontal_insulation = var_horizontal_insulation
        # object-list
        var_horizontal_insulation_material_name = "object-list|Horizontal Insulation Material Name"
        obj.horizontal_insulation_material_name = var_horizontal_insulation_material_name
        # alpha
        var_horizontal_insulation_extents = "Full"
        obj.horizontal_insulation_extents = var_horizontal_insulation_extents
        # real
        var_perimeter_insulation_width = 0.0001
        obj.perimeter_insulation_width = var_perimeter_insulation_width
        # alpha
        var_vertical_insulation = "Yes"
        obj.vertical_insulation = var_vertical_insulation
        # object-list
        var_vertical_insulation_material_name = "object-list|Vertical Insulation Material Name"
        obj.vertical_insulation_material_name = var_vertical_insulation_material_name
        # real
        var_vertical_insulation_depth = 0.0001
        obj.vertical_insulation_depth = var_vertical_insulation_depth
        # alpha
        var_simulation_timestep = "Hourly"
        obj.simulation_timestep = var_simulation_timestep

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitegrounddomainslabs[0].name, var_name)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].ground_domain_depth, var_ground_domain_depth)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].aspect_ratio, var_aspect_ratio)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].perimeter_offset, var_perimeter_offset)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].soil_moisture_content_volume_fraction, var_soil_moisture_content_volume_fraction)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].soil_moisture_content_volume_fraction_at_saturation, var_soil_moisture_content_volume_fraction_at_saturation)
        self.assertEqual(idf2.sitegrounddomainslabs[0].undisturbed_ground_temperature_model_type, var_undisturbed_ground_temperature_model_type)
        self.assertEqual(idf2.sitegrounddomainslabs[0].undisturbed_ground_temperature_model_name, var_undisturbed_ground_temperature_model_name)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].evapotranspiration_ground_cover_parameter, var_evapotranspiration_ground_cover_parameter)
        self.assertEqual(idf2.sitegrounddomainslabs[0].slab_boundary_condition_model_name, var_slab_boundary_condition_model_name)
        self.assertEqual(idf2.sitegrounddomainslabs[0].slab_location, var_slab_location)
        self.assertEqual(idf2.sitegrounddomainslabs[0].slab_material_name, var_slab_material_name)
        self.assertEqual(idf2.sitegrounddomainslabs[0].horizontal_insulation, var_horizontal_insulation)
        self.assertEqual(idf2.sitegrounddomainslabs[0].horizontal_insulation_material_name, var_horizontal_insulation_material_name)
        self.assertEqual(idf2.sitegrounddomainslabs[0].horizontal_insulation_extents, var_horizontal_insulation_extents)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].perimeter_insulation_width, var_perimeter_insulation_width)
        self.assertEqual(idf2.sitegrounddomainslabs[0].vertical_insulation, var_vertical_insulation)
        self.assertEqual(idf2.sitegrounddomainslabs[0].vertical_insulation_material_name, var_vertical_insulation_material_name)
        self.assertAlmostEqual(idf2.sitegrounddomainslabs[0].vertical_insulation_depth, var_vertical_insulation_depth)
        self.assertEqual(idf2.sitegrounddomainslabs[0].simulation_timestep, var_simulation_timestep)