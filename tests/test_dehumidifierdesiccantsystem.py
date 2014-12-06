import os
import tempfile
import unittest
import pyidf
from pyidf.humidifiers_and_dehumidifiers import DehumidifierDesiccantSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDehumidifierDesiccantSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_dehumidifierdesiccantsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DehumidifierDesiccantSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_desiccant_heat_exchanger_object_type = "HeatExchanger:Desiccant:BalancedFlow"
        obj.desiccant_heat_exchanger_object_type = var_desiccant_heat_exchanger_object_type
        # object-list
        var_desiccant_heat_exchanger_name = "object-list|Desiccant Heat Exchanger Name"
        obj.desiccant_heat_exchanger_name = var_desiccant_heat_exchanger_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # alpha
        var_regeneration_air_fan_object_type = "Fan:OnOff"
        obj.regeneration_air_fan_object_type = var_regeneration_air_fan_object_type
        # object-list
        var_regeneration_air_fan_name = "object-list|Regeneration Air Fan Name"
        obj.regeneration_air_fan_name = var_regeneration_air_fan_name
        # alpha
        var_regeneration_air_fan_placement = "BlowThrough"
        obj.regeneration_air_fan_placement = var_regeneration_air_fan_placement
        # alpha
        var_regeneration_air_heater_object_type = "Coil:Heating:Electric"
        obj.regeneration_air_heater_object_type = var_regeneration_air_heater_object_type
        # object-list
        var_regeneration_air_heater_name = "object-list|Regeneration Air Heater Name"
        obj.regeneration_air_heater_name = var_regeneration_air_heater_name
        # real
        var_regeneration_inlet_air_setpoint_temperature = 11.11
        obj.regeneration_inlet_air_setpoint_temperature = var_regeneration_inlet_air_setpoint_temperature
        # alpha
        var_companion_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.companion_cooling_coil_object_type = var_companion_cooling_coil_object_type
        # object-list
        var_companion_cooling_coil_name = "object-list|Companion Cooling Coil Name"
        obj.companion_cooling_coil_name = var_companion_cooling_coil_name
        # alpha
        var_companion_cooling_coil_upstream_of_dehumidifier_process_inlet = "Yes"
        obj.companion_cooling_coil_upstream_of_dehumidifier_process_inlet = var_companion_cooling_coil_upstream_of_dehumidifier_process_inlet
        # alpha
        var_companion_coil_regeneration_air_heating = "Yes"
        obj.companion_coil_regeneration_air_heating = var_companion_coil_regeneration_air_heating
        # real
        var_exhaust_fan_maximum_flow_rate = 16.16
        obj.exhaust_fan_maximum_flow_rate = var_exhaust_fan_maximum_flow_rate
        # real
        var_exhaust_fan_maximum_power = 17.17
        obj.exhaust_fan_maximum_power = var_exhaust_fan_maximum_power
        # alpha
        var_exhaust_fan_power_curve_name = "Exhaust Fan Power Curve Name"
        obj.exhaust_fan_power_curve_name = var_exhaust_fan_power_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].name, var_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].desiccant_heat_exchanger_object_type, var_desiccant_heat_exchanger_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].desiccant_heat_exchanger_name, var_desiccant_heat_exchanger_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].sensor_node_name, var_sensor_node_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_air_fan_object_type, var_regeneration_air_fan_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_air_fan_name, var_regeneration_air_fan_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_air_fan_placement, var_regeneration_air_fan_placement)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_air_heater_object_type, var_regeneration_air_heater_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_air_heater_name, var_regeneration_air_heater_name)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantsystems[0].regeneration_inlet_air_setpoint_temperature, var_regeneration_inlet_air_setpoint_temperature)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].companion_cooling_coil_object_type, var_companion_cooling_coil_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].companion_cooling_coil_name, var_companion_cooling_coil_name)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].companion_cooling_coil_upstream_of_dehumidifier_process_inlet, var_companion_cooling_coil_upstream_of_dehumidifier_process_inlet)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].companion_coil_regeneration_air_heating, var_companion_coil_regeneration_air_heating)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantsystems[0].exhaust_fan_maximum_flow_rate, var_exhaust_fan_maximum_flow_rate)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantsystems[0].exhaust_fan_maximum_power, var_exhaust_fan_maximum_power)
        self.assertEqual(idf2.dehumidifierdesiccantsystems[0].exhaust_fan_power_curve_name, var_exhaust_fan_power_curve_name)