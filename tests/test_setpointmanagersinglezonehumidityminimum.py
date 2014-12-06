import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerSingleZoneHumidityMinimum

log = logging.getLogger(__name__)

class TestSetpointManagerSingleZoneHumidityMinimum(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagersinglezonehumidityminimum(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerSingleZoneHumidityMinimum()
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagersinglezonehumidityminimums[0].name, var_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumidityminimums[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagersinglezonehumidityminimums[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumidityminimums[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)
        self.assertEqual(idf2.setpointmanagersinglezonehumidityminimums[0].control_zone_air_node_name, var_control_zone_air_node_name)