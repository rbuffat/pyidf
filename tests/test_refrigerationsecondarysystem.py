import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationSecondarySystem

log = logging.getLogger(__name__)

class TestRefrigerationSecondarySystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationsecondarysystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationSecondarySystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_refrigerated_case_or_walkin_or_caseandwalkinlist_name = "object-list|Refrigerated Case or Walkin or CaseAndWalkInList Name"
        obj.refrigerated_case_or_walkin_or_caseandwalkinlist_name = var_refrigerated_case_or_walkin_or_caseandwalkinlist_name
        # alpha
        var_circulating_fluid_type = "FluidAlwaysLiquid"
        obj.circulating_fluid_type = var_circulating_fluid_type
        # object-list
        var_circulating_fluid_name = "object-list|Circulating Fluid Name"
        obj.circulating_fluid_name = var_circulating_fluid_name
        # real
        var_evaporator_capacity = 0.0
        obj.evaporator_capacity = var_evaporator_capacity
        # real
        var_evaporator_flow_rate_for_secondary_fluid = 0.0
        obj.evaporator_flow_rate_for_secondary_fluid = var_evaporator_flow_rate_for_secondary_fluid
        # real
        var_evaporator_evaporating_temperature = 7.7
        obj.evaporator_evaporating_temperature = var_evaporator_evaporating_temperature
        # real
        var_evaporator_approach_temperature_difference = 8.8
        obj.evaporator_approach_temperature_difference = var_evaporator_approach_temperature_difference
        # real
        var_evaporator_range_temperature_difference = 9.9
        obj.evaporator_range_temperature_difference = var_evaporator_range_temperature_difference
        # integer
        var_number_of_pumps_in_loop = 10
        obj.number_of_pumps_in_loop = var_number_of_pumps_in_loop
        # real
        var_total_pump_flow_rate = 0.0
        obj.total_pump_flow_rate = var_total_pump_flow_rate
        # real
        var_total_pump_power = 0.0
        obj.total_pump_power = var_total_pump_power
        # real
        var_total_pump_head = 0.0
        obj.total_pump_head = var_total_pump_head
        # real
        var_phasechange_circulating_rate = 1.0
        obj.phasechange_circulating_rate = var_phasechange_circulating_rate
        # alpha
        var_pump_drive_type = "Constant"
        obj.pump_drive_type = var_pump_drive_type
        # object-list
        var_variable_speed_pump_cubic_curve_name = "object-list|Variable Speed Pump Cubic Curve Name"
        obj.variable_speed_pump_cubic_curve_name = var_variable_speed_pump_cubic_curve_name
        # real
        var_pump_motor_heat_to_fluid = 0.75
        obj.pump_motor_heat_to_fluid = var_pump_motor_heat_to_fluid
        # real
        var_sum_ua_distribution_piping = 18.18
        obj.sum_ua_distribution_piping = var_sum_ua_distribution_piping
        # object-list
        var_distribution_piping_zone_name = "object-list|Distribution Piping Zone Name"
        obj.distribution_piping_zone_name = var_distribution_piping_zone_name
        # real
        var_sum_ua_receiver_or_separator_shell = 20.2
        obj.sum_ua_receiver_or_separator_shell = var_sum_ua_receiver_or_separator_shell
        # object-list
        var_receiver_or_separator_zone_name = "object-list|Receiver/Separator Zone Name"
        obj.receiver_or_separator_zone_name = var_receiver_or_separator_zone_name
        # real
        var_evaporator_refrigerant_inventory = 22.22
        obj.evaporator_refrigerant_inventory = var_evaporator_refrigerant_inventory
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].name, var_name)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].refrigerated_case_or_walkin_or_caseandwalkinlist_name, var_refrigerated_case_or_walkin_or_caseandwalkinlist_name)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].circulating_fluid_type, var_circulating_fluid_type)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].circulating_fluid_name, var_circulating_fluid_name)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_capacity, var_evaporator_capacity)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_flow_rate_for_secondary_fluid, var_evaporator_flow_rate_for_secondary_fluid)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_evaporating_temperature, var_evaporator_evaporating_temperature)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_approach_temperature_difference, var_evaporator_approach_temperature_difference)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_range_temperature_difference, var_evaporator_range_temperature_difference)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].number_of_pumps_in_loop, var_number_of_pumps_in_loop)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].total_pump_flow_rate, var_total_pump_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].total_pump_power, var_total_pump_power)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].total_pump_head, var_total_pump_head)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].phasechange_circulating_rate, var_phasechange_circulating_rate)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].pump_drive_type, var_pump_drive_type)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].variable_speed_pump_cubic_curve_name, var_variable_speed_pump_cubic_curve_name)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].pump_motor_heat_to_fluid, var_pump_motor_heat_to_fluid)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].sum_ua_distribution_piping, var_sum_ua_distribution_piping)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].distribution_piping_zone_name, var_distribution_piping_zone_name)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].sum_ua_receiver_or_separator_shell, var_sum_ua_receiver_or_separator_shell)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].receiver_or_separator_zone_name, var_receiver_or_separator_zone_name)
        self.assertAlmostEqual(idf2.refrigerationsecondarysystems[0].evaporator_refrigerant_inventory, var_evaporator_refrigerant_inventory)
        self.assertEqual(idf2.refrigerationsecondarysystems[0].enduse_subcategory, var_enduse_subcategory)