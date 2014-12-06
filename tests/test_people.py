import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import People
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPeople(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_people(self):

        pyidf.validation_level = ValidationLevel.error

        obj = People()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # object-list
        var_number_of_people_schedule_name = "object-list|Number of People Schedule Name"
        obj.number_of_people_schedule_name = var_number_of_people_schedule_name
        # alpha
        var_number_of_people_calculation_method = "People"
        obj.number_of_people_calculation_method = var_number_of_people_calculation_method
        # real
        var_number_of_people = 0.0
        obj.number_of_people = var_number_of_people
        # real
        var_people_per_zone_floor_area = 0.0
        obj.people_per_zone_floor_area = var_people_per_zone_floor_area
        # real
        var_zone_floor_area_per_person = 0.0
        obj.zone_floor_area_per_person = var_zone_floor_area_per_person
        # real
        var_fraction_radiant = 0.5
        obj.fraction_radiant = var_fraction_radiant
        # real
        var_sensible_heat_fraction = 0.5
        obj.sensible_heat_fraction = var_sensible_heat_fraction
        # object-list
        var_activity_level_schedule_name = "object-list|Activity Level Schedule Name"
        obj.activity_level_schedule_name = var_activity_level_schedule_name
        # real
        var_carbon_dioxide_generation_rate = 1.91e-07
        obj.carbon_dioxide_generation_rate = var_carbon_dioxide_generation_rate
        # alpha
        var_enable_ashrae_55_comfort_warnings = "Yes"
        obj.enable_ashrae_55_comfort_warnings = var_enable_ashrae_55_comfort_warnings
        # alpha
        var_mean_radiant_temperature_calculation_type = "ZoneAveraged"
        obj.mean_radiant_temperature_calculation_type = var_mean_radiant_temperature_calculation_type
        # object-list
        var_surface_name_or_angle_factor_list_name = "object-list|Surface Name/Angle Factor List Name"
        obj.surface_name_or_angle_factor_list_name = var_surface_name_or_angle_factor_list_name
        # object-list
        var_work_efficiency_schedule_name = "object-list|Work Efficiency Schedule Name"
        obj.work_efficiency_schedule_name = var_work_efficiency_schedule_name
        # alpha
        var_clothing_insulation_calculation_method = "ClothingInsulationSchedule"
        obj.clothing_insulation_calculation_method = var_clothing_insulation_calculation_method
        # object-list
        var_clothing_insulation_calculation_method_schedule_name = "object-list|Clothing Insulation Calculation Method Schedule Name"
        obj.clothing_insulation_calculation_method_schedule_name = var_clothing_insulation_calculation_method_schedule_name
        # object-list
        var_clothing_insulation_schedule_name = "object-list|Clothing Insulation Schedule Name"
        obj.clothing_insulation_schedule_name = var_clothing_insulation_schedule_name
        # object-list
        var_air_velocity_schedule_name = "object-list|Air Velocity Schedule Name"
        obj.air_velocity_schedule_name = var_air_velocity_schedule_name
        # alpha
        var_thermal_comfort_model_1_type = "Fanger"
        obj.thermal_comfort_model_1_type = var_thermal_comfort_model_1_type
        # alpha
        var_thermal_comfort_model_2_type = "Fanger"
        obj.thermal_comfort_model_2_type = var_thermal_comfort_model_2_type
        # alpha
        var_thermal_comfort_model_3_type = "Fanger"
        obj.thermal_comfort_model_3_type = var_thermal_comfort_model_3_type
        # alpha
        var_thermal_comfort_model_4_type = "Fanger"
        obj.thermal_comfort_model_4_type = var_thermal_comfort_model_4_type
        # alpha
        var_thermal_comfort_model_5_type = "Fanger"
        obj.thermal_comfort_model_5_type = var_thermal_comfort_model_5_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.peoples[0].name, var_name)
        self.assertEqual(idf2.peoples[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.peoples[0].number_of_people_schedule_name, var_number_of_people_schedule_name)
        self.assertEqual(idf2.peoples[0].number_of_people_calculation_method, var_number_of_people_calculation_method)
        self.assertAlmostEqual(idf2.peoples[0].number_of_people, var_number_of_people)
        self.assertAlmostEqual(idf2.peoples[0].people_per_zone_floor_area, var_people_per_zone_floor_area)
        self.assertAlmostEqual(idf2.peoples[0].zone_floor_area_per_person, var_zone_floor_area_per_person)
        self.assertAlmostEqual(idf2.peoples[0].fraction_radiant, var_fraction_radiant)
        self.assertAlmostEqual(idf2.peoples[0].sensible_heat_fraction, var_sensible_heat_fraction)
        self.assertEqual(idf2.peoples[0].activity_level_schedule_name, var_activity_level_schedule_name)
        self.assertAlmostEqual(idf2.peoples[0].carbon_dioxide_generation_rate, var_carbon_dioxide_generation_rate)
        self.assertEqual(idf2.peoples[0].enable_ashrae_55_comfort_warnings, var_enable_ashrae_55_comfort_warnings)
        self.assertEqual(idf2.peoples[0].mean_radiant_temperature_calculation_type, var_mean_radiant_temperature_calculation_type)
        self.assertEqual(idf2.peoples[0].surface_name_or_angle_factor_list_name, var_surface_name_or_angle_factor_list_name)
        self.assertEqual(idf2.peoples[0].work_efficiency_schedule_name, var_work_efficiency_schedule_name)
        self.assertEqual(idf2.peoples[0].clothing_insulation_calculation_method, var_clothing_insulation_calculation_method)
        self.assertEqual(idf2.peoples[0].clothing_insulation_calculation_method_schedule_name, var_clothing_insulation_calculation_method_schedule_name)
        self.assertEqual(idf2.peoples[0].clothing_insulation_schedule_name, var_clothing_insulation_schedule_name)
        self.assertEqual(idf2.peoples[0].air_velocity_schedule_name, var_air_velocity_schedule_name)
        self.assertEqual(idf2.peoples[0].thermal_comfort_model_1_type, var_thermal_comfort_model_1_type)
        self.assertEqual(idf2.peoples[0].thermal_comfort_model_2_type, var_thermal_comfort_model_2_type)
        self.assertEqual(idf2.peoples[0].thermal_comfort_model_3_type, var_thermal_comfort_model_3_type)
        self.assertEqual(idf2.peoples[0].thermal_comfort_model_4_type, var_thermal_comfort_model_4_type)
        self.assertEqual(idf2.peoples[0].thermal_comfort_model_5_type, var_thermal_comfort_model_5_type)