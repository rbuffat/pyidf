import os
import tempfile
import unittest
import pyidf
from pyidf.node import PipeOutdoor
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPipeOutdoor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipeoutdoor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipeOutdoor()
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
        # node
        var_ambient_temperature_outdoor_air_node_name = "node|Ambient Temperature Outdoor Air Node Name"
        obj.ambient_temperature_outdoor_air_node_name = var_ambient_temperature_outdoor_air_node_name
        # real
        var_pipe_inside_diameter = 0.0001
        obj.pipe_inside_diameter = var_pipe_inside_diameter
        # real
        var_pipe_length = 0.0001
        obj.pipe_length = var_pipe_length

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipeoutdoors[0].name, var_name)
        self.assertEqual(idf2.pipeoutdoors[0].construction_name, var_construction_name)
        self.assertEqual(idf2.pipeoutdoors[0].fluid_inlet_node_name, var_fluid_inlet_node_name)
        self.assertEqual(idf2.pipeoutdoors[0].fluid_outlet_node_name, var_fluid_outlet_node_name)
        self.assertEqual(idf2.pipeoutdoors[0].ambient_temperature_outdoor_air_node_name, var_ambient_temperature_outdoor_air_node_name)
        self.assertAlmostEqual(idf2.pipeoutdoors[0].pipe_inside_diameter, var_pipe_inside_diameter)
        self.assertAlmostEqual(idf2.pipeoutdoors[0].pipe_length, var_pipe_length)