import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import CoolingTowerPerformanceYorkCalc

log = logging.getLogger(__name__)

class TestCoolingTowerPerformanceYorkCalc(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coolingtowerperformanceyorkcalc(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoolingTowerPerformanceYorkCalc()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_minimum_inlet_air_wetbulb_temperature = 2.2
        obj.minimum_inlet_air_wetbulb_temperature = var_minimum_inlet_air_wetbulb_temperature
        # real
        var_maximum_inlet_air_wetbulb_temperature = 3.3
        obj.maximum_inlet_air_wetbulb_temperature = var_maximum_inlet_air_wetbulb_temperature
        # real
        var_minimum_range_temperature = 4.4
        obj.minimum_range_temperature = var_minimum_range_temperature
        # real
        var_maximum_range_temperature = 5.5
        obj.maximum_range_temperature = var_maximum_range_temperature
        # real
        var_minimum_approach_temperature = 6.6
        obj.minimum_approach_temperature = var_minimum_approach_temperature
        # real
        var_maximum_approach_temperature = 7.7
        obj.maximum_approach_temperature = var_maximum_approach_temperature
        # real
        var_minimum_water_flow_rate_ratio = 8.8
        obj.minimum_water_flow_rate_ratio = var_minimum_water_flow_rate_ratio
        # real
        var_maximum_water_flow_rate_ratio = 9.9
        obj.maximum_water_flow_rate_ratio = var_maximum_water_flow_rate_ratio
        # real
        var_maximum_liquid_to_gas_ratio = 10.1
        obj.maximum_liquid_to_gas_ratio = var_maximum_liquid_to_gas_ratio
        # real
        var_coefficient_1 = 11.11
        obj.coefficient_1 = var_coefficient_1
        # real
        var_coefficient_2 = 12.12
        obj.coefficient_2 = var_coefficient_2
        # real
        var_coefficient_3 = 13.13
        obj.coefficient_3 = var_coefficient_3
        # real
        var_coefficient_4 = 14.14
        obj.coefficient_4 = var_coefficient_4
        # real
        var_coefficient_5 = 15.15
        obj.coefficient_5 = var_coefficient_5
        # real
        var_coefficient_6 = 16.16
        obj.coefficient_6 = var_coefficient_6
        # real
        var_coefficient_7 = 17.17
        obj.coefficient_7 = var_coefficient_7
        # real
        var_coefficient_8 = 18.18
        obj.coefficient_8 = var_coefficient_8
        # real
        var_coefficient_9 = 19.19
        obj.coefficient_9 = var_coefficient_9
        # real
        var_coefficient_10 = 20.2
        obj.coefficient_10 = var_coefficient_10
        # real
        var_coefficient_11 = 21.21
        obj.coefficient_11 = var_coefficient_11
        # real
        var_coefficient_12 = 22.22
        obj.coefficient_12 = var_coefficient_12
        # real
        var_coefficient_13 = 23.23
        obj.coefficient_13 = var_coefficient_13
        # real
        var_coefficient_14 = 24.24
        obj.coefficient_14 = var_coefficient_14
        # real
        var_coefficient_15 = 25.25
        obj.coefficient_15 = var_coefficient_15
        # real
        var_coefficient_16 = 26.26
        obj.coefficient_16 = var_coefficient_16
        # real
        var_coefficient_17 = 27.27
        obj.coefficient_17 = var_coefficient_17
        # real
        var_coefficient_18 = 28.28
        obj.coefficient_18 = var_coefficient_18
        # real
        var_coefficient_19 = 29.29
        obj.coefficient_19 = var_coefficient_19
        # real
        var_coefficient_20 = 30.3
        obj.coefficient_20 = var_coefficient_20
        # real
        var_coefficient_21 = 31.31
        obj.coefficient_21 = var_coefficient_21
        # real
        var_coefficient_22 = 32.32
        obj.coefficient_22 = var_coefficient_22
        # real
        var_coefficient_23 = 33.33
        obj.coefficient_23 = var_coefficient_23
        # real
        var_coefficient_24 = 34.34
        obj.coefficient_24 = var_coefficient_24
        # real
        var_coefficient_25 = 35.35
        obj.coefficient_25 = var_coefficient_25
        # real
        var_coefficient_26 = 36.36
        obj.coefficient_26 = var_coefficient_26
        # real
        var_coefficient_27 = 37.37
        obj.coefficient_27 = var_coefficient_27

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coolingtowerperformanceyorkcalcs[0].name, var_name)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].minimum_inlet_air_wetbulb_temperature, var_minimum_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].maximum_inlet_air_wetbulb_temperature, var_maximum_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].minimum_range_temperature, var_minimum_range_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].maximum_range_temperature, var_maximum_range_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].minimum_approach_temperature, var_minimum_approach_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].maximum_approach_temperature, var_maximum_approach_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].minimum_water_flow_rate_ratio, var_minimum_water_flow_rate_ratio)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].maximum_water_flow_rate_ratio, var_maximum_water_flow_rate_ratio)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].maximum_liquid_to_gas_ratio, var_maximum_liquid_to_gas_ratio)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_1, var_coefficient_1)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_2, var_coefficient_2)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_3, var_coefficient_3)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_4, var_coefficient_4)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_5, var_coefficient_5)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_6, var_coefficient_6)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_7, var_coefficient_7)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_8, var_coefficient_8)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_9, var_coefficient_9)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_10, var_coefficient_10)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_11, var_coefficient_11)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_12, var_coefficient_12)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_13, var_coefficient_13)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_14, var_coefficient_14)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_15, var_coefficient_15)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_16, var_coefficient_16)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_17, var_coefficient_17)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_18, var_coefficient_18)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_19, var_coefficient_19)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_20, var_coefficient_20)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_21, var_coefficient_21)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_22, var_coefficient_22)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_23, var_coefficient_23)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_24, var_coefficient_24)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_25, var_coefficient_25)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_26, var_coefficient_26)
        self.assertAlmostEqual(idf2.coolingtowerperformanceyorkcalcs[0].coefficient_27, var_coefficient_27)