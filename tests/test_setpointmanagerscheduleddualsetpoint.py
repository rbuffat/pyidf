import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerScheduledDualSetpoint
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerScheduledDualSetpoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerscheduleddualsetpoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerScheduledDualSetpoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # object-list
        var_high_setpoint_schedule_name = "object-list|High Setpoint Schedule Name"
        obj.high_setpoint_schedule_name = var_high_setpoint_schedule_name
        # object-list
        var_low_setpoint_schedule_name = "object-list|Low Setpoint Schedule Name"
        obj.low_setpoint_schedule_name = var_low_setpoint_schedule_name
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagerscheduleddualsetpoints[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerscheduleddualsetpoints[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerscheduleddualsetpoints[0].high_setpoint_schedule_name, var_high_setpoint_schedule_name)
        self.assertEqual(idf2.setpointmanagerscheduleddualsetpoints[0].low_setpoint_schedule_name, var_low_setpoint_schedule_name)
        self.assertEqual(idf2.setpointmanagerscheduleddualsetpoints[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)