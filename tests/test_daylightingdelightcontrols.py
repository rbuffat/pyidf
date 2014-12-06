import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import DaylightingDelightControls
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDaylightingDelightControls(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdelightcontrols(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDelightControls()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # integer
        var_lighting_control_type = 2
        obj.lighting_control_type = var_lighting_control_type
        # real
        var_minimum_input_power_fraction_for_continuous_dimming_control = 0.3
        obj.minimum_input_power_fraction_for_continuous_dimming_control = var_minimum_input_power_fraction_for_continuous_dimming_control
        # real
        var_minimum_light_output_fraction_for_continuous_dimming_control = 0.3
        obj.minimum_light_output_fraction_for_continuous_dimming_control = var_minimum_light_output_fraction_for_continuous_dimming_control
        # integer
        var_number_of_stepped_control_steps = 6
        obj.number_of_stepped_control_steps = var_number_of_stepped_control_steps
        # real
        var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = 0.5
        obj.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control
        # real
        var_gridding_resolution = 0.0001
        obj.gridding_resolution = var_gridding_resolution

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdelightcontrolss[0].name, var_name)
        self.assertEqual(idf2.daylightingdelightcontrolss[0].zone_name, var_zone_name)
        self.assertEqual(idf2.daylightingdelightcontrolss[0].lighting_control_type, var_lighting_control_type)
        self.assertAlmostEqual(idf2.daylightingdelightcontrolss[0].minimum_input_power_fraction_for_continuous_dimming_control, var_minimum_input_power_fraction_for_continuous_dimming_control)
        self.assertAlmostEqual(idf2.daylightingdelightcontrolss[0].minimum_light_output_fraction_for_continuous_dimming_control, var_minimum_light_output_fraction_for_continuous_dimming_control)
        self.assertEqual(idf2.daylightingdelightcontrolss[0].number_of_stepped_control_steps, var_number_of_stepped_control_steps)
        self.assertAlmostEqual(idf2.daylightingdelightcontrolss[0].probability_lighting_will_be_reset_when_needed_in_manual_stepped_control, var_probability_lighting_will_be_reset_when_needed_in_manual_stepped_control)
        self.assertAlmostEqual(idf2.daylightingdelightcontrolss[0].gridding_resolution, var_gridding_resolution)