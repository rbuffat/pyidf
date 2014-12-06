import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateZoneBaseboardHeat
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateZoneBaseboardHeat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonebaseboardheat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneBaseboardHeat()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 6.6
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity
        # object-list
        var_dedicated_outdoor_air_system_name = "object-list|Dedicated Outdoor Air System Name"
        obj.dedicated_outdoor_air_system_name = var_dedicated_outdoor_air_system_name
        # alpha
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 9.9
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 10.1
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 11.11
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonebaseboardheats[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonebaseboardheats[0].baseboard_heating_capacity, var_baseboard_heating_capacity)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].dedicated_outdoor_air_system_name, var_dedicated_outdoor_air_system_name)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonebaseboardheats[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonebaseboardheats[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonebaseboardheats[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezonebaseboardheats[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)