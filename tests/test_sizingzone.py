import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import SizingZone

log = logging.getLogger(__name__)

class TestSizingZone(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingzone(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingZone()
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 3.3
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 4.4
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 6.6
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 7.7
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # real
        var_zone_cooling_design_supply_air_humidity_ratio = 0.0
        obj.zone_cooling_design_supply_air_humidity_ratio = var_zone_cooling_design_supply_air_humidity_ratio
        # real
        var_zone_heating_design_supply_air_humidity_ratio = 0.0
        obj.zone_heating_design_supply_air_humidity_ratio = var_zone_heating_design_supply_air_humidity_ratio
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # real
        var_zone_cooling_sizing_factor = 0.0
        obj.zone_cooling_sizing_factor = var_zone_cooling_sizing_factor
        # alpha
        var_cooling_design_air_flow_method = "Flow/Zone"
        obj.cooling_design_air_flow_method = var_cooling_design_air_flow_method
        # real
        var_cooling_design_air_flow_rate = 0.0
        obj.cooling_design_air_flow_rate = var_cooling_design_air_flow_rate
        # real
        var_cooling_minimum_air_flow_per_zone_floor_area = 0.0
        obj.cooling_minimum_air_flow_per_zone_floor_area = var_cooling_minimum_air_flow_per_zone_floor_area
        # real
        var_cooling_minimum_air_flow = 0.0
        obj.cooling_minimum_air_flow = var_cooling_minimum_air_flow
        # real
        var_cooling_minimum_air_flow_fraction = 0.0
        obj.cooling_minimum_air_flow_fraction = var_cooling_minimum_air_flow_fraction
        # alpha
        var_heating_design_air_flow_method = "Flow/Zone"
        obj.heating_design_air_flow_method = var_heating_design_air_flow_method
        # real
        var_heating_design_air_flow_rate = 0.0
        obj.heating_design_air_flow_rate = var_heating_design_air_flow_rate
        # real
        var_heating_maximum_air_flow_per_zone_floor_area = 0.0
        obj.heating_maximum_air_flow_per_zone_floor_area = var_heating_maximum_air_flow_per_zone_floor_area
        # real
        var_heating_maximum_air_flow = 0.0
        obj.heating_maximum_air_flow = var_heating_maximum_air_flow
        # real
        var_heating_maximum_air_flow_fraction = 0.0
        obj.heating_maximum_air_flow_fraction = var_heating_maximum_air_flow_fraction
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name
        # alpha
        var_account_for_dedicated_outdoor_air_system = "Yes"
        obj.account_for_dedicated_outdoor_air_system = var_account_for_dedicated_outdoor_air_system
        # alpha
        var_dedicated_outdoor_air_system_control_strategy = "NeutralSupplyAir"
        obj.dedicated_outdoor_air_system_control_strategy = var_dedicated_outdoor_air_system_control_strategy
        # real
        var_dedicated_outdoor_air_low_setpoint_temperature_for_design = 26.26
        obj.dedicated_outdoor_air_low_setpoint_temperature_for_design = var_dedicated_outdoor_air_low_setpoint_temperature_for_design
        # real
        var_dedicated_outdoor_air_high_setpoint_temperature_for_design = 27.27
        obj.dedicated_outdoor_air_high_setpoint_temperature_for_design = var_dedicated_outdoor_air_high_setpoint_temperature_for_design

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sizingzones[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.sizingzones[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.sizingzones[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_cooling_design_supply_air_humidity_ratio, var_zone_cooling_design_supply_air_humidity_ratio)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_heating_design_supply_air_humidity_ratio, var_zone_heating_design_supply_air_humidity_ratio)
        self.assertEqual(idf2.sizingzones[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.sizingzones[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertEqual(idf2.sizingzones[0].cooling_design_air_flow_method, var_cooling_design_air_flow_method)
        self.assertAlmostEqual(idf2.sizingzones[0].cooling_design_air_flow_rate, var_cooling_design_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingzones[0].cooling_minimum_air_flow_per_zone_floor_area, var_cooling_minimum_air_flow_per_zone_floor_area)
        self.assertAlmostEqual(idf2.sizingzones[0].cooling_minimum_air_flow, var_cooling_minimum_air_flow)
        self.assertAlmostEqual(idf2.sizingzones[0].cooling_minimum_air_flow_fraction, var_cooling_minimum_air_flow_fraction)
        self.assertEqual(idf2.sizingzones[0].heating_design_air_flow_method, var_heating_design_air_flow_method)
        self.assertAlmostEqual(idf2.sizingzones[0].heating_design_air_flow_rate, var_heating_design_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingzones[0].heating_maximum_air_flow_per_zone_floor_area, var_heating_maximum_air_flow_per_zone_floor_area)
        self.assertAlmostEqual(idf2.sizingzones[0].heating_maximum_air_flow, var_heating_maximum_air_flow)
        self.assertAlmostEqual(idf2.sizingzones[0].heating_maximum_air_flow_fraction, var_heating_maximum_air_flow_fraction)
        self.assertEqual(idf2.sizingzones[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)
        self.assertEqual(idf2.sizingzones[0].account_for_dedicated_outdoor_air_system, var_account_for_dedicated_outdoor_air_system)
        self.assertEqual(idf2.sizingzones[0].dedicated_outdoor_air_system_control_strategy, var_dedicated_outdoor_air_system_control_strategy)
        self.assertAlmostEqual(idf2.sizingzones[0].dedicated_outdoor_air_low_setpoint_temperature_for_design, var_dedicated_outdoor_air_low_setpoint_temperature_for_design)
        self.assertAlmostEqual(idf2.sizingzones[0].dedicated_outdoor_air_high_setpoint_temperature_for_design, var_dedicated_outdoor_air_high_setpoint_temperature_for_design)