import os
import tempfile
import unittest
import pyidf
from pyidf.condenser_equipment_and_heat_exchangers import GroundHeatExchangerHorizontalTrench
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatExchangerHorizontalTrench(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheatexchangerhorizontaltrench(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatExchangerHorizontalTrench()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_design_flow_rate = 0.0001
        obj.design_flow_rate = var_design_flow_rate
        # real
        var_trench_length_in_pipe_axial_direction = 0.0001
        obj.trench_length_in_pipe_axial_direction = var_trench_length_in_pipe_axial_direction
        # integer
        var_number_of_trenches = 1
        obj.number_of_trenches = var_number_of_trenches
        # real
        var_horizontal_spacing_between_pipes = 0.0001
        obj.horizontal_spacing_between_pipes = var_horizontal_spacing_between_pipes
        # real
        var_pipe_inner_diameter = 0.0001
        obj.pipe_inner_diameter = var_pipe_inner_diameter
        # real
        var_pipe_outer_diameter = 0.0001
        obj.pipe_outer_diameter = var_pipe_outer_diameter
        # real
        var_burial_depth = 0.0001
        obj.burial_depth = var_burial_depth
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
        var_pipe_thermal_conductivity = 0.0001
        obj.pipe_thermal_conductivity = var_pipe_thermal_conductivity
        # real
        var_pipe_density = 0.0001
        obj.pipe_density = var_pipe_density
        # real
        var_pipe_specific_heat = 0.0001
        obj.pipe_specific_heat = var_pipe_specific_heat
        # real
        var_soil_moisture_content_percent = 50.0
        obj.soil_moisture_content_percent = var_soil_moisture_content_percent
        # real
        var_soil_moisture_content_percent_at_saturation = 50.0
        obj.soil_moisture_content_percent_at_saturation = var_soil_moisture_content_percent_at_saturation
        # real
        var_kusudaachenbach_average_surface_temperature = 19.19
        obj.kusudaachenbach_average_surface_temperature = var_kusudaachenbach_average_surface_temperature
        # real
        var_kusudaachenbach_average_amplitude_of_surface_temperature = 20.2
        obj.kusudaachenbach_average_amplitude_of_surface_temperature = var_kusudaachenbach_average_amplitude_of_surface_temperature
        # real
        var_kusudaachenbach_phase_shift_of_minimum_surface_temperature = 21.21
        obj.kusudaachenbach_phase_shift_of_minimum_surface_temperature = var_kusudaachenbach_phase_shift_of_minimum_surface_temperature
        # real
        var_evapotranspiration_ground_cover_parameter = 0.75
        obj.evapotranspiration_ground_cover_parameter = var_evapotranspiration_ground_cover_parameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheatexchangerhorizontaltrenchs[0].name, var_name)
        self.assertEqual(idf2.groundheatexchangerhorizontaltrenchs[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.groundheatexchangerhorizontaltrenchs[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].trench_length_in_pipe_axial_direction, var_trench_length_in_pipe_axial_direction)
        self.assertEqual(idf2.groundheatexchangerhorizontaltrenchs[0].number_of_trenches, var_number_of_trenches)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].horizontal_spacing_between_pipes, var_horizontal_spacing_between_pipes)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].pipe_inner_diameter, var_pipe_inner_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].pipe_outer_diameter, var_pipe_outer_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].burial_depth, var_burial_depth)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].pipe_thermal_conductivity, var_pipe_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].pipe_density, var_pipe_density)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].pipe_specific_heat, var_pipe_specific_heat)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].soil_moisture_content_percent, var_soil_moisture_content_percent)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].soil_moisture_content_percent_at_saturation, var_soil_moisture_content_percent_at_saturation)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].kusudaachenbach_average_surface_temperature, var_kusudaachenbach_average_surface_temperature)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].kusudaachenbach_average_amplitude_of_surface_temperature, var_kusudaachenbach_average_amplitude_of_surface_temperature)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].kusudaachenbach_phase_shift_of_minimum_surface_temperature, var_kusudaachenbach_phase_shift_of_minimum_surface_temperature)
        self.assertAlmostEqual(idf2.groundheatexchangerhorizontaltrenchs[0].evapotranspiration_ground_cover_parameter, var_evapotranspiration_ground_cover_parameter)