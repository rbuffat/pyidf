import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import WaterHeaterMixed

log = logging.getLogger(__name__)

class TestWaterHeaterMixed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterheatermixed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterHeaterMixed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_tank_volume = 0.0
        obj.tank_volume = var_tank_volume
        # object-list
        var_setpoint_temperature_schedule_name = "object-list|Setpoint Temperature Schedule Name"
        obj.setpoint_temperature_schedule_name = var_setpoint_temperature_schedule_name
        # real
        var_deadband_temperature_difference = 0.0
        obj.deadband_temperature_difference = var_deadband_temperature_difference
        # real
        var_maximum_temperature_limit = 5.5
        obj.maximum_temperature_limit = var_maximum_temperature_limit
        # alpha
        var_heater_control_type = "Cycle"
        obj.heater_control_type = var_heater_control_type
        # real
        var_heater_maximum_capacity = 0.0
        obj.heater_maximum_capacity = var_heater_maximum_capacity
        # real
        var_heater_minimum_capacity = 0.0
        obj.heater_minimum_capacity = var_heater_minimum_capacity
        # real
        var_heater_ignition_minimum_flow_rate = 0.0
        obj.heater_ignition_minimum_flow_rate = var_heater_ignition_minimum_flow_rate
        # real
        var_heater_ignition_delay = 0.0
        obj.heater_ignition_delay = var_heater_ignition_delay
        # alpha
        var_heater_fuel_type = "Electricity"
        obj.heater_fuel_type = var_heater_fuel_type
        # real
        var_heater_thermal_efficiency = 0.50005
        obj.heater_thermal_efficiency = var_heater_thermal_efficiency
        # object-list
        var_part_load_factor_curve_name = "object-list|Part Load Factor Curve Name"
        obj.part_load_factor_curve_name = var_part_load_factor_curve_name
        # real
        var_off_cycle_parasitic_fuel_consumption_rate = 0.0
        obj.off_cycle_parasitic_fuel_consumption_rate = var_off_cycle_parasitic_fuel_consumption_rate
        # alpha
        var_off_cycle_parasitic_fuel_type = "Electricity"
        obj.off_cycle_parasitic_fuel_type = var_off_cycle_parasitic_fuel_type
        # real
        var_off_cycle_parasitic_heat_fraction_to_tank = 0.5
        obj.off_cycle_parasitic_heat_fraction_to_tank = var_off_cycle_parasitic_heat_fraction_to_tank
        # real
        var_on_cycle_parasitic_fuel_consumption_rate = 0.0
        obj.on_cycle_parasitic_fuel_consumption_rate = var_on_cycle_parasitic_fuel_consumption_rate
        # alpha
        var_on_cycle_parasitic_fuel_type = "Electricity"
        obj.on_cycle_parasitic_fuel_type = var_on_cycle_parasitic_fuel_type
        # real
        var_on_cycle_parasitic_heat_fraction_to_tank = 0.5
        obj.on_cycle_parasitic_heat_fraction_to_tank = var_on_cycle_parasitic_heat_fraction_to_tank
        # alpha
        var_ambient_temperature_indicator = "Schedule"
        obj.ambient_temperature_indicator = var_ambient_temperature_indicator
        # object-list
        var_ambient_temperature_schedule_name = "object-list|Ambient Temperature Schedule Name"
        obj.ambient_temperature_schedule_name = var_ambient_temperature_schedule_name
        # object-list
        var_ambient_temperature_zone_name = "object-list|Ambient Temperature Zone Name"
        obj.ambient_temperature_zone_name = var_ambient_temperature_zone_name
        # node
        var_ambient_temperature_outdoor_air_node_name = "node|Ambient Temperature Outdoor Air Node Name"
        obj.ambient_temperature_outdoor_air_node_name = var_ambient_temperature_outdoor_air_node_name
        # real
        var_off_cycle_loss_coefficient_to_ambient_temperature = 0.0
        obj.off_cycle_loss_coefficient_to_ambient_temperature = var_off_cycle_loss_coefficient_to_ambient_temperature
        # real
        var_off_cycle_loss_fraction_to_zone = 0.5
        obj.off_cycle_loss_fraction_to_zone = var_off_cycle_loss_fraction_to_zone
        # real
        var_on_cycle_loss_coefficient_to_ambient_temperature = 0.0
        obj.on_cycle_loss_coefficient_to_ambient_temperature = var_on_cycle_loss_coefficient_to_ambient_temperature
        # real
        var_on_cycle_loss_fraction_to_zone = 0.5
        obj.on_cycle_loss_fraction_to_zone = var_on_cycle_loss_fraction_to_zone
        # real
        var_peak_use_flow_rate = 0.0
        obj.peak_use_flow_rate = var_peak_use_flow_rate
        # object-list
        var_use_flow_rate_fraction_schedule_name = "object-list|Use Flow Rate Fraction Schedule Name"
        obj.use_flow_rate_fraction_schedule_name = var_use_flow_rate_fraction_schedule_name
        # object-list
        var_cold_water_supply_temperature_schedule_name = "object-list|Cold Water Supply Temperature Schedule Name"
        obj.cold_water_supply_temperature_schedule_name = var_cold_water_supply_temperature_schedule_name
        # node
        var_use_side_inlet_node_name = "node|Use Side Inlet Node Name"
        obj.use_side_inlet_node_name = var_use_side_inlet_node_name
        # node
        var_use_side_outlet_node_name = "node|Use Side Outlet Node Name"
        obj.use_side_outlet_node_name = var_use_side_outlet_node_name
        # real
        var_use_side_effectiveness = 0.5
        obj.use_side_effectiveness = var_use_side_effectiveness
        # node
        var_source_side_inlet_node_name = "node|Source Side Inlet Node Name"
        obj.source_side_inlet_node_name = var_source_side_inlet_node_name
        # node
        var_source_side_outlet_node_name = "node|Source Side Outlet Node Name"
        obj.source_side_outlet_node_name = var_source_side_outlet_node_name
        # real
        var_source_side_effectiveness = 0.5
        obj.source_side_effectiveness = var_source_side_effectiveness
        # real
        var_use_side_design_flow_rate = 0.0
        obj.use_side_design_flow_rate = var_use_side_design_flow_rate
        # real
        var_source_side_design_flow_rate = 0.0
        obj.source_side_design_flow_rate = var_source_side_design_flow_rate
        # real
        var_indirect_water_heating_recovery_time = 0.0001
        obj.indirect_water_heating_recovery_time = var_indirect_water_heating_recovery_time
        # alpha
        var_source_side_flow_control_mode = "StorageTank"
        obj.source_side_flow_control_mode = var_source_side_flow_control_mode
        # object-list
        var_indirect_alternate_setpoint_temperature_schedule_name = "object-list|Indirect Alternate Setpoint Temperature Schedule Name"
        obj.indirect_alternate_setpoint_temperature_schedule_name = var_indirect_alternate_setpoint_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterheatermixeds[0].name, var_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].tank_volume, var_tank_volume)
        self.assertEqual(idf2.waterheatermixeds[0].setpoint_temperature_schedule_name, var_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].deadband_temperature_difference, var_deadband_temperature_difference)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].maximum_temperature_limit, var_maximum_temperature_limit)
        self.assertEqual(idf2.waterheatermixeds[0].heater_control_type, var_heater_control_type)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].heater_maximum_capacity, var_heater_maximum_capacity)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].heater_minimum_capacity, var_heater_minimum_capacity)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].heater_ignition_minimum_flow_rate, var_heater_ignition_minimum_flow_rate)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].heater_ignition_delay, var_heater_ignition_delay)
        self.assertEqual(idf2.waterheatermixeds[0].heater_fuel_type, var_heater_fuel_type)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].heater_thermal_efficiency, var_heater_thermal_efficiency)
        self.assertEqual(idf2.waterheatermixeds[0].part_load_factor_curve_name, var_part_load_factor_curve_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].off_cycle_parasitic_fuel_consumption_rate, var_off_cycle_parasitic_fuel_consumption_rate)
        self.assertEqual(idf2.waterheatermixeds[0].off_cycle_parasitic_fuel_type, var_off_cycle_parasitic_fuel_type)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].off_cycle_parasitic_heat_fraction_to_tank, var_off_cycle_parasitic_heat_fraction_to_tank)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].on_cycle_parasitic_fuel_consumption_rate, var_on_cycle_parasitic_fuel_consumption_rate)
        self.assertEqual(idf2.waterheatermixeds[0].on_cycle_parasitic_fuel_type, var_on_cycle_parasitic_fuel_type)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].on_cycle_parasitic_heat_fraction_to_tank, var_on_cycle_parasitic_heat_fraction_to_tank)
        self.assertEqual(idf2.waterheatermixeds[0].ambient_temperature_indicator, var_ambient_temperature_indicator)
        self.assertEqual(idf2.waterheatermixeds[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.waterheatermixeds[0].ambient_temperature_zone_name, var_ambient_temperature_zone_name)
        self.assertEqual(idf2.waterheatermixeds[0].ambient_temperature_outdoor_air_node_name, var_ambient_temperature_outdoor_air_node_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].off_cycle_loss_coefficient_to_ambient_temperature, var_off_cycle_loss_coefficient_to_ambient_temperature)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].off_cycle_loss_fraction_to_zone, var_off_cycle_loss_fraction_to_zone)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].on_cycle_loss_coefficient_to_ambient_temperature, var_on_cycle_loss_coefficient_to_ambient_temperature)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].on_cycle_loss_fraction_to_zone, var_on_cycle_loss_fraction_to_zone)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].peak_use_flow_rate, var_peak_use_flow_rate)
        self.assertEqual(idf2.waterheatermixeds[0].use_flow_rate_fraction_schedule_name, var_use_flow_rate_fraction_schedule_name)
        self.assertEqual(idf2.waterheatermixeds[0].cold_water_supply_temperature_schedule_name, var_cold_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.waterheatermixeds[0].use_side_inlet_node_name, var_use_side_inlet_node_name)
        self.assertEqual(idf2.waterheatermixeds[0].use_side_outlet_node_name, var_use_side_outlet_node_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].use_side_effectiveness, var_use_side_effectiveness)
        self.assertEqual(idf2.waterheatermixeds[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.waterheatermixeds[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].source_side_effectiveness, var_source_side_effectiveness)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].use_side_design_flow_rate, var_use_side_design_flow_rate)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].source_side_design_flow_rate, var_source_side_design_flow_rate)
        self.assertAlmostEqual(idf2.waterheatermixeds[0].indirect_water_heating_recovery_time, var_indirect_water_heating_recovery_time)
        self.assertEqual(idf2.waterheatermixeds[0].source_side_flow_control_mode, var_source_side_flow_control_mode)
        self.assertEqual(idf2.waterheatermixeds[0].indirect_alternate_setpoint_temperature_schedule_name, var_indirect_alternate_setpoint_temperature_schedule_name)