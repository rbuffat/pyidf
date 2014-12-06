import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorWindTurbine

log = logging.getLogger(__name__)

class TestGeneratorWindTurbine(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorwindturbine(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorWindTurbine()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_rotor_type = "HorizontalAxisWindTurbine"
        obj.rotor_type = var_rotor_type
        # alpha
        var_power_control = "FixedSpeedFixedPitch"
        obj.power_control = var_power_control
        # real
        var_rated_rotor_speed = 0.0001
        obj.rated_rotor_speed = var_rated_rotor_speed
        # real
        var_rotor_diameter = 0.0001
        obj.rotor_diameter = var_rotor_diameter
        # real
        var_overall_height = 0.0001
        obj.overall_height = var_overall_height
        # real
        var_number_of_blades = 2.0
        obj.number_of_blades = var_number_of_blades
        # real
        var_rated_power = 0.0001
        obj.rated_power = var_rated_power
        # real
        var_rated_wind_speed = 0.0001
        obj.rated_wind_speed = var_rated_wind_speed
        # real
        var_cut_in_wind_speed = 0.0001
        obj.cut_in_wind_speed = var_cut_in_wind_speed
        # real
        var_cut_out_wind_speed = 0.0001
        obj.cut_out_wind_speed = var_cut_out_wind_speed
        # real
        var_fraction_system_efficiency = 0.50005
        obj.fraction_system_efficiency = var_fraction_system_efficiency
        # real
        var_maximum_tip_speed_ratio = 6.00005
        obj.maximum_tip_speed_ratio = var_maximum_tip_speed_ratio
        # real
        var_maximum_power_coefficient = 0.29505
        obj.maximum_power_coefficient = var_maximum_power_coefficient
        # real
        var_annual_local_average_wind_speed = 0.0001
        obj.annual_local_average_wind_speed = var_annual_local_average_wind_speed
        # real
        var_height_for_local_average_wind_speed = 0.0001
        obj.height_for_local_average_wind_speed = var_height_for_local_average_wind_speed
        # real
        var_blade_chord_area = 18.18
        obj.blade_chord_area = var_blade_chord_area
        # real
        var_blade_drag_coefficient = 19.19
        obj.blade_drag_coefficient = var_blade_drag_coefficient
        # real
        var_blade_lift_coefficient = 20.2
        obj.blade_lift_coefficient = var_blade_lift_coefficient
        # real
        var_power_coefficient_c1 = 0.0001
        obj.power_coefficient_c1 = var_power_coefficient_c1
        # real
        var_power_coefficient_c2 = 0.0001
        obj.power_coefficient_c2 = var_power_coefficient_c2
        # real
        var_power_coefficient_c3 = 0.0001
        obj.power_coefficient_c3 = var_power_coefficient_c3
        # real
        var_power_coefficient_c4 = 0.0
        obj.power_coefficient_c4 = var_power_coefficient_c4
        # real
        var_power_coefficient_c5 = 0.0001
        obj.power_coefficient_c5 = var_power_coefficient_c5
        # real
        var_power_coefficient_c6 = 0.0001
        obj.power_coefficient_c6 = var_power_coefficient_c6

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorwindturbines[0].name, var_name)
        self.assertEqual(idf2.generatorwindturbines[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.generatorwindturbines[0].rotor_type, var_rotor_type)
        self.assertEqual(idf2.generatorwindturbines[0].power_control, var_power_control)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].rated_rotor_speed, var_rated_rotor_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].rotor_diameter, var_rotor_diameter)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].overall_height, var_overall_height)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].number_of_blades, var_number_of_blades)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].rated_power, var_rated_power)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].rated_wind_speed, var_rated_wind_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].cut_in_wind_speed, var_cut_in_wind_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].cut_out_wind_speed, var_cut_out_wind_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].fraction_system_efficiency, var_fraction_system_efficiency)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].maximum_tip_speed_ratio, var_maximum_tip_speed_ratio)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].maximum_power_coefficient, var_maximum_power_coefficient)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].annual_local_average_wind_speed, var_annual_local_average_wind_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].height_for_local_average_wind_speed, var_height_for_local_average_wind_speed)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].blade_chord_area, var_blade_chord_area)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].blade_drag_coefficient, var_blade_drag_coefficient)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].blade_lift_coefficient, var_blade_lift_coefficient)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c1, var_power_coefficient_c1)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c2, var_power_coefficient_c2)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c3, var_power_coefficient_c3)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c4, var_power_coefficient_c4)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c5, var_power_coefficient_c5)
        self.assertAlmostEqual(idf2.generatorwindturbines[0].power_coefficient_c6, var_power_coefficient_c6)