import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerMixedAir

log = logging.getLogger(__name__)

class TestSetpointManagerMixedAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagermixedair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerMixedAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # node
        var_reference_setpoint_node_name = "node|Reference Setpoint Node Name"
        obj.reference_setpoint_node_name = var_reference_setpoint_node_name
        # node
        var_fan_inlet_node_name = "node|Fan Inlet Node Name"
        obj.fan_inlet_node_name = var_fan_inlet_node_name
        # node
        var_fan_outlet_node_name = "node|Fan Outlet Node Name"
        obj.fan_outlet_node_name = var_fan_outlet_node_name
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagermixedairs[0].name, var_name)
        self.assertEqual(idf2.setpointmanagermixedairs[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagermixedairs[0].reference_setpoint_node_name, var_reference_setpoint_node_name)
        self.assertEqual(idf2.setpointmanagermixedairs[0].fan_inlet_node_name, var_fan_inlet_node_name)
        self.assertEqual(idf2.setpointmanagermixedairs[0].fan_outlet_node_name, var_fan_outlet_node_name)
        self.assertEqual(idf2.setpointmanagermixedairs[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)