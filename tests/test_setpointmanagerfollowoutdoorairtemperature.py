import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerFollowOutdoorAirTemperature
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerFollowOutdoorAirTemperature(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerfollowoutdoorairtemperature(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerFollowOutdoorAirTemperature()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # alpha
        var_reference_temperature_type = "OutdoorAirWetBulb"
        obj.reference_temperature_type = var_reference_temperature_type
        # real
        var_offset_temperature_difference = 4.4
        obj.offset_temperature_difference = var_offset_temperature_difference
        # real
        var_maximum_setpoint_temperature = 5.5
        obj.maximum_setpoint_temperature = var_maximum_setpoint_temperature
        # real
        var_minimum_setpoint_temperature = 6.6
        obj.minimum_setpoint_temperature = var_minimum_setpoint_temperature
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
        self.assertEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].reference_temperature_type, var_reference_temperature_type)
        self.assertAlmostEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].offset_temperature_difference, var_offset_temperature_difference)
        self.assertAlmostEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].maximum_setpoint_temperature, var_maximum_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].minimum_setpoint_temperature, var_minimum_setpoint_temperature)
        self.assertEqual(idf2.setpointmanagerfollowoutdoorairtemperatures[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)