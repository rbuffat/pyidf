import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationWalkIn

log = logging.getLogger(__name__)

class TestRefrigerationWalkIn(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationwalkin(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationWalkIn()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_rated_coil_cooling_capacity = 3.3
        obj.rated_coil_cooling_capacity = var_rated_coil_cooling_capacity
        # real
        var_operating_temperature = 19.9999
        obj.operating_temperature = var_operating_temperature
        # real
        var_rated_cooling_source_temperature = -15.0
        obj.rated_cooling_source_temperature = var_rated_cooling_source_temperature
        # real
        var_rated_total_heating_power = 6.6
        obj.rated_total_heating_power = var_rated_total_heating_power
        # object-list
        var_heating_power_schedule_name = "object-list|Heating Power Schedule Name"
        obj.heating_power_schedule_name = var_heating_power_schedule_name
        # real
        var_rated_cooling_coil_fan_power = 0.0
        obj.rated_cooling_coil_fan_power = var_rated_cooling_coil_fan_power
        # real
        var_rated_circulation_fan_power = 0.0
        obj.rated_circulation_fan_power = var_rated_circulation_fan_power
        # real
        var_rated_total_lighting_power = 10.1
        obj.rated_total_lighting_power = var_rated_total_lighting_power
        # object-list
        var_lighting_schedule_name = "object-list|Lighting Schedule Name"
        obj.lighting_schedule_name = var_lighting_schedule_name
        # alpha
        var_defrost_type = "HotFluid"
        obj.defrost_type = var_defrost_type
        # alpha
        var_defrost_control_type = "TimeSchedule"
        obj.defrost_control_type = var_defrost_control_type
        # object-list
        var_defrost_schedule_name = "object-list|Defrost Schedule Name"
        obj.defrost_schedule_name = var_defrost_schedule_name
        # object-list
        var_defrost_dripdown_schedule_name = "object-list|Defrost Drip-Down Schedule Name"
        obj.defrost_dripdown_schedule_name = var_defrost_dripdown_schedule_name
        # real
        var_defrost_power = 0.0
        obj.defrost_power = var_defrost_power
        # real
        var_temperature_termination_defrost_fraction_to_ice = 0.50005
        obj.temperature_termination_defrost_fraction_to_ice = var_temperature_termination_defrost_fraction_to_ice
        # object-list
        var_restocking_schedule_name = "object-list|Restocking Schedule Name"
        obj.restocking_schedule_name = var_restocking_schedule_name
        # real
        var_average_refrigerant_charge_inventory = 19.19
        obj.average_refrigerant_charge_inventory = var_average_refrigerant_charge_inventory
        # real
        var_insulated_floor_surface_area = 0.0001
        obj.insulated_floor_surface_area = var_insulated_floor_surface_area
        # real
        var_insulated_floor_uvalue = 0.0001
        obj.insulated_floor_uvalue = var_insulated_floor_uvalue
        paras = []
        var_zone_1_name = "object-list|Zone 1 Name"
        paras.append(var_zone_1_name)
        var_total_insulated_surface_area_facing_zone_1 = 0.0001
        paras.append(var_total_insulated_surface_area_facing_zone_1)
        var_insulated_surface_uvalue_facing_zone_1 = 0.0001
        paras.append(var_insulated_surface_uvalue_facing_zone_1)
        var_area_of_glass_reach_in_doors_facing_zone_1 = 25.25
        paras.append(var_area_of_glass_reach_in_doors_facing_zone_1)
        var_height_of_glass_reach_in_doors_facing_zone_1 = 26.26
        paras.append(var_height_of_glass_reach_in_doors_facing_zone_1)
        var_glass_reach_in_door_u_value_facing_zone_1 = 0.0001
        paras.append(var_glass_reach_in_door_u_value_facing_zone_1)
        var_glass_reach_in_door_opening_schedule_name_facing_zone_1 = "object-list|Glass Reach In Door Opening Schedule Name Facing Zone 1"
        paras.append(var_glass_reach_in_door_opening_schedule_name_facing_zone_1)
        var_area_of_stocking_doors_facing_zone_1 = 29.29
        paras.append(var_area_of_stocking_doors_facing_zone_1)
        var_height_of_stocking_doors_facing_zone_1 = 30.3
        paras.append(var_height_of_stocking_doors_facing_zone_1)
        var_stocking_door_u_value_facing_zone_1 = 0.0001
        paras.append(var_stocking_door_u_value_facing_zone_1)
        var_stocking_door_opening_schedule_name_facing_zone_1 = "object-list|Stocking Door Opening Schedule Name Facing Zone 1"
        paras.append(var_stocking_door_opening_schedule_name_facing_zone_1)
        var_stocking_door_opening_protection_type_facing_zone_1 = "None"
        paras.append(var_stocking_door_opening_protection_type_facing_zone_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationwalkins[0].name, var_name)
        self.assertEqual(idf2.refrigerationwalkins[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_coil_cooling_capacity, var_rated_coil_cooling_capacity)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].operating_temperature, var_operating_temperature)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_cooling_source_temperature, var_rated_cooling_source_temperature)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_total_heating_power, var_rated_total_heating_power)
        self.assertEqual(idf2.refrigerationwalkins[0].heating_power_schedule_name, var_heating_power_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_cooling_coil_fan_power, var_rated_cooling_coil_fan_power)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_circulation_fan_power, var_rated_circulation_fan_power)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].rated_total_lighting_power, var_rated_total_lighting_power)
        self.assertEqual(idf2.refrigerationwalkins[0].lighting_schedule_name, var_lighting_schedule_name)
        self.assertEqual(idf2.refrigerationwalkins[0].defrost_type, var_defrost_type)
        self.assertEqual(idf2.refrigerationwalkins[0].defrost_control_type, var_defrost_control_type)
        self.assertEqual(idf2.refrigerationwalkins[0].defrost_schedule_name, var_defrost_schedule_name)
        self.assertEqual(idf2.refrigerationwalkins[0].defrost_dripdown_schedule_name, var_defrost_dripdown_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].defrost_power, var_defrost_power)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].temperature_termination_defrost_fraction_to_ice, var_temperature_termination_defrost_fraction_to_ice)
        self.assertEqual(idf2.refrigerationwalkins[0].restocking_schedule_name, var_restocking_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].average_refrigerant_charge_inventory, var_average_refrigerant_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].insulated_floor_surface_area, var_insulated_floor_surface_area)
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].insulated_floor_uvalue, var_insulated_floor_uvalue)
        index = obj.extensible_field_index("Zone 1 Name")
        self.assertEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_zone_1_name)
        index = obj.extensible_field_index("Total Insulated Surface Area Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_total_insulated_surface_area_facing_zone_1)
        index = obj.extensible_field_index("Insulated Surface U-Value Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_insulated_surface_uvalue_facing_zone_1)
        index = obj.extensible_field_index("Area of Glass Reach In Doors Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_area_of_glass_reach_in_doors_facing_zone_1)
        index = obj.extensible_field_index("Height of Glass Reach In Doors Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_height_of_glass_reach_in_doors_facing_zone_1)
        index = obj.extensible_field_index("Glass Reach In Door U Value Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_glass_reach_in_door_u_value_facing_zone_1)
        index = obj.extensible_field_index("Glass Reach In Door Opening Schedule Name Facing Zone 1")
        self.assertEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_glass_reach_in_door_opening_schedule_name_facing_zone_1)
        index = obj.extensible_field_index("Area of Stocking Doors Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_area_of_stocking_doors_facing_zone_1)
        index = obj.extensible_field_index("Height of Stocking Doors Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_height_of_stocking_doors_facing_zone_1)
        index = obj.extensible_field_index("Stocking Door U Value Facing Zone 1")
        self.assertAlmostEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_stocking_door_u_value_facing_zone_1)
        index = obj.extensible_field_index("Stocking Door Opening Schedule Name Facing Zone 1")
        self.assertEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_stocking_door_opening_schedule_name_facing_zone_1)
        index = obj.extensible_field_index("Stocking Door Opening Protection Type Facing Zone 1")
        self.assertEqual(idf2.refrigerationwalkins[0].extensibles[0][index], var_stocking_door_opening_protection_type_facing_zone_1)