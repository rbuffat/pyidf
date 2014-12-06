import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.heat_recovery import HeatExchangerDesiccantBalancedFlowPerformanceDataType1

log = logging.getLogger(__name__)

class TestHeatExchangerDesiccantBalancedFlowPerformanceDataType1(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatexchangerdesiccantbalancedflowperformancedatatype1(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatExchangerDesiccantBalancedFlowPerformanceDataType1()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_nominal_air_flow_rate = 0.0001
        obj.nominal_air_flow_rate = var_nominal_air_flow_rate
        # real
        var_nominal_air_face_velocity = 3.00005
        obj.nominal_air_face_velocity = var_nominal_air_face_velocity
        # real
        var_nominal_electric_power = 0.0
        obj.nominal_electric_power = var_nominal_electric_power
        # real
        var_temperature_equation_coefficient_1 = 5.5
        obj.temperature_equation_coefficient_1 = var_temperature_equation_coefficient_1
        # real
        var_temperature_equation_coefficient_2 = 6.6
        obj.temperature_equation_coefficient_2 = var_temperature_equation_coefficient_2
        # real
        var_temperature_equation_coefficient_3 = 7.7
        obj.temperature_equation_coefficient_3 = var_temperature_equation_coefficient_3
        # real
        var_temperature_equation_coefficient_4 = 8.8
        obj.temperature_equation_coefficient_4 = var_temperature_equation_coefficient_4
        # real
        var_temperature_equation_coefficient_5 = 9.9
        obj.temperature_equation_coefficient_5 = var_temperature_equation_coefficient_5
        # real
        var_temperature_equation_coefficient_6 = 10.1
        obj.temperature_equation_coefficient_6 = var_temperature_equation_coefficient_6
        # real
        var_temperature_equation_coefficient_7 = 11.11
        obj.temperature_equation_coefficient_7 = var_temperature_equation_coefficient_7
        # real
        var_temperature_equation_coefficient_8 = 12.12
        obj.temperature_equation_coefficient_8 = var_temperature_equation_coefficient_8
        # real
        var_minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = 0.5
        obj.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = var_minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation
        # real
        var_maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = 0.5
        obj.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = var_maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation
        # real
        var_minimum_regeneration_inlet_air_temperature_for_temperature_equation = 15.15
        obj.minimum_regeneration_inlet_air_temperature_for_temperature_equation = var_minimum_regeneration_inlet_air_temperature_for_temperature_equation
        # real
        var_maximum_regeneration_inlet_air_temperature_for_temperature_equation = 16.16
        obj.maximum_regeneration_inlet_air_temperature_for_temperature_equation = var_maximum_regeneration_inlet_air_temperature_for_temperature_equation
        # real
        var_minimum_process_inlet_air_humidity_ratio_for_temperature_equation = 0.5
        obj.minimum_process_inlet_air_humidity_ratio_for_temperature_equation = var_minimum_process_inlet_air_humidity_ratio_for_temperature_equation
        # real
        var_maximum_process_inlet_air_humidity_ratio_for_temperature_equation = 0.5
        obj.maximum_process_inlet_air_humidity_ratio_for_temperature_equation = var_maximum_process_inlet_air_humidity_ratio_for_temperature_equation
        # real
        var_minimum_process_inlet_air_temperature_for_temperature_equation = 19.19
        obj.minimum_process_inlet_air_temperature_for_temperature_equation = var_minimum_process_inlet_air_temperature_for_temperature_equation
        # real
        var_maximum_process_inlet_air_temperature_for_temperature_equation = 20.2
        obj.maximum_process_inlet_air_temperature_for_temperature_equation = var_maximum_process_inlet_air_temperature_for_temperature_equation
        # real
        var_minimum_regeneration_air_velocity_for_temperature_equation = 0.0001
        obj.minimum_regeneration_air_velocity_for_temperature_equation = var_minimum_regeneration_air_velocity_for_temperature_equation
        # real
        var_maximum_regeneration_air_velocity_for_temperature_equation = 0.0001
        obj.maximum_regeneration_air_velocity_for_temperature_equation = var_maximum_regeneration_air_velocity_for_temperature_equation
        # real
        var_minimum_regeneration_outlet_air_temperature_for_temperature_equation = 23.23
        obj.minimum_regeneration_outlet_air_temperature_for_temperature_equation = var_minimum_regeneration_outlet_air_temperature_for_temperature_equation
        # real
        var_maximum_regeneration_outlet_air_temperature_for_temperature_equation = 24.24
        obj.maximum_regeneration_outlet_air_temperature_for_temperature_equation = var_maximum_regeneration_outlet_air_temperature_for_temperature_equation
        # real
        var_minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = 50.0
        obj.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = var_minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation
        # real
        var_maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = 50.0
        obj.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = var_maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation
        # real
        var_minimum_process_inlet_air_relative_humidity_for_temperature_equation = 50.0
        obj.minimum_process_inlet_air_relative_humidity_for_temperature_equation = var_minimum_process_inlet_air_relative_humidity_for_temperature_equation
        # real
        var_maximum_process_inlet_air_relative_humidity_for_temperature_equation = 50.0
        obj.maximum_process_inlet_air_relative_humidity_for_temperature_equation = var_maximum_process_inlet_air_relative_humidity_for_temperature_equation
        # real
        var_humidity_ratio_equation_coefficient_1 = 29.29
        obj.humidity_ratio_equation_coefficient_1 = var_humidity_ratio_equation_coefficient_1
        # real
        var_humidity_ratio_equation_coefficient_2 = 30.3
        obj.humidity_ratio_equation_coefficient_2 = var_humidity_ratio_equation_coefficient_2
        # real
        var_humidity_ratio_equation_coefficient_3 = 31.31
        obj.humidity_ratio_equation_coefficient_3 = var_humidity_ratio_equation_coefficient_3
        # real
        var_humidity_ratio_equation_coefficient_4 = 32.32
        obj.humidity_ratio_equation_coefficient_4 = var_humidity_ratio_equation_coefficient_4
        # real
        var_humidity_ratio_equation_coefficient_5 = 33.33
        obj.humidity_ratio_equation_coefficient_5 = var_humidity_ratio_equation_coefficient_5
        # real
        var_humidity_ratio_equation_coefficient_6 = 34.34
        obj.humidity_ratio_equation_coefficient_6 = var_humidity_ratio_equation_coefficient_6
        # real
        var_humidity_ratio_equation_coefficient_7 = 35.35
        obj.humidity_ratio_equation_coefficient_7 = var_humidity_ratio_equation_coefficient_7
        # real
        var_humidity_ratio_equation_coefficient_8 = 36.36
        obj.humidity_ratio_equation_coefficient_8 = var_humidity_ratio_equation_coefficient_8
        # real
        var_minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = var_minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = var_maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = 39.39
        obj.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = var_minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation
        # real
        var_maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = 40.4
        obj.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = var_maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation
        # real
        var_minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = var_minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = var_maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_minimum_process_inlet_air_temperature_for_humidity_ratio_equation = 43.43
        obj.minimum_process_inlet_air_temperature_for_humidity_ratio_equation = var_minimum_process_inlet_air_temperature_for_humidity_ratio_equation
        # real
        var_maximum_process_inlet_air_temperature_for_humidity_ratio_equation = 44.44
        obj.maximum_process_inlet_air_temperature_for_humidity_ratio_equation = var_maximum_process_inlet_air_temperature_for_humidity_ratio_equation
        # real
        var_minimum_regeneration_air_velocity_for_humidity_ratio_equation = 0.0001
        obj.minimum_regeneration_air_velocity_for_humidity_ratio_equation = var_minimum_regeneration_air_velocity_for_humidity_ratio_equation
        # real
        var_maximum_regeneration_air_velocity_for_humidity_ratio_equation = 0.0001
        obj.maximum_regeneration_air_velocity_for_humidity_ratio_equation = var_maximum_regeneration_air_velocity_for_humidity_ratio_equation
        # real
        var_minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = var_minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = 0.5
        obj.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = var_maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation
        # real
        var_minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = 50.0
        obj.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = var_minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation
        # real
        var_maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = 50.0
        obj.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = var_maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation
        # real
        var_minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = 50.0
        obj.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = var_minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation
        # real
        var_maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = 50.0
        obj.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = var_maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].name, var_name)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].nominal_air_flow_rate, var_nominal_air_flow_rate)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].nominal_air_face_velocity, var_nominal_air_face_velocity)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].nominal_electric_power, var_nominal_electric_power)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_1, var_temperature_equation_coefficient_1)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_2, var_temperature_equation_coefficient_2)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_3, var_temperature_equation_coefficient_3)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_4, var_temperature_equation_coefficient_4)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_5, var_temperature_equation_coefficient_5)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_6, var_temperature_equation_coefficient_6)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_7, var_temperature_equation_coefficient_7)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].temperature_equation_coefficient_8, var_temperature_equation_coefficient_8)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation, var_minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation, var_maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_temperature_for_temperature_equation, var_minimum_regeneration_inlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_temperature_for_temperature_equation, var_maximum_regeneration_inlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_humidity_ratio_for_temperature_equation, var_minimum_process_inlet_air_humidity_ratio_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_humidity_ratio_for_temperature_equation, var_maximum_process_inlet_air_humidity_ratio_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_temperature_for_temperature_equation, var_minimum_process_inlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_temperature_for_temperature_equation, var_maximum_process_inlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_air_velocity_for_temperature_equation, var_minimum_regeneration_air_velocity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_air_velocity_for_temperature_equation, var_maximum_regeneration_air_velocity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_outlet_air_temperature_for_temperature_equation, var_minimum_regeneration_outlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_outlet_air_temperature_for_temperature_equation, var_maximum_regeneration_outlet_air_temperature_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation, var_minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation, var_maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_relative_humidity_for_temperature_equation, var_minimum_process_inlet_air_relative_humidity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_relative_humidity_for_temperature_equation, var_maximum_process_inlet_air_relative_humidity_for_temperature_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_1, var_humidity_ratio_equation_coefficient_1)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_2, var_humidity_ratio_equation_coefficient_2)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_3, var_humidity_ratio_equation_coefficient_3)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_4, var_humidity_ratio_equation_coefficient_4)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_5, var_humidity_ratio_equation_coefficient_5)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_6, var_humidity_ratio_equation_coefficient_6)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_7, var_humidity_ratio_equation_coefficient_7)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].humidity_ratio_equation_coefficient_8, var_humidity_ratio_equation_coefficient_8)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation, var_minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation, var_maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation, var_minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation, var_maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation, var_minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation, var_maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_temperature_for_humidity_ratio_equation, var_minimum_process_inlet_air_temperature_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_temperature_for_humidity_ratio_equation, var_maximum_process_inlet_air_temperature_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_air_velocity_for_humidity_ratio_equation, var_minimum_regeneration_air_velocity_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_air_velocity_for_humidity_ratio_equation, var_maximum_regeneration_air_velocity_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation, var_minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation, var_maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation, var_minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation, var_maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation, var_minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation)
        self.assertAlmostEqual(idf2.heatexchangerdesiccantbalancedflowperformancedatatype1s[0].maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation, var_maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation)