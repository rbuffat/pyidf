import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.solar_collectors import SolarCollectorUnglazedTranspired

log = logging.getLogger(__name__)

class TestSolarCollectorUnglazedTranspired(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorunglazedtranspired(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorUnglazedTranspired()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_boundary_conditions_model_name = "object-list|Boundary Conditions Model Name"
        obj.boundary_conditions_model_name = var_boundary_conditions_model_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # node
        var_setpoint_node_name = "node|Setpoint Node Name"
        obj.setpoint_node_name = var_setpoint_node_name
        # node
        var_zone_node_name = "node|Zone Node Name"
        obj.zone_node_name = var_zone_node_name
        # object-list
        var_free_heating_setpoint_schedule_name = "object-list|Free Heating Setpoint Schedule Name"
        obj.free_heating_setpoint_schedule_name = var_free_heating_setpoint_schedule_name
        # real
        var_diameter_of_perforations_in_collector = 0.0001
        obj.diameter_of_perforations_in_collector = var_diameter_of_perforations_in_collector
        # real
        var_distance_between_perforations_in_collector = 0.0001
        obj.distance_between_perforations_in_collector = var_distance_between_perforations_in_collector
        # real
        var_thermal_emissivity_of_collector_surface = 0.5
        obj.thermal_emissivity_of_collector_surface = var_thermal_emissivity_of_collector_surface
        # real
        var_solar_absorbtivity_of_collector_surface = 0.5
        obj.solar_absorbtivity_of_collector_surface = var_solar_absorbtivity_of_collector_surface
        # real
        var_effective_overall_height_of_collector = 0.0001
        obj.effective_overall_height_of_collector = var_effective_overall_height_of_collector
        # real
        var_effective_gap_thickness_of_plenum_behind_collector = 0.0001
        obj.effective_gap_thickness_of_plenum_behind_collector = var_effective_gap_thickness_of_plenum_behind_collector
        # real
        var_effective_cross_section_area_of_plenum_behind_collector = 0.0001
        obj.effective_cross_section_area_of_plenum_behind_collector = var_effective_cross_section_area_of_plenum_behind_collector
        # alpha
        var_hole_layout_pattern_for_pitch = "Triangle"
        obj.hole_layout_pattern_for_pitch = var_hole_layout_pattern_for_pitch
        # alpha
        var_heat_exchange_effectiveness_correlation = "Kutscher1994"
        obj.heat_exchange_effectiveness_correlation = var_heat_exchange_effectiveness_correlation
        # real
        var_ratio_of_actual_collector_surface_area_to_projected_surface_area = 1.5
        obj.ratio_of_actual_collector_surface_area_to_projected_surface_area = var_ratio_of_actual_collector_surface_area_to_projected_surface_area
        # alpha
        var_roughness_of_collector = "VeryRough"
        obj.roughness_of_collector = var_roughness_of_collector
        # real
        var_collector_thickness = 0.00375
        obj.collector_thickness = var_collector_thickness
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].name, var_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].boundary_conditions_model_name, var_boundary_conditions_model_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].setpoint_node_name, var_setpoint_node_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].zone_node_name, var_zone_node_name)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].free_heating_setpoint_schedule_name, var_free_heating_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].diameter_of_perforations_in_collector, var_diameter_of_perforations_in_collector)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].distance_between_perforations_in_collector, var_distance_between_perforations_in_collector)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].thermal_emissivity_of_collector_surface, var_thermal_emissivity_of_collector_surface)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].solar_absorbtivity_of_collector_surface, var_solar_absorbtivity_of_collector_surface)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].effective_overall_height_of_collector, var_effective_overall_height_of_collector)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].effective_gap_thickness_of_plenum_behind_collector, var_effective_gap_thickness_of_plenum_behind_collector)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].effective_cross_section_area_of_plenum_behind_collector, var_effective_cross_section_area_of_plenum_behind_collector)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].hole_layout_pattern_for_pitch, var_hole_layout_pattern_for_pitch)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].heat_exchange_effectiveness_correlation, var_heat_exchange_effectiveness_correlation)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].ratio_of_actual_collector_surface_area_to_projected_surface_area, var_ratio_of_actual_collector_surface_area_to_projected_surface_area)
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].roughness_of_collector, var_roughness_of_collector)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].collector_thickness, var_collector_thickness)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].effectiveness_for_perforations_with_respect_to_wind, var_effectiveness_for_perforations_with_respect_to_wind)
        self.assertAlmostEqual(idf2.solarcollectorunglazedtranspireds[0].discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow, var_discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.solarcollectorunglazedtranspireds[0].extensibles[0][index], var_surface_1_name)