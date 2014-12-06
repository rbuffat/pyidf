import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneThermalChimney

log = logging.getLogger(__name__)

class TestZoneThermalChimney(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonethermalchimney(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneThermalChimney()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_width_of_the_absorber_wall = 0.0
        obj.width_of_the_absorber_wall = var_width_of_the_absorber_wall
        # real
        var_cross_sectional_area_of_air_channel_outlet = 0.0
        obj.cross_sectional_area_of_air_channel_outlet = var_cross_sectional_area_of_air_channel_outlet
        # real
        var_discharge_coefficient = 0.5
        obj.discharge_coefficient = var_discharge_coefficient
        # object-list
        var_zone_1_name = "object-list|Zone 1 Name"
        obj.zone_1_name = var_zone_1_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_1 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_1 = var_distance_from_top_of_thermal_chimney_to_inlet_1
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_1 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_1 = var_relative_ratios_of_air_flow_rates_passing_through_zone_1
        # real
        var_cross_sectional_areas_of_air_channel_inlet_1 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_1 = var_cross_sectional_areas_of_air_channel_inlet_1
        # object-list
        var_zone_2_name = "object-list|Zone 2 Name"
        obj.zone_2_name = var_zone_2_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_2 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_2 = var_distance_from_top_of_thermal_chimney_to_inlet_2
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_2 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_2 = var_relative_ratios_of_air_flow_rates_passing_through_zone_2
        # real
        var_cross_sectional_areas_of_air_channel_inlet_2 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_2 = var_cross_sectional_areas_of_air_channel_inlet_2
        # object-list
        var_zone_3_name = "object-list|Zone 3 Name"
        obj.zone_3_name = var_zone_3_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_3 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_3 = var_distance_from_top_of_thermal_chimney_to_inlet_3
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_3 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_3 = var_relative_ratios_of_air_flow_rates_passing_through_zone_3
        # real
        var_cross_sectional_areas_of_air_channel_inlet_3 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_3 = var_cross_sectional_areas_of_air_channel_inlet_3
        # object-list
        var_zone_4_name = "object-list|Zone 4 Name"
        obj.zone_4_name = var_zone_4_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_4 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_4 = var_distance_from_top_of_thermal_chimney_to_inlet_4
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_4 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_4 = var_relative_ratios_of_air_flow_rates_passing_through_zone_4
        # real
        var_cross_sectional_areas_of_air_channel_inlet_4 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_4 = var_cross_sectional_areas_of_air_channel_inlet_4
        # object-list
        var_zone_5_name = "object-list|Zone 5 Name"
        obj.zone_5_name = var_zone_5_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_5 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_5 = var_distance_from_top_of_thermal_chimney_to_inlet_5
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_5 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_5 = var_relative_ratios_of_air_flow_rates_passing_through_zone_5
        # real
        var_cross_sectional_areas_of_air_channel_inlet_5 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_5 = var_cross_sectional_areas_of_air_channel_inlet_5
        # object-list
        var_zone_6_name = "object-list|Zone 6 Name"
        obj.zone_6_name = var_zone_6_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_6 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_6 = var_distance_from_top_of_thermal_chimney_to_inlet_6
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_6 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_6 = var_relative_ratios_of_air_flow_rates_passing_through_zone_6
        # real
        var_cross_sectional_areas_of_air_channel_inlet_6 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_6 = var_cross_sectional_areas_of_air_channel_inlet_6
        # object-list
        var_zone_7_name = "object-list|Zone 7 Name"
        obj.zone_7_name = var_zone_7_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_7 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_7 = var_distance_from_top_of_thermal_chimney_to_inlet_7
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_7 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_7 = var_relative_ratios_of_air_flow_rates_passing_through_zone_7
        # real
        var_cross_sectional_areas_of_air_channel_inlet_7 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_7 = var_cross_sectional_areas_of_air_channel_inlet_7
        # object-list
        var_zone_8_name = "object-list|Zone 8 Name"
        obj.zone_8_name = var_zone_8_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_8 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_8 = var_distance_from_top_of_thermal_chimney_to_inlet_8
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_8 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_8 = var_relative_ratios_of_air_flow_rates_passing_through_zone_8
        # real
        var_cross_sectional_areas_of_air_channel_inlet_8 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_8 = var_cross_sectional_areas_of_air_channel_inlet_8
        # object-list
        var_zone_9_name = "object-list|Zone 9 Name"
        obj.zone_9_name = var_zone_9_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_9 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_9 = var_distance_from_top_of_thermal_chimney_to_inlet_9
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_9 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_9 = var_relative_ratios_of_air_flow_rates_passing_through_zone_9
        # real
        var_cross_sectional_areas_of_air_channel_inlet_9 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_9 = var_cross_sectional_areas_of_air_channel_inlet_9
        # object-list
        var_zone_10_name = "object-list|Zone 10 Name"
        obj.zone_10_name = var_zone_10_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_10 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_10 = var_distance_from_top_of_thermal_chimney_to_inlet_10
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_10 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_10 = var_relative_ratios_of_air_flow_rates_passing_through_zone_10
        # real
        var_cross_sectional_areas_of_air_channel_inlet_10 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_10 = var_cross_sectional_areas_of_air_channel_inlet_10
        # object-list
        var_zone_11_name = "object-list|Zone 11 Name"
        obj.zone_11_name = var_zone_11_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_11 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_11 = var_distance_from_top_of_thermal_chimney_to_inlet_11
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_11 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_11 = var_relative_ratios_of_air_flow_rates_passing_through_zone_11
        # real
        var_cross_sectional_areas_of_air_channel_inlet_11 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_11 = var_cross_sectional_areas_of_air_channel_inlet_11
        # object-list
        var_zone_12_name = "object-list|Zone 12 Name"
        obj.zone_12_name = var_zone_12_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_12 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_12 = var_distance_from_top_of_thermal_chimney_to_inlet_12
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_12 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_12 = var_relative_ratios_of_air_flow_rates_passing_through_zone_12
        # real
        var_cross_sectional_areas_of_air_channel_inlet_12 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_12 = var_cross_sectional_areas_of_air_channel_inlet_12
        # object-list
        var_zone_13_name = "object-list|Zone 13 Name"
        obj.zone_13_name = var_zone_13_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_13 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_13 = var_distance_from_top_of_thermal_chimney_to_inlet_13
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_13 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_13 = var_relative_ratios_of_air_flow_rates_passing_through_zone_13
        # real
        var_cross_sectional_areas_of_air_channel_inlet_13 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_13 = var_cross_sectional_areas_of_air_channel_inlet_13
        # object-list
        var_zone_14_name = "object-list|Zone 14 Name"
        obj.zone_14_name = var_zone_14_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_14 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_14 = var_distance_from_top_of_thermal_chimney_to_inlet_14
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_14 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_14 = var_relative_ratios_of_air_flow_rates_passing_through_zone_14
        # real
        var_cross_sectional_areas_of_air_channel_inlet_14 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_14 = var_cross_sectional_areas_of_air_channel_inlet_14
        # object-list
        var_zone_15_name = "object-list|Zone 15 Name"
        obj.zone_15_name = var_zone_15_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_15 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_15 = var_distance_from_top_of_thermal_chimney_to_inlet_15
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_15 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_15 = var_relative_ratios_of_air_flow_rates_passing_through_zone_15
        # real
        var_cross_sectional_areas_of_air_channel_inlet_15 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_15 = var_cross_sectional_areas_of_air_channel_inlet_15
        # object-list
        var_zone_16_name = "object-list|Zone 16 Name"
        obj.zone_16_name = var_zone_16_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_16 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_16 = var_distance_from_top_of_thermal_chimney_to_inlet_16
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_16 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_16 = var_relative_ratios_of_air_flow_rates_passing_through_zone_16
        # real
        var_cross_sectional_areas_of_air_channel_inlet_16 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_16 = var_cross_sectional_areas_of_air_channel_inlet_16
        # object-list
        var_zone_17_name = "object-list|Zone 17 Name"
        obj.zone_17_name = var_zone_17_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_17 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_17 = var_distance_from_top_of_thermal_chimney_to_inlet_17
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_17 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_17 = var_relative_ratios_of_air_flow_rates_passing_through_zone_17
        # real
        var_cross_sectional_areas_of_air_channel_inlet_17 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_17 = var_cross_sectional_areas_of_air_channel_inlet_17
        # object-list
        var_zone_18_name = "object-list|Zone 18 Name"
        obj.zone_18_name = var_zone_18_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_18 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_18 = var_distance_from_top_of_thermal_chimney_to_inlet_18
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_18 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_18 = var_relative_ratios_of_air_flow_rates_passing_through_zone_18
        # real
        var_cross_sectional_areas_of_air_channel_inlet_18 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_18 = var_cross_sectional_areas_of_air_channel_inlet_18
        # object-list
        var_zone_19_name = "object-list|Zone 19 Name"
        obj.zone_19_name = var_zone_19_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_19 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_19 = var_distance_from_top_of_thermal_chimney_to_inlet_19
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_19 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_19 = var_relative_ratios_of_air_flow_rates_passing_through_zone_19
        # real
        var_cross_sectional_areas_of_air_channel_inlet_19 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_19 = var_cross_sectional_areas_of_air_channel_inlet_19
        # object-list
        var_zone_20_name = "object-list|Zone 20 Name"
        obj.zone_20_name = var_zone_20_name
        # real
        var_distance_from_top_of_thermal_chimney_to_inlet_20 = 0.0
        obj.distance_from_top_of_thermal_chimney_to_inlet_20 = var_distance_from_top_of_thermal_chimney_to_inlet_20
        # real
        var_relative_ratios_of_air_flow_rates_passing_through_zone_20 = 0.5
        obj.relative_ratios_of_air_flow_rates_passing_through_zone_20 = var_relative_ratios_of_air_flow_rates_passing_through_zone_20
        # real
        var_cross_sectional_areas_of_air_channel_inlet_20 = 0.0
        obj.cross_sectional_areas_of_air_channel_inlet_20 = var_cross_sectional_areas_of_air_channel_inlet_20

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonethermalchimneys[0].name, var_name)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonethermalchimneys[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].width_of_the_absorber_wall, var_width_of_the_absorber_wall)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_area_of_air_channel_outlet, var_cross_sectional_area_of_air_channel_outlet)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].discharge_coefficient, var_discharge_coefficient)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_1_name, var_zone_1_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_1, var_distance_from_top_of_thermal_chimney_to_inlet_1)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_1, var_relative_ratios_of_air_flow_rates_passing_through_zone_1)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_1, var_cross_sectional_areas_of_air_channel_inlet_1)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_2_name, var_zone_2_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_2, var_distance_from_top_of_thermal_chimney_to_inlet_2)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_2, var_relative_ratios_of_air_flow_rates_passing_through_zone_2)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_2, var_cross_sectional_areas_of_air_channel_inlet_2)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_3_name, var_zone_3_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_3, var_distance_from_top_of_thermal_chimney_to_inlet_3)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_3, var_relative_ratios_of_air_flow_rates_passing_through_zone_3)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_3, var_cross_sectional_areas_of_air_channel_inlet_3)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_4_name, var_zone_4_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_4, var_distance_from_top_of_thermal_chimney_to_inlet_4)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_4, var_relative_ratios_of_air_flow_rates_passing_through_zone_4)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_4, var_cross_sectional_areas_of_air_channel_inlet_4)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_5_name, var_zone_5_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_5, var_distance_from_top_of_thermal_chimney_to_inlet_5)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_5, var_relative_ratios_of_air_flow_rates_passing_through_zone_5)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_5, var_cross_sectional_areas_of_air_channel_inlet_5)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_6_name, var_zone_6_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_6, var_distance_from_top_of_thermal_chimney_to_inlet_6)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_6, var_relative_ratios_of_air_flow_rates_passing_through_zone_6)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_6, var_cross_sectional_areas_of_air_channel_inlet_6)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_7_name, var_zone_7_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_7, var_distance_from_top_of_thermal_chimney_to_inlet_7)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_7, var_relative_ratios_of_air_flow_rates_passing_through_zone_7)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_7, var_cross_sectional_areas_of_air_channel_inlet_7)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_8_name, var_zone_8_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_8, var_distance_from_top_of_thermal_chimney_to_inlet_8)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_8, var_relative_ratios_of_air_flow_rates_passing_through_zone_8)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_8, var_cross_sectional_areas_of_air_channel_inlet_8)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_9_name, var_zone_9_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_9, var_distance_from_top_of_thermal_chimney_to_inlet_9)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_9, var_relative_ratios_of_air_flow_rates_passing_through_zone_9)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_9, var_cross_sectional_areas_of_air_channel_inlet_9)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_10_name, var_zone_10_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_10, var_distance_from_top_of_thermal_chimney_to_inlet_10)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_10, var_relative_ratios_of_air_flow_rates_passing_through_zone_10)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_10, var_cross_sectional_areas_of_air_channel_inlet_10)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_11_name, var_zone_11_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_11, var_distance_from_top_of_thermal_chimney_to_inlet_11)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_11, var_relative_ratios_of_air_flow_rates_passing_through_zone_11)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_11, var_cross_sectional_areas_of_air_channel_inlet_11)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_12_name, var_zone_12_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_12, var_distance_from_top_of_thermal_chimney_to_inlet_12)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_12, var_relative_ratios_of_air_flow_rates_passing_through_zone_12)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_12, var_cross_sectional_areas_of_air_channel_inlet_12)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_13_name, var_zone_13_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_13, var_distance_from_top_of_thermal_chimney_to_inlet_13)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_13, var_relative_ratios_of_air_flow_rates_passing_through_zone_13)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_13, var_cross_sectional_areas_of_air_channel_inlet_13)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_14_name, var_zone_14_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_14, var_distance_from_top_of_thermal_chimney_to_inlet_14)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_14, var_relative_ratios_of_air_flow_rates_passing_through_zone_14)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_14, var_cross_sectional_areas_of_air_channel_inlet_14)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_15_name, var_zone_15_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_15, var_distance_from_top_of_thermal_chimney_to_inlet_15)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_15, var_relative_ratios_of_air_flow_rates_passing_through_zone_15)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_15, var_cross_sectional_areas_of_air_channel_inlet_15)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_16_name, var_zone_16_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_16, var_distance_from_top_of_thermal_chimney_to_inlet_16)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_16, var_relative_ratios_of_air_flow_rates_passing_through_zone_16)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_16, var_cross_sectional_areas_of_air_channel_inlet_16)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_17_name, var_zone_17_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_17, var_distance_from_top_of_thermal_chimney_to_inlet_17)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_17, var_relative_ratios_of_air_flow_rates_passing_through_zone_17)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_17, var_cross_sectional_areas_of_air_channel_inlet_17)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_18_name, var_zone_18_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_18, var_distance_from_top_of_thermal_chimney_to_inlet_18)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_18, var_relative_ratios_of_air_flow_rates_passing_through_zone_18)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_18, var_cross_sectional_areas_of_air_channel_inlet_18)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_19_name, var_zone_19_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_19, var_distance_from_top_of_thermal_chimney_to_inlet_19)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_19, var_relative_ratios_of_air_flow_rates_passing_through_zone_19)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_19, var_cross_sectional_areas_of_air_channel_inlet_19)
        self.assertEqual(idf2.zonethermalchimneys[0].zone_20_name, var_zone_20_name)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].distance_from_top_of_thermal_chimney_to_inlet_20, var_distance_from_top_of_thermal_chimney_to_inlet_20)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].relative_ratios_of_air_flow_rates_passing_through_zone_20, var_relative_ratios_of_air_flow_rates_passing_through_zone_20)
        self.assertAlmostEqual(idf2.zonethermalchimneys[0].cross_sectional_areas_of_air_channel_inlet_20, var_cross_sectional_areas_of_air_channel_inlet_20)