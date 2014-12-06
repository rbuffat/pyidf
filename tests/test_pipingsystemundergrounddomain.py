import os
import tempfile
import unittest
import pyidf
from pyidf.node import PipingSystemUndergroundDomain
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPipingSystemUndergroundDomain(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipingsystemundergrounddomain(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipingSystemUndergroundDomain()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_xmax = 0.0001
        obj.xmax = var_xmax
        # real
        var_ymax = 0.0001
        obj.ymax = var_ymax
        # real
        var_zmax = 0.0001
        obj.zmax = var_zmax
        # integer
        var_xdirection_mesh_density_parameter = 1
        obj.xdirection_mesh_density_parameter = var_xdirection_mesh_density_parameter
        # alpha
        var_xdirection_mesh_type = "Uniform"
        obj.xdirection_mesh_type = var_xdirection_mesh_type
        # real
        var_xdirection_geometric_coefficient = 1.5
        obj.xdirection_geometric_coefficient = var_xdirection_geometric_coefficient
        # integer
        var_ydirection_mesh_density_parameter = 1
        obj.ydirection_mesh_density_parameter = var_ydirection_mesh_density_parameter
        # alpha
        var_ydirection_mesh_type = "Uniform"
        obj.ydirection_mesh_type = var_ydirection_mesh_type
        # real
        var_ydirection_geometric_coefficient = 1.5
        obj.ydirection_geometric_coefficient = var_ydirection_geometric_coefficient
        # integer
        var_zdirection_mesh_density_parameter = 1
        obj.zdirection_mesh_density_parameter = var_zdirection_mesh_density_parameter
        # alpha
        var_zdirection_mesh_type = "Uniform"
        obj.zdirection_mesh_type = var_zdirection_mesh_type
        # real
        var_zdirection_geometric_coefficient = 1.5
        obj.zdirection_geometric_coefficient = var_zdirection_geometric_coefficient
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
        # real
        var_kusudaachenbach_average_surface_temperature = 19.19
        obj.kusudaachenbach_average_surface_temperature = var_kusudaachenbach_average_surface_temperature
        # real
        var_kusudaachenbach_average_amplitude_of_surface_temperature = 20.2
        obj.kusudaachenbach_average_amplitude_of_surface_temperature = var_kusudaachenbach_average_amplitude_of_surface_temperature
        # real
        var_kusudaachenbach_phase_shift_of_minimum_surface_temperature = 21.21
        obj.kusudaachenbach_phase_shift_of_minimum_surface_temperature = var_kusudaachenbach_phase_shift_of_minimum_surface_temperature
        # alpha
        var_this_domain_includes_basement_surface_interaction = "Yes"
        obj.this_domain_includes_basement_surface_interaction = var_this_domain_includes_basement_surface_interaction
        # real
        var_width_of_basement_floor_in_ground_domain = 23.23
        obj.width_of_basement_floor_in_ground_domain = var_width_of_basement_floor_in_ground_domain
        # real
        var_depth_of_basement_wall_in_ground_domain = 24.24
        obj.depth_of_basement_wall_in_ground_domain = var_depth_of_basement_wall_in_ground_domain
        # alpha
        var_shift_pipe_x_coordinates_by_basement_width = "Yes"
        obj.shift_pipe_x_coordinates_by_basement_width = var_shift_pipe_x_coordinates_by_basement_width
        # object-list
        var_name_of_basement_wall_boundary_condition_model = "object-list|Name of Basement Wall Boundary Condition Model"
        obj.name_of_basement_wall_boundary_condition_model = var_name_of_basement_wall_boundary_condition_model
        # object-list
        var_name_of_basement_floor_boundary_condition_model = "object-list|Name of Basement Floor Boundary Condition Model"
        obj.name_of_basement_floor_boundary_condition_model = var_name_of_basement_floor_boundary_condition_model
        # real
        var_convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = 0.2500005
        obj.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = var_convergence_criterion_for_the_outer_cartesian_domain_iteration_loop
        # integer
        var_maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = 5001
        obj.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = var_maximum_iterations_in_the_outer_cartesian_domain_iteration_loop
        # real
        var_evapotranspiration_ground_cover_parameter = 0.75
        obj.evapotranspiration_ground_cover_parameter = var_evapotranspiration_ground_cover_parameter
        # integer
        var_number_of_pipe_circuits_entered_for_this_domain = 1
        obj.number_of_pipe_circuits_entered_for_this_domain = var_number_of_pipe_circuits_entered_for_this_domain
        paras = []
        var_pipe_circuit_1 = "object-list|Pipe Circuit 1"
        paras.append(var_pipe_circuit_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].name, var_name)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].xmax, var_xmax)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].ymax, var_ymax)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].zmax, var_zmax)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].xdirection_mesh_density_parameter, var_xdirection_mesh_density_parameter)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].xdirection_mesh_type, var_xdirection_mesh_type)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].xdirection_geometric_coefficient, var_xdirection_geometric_coefficient)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].ydirection_mesh_density_parameter, var_ydirection_mesh_density_parameter)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].ydirection_mesh_type, var_ydirection_mesh_type)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].ydirection_geometric_coefficient, var_ydirection_geometric_coefficient)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].zdirection_mesh_density_parameter, var_zdirection_mesh_density_parameter)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].zdirection_mesh_type, var_zdirection_mesh_type)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].zdirection_geometric_coefficient, var_zdirection_geometric_coefficient)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].soil_moisture_content_volume_fraction, var_soil_moisture_content_volume_fraction)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].soil_moisture_content_volume_fraction_at_saturation, var_soil_moisture_content_volume_fraction_at_saturation)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].kusudaachenbach_average_surface_temperature, var_kusudaachenbach_average_surface_temperature)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].kusudaachenbach_average_amplitude_of_surface_temperature, var_kusudaachenbach_average_amplitude_of_surface_temperature)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].kusudaachenbach_phase_shift_of_minimum_surface_temperature, var_kusudaachenbach_phase_shift_of_minimum_surface_temperature)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].this_domain_includes_basement_surface_interaction, var_this_domain_includes_basement_surface_interaction)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].width_of_basement_floor_in_ground_domain, var_width_of_basement_floor_in_ground_domain)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].depth_of_basement_wall_in_ground_domain, var_depth_of_basement_wall_in_ground_domain)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].shift_pipe_x_coordinates_by_basement_width, var_shift_pipe_x_coordinates_by_basement_width)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].name_of_basement_wall_boundary_condition_model, var_name_of_basement_wall_boundary_condition_model)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].name_of_basement_floor_boundary_condition_model, var_name_of_basement_floor_boundary_condition_model)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].convergence_criterion_for_the_outer_cartesian_domain_iteration_loop, var_convergence_criterion_for_the_outer_cartesian_domain_iteration_loop)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].maximum_iterations_in_the_outer_cartesian_domain_iteration_loop, var_maximum_iterations_in_the_outer_cartesian_domain_iteration_loop)
        self.assertAlmostEqual(idf2.pipingsystemundergrounddomains[0].evapotranspiration_ground_cover_parameter, var_evapotranspiration_ground_cover_parameter)
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].number_of_pipe_circuits_entered_for_this_domain, var_number_of_pipe_circuits_entered_for_this_domain)
        index = obj.extensible_field_index("Pipe Circuit 1")
        self.assertEqual(idf2.pipingsystemundergrounddomains[0].extensibles[0][index], var_pipe_circuit_1)