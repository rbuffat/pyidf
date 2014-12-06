import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.humidifiers_and_dehumidifiers import DehumidifierDesiccantNoFans

log = logging.getLogger(__name__)

class TestDehumidifierDesiccantNoFans(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_dehumidifierdesiccantnofans(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DehumidifierDesiccantNoFans()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_process_air_inlet_node_name = "node|Process Air Inlet Node Name"
        obj.process_air_inlet_node_name = var_process_air_inlet_node_name
        # node
        var_process_air_outlet_node_name = "node|Process Air Outlet Node Name"
        obj.process_air_outlet_node_name = var_process_air_outlet_node_name
        # node
        var_regeneration_air_inlet_node_name = "node|Regeneration Air Inlet Node Name"
        obj.regeneration_air_inlet_node_name = var_regeneration_air_inlet_node_name
        # node
        var_regeneration_fan_inlet_node_name = "node|Regeneration Fan Inlet Node Name"
        obj.regeneration_fan_inlet_node_name = var_regeneration_fan_inlet_node_name
        # alpha
        var_control_type = "LeavingMaximumHumidityRatioSetpoint"
        obj.control_type = var_control_type
        # real
        var_leaving_maximum_humidity_ratio_setpoint = 8.8
        obj.leaving_maximum_humidity_ratio_setpoint = var_leaving_maximum_humidity_ratio_setpoint
        # real
        var_nominal_process_air_flow_rate = 0.0001
        obj.nominal_process_air_flow_rate = var_nominal_process_air_flow_rate
        # real
        var_nominal_process_air_velocity = 3.00005
        obj.nominal_process_air_velocity = var_nominal_process_air_velocity
        # real
        var_rotor_power = 0.0
        obj.rotor_power = var_rotor_power
        # alpha
        var_regeneration_coil_object_type = "Coil:Heating:Electric"
        obj.regeneration_coil_object_type = var_regeneration_coil_object_type
        # object-list
        var_regeneration_coil_name = "object-list|Regeneration Coil Name"
        obj.regeneration_coil_name = var_regeneration_coil_name
        # alpha
        var_regeneration_fan_object_type = "Fan:VariableVolume"
        obj.regeneration_fan_object_type = var_regeneration_fan_object_type
        # object-list
        var_regeneration_fan_name = "object-list|Regeneration Fan Name"
        obj.regeneration_fan_name = var_regeneration_fan_name
        # alpha
        var_performance_model_type = "Default"
        obj.performance_model_type = var_performance_model_type
        # object-list
        var_leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = "object-list|Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"
        obj.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = var_leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name
        # object-list
        var_leaving_drybulb_function_of_air_velocity_curve_name = "object-list|Leaving Dry-Bulb Function of Air Velocity Curve Name"
        obj.leaving_drybulb_function_of_air_velocity_curve_name = var_leaving_drybulb_function_of_air_velocity_curve_name
        # object-list
        var_leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = "object-list|Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"
        obj.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = var_leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name
        # object-list
        var_leaving_humidity_ratio_function_of_air_velocity_curve_name = "object-list|Leaving Humidity Ratio Function of Air Velocity Curve Name"
        obj.leaving_humidity_ratio_function_of_air_velocity_curve_name = var_leaving_humidity_ratio_function_of_air_velocity_curve_name
        # object-list
        var_regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = "object-list|Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"
        obj.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = var_regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name
        # object-list
        var_regeneration_energy_function_of_air_velocity_curve_name = "object-list|Regeneration Energy Function of Air Velocity Curve Name"
        obj.regeneration_energy_function_of_air_velocity_curve_name = var_regeneration_energy_function_of_air_velocity_curve_name
        # object-list
        var_regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = "object-list|Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"
        obj.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = var_regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name
        # object-list
        var_regeneration_velocity_function_of_air_velocity_curve_name = "object-list|Regeneration Velocity Function of Air Velocity Curve Name"
        obj.regeneration_velocity_function_of_air_velocity_curve_name = var_regeneration_velocity_function_of_air_velocity_curve_name
        # real
        var_nominal_regeneration_temperature = 145.0
        obj.nominal_regeneration_temperature = var_nominal_regeneration_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].name, var_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].process_air_inlet_node_name, var_process_air_inlet_node_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].process_air_outlet_node_name, var_process_air_outlet_node_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_air_inlet_node_name, var_regeneration_air_inlet_node_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_fan_inlet_node_name, var_regeneration_fan_inlet_node_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].control_type, var_control_type)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantnofanss[0].leaving_maximum_humidity_ratio_setpoint, var_leaving_maximum_humidity_ratio_setpoint)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantnofanss[0].nominal_process_air_flow_rate, var_nominal_process_air_flow_rate)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantnofanss[0].nominal_process_air_velocity, var_nominal_process_air_velocity)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantnofanss[0].rotor_power, var_rotor_power)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_coil_object_type, var_regeneration_coil_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_coil_name, var_regeneration_coil_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_fan_object_type, var_regeneration_fan_object_type)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_fan_name, var_regeneration_fan_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].performance_model_type, var_performance_model_type)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name, var_leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].leaving_drybulb_function_of_air_velocity_curve_name, var_leaving_drybulb_function_of_air_velocity_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name, var_leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].leaving_humidity_ratio_function_of_air_velocity_curve_name, var_leaving_humidity_ratio_function_of_air_velocity_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name, var_regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_energy_function_of_air_velocity_curve_name, var_regeneration_energy_function_of_air_velocity_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name, var_regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name)
        self.assertEqual(idf2.dehumidifierdesiccantnofanss[0].regeneration_velocity_function_of_air_velocity_curve_name, var_regeneration_velocity_function_of_air_velocity_curve_name)
        self.assertAlmostEqual(idf2.dehumidifierdesiccantnofanss[0].nominal_regeneration_temperature, var_nominal_regeneration_temperature)