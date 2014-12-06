import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorFuelCellPowerModule

log = logging.getLogger(__name__)

class TestGeneratorFuelCellPowerModule(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellpowermodule(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellPowerModule()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_efficiency_curve_mode = "Annex42"
        obj.efficiency_curve_mode = var_efficiency_curve_mode
        # object-list
        var_efficiency_curve_name = "object-list|Efficiency Curve Name"
        obj.efficiency_curve_name = var_efficiency_curve_name
        # real
        var_nominal_efficiency = 4.4
        obj.nominal_efficiency = var_nominal_efficiency
        # real
        var_nominal_electrical_power = 5.5
        obj.nominal_electrical_power = var_nominal_electrical_power
        # real
        var_number_of_stops_at_start_of_simulation = 6.6
        obj.number_of_stops_at_start_of_simulation = var_number_of_stops_at_start_of_simulation
        # real
        var_cycling_performance_degradation_coefficient = 7.7
        obj.cycling_performance_degradation_coefficient = var_cycling_performance_degradation_coefficient
        # real
        var_number_of_run_hours_at_beginning_of_simulation = 8.8
        obj.number_of_run_hours_at_beginning_of_simulation = var_number_of_run_hours_at_beginning_of_simulation
        # real
        var_accumulated_run_time_degradation_coefficient = 9.9
        obj.accumulated_run_time_degradation_coefficient = var_accumulated_run_time_degradation_coefficient
        # real
        var_run_time_degradation_initiation_time_threshold = 10.1
        obj.run_time_degradation_initiation_time_threshold = var_run_time_degradation_initiation_time_threshold
        # real
        var_power_up_transient_limit = 11.11
        obj.power_up_transient_limit = var_power_up_transient_limit
        # real
        var_power_down_transient_limit = 12.12
        obj.power_down_transient_limit = var_power_down_transient_limit
        # real
        var_start_up_time = 13.13
        obj.start_up_time = var_start_up_time
        # real
        var_start_up_fuel = 14.14
        obj.start_up_fuel = var_start_up_fuel
        # real
        var_start_up_electricity_consumption = 15.15
        obj.start_up_electricity_consumption = var_start_up_electricity_consumption
        # real
        var_start_up_electricity_produced = 16.16
        obj.start_up_electricity_produced = var_start_up_electricity_produced
        # real
        var_shut_down_time = 17.17
        obj.shut_down_time = var_shut_down_time
        # real
        var_shut_down_fuel = 18.18
        obj.shut_down_fuel = var_shut_down_fuel
        # real
        var_shut_down_electricity_consumption = 19.19
        obj.shut_down_electricity_consumption = var_shut_down_electricity_consumption
        # real
        var_ancilliary_electricity_constant_term = 20.2
        obj.ancilliary_electricity_constant_term = var_ancilliary_electricity_constant_term
        # real
        var_ancilliary_electricity_linear_term = 21.21
        obj.ancilliary_electricity_linear_term = var_ancilliary_electricity_linear_term
        # alpha
        var_skin_loss_calculation_mode = "ConstantRate"
        obj.skin_loss_calculation_mode = var_skin_loss_calculation_mode
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_skin_loss_radiative_fraction = 0.5
        obj.skin_loss_radiative_fraction = var_skin_loss_radiative_fraction
        # real
        var_constant_skin_loss_rate = 25.25
        obj.constant_skin_loss_rate = var_constant_skin_loss_rate
        # real
        var_skin_loss_ufactor_times_area_term = 26.26
        obj.skin_loss_ufactor_times_area_term = var_skin_loss_ufactor_times_area_term
        # object-list
        var_skin_loss_quadratic_curve_name = "object-list|Skin Loss Quadratic Curve Name"
        obj.skin_loss_quadratic_curve_name = var_skin_loss_quadratic_curve_name
        # real
        var_dilution_air_flow_rate = 28.28
        obj.dilution_air_flow_rate = var_dilution_air_flow_rate
        # real
        var_stack_heat_loss_to_dilution_air = 29.29
        obj.stack_heat_loss_to_dilution_air = var_stack_heat_loss_to_dilution_air
        # node
        var_dilution_inlet_air_node_name = "node|Dilution Inlet Air Node Name"
        obj.dilution_inlet_air_node_name = var_dilution_inlet_air_node_name
        # node
        var_dilution_outlet_air_node_name = "node|Dilution Outlet Air Node Name"
        obj.dilution_outlet_air_node_name = var_dilution_outlet_air_node_name
        # real
        var_minimum_operating_point = 32.32
        obj.minimum_operating_point = var_minimum_operating_point
        # real
        var_maximum_operating_point = 33.33
        obj.maximum_operating_point = var_maximum_operating_point

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].efficiency_curve_mode, var_efficiency_curve_mode)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].efficiency_curve_name, var_efficiency_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].nominal_efficiency, var_nominal_efficiency)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].nominal_electrical_power, var_nominal_electrical_power)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].number_of_stops_at_start_of_simulation, var_number_of_stops_at_start_of_simulation)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].cycling_performance_degradation_coefficient, var_cycling_performance_degradation_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].number_of_run_hours_at_beginning_of_simulation, var_number_of_run_hours_at_beginning_of_simulation)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].accumulated_run_time_degradation_coefficient, var_accumulated_run_time_degradation_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].run_time_degradation_initiation_time_threshold, var_run_time_degradation_initiation_time_threshold)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].power_up_transient_limit, var_power_up_transient_limit)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].power_down_transient_limit, var_power_down_transient_limit)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].start_up_time, var_start_up_time)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].start_up_fuel, var_start_up_fuel)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].start_up_electricity_consumption, var_start_up_electricity_consumption)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].start_up_electricity_produced, var_start_up_electricity_produced)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].shut_down_time, var_shut_down_time)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].shut_down_fuel, var_shut_down_fuel)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].shut_down_electricity_consumption, var_shut_down_electricity_consumption)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].ancilliary_electricity_constant_term, var_ancilliary_electricity_constant_term)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].ancilliary_electricity_linear_term, var_ancilliary_electricity_linear_term)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].skin_loss_calculation_mode, var_skin_loss_calculation_mode)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].skin_loss_radiative_fraction, var_skin_loss_radiative_fraction)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].constant_skin_loss_rate, var_constant_skin_loss_rate)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].skin_loss_ufactor_times_area_term, var_skin_loss_ufactor_times_area_term)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].skin_loss_quadratic_curve_name, var_skin_loss_quadratic_curve_name)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].dilution_air_flow_rate, var_dilution_air_flow_rate)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].stack_heat_loss_to_dilution_air, var_stack_heat_loss_to_dilution_air)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].dilution_inlet_air_node_name, var_dilution_inlet_air_node_name)
        self.assertEqual(idf2.generatorfuelcellpowermodules[0].dilution_outlet_air_node_name, var_dilution_outlet_air_node_name)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].minimum_operating_point, var_minimum_operating_point)
        self.assertAlmostEqual(idf2.generatorfuelcellpowermodules[0].maximum_operating_point, var_maximum_operating_point)