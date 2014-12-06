import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfacePropertyExteriorNaturalVentedCavity
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfacePropertyExteriorNaturalVentedCavity(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyexteriornaturalventedcavity(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyExteriorNaturalVentedCavity()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_boundary_conditions_model_name = "object-list|Boundary Conditions Model Name"
        obj.boundary_conditions_model_name = var_boundary_conditions_model_name
        # real
        var_area_fraction_of_openings = 0.50005
        obj.area_fraction_of_openings = var_area_fraction_of_openings
        # real
        var_thermal_emissivity_of_exterior_baffle_material = 0.5
        obj.thermal_emissivity_of_exterior_baffle_material = var_thermal_emissivity_of_exterior_baffle_material
        # real
        var_solar_absorbtivity_of_exterior_baffle = 0.5
        obj.solar_absorbtivity_of_exterior_baffle = var_solar_absorbtivity_of_exterior_baffle
        # real
        var_height_scale_for_buoyancydriven_ventilation = 0.0001
        obj.height_scale_for_buoyancydriven_ventilation = var_height_scale_for_buoyancydriven_ventilation
        # real
        var_effective_thickness_of_cavity_behind_exterior_baffle = 0.0001
        obj.effective_thickness_of_cavity_behind_exterior_baffle = var_effective_thickness_of_cavity_behind_exterior_baffle
        # real
        var_ratio_of_actual_surface_area_to_projected_surface_area = 1.4
        obj.ratio_of_actual_surface_area_to_projected_surface_area = var_ratio_of_actual_surface_area_to_projected_surface_area
        # alpha
        var_roughness_of_exterior_surface = "VeryRough"
        obj.roughness_of_exterior_surface = var_roughness_of_exterior_surface
        # real
        var_effectiveness_for_perforations_with_respect_to_wind = 0.75005
        obj.effectiveness_for_perforations_with_respect_to_wind = var_effectiveness_for_perforations_with_respect_to_wind
        # real
        var_discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = 0.75005
        obj.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = var_discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow
        paras = []
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].name, var_name)
        self.assertEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].boundary_conditions_model_name, var_boundary_conditions_model_name)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].area_fraction_of_openings, var_area_fraction_of_openings)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].thermal_emissivity_of_exterior_baffle_material, var_thermal_emissivity_of_exterior_baffle_material)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].solar_absorbtivity_of_exterior_baffle, var_solar_absorbtivity_of_exterior_baffle)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].height_scale_for_buoyancydriven_ventilation, var_height_scale_for_buoyancydriven_ventilation)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].effective_thickness_of_cavity_behind_exterior_baffle, var_effective_thickness_of_cavity_behind_exterior_baffle)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].ratio_of_actual_surface_area_to_projected_surface_area, var_ratio_of_actual_surface_area_to_projected_surface_area)
        self.assertEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].roughness_of_exterior_surface, var_roughness_of_exterior_surface)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].effectiveness_for_perforations_with_respect_to_wind, var_effectiveness_for_perforations_with_respect_to_wind)
        self.assertAlmostEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow, var_discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.surfacepropertyexteriornaturalventedcavitys[0].extensibles[0][index], var_surface_1_name)