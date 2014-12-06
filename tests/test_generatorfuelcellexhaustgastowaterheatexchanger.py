import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelCellExhaustGasToWaterHeatExchanger
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelCellExhaustGasToWaterHeatExchanger(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellexhaustgastowaterheatexchanger(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellExhaustGasToWaterHeatExchanger()
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
        var_heat_recovery_water_maximum_flow_rate = 4.4
        obj.heat_recovery_water_maximum_flow_rate = var_heat_recovery_water_maximum_flow_rate
        # node
        var_exhaust_outlet_air_node_name = "node|Exhaust Outlet Air Node Name"
        obj.exhaust_outlet_air_node_name = var_exhaust_outlet_air_node_name
        # alpha
        var_heat_exchanger_calculation_method = "FixedEffectiveness"
        obj.heat_exchanger_calculation_method = var_heat_exchanger_calculation_method
        # real
        var_method_1_heat_exchanger_effectiveness = 7.7
        obj.method_1_heat_exchanger_effectiveness = var_method_1_heat_exchanger_effectiveness
        # real
        var_method_2_parameter_hxs0 = 8.8
        obj.method_2_parameter_hxs0 = var_method_2_parameter_hxs0
        # real
        var_method_2_parameter_hxs1 = 9.9
        obj.method_2_parameter_hxs1 = var_method_2_parameter_hxs1
        # real
        var_method_2_parameter_hxs2 = 10.1
        obj.method_2_parameter_hxs2 = var_method_2_parameter_hxs2
        # real
        var_method_2_parameter_hxs3 = 11.11
        obj.method_2_parameter_hxs3 = var_method_2_parameter_hxs3
        # real
        var_method_2_parameter_hxs4 = 12.12
        obj.method_2_parameter_hxs4 = var_method_2_parameter_hxs4
        # real
        var_method_3_h0gas_coefficient = 13.13
        obj.method_3_h0gas_coefficient = var_method_3_h0gas_coefficient
        # real
        var_method_3_ndotgasref_coefficient = 14.14
        obj.method_3_ndotgasref_coefficient = var_method_3_ndotgasref_coefficient
        # real
        var_method_3_n_coefficient = 15.15
        obj.method_3_n_coefficient = var_method_3_n_coefficient
        # real
        var_method_3_gas_area = 16.16
        obj.method_3_gas_area = var_method_3_gas_area
        # real
        var_method_3_h0_water_coefficient = 17.17
        obj.method_3_h0_water_coefficient = var_method_3_h0_water_coefficient
        # real
        var_method_3_n_dot_water_ref_coefficient = 18.18
        obj.method_3_n_dot_water_ref_coefficient = var_method_3_n_dot_water_ref_coefficient
        # real
        var_method_3_m_coefficient = 19.19
        obj.method_3_m_coefficient = var_method_3_m_coefficient
        # real
        var_method_3_water_area = 20.2
        obj.method_3_water_area = var_method_3_water_area
        # real
        var_method_3_f_adjustment_factor = 21.21
        obj.method_3_f_adjustment_factor = var_method_3_f_adjustment_factor
        # real
        var_method_4_hxl1_coefficient = 22.22
        obj.method_4_hxl1_coefficient = var_method_4_hxl1_coefficient
        # real
        var_method_4_hxl2_coefficient = 23.23
        obj.method_4_hxl2_coefficient = var_method_4_hxl2_coefficient
        # real
        var_method_4_condensation_threshold = 24.24
        obj.method_4_condensation_threshold = var_method_4_condensation_threshold

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].heat_recovery_water_inlet_node_name, var_heat_recovery_water_inlet_node_name)
        self.assertEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].heat_recovery_water_outlet_node_name, var_heat_recovery_water_outlet_node_name)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].heat_recovery_water_maximum_flow_rate, var_heat_recovery_water_maximum_flow_rate)
        self.assertEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].exhaust_outlet_air_node_name, var_exhaust_outlet_air_node_name)
        self.assertEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].heat_exchanger_calculation_method, var_heat_exchanger_calculation_method)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_1_heat_exchanger_effectiveness, var_method_1_heat_exchanger_effectiveness)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_2_parameter_hxs0, var_method_2_parameter_hxs0)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_2_parameter_hxs1, var_method_2_parameter_hxs1)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_2_parameter_hxs2, var_method_2_parameter_hxs2)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_2_parameter_hxs3, var_method_2_parameter_hxs3)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_2_parameter_hxs4, var_method_2_parameter_hxs4)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_h0gas_coefficient, var_method_3_h0gas_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_ndotgasref_coefficient, var_method_3_ndotgasref_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_n_coefficient, var_method_3_n_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_gas_area, var_method_3_gas_area)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_h0_water_coefficient, var_method_3_h0_water_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_n_dot_water_ref_coefficient, var_method_3_n_dot_water_ref_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_m_coefficient, var_method_3_m_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_water_area, var_method_3_water_area)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_3_f_adjustment_factor, var_method_3_f_adjustment_factor)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_4_hxl1_coefficient, var_method_4_hxl1_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_4_hxl2_coefficient, var_method_4_hxl2_coefficient)
        self.assertAlmostEqual(idf2.generatorfuelcellexhaustgastowaterheatexchangers[0].method_4_condensation_threshold, var_method_4_condensation_threshold)