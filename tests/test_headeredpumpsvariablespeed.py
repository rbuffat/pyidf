import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.pumps import HeaderedPumpsVariableSpeed

log = logging.getLogger(__name__)

class TestHeaderedPumpsVariableSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_headeredpumpsvariablespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeaderedPumpsVariableSpeed()
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
        var_total_rated_flow_rate = 0.0001
        obj.total_rated_flow_rate = var_total_rated_flow_rate
        # integer
        var_number_of_pumps_in_bank = 5
        obj.number_of_pumps_in_bank = var_number_of_pumps_in_bank
        # alpha
        var_flow_sequencing_control_scheme = "Sequential"
        obj.flow_sequencing_control_scheme = var_flow_sequencing_control_scheme
        # real
        var_rated_pump_head = 7.7
        obj.rated_pump_head = var_rated_pump_head
        # real
        var_rated_power_consumption = 8.8
        obj.rated_power_consumption = var_rated_power_consumption
        # real
        var_motor_efficiency = 0.50005
        obj.motor_efficiency = var_motor_efficiency
        # real
        var_fraction_of_motor_inefficiencies_to_fluid_stream = 0.5
        obj.fraction_of_motor_inefficiencies_to_fluid_stream = var_fraction_of_motor_inefficiencies_to_fluid_stream
        # real
        var_coefficient_1_of_the_part_load_performance_curve = 11.11
        obj.coefficient_1_of_the_part_load_performance_curve = var_coefficient_1_of_the_part_load_performance_curve
        # real
        var_coefficient_2_of_the_part_load_performance_curve = 12.12
        obj.coefficient_2_of_the_part_load_performance_curve = var_coefficient_2_of_the_part_load_performance_curve
        # real
        var_coefficient_3_of_the_part_load_performance_curve = 13.13
        obj.coefficient_3_of_the_part_load_performance_curve = var_coefficient_3_of_the_part_load_performance_curve
        # real
        var_coefficient_4_of_the_part_load_performance_curve = 14.14
        obj.coefficient_4_of_the_part_load_performance_curve = var_coefficient_4_of_the_part_load_performance_curve
        # real
        var_minimum_flow_rate_fraction = 0.5
        obj.minimum_flow_rate_fraction = var_minimum_flow_rate_fraction
        # alpha
        var_pump_control_type = "Continuous"
        obj.pump_control_type = var_pump_control_type
        # object-list
        var_pump_flow_rate_schedule_name = "object-list|Pump Flow Rate Schedule Name"
        obj.pump_flow_rate_schedule_name = var_pump_flow_rate_schedule_name
        # Object-list
        var_zone_name = "Object-list|Zone Name"
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
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].name, var_name)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].total_rated_flow_rate, var_total_rated_flow_rate)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].number_of_pumps_in_bank, var_number_of_pumps_in_bank)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].flow_sequencing_control_scheme, var_flow_sequencing_control_scheme)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].rated_pump_head, var_rated_pump_head)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].rated_power_consumption, var_rated_power_consumption)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].fraction_of_motor_inefficiencies_to_fluid_stream, var_fraction_of_motor_inefficiencies_to_fluid_stream)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].coefficient_1_of_the_part_load_performance_curve, var_coefficient_1_of_the_part_load_performance_curve)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].coefficient_2_of_the_part_load_performance_curve, var_coefficient_2_of_the_part_load_performance_curve)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].coefficient_3_of_the_part_load_performance_curve, var_coefficient_3_of_the_part_load_performance_curve)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].coefficient_4_of_the_part_load_performance_curve, var_coefficient_4_of_the_part_load_performance_curve)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].minimum_flow_rate_fraction, var_minimum_flow_rate_fraction)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].pump_control_type, var_pump_control_type)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].pump_flow_rate_schedule_name, var_pump_flow_rate_schedule_name)
        self.assertEqual(idf2.headeredpumpsvariablespeeds[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.headeredpumpsvariablespeeds[0].skin_loss_radiative_fraction, var_skin_loss_radiative_fraction)