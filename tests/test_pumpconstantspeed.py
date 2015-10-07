import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.pumps import PumpConstantSpeed

log = logging.getLogger(__name__)

class TestPumpConstantSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pumpconstantspeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PumpConstantSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_rated_flow_rate = 0.0001
        obj.rated_flow_rate = var_rated_flow_rate
        # real
        var_rated_pump_head = 5.5
        obj.rated_pump_head = var_rated_pump_head
        # real
        var_rated_power_consumption = 6.6
        obj.rated_power_consumption = var_rated_power_consumption
        # real
        var_motor_efficiency = 0.50005
        obj.motor_efficiency = var_motor_efficiency
        # real
        var_fraction_of_motor_inefficiencies_to_fluid_stream = 0.5
        obj.fraction_of_motor_inefficiencies_to_fluid_stream = var_fraction_of_motor_inefficiencies_to_fluid_stream
        # alpha
        var_pump_control_type = "Continuous"
        obj.pump_control_type = var_pump_control_type
        # object-list
        var_pump_flow_rate_schedule_name = "object-list|Pump Flow Rate Schedule Name"
        obj.pump_flow_rate_schedule_name = var_pump_flow_rate_schedule_name
        # object-list
        var_pump_curve_name = "object-list|Pump Curve Name"
        obj.pump_curve_name = var_pump_curve_name
        # real
        var_impeller_diameter = 12.12
        obj.impeller_diameter = var_impeller_diameter
        # real
        var_rotational_speed = 13.13
        obj.rotational_speed = var_rotational_speed
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_skin_loss_radiative_fraction = 0.5
        obj.skin_loss_radiative_fraction = var_skin_loss_radiative_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pumpconstantspeeds[0].name, var_name)
        self.assertEqual(idf2.pumpconstantspeeds[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.pumpconstantspeeds[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].rated_flow_rate, var_rated_flow_rate)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].rated_pump_head, var_rated_pump_head)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].rated_power_consumption, var_rated_power_consumption)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].fraction_of_motor_inefficiencies_to_fluid_stream, var_fraction_of_motor_inefficiencies_to_fluid_stream)
        self.assertEqual(idf2.pumpconstantspeeds[0].pump_control_type, var_pump_control_type)
        self.assertEqual(idf2.pumpconstantspeeds[0].pump_flow_rate_schedule_name, var_pump_flow_rate_schedule_name)
        self.assertEqual(idf2.pumpconstantspeeds[0].pump_curve_name, var_pump_curve_name)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].impeller_diameter, var_impeller_diameter)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].rotational_speed, var_rotational_speed)
        self.assertEqual(idf2.pumpconstantspeeds[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.pumpconstantspeeds[0].skin_loss_radiative_fraction, var_skin_loss_radiative_fraction)