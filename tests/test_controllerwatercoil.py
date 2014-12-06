import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.controllers import ControllerWaterCoil

log = logging.getLogger(__name__)

class TestControllerWaterCoil(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_controllerwatercoil(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ControllerWaterCoil()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # alpha
        var_action = "Normal"
        obj.action = var_action
        # alpha
        var_actuator_variable = "Flow"
        obj.actuator_variable = var_actuator_variable
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # node
        var_actuator_node_name = "node|Actuator Node Name"
        obj.actuator_node_name = var_actuator_node_name
        # real
        var_controller_convergence_tolerance = 7.7
        obj.controller_convergence_tolerance = var_controller_convergence_tolerance
        # real
        var_maximum_actuated_flow = 8.8
        obj.maximum_actuated_flow = var_maximum_actuated_flow
        # real
        var_minimum_actuated_flow = 9.9
        obj.minimum_actuated_flow = var_minimum_actuated_flow

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.controllerwatercoils[0].name, var_name)
        self.assertEqual(idf2.controllerwatercoils[0].control_variable, var_control_variable)
        self.assertEqual(idf2.controllerwatercoils[0].action, var_action)
        self.assertEqual(idf2.controllerwatercoils[0].actuator_variable, var_actuator_variable)
        self.assertEqual(idf2.controllerwatercoils[0].sensor_node_name, var_sensor_node_name)
        self.assertEqual(idf2.controllerwatercoils[0].actuator_node_name, var_actuator_node_name)
        self.assertAlmostEqual(idf2.controllerwatercoils[0].controller_convergence_tolerance, var_controller_convergence_tolerance)
        self.assertAlmostEqual(idf2.controllerwatercoils[0].maximum_actuated_flow, var_maximum_actuated_flow)
        self.assertAlmostEqual(idf2.controllerwatercoils[0].minimum_actuated_flow, var_minimum_actuated_flow)