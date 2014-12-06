import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorFuelCellStackCooler

log = logging.getLogger(__name__)

class TestGeneratorFuelCellStackCooler(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellstackcooler(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellStackCooler()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_heat_recovery_water_inlet_node_name = "node|Heat Recovery Water Inlet Node Name"
        obj.heat_recovery_water_inlet_node_name = var_heat_recovery_water_inlet_node_name
        # node
        var_heat_recovery_water_outlet_node_name = "node|Heat Recovery Water Outlet Node Name"
        obj.heat_recovery_water_outlet_node_name = var_heat_recovery_water_outlet_node_name
        # real
        var_nominal_stack_temperature = 4.4
        obj.nominal_stack_temperature = var_nominal_stack_temperature
        # real
        var_actual_stack_temperature = 5.5
        obj.actual_stack_temperature = var_actual_stack_temperature
        # real
        var_coefficient_r0 = 6.6
        obj.coefficient_r0 = var_coefficient_r0
        # real
        var_coefficient_r1 = 7.7
        obj.coefficient_r1 = var_coefficient_r1
        # real
        var_coefficient_r2 = 8.8
        obj.coefficient_r2 = var_coefficient_r2
        # real
        var_coefficient_r3 = 9.9
        obj.coefficient_r3 = var_coefficient_r3
        # real
        var_stack_coolant_flow_rate = 10.1
        obj.stack_coolant_flow_rate = var_stack_coolant_flow_rate
        # real
        var_stack_cooler_ufactor_times_area_value = 11.11
        obj.stack_cooler_ufactor_times_area_value = var_stack_cooler_ufactor_times_area_value
        # real
        var_fscogen_adjustment_factor = 12.12
        obj.fscogen_adjustment_factor = var_fscogen_adjustment_factor
        # real
        var_stack_cogeneration_exchanger_area = 13.13
        obj.stack_cogeneration_exchanger_area = var_stack_cogeneration_exchanger_area
        # real
        var_stack_cogeneration_exchanger_nominal_flow_rate = 14.14
        obj.stack_cogeneration_exchanger_nominal_flow_rate = var_stack_cogeneration_exchanger_nominal_flow_rate
        # real
        var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient = 15.15
        obj.stack_cogeneration_exchanger_nominal_heat_transfer_coefficient = var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient
        # real
        var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent = 16.16
        obj.stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent = var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent
        # real
        var_stack_cooler_pump_power = 17.17
        obj.stack_cooler_pump_power = var_stack_cooler_pump_power
        # real
        var_stack_cooler_pump_heat_loss_fraction = 0.5
        obj.stack_cooler_pump_heat_loss_fraction = var_stack_cooler_pump_heat_loss_fraction
        # real
        var_stack_air_cooler_fan_coefficient_f0 = 19.19
        obj.stack_air_cooler_fan_coefficient_f0 = var_stack_air_cooler_fan_coefficient_f0
        # real
        var_stack_air_cooler_fan_coefficient_f1 = 20.2
        obj.stack_air_cooler_fan_coefficient_f1 = var_stack_air_cooler_fan_coefficient_f1
        # real
        var_stack_air_cooler_fan_coefficient_f2 = 21.21
        obj.stack_air_cooler_fan_coefficient_f2 = var_stack_air_cooler_fan_coefficient_f2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellstackcoolers[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellstackcoolers[0].heat_recovery_water_inlet_node_name, var_heat_recovery_water_inlet_node_name)
        self.assertEqual(idf2.generatorfuelcellstackcoolers[0].heat_recovery_water_outlet_node_name, var_heat_recovery_water_outlet_node_name)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].nominal_stack_temperature, var_nominal_stack_temperature)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].actual_stack_temperature, var_actual_stack_temperature)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].coefficient_r0, var_coefficient_r0)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].coefficient_r1, var_coefficient_r1)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].coefficient_r2, var_coefficient_r2)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].coefficient_r3, var_coefficient_r3)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_coolant_flow_rate, var_stack_coolant_flow_rate)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cooler_ufactor_times_area_value, var_stack_cooler_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].fscogen_adjustment_factor, var_fscogen_adjustment_factor)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cogeneration_exchanger_area, var_stack_cogeneration_exchanger_area)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cogeneration_exchanger_nominal_flow_rate, var_stack_cogeneration_exchanger_nominal_flow_rate)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cogeneration_exchanger_nominal_heat_transfer_coefficient, var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent, var_stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cooler_pump_power, var_stack_cooler_pump_power)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_cooler_pump_heat_loss_fraction, var_stack_cooler_pump_heat_loss_fraction)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_air_cooler_fan_coefficient_f0, var_stack_air_cooler_fan_coefficient_f0)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_air_cooler_fan_coefficient_f1, var_stack_air_cooler_fan_coefficient_f1)
        self.assertAlmostEqual(idf2.generatorfuelcellstackcoolers[0].stack_air_cooler_fan_coefficient_f2, var_stack_air_cooler_fan_coefficient_f2)