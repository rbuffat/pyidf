import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacVentilatedSlab
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacVentilatedSlab(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacventilatedslab(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacVentilatedSlab()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_surface_name_or_radiant_surface_group_name = "object-list|Surface Name or Radiant Surface Group Name"
        obj.surface_name_or_radiant_surface_group_name = var_surface_name_or_radiant_surface_group_name
        # real
        var_maximum_air_flow_rate = 0.0001
        obj.maximum_air_flow_rate = var_maximum_air_flow_rate
        # alpha
        var_outdoor_air_control_type = "VariablePercent"
        obj.outdoor_air_control_type = var_outdoor_air_control_type
        # real
        var_minimum_outdoor_air_flow_rate = 0.0
        obj.minimum_outdoor_air_flow_rate = var_minimum_outdoor_air_flow_rate
        # object-list
        var_minimum_outdoor_air_schedule_name = "object-list|Minimum Outdoor Air Schedule Name"
        obj.minimum_outdoor_air_schedule_name = var_minimum_outdoor_air_schedule_name
        # real
        var_maximum_outdoor_air_flow_rate = 0.0
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # object-list
        var_maximum_outdoor_air_fraction_or_temperature_schedule_name = "object-list|Maximum Outdoor Air Fraction or Temperature Schedule Name"
        obj.maximum_outdoor_air_fraction_or_temperature_schedule_name = var_maximum_outdoor_air_fraction_or_temperature_schedule_name
        # alpha
        var_system_configuration_type = "SlabOnly"
        obj.system_configuration_type = var_system_configuration_type
        # real
        var_hollow_core_inside_diameter = 0.0
        obj.hollow_core_inside_diameter = var_hollow_core_inside_diameter
        # real
        var_hollow_core_length = 0.0
        obj.hollow_core_length = var_hollow_core_length
        # real
        var_number_of_cores = 0.0
        obj.number_of_cores = var_number_of_cores
        # alpha
        var_temperature_control_type = "MeanAirTemperature"
        obj.temperature_control_type = var_temperature_control_type
        # object-list
        var_heating_high_air_temperature_schedule_name = "object-list|Heating High Air Temperature Schedule Name"
        obj.heating_high_air_temperature_schedule_name = var_heating_high_air_temperature_schedule_name
        # object-list
        var_heating_low_air_temperature_schedule_name = "object-list|Heating Low Air Temperature Schedule Name"
        obj.heating_low_air_temperature_schedule_name = var_heating_low_air_temperature_schedule_name
        # object-list
        var_heating_high_control_temperature_schedule_name = "object-list|Heating High Control Temperature Schedule Name"
        obj.heating_high_control_temperature_schedule_name = var_heating_high_control_temperature_schedule_name
        # object-list
        var_heating_low_control_temperature_schedule_name = "object-list|Heating Low Control Temperature Schedule Name"
        obj.heating_low_control_temperature_schedule_name = var_heating_low_control_temperature_schedule_name
        # object-list
        var_cooling_high_air_temperature_schedule_name = "object-list|Cooling High Air Temperature Schedule Name"
        obj.cooling_high_air_temperature_schedule_name = var_cooling_high_air_temperature_schedule_name
        # object-list
        var_cooling_low_air_temperature_schedule_name = "object-list|Cooling Low Air Temperature Schedule Name"
        obj.cooling_low_air_temperature_schedule_name = var_cooling_low_air_temperature_schedule_name
        # object-list
        var_cooling_high_control_temperature_schedule_name = "object-list|Cooling High Control Temperature Schedule Name"
        obj.cooling_high_control_temperature_schedule_name = var_cooling_high_control_temperature_schedule_name
        # object-list
        var_cooling_low_control_temperature_schedule_name = "object-list|Cooling Low Control Temperature Schedule Name"
        obj.cooling_low_control_temperature_schedule_name = var_cooling_low_control_temperature_schedule_name
        # node
        var_return_air_node_name = "node|Return Air Node Name"
        obj.return_air_node_name = var_return_air_node_name
        # node
        var_slab_in_node_name = "node|Slab In Node Name"
        obj.slab_in_node_name = var_slab_in_node_name
        # node
        var_zone_supply_air_node_name = "node|Zone Supply Air Node Name"
        obj.zone_supply_air_node_name = var_zone_supply_air_node_name
        # node
        var_outdoor_air_node_name = "node|Outdoor Air Node Name"
        obj.outdoor_air_node_name = var_outdoor_air_node_name
        # node
        var_relief_air_node_name = "node|Relief Air Node Name"
        obj.relief_air_node_name = var_relief_air_node_name
        # node
        var_outdoor_air_mixer_outlet_node_name = "node|Outdoor Air Mixer Outlet Node Name"
        obj.outdoor_air_mixer_outlet_node_name = var_outdoor_air_mixer_outlet_node_name
        # node
        var_fan_outlet_node_name = "node|Fan Outlet Node Name"
        obj.fan_outlet_node_name = var_fan_outlet_node_name
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # alpha
        var_coil_option_type = "None"
        obj.coil_option_type = var_coil_option_type
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Water"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # node
        var_hot_water_or_steam_inlet_node_name = "node|Hot Water or Steam Inlet Node Name"
        obj.hot_water_or_steam_inlet_node_name = var_hot_water_or_steam_inlet_node_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:Water"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # node
        var_cold_water_inlet_node_name = "node|Cold Water Inlet Node Name"
        obj.cold_water_inlet_node_name = var_cold_water_inlet_node_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].name, var_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].surface_name_or_radiant_surface_group_name, var_surface_name_or_radiant_surface_group_name)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].maximum_air_flow_rate, var_maximum_air_flow_rate)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].outdoor_air_control_type, var_outdoor_air_control_type)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].maximum_outdoor_air_fraction_or_temperature_schedule_name, var_maximum_outdoor_air_fraction_or_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].system_configuration_type, var_system_configuration_type)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].hollow_core_inside_diameter, var_hollow_core_inside_diameter)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].hollow_core_length, var_hollow_core_length)
        self.assertAlmostEqual(idf2.zonehvacventilatedslabs[0].number_of_cores, var_number_of_cores)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].temperature_control_type, var_temperature_control_type)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_high_air_temperature_schedule_name, var_heating_high_air_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_low_air_temperature_schedule_name, var_heating_low_air_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_high_control_temperature_schedule_name, var_heating_high_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_low_control_temperature_schedule_name, var_heating_low_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_high_air_temperature_schedule_name, var_cooling_high_air_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_low_air_temperature_schedule_name, var_cooling_low_air_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_high_control_temperature_schedule_name, var_cooling_high_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_low_control_temperature_schedule_name, var_cooling_low_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].return_air_node_name, var_return_air_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].slab_in_node_name, var_slab_in_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].zone_supply_air_node_name, var_zone_supply_air_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].outdoor_air_node_name, var_outdoor_air_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].relief_air_node_name, var_relief_air_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].outdoor_air_mixer_outlet_node_name, var_outdoor_air_mixer_outlet_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].fan_outlet_node_name, var_fan_outlet_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].fan_name, var_fan_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].coil_option_type, var_coil_option_type)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].hot_water_or_steam_inlet_node_name, var_hot_water_or_steam_inlet_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].cold_water_inlet_node_name, var_cold_water_inlet_node_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacventilatedslabs[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)