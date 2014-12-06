import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.demand_limiting_controls import DemandManagerThermostats

log = logging.getLogger(__name__)

class TestDemandManagerThermostats(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_demandmanagerthermostats(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DemandManagerThermostats()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_reset_control = "Off"
        obj.reset_control = var_reset_control
        # integer
        var_minimum_reset_duration = 1
        obj.minimum_reset_duration = var_minimum_reset_duration
        # real
        var_maximum_heating_setpoint_reset = 5.5
        obj.maximum_heating_setpoint_reset = var_maximum_heating_setpoint_reset
        # real
        var_maximum_cooling_setpoint_reset = 6.6
        obj.maximum_cooling_setpoint_reset = var_maximum_cooling_setpoint_reset
        # real
        var_reset_step_change = 7.7
        obj.reset_step_change = var_reset_step_change
        # alpha
        var_selection_control = "All"
        obj.selection_control = var_selection_control
        # integer
        var_rotation_duration = 0
        obj.rotation_duration = var_rotation_duration
        paras = []
        var_thermostat_1_name = "object-list|Thermostat 1 Name"
        paras.append(var_thermostat_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.demandmanagerthermostatss[0].name, var_name)
        self.assertEqual(idf2.demandmanagerthermostatss[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.demandmanagerthermostatss[0].reset_control, var_reset_control)
        self.assertEqual(idf2.demandmanagerthermostatss[0].minimum_reset_duration, var_minimum_reset_duration)
        self.assertAlmostEqual(idf2.demandmanagerthermostatss[0].maximum_heating_setpoint_reset, var_maximum_heating_setpoint_reset)
        self.assertAlmostEqual(idf2.demandmanagerthermostatss[0].maximum_cooling_setpoint_reset, var_maximum_cooling_setpoint_reset)
        self.assertAlmostEqual(idf2.demandmanagerthermostatss[0].reset_step_change, var_reset_step_change)
        self.assertEqual(idf2.demandmanagerthermostatss[0].selection_control, var_selection_control)
        self.assertEqual(idf2.demandmanagerthermostatss[0].rotation_duration, var_rotation_duration)
        index = obj.extensible_field_index("Thermostat 1 Name")
        self.assertEqual(idf2.demandmanagerthermostatss[0].extensibles[0][index], var_thermostat_1_name)