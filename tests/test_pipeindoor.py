import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import PipeIndoor

log = logging.getLogger(__name__)

class TestPipeIndoor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipeindoor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipeIndoor()
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
        var_environment_type = "Zone"
        obj.environment_type = var_environment_type
        # object-list
        var_ambient_temperature_zone_name = "object-list|Ambient Temperature Zone Name"
        obj.ambient_temperature_zone_name = var_ambient_temperature_zone_name
        # object-list
        var_ambient_temperature_schedule_name = "object-list|Ambient Temperature Schedule Name"
        obj.ambient_temperature_schedule_name = var_ambient_temperature_schedule_name
        # object-list
        var_ambient_air_velocity_schedule_name = "object-list|Ambient Air Velocity Schedule Name"
        obj.ambient_air_velocity_schedule_name = var_ambient_air_velocity_schedule_name
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipeindoors[0].name, var_name)
        self.assertEqual(idf2.pipeindoors[0].construction_name, var_construction_name)
        self.assertEqual(idf2.pipeindoors[0].fluid_inlet_node_name, var_fluid_inlet_node_name)
        self.assertEqual(idf2.pipeindoors[0].fluid_outlet_node_name, var_fluid_outlet_node_name)
        self.assertEqual(idf2.pipeindoors[0].environment_type, var_environment_type)
        self.assertEqual(idf2.pipeindoors[0].ambient_temperature_zone_name, var_ambient_temperature_zone_name)
        self.assertEqual(idf2.pipeindoors[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.pipeindoors[0].ambient_air_velocity_schedule_name, var_ambient_air_velocity_schedule_name)
        self.assertAlmostEqual(idf2.pipeindoors[0].pipe_inside_diameter, var_pipe_inside_diameter)
        self.assertAlmostEqual(idf2.pipeindoors[0].pipe_length, var_pipe_length)