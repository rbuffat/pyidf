import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import DaylightingControls
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDaylightingControls(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingcontrols(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingControls()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # integer
        var_total_daylighting_reference_points = 1
        obj.total_daylighting_reference_points = var_total_daylighting_reference_points
        # real
        var_xcoordinate_of_first_reference_point = 3.3
        obj.xcoordinate_of_first_reference_point = var_xcoordinate_of_first_reference_point
        # real
        var_ycoordinate_of_first_reference_point = 4.4
        obj.ycoordinate_of_first_reference_point = var_ycoordinate_of_first_reference_point
        # real
        var_zcoordinate_of_first_reference_point = 5.5
        obj.zcoordinate_of_first_reference_point = var_zcoordinate_of_first_reference_point
        # real
        var_xcoordinate_of_second_reference_point = 6.6
        obj.xcoordinate_of_second_reference_point = var_xcoordinate_of_second_reference_point
        # real
        var_ycoordinate_of_second_reference_point = 7.7
        obj.ycoordinate_of_second_reference_point = var_ycoordinate_of_second_reference_point
        # real
        var_zcoordinate_of_second_reference_point = 8.8
        obj.zcoordinate_of_second_reference_point = var_zcoordinate_of_second_reference_point
        # real
        var_fraction_of_zone_controlled_by_first_reference_point = 0.5
        obj.fraction_of_zone_controlled_by_first_reference_point = var_fraction_of_zone_controlled_by_first_reference_point
        # real
        var_fraction_of_zone_controlled_by_second_reference_point = 0.5
        obj.fraction_of_zone_controlled_by_second_reference_point = var_fraction_of_zone_controlled_by_second_reference_point
        # real
        var_illuminance_setpoint_at_first_reference_point = 0.0
        obj.illuminance_setpoint_at_first_reference_point = var_illuminance_setpoint_at_first_reference_point
        # real
        var_illuminance_setpoint_at_second_reference_point = 0.0
        obj.illuminance_setpoint_at_second_reference_point = var_illuminance_setpoint_at_second_reference_point
        # integer
        var_lighting_control_type = 2
        obj.lighting_control_type = var_lighting_control_type
        # real
        var_glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = 180.0
        obj.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = var_glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis
        # real
        var_maximum_allowable_discomfort_glare_index = 1.0
        obj.maximum_allowable_discomfort_glare_index = var_maximum_allowable_discomfort_glare_index
        # real
        var_minimum_input_power_fraction_for_continuous_dimming_control = 0.3
        obj.minimum_input_power_fraction_for_continuous_dimming_control = var_minimum_input_power_fraction_for_continuous_dimming_control
        # real
        var_minimum_light_output_fraction_for_continuous_dimming_control = 0.3
        obj.minimum_light_output_fraction_for_continuous_dimming_control = var_minimum_light_output_fraction_for_continuous_dimming_control
        # integer
        var_number_of_stepped_control_steps = 18
        obj.number_of_stepped_control_steps = var_number_of_stepped_control_steps
        # real
        var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = 0.5
        obj.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingcontrolss[0].zone_name, var_zone_name)
        self.assertEqual(idf2.daylightingcontrolss[0].total_daylighting_reference_points, var_total_daylighting_reference_points)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].xcoordinate_of_first_reference_point, var_xcoordinate_of_first_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].ycoordinate_of_first_reference_point, var_ycoordinate_of_first_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].zcoordinate_of_first_reference_point, var_zcoordinate_of_first_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].xcoordinate_of_second_reference_point, var_xcoordinate_of_second_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].ycoordinate_of_second_reference_point, var_ycoordinate_of_second_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].zcoordinate_of_second_reference_point, var_zcoordinate_of_second_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].fraction_of_zone_controlled_by_first_reference_point, var_fraction_of_zone_controlled_by_first_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].fraction_of_zone_controlled_by_second_reference_point, var_fraction_of_zone_controlled_by_second_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].illuminance_setpoint_at_first_reference_point, var_illuminance_setpoint_at_first_reference_point)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].illuminance_setpoint_at_second_reference_point, var_illuminance_setpoint_at_second_reference_point)
        self.assertEqual(idf2.daylightingcontrolss[0].lighting_control_type, var_lighting_control_type)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis, var_glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].maximum_allowable_discomfort_glare_index, var_maximum_allowable_discomfort_glare_index)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].minimum_input_power_fraction_for_continuous_dimming_control, var_minimum_input_power_fraction_for_continuous_dimming_control)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].minimum_light_output_fraction_for_continuous_dimming_control, var_minimum_light_output_fraction_for_continuous_dimming_control)
        self.assertEqual(idf2.daylightingcontrolss[0].number_of_stepped_control_steps, var_number_of_stepped_control_steps)
        self.assertAlmostEqual(idf2.daylightingcontrolss[0].probability_lighting_will_be_reset_when_needed_in_manual_stepped_control, var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control)
        self.assertEqual(idf2.daylightingcontrolss[0].availability_schedule_name, var_availability_schedule_name)