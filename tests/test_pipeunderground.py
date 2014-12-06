import os
import tempfile
import unittest
import pyidf
from pyidf.node import PipeUnderground
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPipeUnderground(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipeunderground(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipeUnderground()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # node
        var_fluid_inlet_node_name = "node|Fluid Inlet Node Name"
        obj.fluid_inlet_node_name = var_fluid_inlet_node_name
        # node
        var_fluid_outlet_node_name = "node|Fluid Outlet Node Name"
        obj.fluid_outlet_node_name = var_fluid_outlet_node_name
        # alpha
        var_sun_exposure = "SunExposed"
        obj.sun_exposure = var_sun_exposure
        # real
        var_pipe_inside_diameter = 0.0001
        obj.pipe_inside_diameter = var_pipe_inside_diameter
        # real
        var_pipe_length = 0.0001
        obj.pipe_length = var_pipe_length
        # alpha
        var_soil_material_name = "Soil Material Name"
        obj.soil_material_name = var_soil_material_name
        # real
        var_average_soil_surface_temperature = 9.9
        obj.average_soil_surface_temperature = var_average_soil_surface_temperature
        # real
        var_amplitude_of_soil_surface_temperature = 0.0
        obj.amplitude_of_soil_surface_temperature = var_amplitude_of_soil_surface_temperature
        # real
        var_phase_constant_of_soil_surface_temperature = 0.0
        obj.phase_constant_of_soil_surface_temperature = var_phase_constant_of_soil_surface_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipeundergrounds[0].name, var_name)
        self.assertEqual(idf2.pipeundergrounds[0].construction_name, var_construction_name)
        self.assertEqual(idf2.pipeundergrounds[0].fluid_inlet_node_name, var_fluid_inlet_node_name)
        self.assertEqual(idf2.pipeundergrounds[0].fluid_outlet_node_name, var_fluid_outlet_node_name)
        self.assertEqual(idf2.pipeundergrounds[0].sun_exposure, var_sun_exposure)
        self.assertAlmostEqual(idf2.pipeundergrounds[0].pipe_inside_diameter, var_pipe_inside_diameter)
        self.assertAlmostEqual(idf2.pipeundergrounds[0].pipe_length, var_pipe_length)
        self.assertEqual(idf2.pipeundergrounds[0].soil_material_name, var_soil_material_name)
        self.assertAlmostEqual(idf2.pipeundergrounds[0].average_soil_surface_temperature, var_average_soil_surface_temperature)
        self.assertAlmostEqual(idf2.pipeundergrounds[0].amplitude_of_soil_surface_temperature, var_amplitude_of_soil_surface_temperature)
        self.assertAlmostEqual(idf2.pipeundergrounds[0].phase_constant_of_soil_surface_temperature, var_phase_constant_of_soil_surface_temperature)