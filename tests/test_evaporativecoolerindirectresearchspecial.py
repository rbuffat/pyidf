import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.evaporative_coolers import EvaporativeCoolerIndirectResearchSpecial

log = logging.getLogger(__name__)

class TestEvaporativeCoolerIndirectResearchSpecial(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativecoolerindirectresearchspecial(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeCoolerIndirectResearchSpecial()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_cooler_wetbulb_design_effectiveness = 1.0
        obj.cooler_wetbulb_design_effectiveness = var_cooler_wetbulb_design_effectiveness
        # object-list
        var_wetbulb_effectiveness_flow_ratio_modifier_curve_name = "object-list|Wetbulb Effectiveness Flow Ratio Modifier Curve Name"
        obj.wetbulb_effectiveness_flow_ratio_modifier_curve_name = var_wetbulb_effectiveness_flow_ratio_modifier_curve_name
        # real
        var_cooler_drybulb_design_effectiveness = 0.0
        obj.cooler_drybulb_design_effectiveness = var_cooler_drybulb_design_effectiveness
        # object-list
        var_drybulb_effectiveness_flow_ratio_modifier_curve_name = "object-list|Drybulb Effectiveness Flow Ratio Modifier Curve Name"
        obj.drybulb_effectiveness_flow_ratio_modifier_curve_name = var_drybulb_effectiveness_flow_ratio_modifier_curve_name
        # real
        var_recirculating_water_pump_design_power = 7.7
        obj.recirculating_water_pump_design_power = var_recirculating_water_pump_design_power
        # real
        var_water_pump_power_sizing_factor = 8.8
        obj.water_pump_power_sizing_factor = var_water_pump_power_sizing_factor
        # object-list
        var_water_pump_power_modifier_curve_name = "object-list|Water Pump Power Modifier Curve Name"
        obj.water_pump_power_modifier_curve_name = var_water_pump_power_modifier_curve_name
        # real
        var_secondary_air_design_flow_rate = 0.0001
        obj.secondary_air_design_flow_rate = var_secondary_air_design_flow_rate
        # real
        var_secondary_air_flow_scaling_factor = 11.11
        obj.secondary_air_flow_scaling_factor = var_secondary_air_flow_scaling_factor
        # real
        var_secondary_air_fan_design_power = 12.12
        obj.secondary_air_fan_design_power = var_secondary_air_fan_design_power
        # real
        var_secondary_air_fan_sizing_specific_power = 13.13
        obj.secondary_air_fan_sizing_specific_power = var_secondary_air_fan_sizing_specific_power
        # object-list
        var_secondary_air_fan_power_modifier_curve_name = "object-list|Secondary Air Fan Power Modifier Curve Name"
        obj.secondary_air_fan_power_modifier_curve_name = var_secondary_air_fan_power_modifier_curve_name
        # node
        var_primary_air_inlet_node_name = "node|Primary Air Inlet Node Name"
        obj.primary_air_inlet_node_name = var_primary_air_inlet_node_name
        # node
        var_primary_air_outlet_node_name = "node|Primary Air Outlet Node Name"
        obj.primary_air_outlet_node_name = var_primary_air_outlet_node_name
        # real
        var_primary_air_design_flow_rate = 0.0001
        obj.primary_air_design_flow_rate = var_primary_air_design_flow_rate
        # real
        var_dewpoint_effectiveness_factor = 0.0
        obj.dewpoint_effectiveness_factor = var_dewpoint_effectiveness_factor
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name
        # node
        var_secondary_air_outlet_node_name = "node|Secondary Air Outlet Node Name"
        obj.secondary_air_outlet_node_name = var_secondary_air_outlet_node_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # node
        var_relief_air_inlet_node_name = "node|Relief Air Inlet Node Name"
        obj.relief_air_inlet_node_name = var_relief_air_inlet_node_name
        # object-list
        var_water_supply_storage_tank_name = "object-list|Water Supply Storage Tank Name"
        obj.water_supply_storage_tank_name = var_water_supply_storage_tank_name
        # real
        var_drift_loss_fraction = 0.0
        obj.drift_loss_fraction = var_drift_loss_fraction
        # real
        var_blowdown_concentration_ratio = 2.0
        obj.blowdown_concentration_ratio = var_blowdown_concentration_ratio
        # real
        var_evaporative_operation_minimum_limit_secondary_air_drybulb_temperature = 26.26
        obj.evaporative_operation_minimum_limit_secondary_air_drybulb_temperature = var_evaporative_operation_minimum_limit_secondary_air_drybulb_temperature
        # real
        var_evaporative_operation_maximum_limit_outdoor_wetbulb_temperature = 27.27
        obj.evaporative_operation_maximum_limit_outdoor_wetbulb_temperature = var_evaporative_operation_maximum_limit_outdoor_wetbulb_temperature
        # real
        var_dry_operation_maximum_limit_outdoor_drybulb_temperature = 28.28
        obj.dry_operation_maximum_limit_outdoor_drybulb_temperature = var_dry_operation_maximum_limit_outdoor_drybulb_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].name, var_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].cooler_wetbulb_design_effectiveness, var_cooler_wetbulb_design_effectiveness)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].wetbulb_effectiveness_flow_ratio_modifier_curve_name, var_wetbulb_effectiveness_flow_ratio_modifier_curve_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].cooler_drybulb_design_effectiveness, var_cooler_drybulb_design_effectiveness)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].drybulb_effectiveness_flow_ratio_modifier_curve_name, var_drybulb_effectiveness_flow_ratio_modifier_curve_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].recirculating_water_pump_design_power, var_recirculating_water_pump_design_power)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].water_pump_power_sizing_factor, var_water_pump_power_sizing_factor)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].water_pump_power_modifier_curve_name, var_water_pump_power_modifier_curve_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_design_flow_rate, var_secondary_air_design_flow_rate)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_flow_scaling_factor, var_secondary_air_flow_scaling_factor)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_fan_design_power, var_secondary_air_fan_design_power)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_fan_sizing_specific_power, var_secondary_air_fan_sizing_specific_power)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_fan_power_modifier_curve_name, var_secondary_air_fan_power_modifier_curve_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].primary_air_inlet_node_name, var_primary_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].primary_air_outlet_node_name, var_primary_air_outlet_node_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].primary_air_design_flow_rate, var_primary_air_design_flow_rate)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].dewpoint_effectiveness_factor, var_dewpoint_effectiveness_factor)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_outlet_node_name, var_secondary_air_outlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].sensor_node_name, var_sensor_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].relief_air_inlet_node_name, var_relief_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].drift_loss_fraction, var_drift_loss_fraction)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].evaporative_operation_minimum_limit_secondary_air_drybulb_temperature, var_evaporative_operation_minimum_limit_secondary_air_drybulb_temperature)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].evaporative_operation_maximum_limit_outdoor_wetbulb_temperature, var_evaporative_operation_maximum_limit_outdoor_wetbulb_temperature)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].dry_operation_maximum_limit_outdoor_drybulb_temperature, var_dry_operation_maximum_limit_outdoor_drybulb_temperature)