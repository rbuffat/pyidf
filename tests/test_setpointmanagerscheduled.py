import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerScheduled
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerScheduled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerscheduled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerScheduled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
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
        self.assertEqual(idf2.setpointmanagerscheduleds[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerscheduleds[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerscheduleds[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.setpointmanagerscheduleds[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)