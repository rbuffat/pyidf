import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerSingleZoneHumidityMaximum
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerSingleZoneHumidityMaximum(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagersinglezonehumiditymaximum(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerSingleZoneHumidityMaximum()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Control Variable"
        obj.control_variable = var_control_variable
        # alpha
        var_schedule_name = "Schedule Name"
        obj.schedule_name = var_schedule_name
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name
        # node
        var_control_zone_air_node_name = "node|Control Zone Air Node Name"
        obj.control_zone_air_node_name = var_control_zone_air_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagersinglezonehumiditymaximums[0].name, var_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumiditymaximums[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagersinglezonehumiditymaximums[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumiditymaximums[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumiditymaximums[0].control_zone_air_node_name, var_control_zone_air_node_name)