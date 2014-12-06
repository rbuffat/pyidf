import os
import tempfile
import unittest
import pyidf
from pyidf.condenser_equipment_and_heat_exchangers import CoolingTowerPerformanceCoolTools
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoolingTowerPerformanceCoolTools(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coolingtowerperformancecooltools(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoolingTowerPerformanceCoolTools()
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
        var_coefficient_1 = 10.1
        obj.coefficient_1 = var_coefficient_1
        # real
        var_coefficient_2 = 11.11
        obj.coefficient_2 = var_coefficient_2
        # real
        var_coefficient_3 = 12.12
        obj.coefficient_3 = var_coefficient_3
        # real
        var_coefficient_4 = 13.13
        obj.coefficient_4 = var_coefficient_4
        # real
        var_coefficient_5 = 14.14
        obj.coefficient_5 = var_coefficient_5
        # real
        var_coefficient_6 = 15.15
        obj.coefficient_6 = var_coefficient_6
        # real
        var_coefficient_7 = 16.16
        obj.coefficient_7 = var_coefficient_7
        # real
        var_coefficient_8 = 17.17
        obj.coefficient_8 = var_coefficient_8
        # real
        var_coefficient_9 = 18.18
        obj.coefficient_9 = var_coefficient_9
        # real
        var_coefficient_10 = 19.19
        obj.coefficient_10 = var_coefficient_10
        # real
        var_coefficient_11 = 20.2
        obj.coefficient_11 = var_coefficient_11
        # real
        var_coefficient_12 = 21.21
        obj.coefficient_12 = var_coefficient_12
        # real
        var_coefficient_13 = 22.22
        obj.coefficient_13 = var_coefficient_13
        # real
        var_coefficient_14 = 23.23
        obj.coefficient_14 = var_coefficient_14
        # real
        var_coefficient_15 = 24.24
        obj.coefficient_15 = var_coefficient_15
        # real
        var_coefficient_16 = 25.25
        obj.coefficient_16 = var_coefficient_16
        # real
        var_coefficient_17 = 26.26
        obj.coefficient_17 = var_coefficient_17
        # real
        var_coefficient_18 = 27.27
        obj.coefficient_18 = var_coefficient_18
        # real
        var_coefficient_19 = 28.28
        obj.coefficient_19 = var_coefficient_19
        # real
        var_coefficient_20 = 29.29
        obj.coefficient_20 = var_coefficient_20
        # real
        var_coefficient_21 = 30.3
        obj.coefficient_21 = var_coefficient_21
        # real
        var_coefficient_22 = 31.31
        obj.coefficient_22 = var_coefficient_22
        # real
        var_coefficient_23 = 32.32
        obj.coefficient_23 = var_coefficient_23
        # real
        var_coefficient_24 = 33.33
        obj.coefficient_24 = var_coefficient_24
        # real
        var_coefficient_25 = 34.34
        obj.coefficient_25 = var_coefficient_25
        # real
        var_coefficient_26 = 35.35
        obj.coefficient_26 = var_coefficient_26
        # real
        var_coefficient_27 = 36.36
        obj.coefficient_27 = var_coefficient_27
        # real
        var_coefficient_28 = 37.37
        obj.coefficient_28 = var_coefficient_28
        # real
        var_coefficient_29 = 38.38
        obj.coefficient_29 = var_coefficient_29
        # real
        var_coefficient_30 = 39.39
        obj.coefficient_30 = var_coefficient_30
        # real
        var_coefficient_31 = 40.4
        obj.coefficient_31 = var_coefficient_31
        # real
        var_coefficient_32 = 41.41
        obj.coefficient_32 = var_coefficient_32
        # real
        var_coefficient_33 = 42.42
        obj.coefficient_33 = var_coefficient_33
        # real
        var_coefficient_34 = 43.43
        obj.coefficient_34 = var_coefficient_34
        # real
        var_coefficient_35 = 44.44
        obj.coefficient_35 = var_coefficient_35

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coolingtowerperformancecooltoolss[0].name, var_name)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].minimum_inlet_air_wetbulb_temperature, var_minimum_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].maximum_inlet_air_wetbulb_temperature, var_maximum_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].minimum_range_temperature, var_minimum_range_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].maximum_range_temperature, var_maximum_range_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].minimum_approach_temperature, var_minimum_approach_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].maximum_approach_temperature, var_maximum_approach_temperature)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].minimum_water_flow_rate_ratio, var_minimum_water_flow_rate_ratio)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].maximum_water_flow_rate_ratio, var_maximum_water_flow_rate_ratio)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_1, var_coefficient_1)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_2, var_coefficient_2)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_3, var_coefficient_3)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_4, var_coefficient_4)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_5, var_coefficient_5)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_6, var_coefficient_6)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_7, var_coefficient_7)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_8, var_coefficient_8)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_9, var_coefficient_9)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_10, var_coefficient_10)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_11, var_coefficient_11)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_12, var_coefficient_12)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_13, var_coefficient_13)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_14, var_coefficient_14)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_15, var_coefficient_15)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_16, var_coefficient_16)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_17, var_coefficient_17)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_18, var_coefficient_18)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_19, var_coefficient_19)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_20, var_coefficient_20)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_21, var_coefficient_21)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_22, var_coefficient_22)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_23, var_coefficient_23)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_24, var_coefficient_24)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_25, var_coefficient_25)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_26, var_coefficient_26)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_27, var_coefficient_27)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_28, var_coefficient_28)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_29, var_coefficient_29)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_30, var_coefficient_30)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_31, var_coefficient_31)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_32, var_coefficient_32)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_33, var_coefficient_33)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_34, var_coefficient_34)
        self.assertAlmostEqual(idf2.coolingtowerperformancecooltoolss[0].coefficient_35, var_coefficient_35)