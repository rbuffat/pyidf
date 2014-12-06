import os
import tempfile
import unittest
import pyidf
from pyidf.node import PipingSystemUndergroundPipeCircuit
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPipingSystemUndergroundPipeCircuit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipingsystemundergroundpipecircuit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipingSystemUndergroundPipeCircuit()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_pipe_thermal_conductivity = 0.0001
        obj.pipe_thermal_conductivity = var_pipe_thermal_conductivity
        # real
        var_pipe_density = 0.0001
        obj.pipe_density = var_pipe_density
        # real
        var_pipe_specific_heat = 0.0001
        obj.pipe_specific_heat = var_pipe_specific_heat
        # real
        var_pipe_inner_diameter = 0.0001
        obj.pipe_inner_diameter = var_pipe_inner_diameter
        # real
        var_pipe_outer_diameter = 0.0001
        obj.pipe_outer_diameter = var_pipe_outer_diameter
        # real
        var_design_flow_rate = 0.0001
        obj.design_flow_rate = var_design_flow_rate
        # node
        var_circuit_inlet_node = "node|Circuit Inlet Node"
        obj.circuit_inlet_node = var_circuit_inlet_node
        # node
        var_circuit_outlet_node = "node|Circuit Outlet Node"
        obj.circuit_outlet_node = var_circuit_outlet_node
        # real
        var_convergence_criterion_for_the_inner_radial_iteration_loop = 0.2500005
        obj.convergence_criterion_for_the_inner_radial_iteration_loop = var_convergence_criterion_for_the_inner_radial_iteration_loop
        # integer
        var_maximum_iterations_in_the_inner_radial_iteration_loop = 5001
        obj.maximum_iterations_in_the_inner_radial_iteration_loop = var_maximum_iterations_in_the_inner_radial_iteration_loop
        # integer
        var_number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = 8
        obj.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = var_number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region
        # real
        var_radial_thickness_of_inner_radial_near_pipe_mesh_region = 0.0001
        obj.radial_thickness_of_inner_radial_near_pipe_mesh_region = var_radial_thickness_of_inner_radial_near_pipe_mesh_region
        # integer
        var_number_of_pipe_segments_entered_for_this_pipe_circuit = 1
        obj.number_of_pipe_segments_entered_for_this_pipe_circuit = var_number_of_pipe_segments_entered_for_this_pipe_circuit
        paras = []
        var_pipe_segment_1 = "object-list|Pipe Segment 1"
        paras.append(var_pipe_segment_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].name, var_name)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].pipe_thermal_conductivity, var_pipe_thermal_conductivity)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].pipe_density, var_pipe_density)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].pipe_specific_heat, var_pipe_specific_heat)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].pipe_inner_diameter, var_pipe_inner_diameter)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].pipe_outer_diameter, var_pipe_outer_diameter)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].design_flow_rate, var_design_flow_rate)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].circuit_inlet_node, var_circuit_inlet_node)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].circuit_outlet_node, var_circuit_outlet_node)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].convergence_criterion_for_the_inner_radial_iteration_loop, var_convergence_criterion_for_the_inner_radial_iteration_loop)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].maximum_iterations_in_the_inner_radial_iteration_loop, var_maximum_iterations_in_the_inner_radial_iteration_loop)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region, var_number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipecircuits[0].radial_thickness_of_inner_radial_near_pipe_mesh_region, var_radial_thickness_of_inner_radial_near_pipe_mesh_region)
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].number_of_pipe_segments_entered_for_this_pipe_circuit, var_number_of_pipe_segments_entered_for_this_pipe_circuit)
        index = obj.extensible_field_index("Pipe Segment 1")
        self.assertEqual(idf2.pipingsystemundergroundpipecircuits[0].extensibles[0][index], var_pipe_segment_1)