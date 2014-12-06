import os
import tempfile
import unittest
import pyidf
from pyidf.controllers import ControllerOutdoorAir
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestControllerOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_controlleroutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ControllerOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_relief_air_outlet_node_name = "node|Relief Air Outlet Node Name"
        obj.relief_air_outlet_node_name = var_relief_air_outlet_node_name
        # node
        var_return_air_node_name = "node|Return Air Node Name"
        obj.return_air_node_name = var_return_air_node_name
        # node
        var_mixed_air_node_name = "node|Mixed Air Node Name"
        obj.mixed_air_node_name = var_mixed_air_node_name
        # node
        var_actuator_node_name = "node|Actuator Node Name"
        obj.actuator_node_name = var_actuator_node_name
        # real
        var_minimum_outdoor_air_flow_rate = 6.6
        obj.minimum_outdoor_air_flow_rate = var_minimum_outdoor_air_flow_rate
        # real
        var_maximum_outdoor_air_flow_rate = 7.7
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # alpha
        var_economizer_control_type = "FixedDryBulb"
        obj.economizer_control_type = var_economizer_control_type
        # alpha
        var_economizer_control_action_type = "ModulateFlow"
        obj.economizer_control_action_type = var_economizer_control_action_type
        # real
        var_economizer_maximum_limit_drybulb_temperature = 10.1
        obj.economizer_maximum_limit_drybulb_temperature = var_economizer_maximum_limit_drybulb_temperature
        # real
        var_economizer_maximum_limit_enthalpy = 11.11
        obj.economizer_maximum_limit_enthalpy = var_economizer_maximum_limit_enthalpy
        # real
        var_economizer_maximum_limit_dewpoint_temperature = 12.12
        obj.economizer_maximum_limit_dewpoint_temperature = var_economizer_maximum_limit_dewpoint_temperature
        # object-list
        var_electronic_enthalpy_limit_curve_name = "object-list|Electronic Enthalpy Limit Curve Name"
        obj.electronic_enthalpy_limit_curve_name = var_electronic_enthalpy_limit_curve_name
        # real
        var_economizer_minimum_limit_drybulb_temperature = 14.14
        obj.economizer_minimum_limit_drybulb_temperature = var_economizer_minimum_limit_drybulb_temperature
        # alpha
        var_lockout_type = "NoLockout"
        obj.lockout_type = var_lockout_type
        # alpha
        var_minimum_limit_type = "FixedMinimum"
        obj.minimum_limit_type = var_minimum_limit_type
        # object-list
        var_minimum_outdoor_air_schedule_name = "object-list|Minimum Outdoor Air Schedule Name"
        obj.minimum_outdoor_air_schedule_name = var_minimum_outdoor_air_schedule_name
        # object-list
        var_minimum_fraction_of_outdoor_air_schedule_name = "object-list|Minimum Fraction of Outdoor Air Schedule Name"
        obj.minimum_fraction_of_outdoor_air_schedule_name = var_minimum_fraction_of_outdoor_air_schedule_name
        # object-list
        var_maximum_fraction_of_outdoor_air_schedule_name = "object-list|Maximum Fraction of Outdoor Air Schedule Name"
        obj.maximum_fraction_of_outdoor_air_schedule_name = var_maximum_fraction_of_outdoor_air_schedule_name
        # object-list
        var_mechanical_ventilation_controller_name = "object-list|Mechanical Ventilation Controller Name"
        obj.mechanical_ventilation_controller_name = var_mechanical_ventilation_controller_name
        # object-list
        var_time_of_day_economizer_control_schedule_name = "object-list|Time of Day Economizer Control Schedule Name"
        obj.time_of_day_economizer_control_schedule_name = var_time_of_day_economizer_control_schedule_name
        # alpha
        var_high_humidity_control = "Yes"
        obj.high_humidity_control = var_high_humidity_control
        # object-list
        var_humidistat_control_zone_name = "object-list|Humidistat Control Zone Name"
        obj.humidistat_control_zone_name = var_humidistat_control_zone_name
        # real
        var_high_humidity_outdoor_air_flow_ratio = 0.0001
        obj.high_humidity_outdoor_air_flow_ratio = var_high_humidity_outdoor_air_flow_ratio
        # alpha
        var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio = "Yes"
        obj.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio
        # alpha
        var_heat_recovery_bypass_control_type = "BypassWhenWithinEconomizerLimits"
        obj.heat_recovery_bypass_control_type = var_heat_recovery_bypass_control_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.controlleroutdoorairs[0].name, var_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].relief_air_outlet_node_name, var_relief_air_outlet_node_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].return_air_node_name, var_return_air_node_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].mixed_air_node_name, var_mixed_air_node_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].actuator_node_name, var_actuator_node_name)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertEqual(idf2.controlleroutdoorairs[0].economizer_control_type, var_economizer_control_type)
        self.assertEqual(idf2.controlleroutdoorairs[0].economizer_control_action_type, var_economizer_control_action_type)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].economizer_maximum_limit_drybulb_temperature, var_economizer_maximum_limit_drybulb_temperature)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].economizer_maximum_limit_enthalpy, var_economizer_maximum_limit_enthalpy)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].economizer_maximum_limit_dewpoint_temperature, var_economizer_maximum_limit_dewpoint_temperature)
        self.assertEqual(idf2.controlleroutdoorairs[0].electronic_enthalpy_limit_curve_name, var_electronic_enthalpy_limit_curve_name)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].economizer_minimum_limit_drybulb_temperature, var_economizer_minimum_limit_drybulb_temperature)
        self.assertEqual(idf2.controlleroutdoorairs[0].lockout_type, var_lockout_type)
        self.assertEqual(idf2.controlleroutdoorairs[0].minimum_limit_type, var_minimum_limit_type)
        self.assertEqual(idf2.controlleroutdoorairs[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].minimum_fraction_of_outdoor_air_schedule_name, var_minimum_fraction_of_outdoor_air_schedule_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].maximum_fraction_of_outdoor_air_schedule_name, var_maximum_fraction_of_outdoor_air_schedule_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].mechanical_ventilation_controller_name, var_mechanical_ventilation_controller_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].time_of_day_economizer_control_schedule_name, var_time_of_day_economizer_control_schedule_name)
        self.assertEqual(idf2.controlleroutdoorairs[0].high_humidity_control, var_high_humidity_control)
        self.assertEqual(idf2.controlleroutdoorairs[0].humidistat_control_zone_name, var_humidistat_control_zone_name)
        self.assertAlmostEqual(idf2.controlleroutdoorairs[0].high_humidity_outdoor_air_flow_ratio, var_high_humidity_outdoor_air_flow_ratio)
        self.assertEqual(idf2.controlleroutdoorairs[0].control_high_indoor_humidity_based_on_outdoor_humidity_ratio, var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio)
        self.assertEqual(idf2.controlleroutdoorairs[0].heat_recovery_bypass_control_type, var_heat_recovery_bypass_control_type)