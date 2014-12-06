import os
import tempfile
import unittest
import pyidf
from pyidf.setpoint_managers import SetpointManagerOutdoorAirReset
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSetpointManagerOutdoorAirReset(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanageroutdoorairreset(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerOutdoorAirReset()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # real
        var_setpoint_at_outdoor_low_temperature = 3.3
        obj.setpoint_at_outdoor_low_temperature = var_setpoint_at_outdoor_low_temperature
        # real
        var_outdoor_low_temperature = 4.4
        obj.outdoor_low_temperature = var_outdoor_low_temperature
        # real
        var_setpoint_at_outdoor_high_temperature = 5.5
        obj.setpoint_at_outdoor_high_temperature = var_setpoint_at_outdoor_high_temperature
        # real
        var_outdoor_high_temperature = 6.6
        obj.outdoor_high_temperature = var_outdoor_high_temperature
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_setpoint_at_outdoor_low_temperature_2 = 9.9
        obj.setpoint_at_outdoor_low_temperature_2 = var_setpoint_at_outdoor_low_temperature_2
        # real
        var_outdoor_low_temperature_2 = 10.1
        obj.outdoor_low_temperature_2 = var_outdoor_low_temperature_2
        # real
        var_setpoint_at_outdoor_high_temperature_2 = 11.11
        obj.setpoint_at_outdoor_high_temperature_2 = var_setpoint_at_outdoor_high_temperature_2
        # real
        var_outdoor_high_temperature_2 = 12.12
        obj.outdoor_high_temperature_2 = var_outdoor_high_temperature_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanageroutdoorairresets[0].name, var_name)
        self.assertEqual(idf2.setpointmanageroutdoorairresets[0].control_variable, var_control_variable)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].setpoint_at_outdoor_low_temperature, var_setpoint_at_outdoor_low_temperature)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].outdoor_low_temperature, var_outdoor_low_temperature)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].setpoint_at_outdoor_high_temperature, var_setpoint_at_outdoor_high_temperature)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].outdoor_high_temperature, var_outdoor_high_temperature)
        self.assertEqual(idf2.setpointmanageroutdoorairresets[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)
        self.assertEqual(idf2.setpointmanageroutdoorairresets[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].setpoint_at_outdoor_low_temperature_2, var_setpoint_at_outdoor_low_temperature_2)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].outdoor_low_temperature_2, var_outdoor_low_temperature_2)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].setpoint_at_outdoor_high_temperature_2, var_setpoint_at_outdoor_high_temperature_2)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairresets[0].outdoor_high_temperature_2, var_outdoor_high_temperature_2)