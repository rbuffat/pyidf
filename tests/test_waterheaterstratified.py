import os
import tempfile
import unittest
import pyidf
from pyidf.water_heaters_and_thermal_storage import WaterHeaterStratified
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWaterHeaterStratified(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterheaterstratified(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterHeaterStratified()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_tank_volume = 0.0001
        obj.tank_volume = var_tank_volume
        # real
        var_tank_height = 0.0001
        obj.tank_height = var_tank_height
        # alpha
        var_tank_shape = "VerticalCylinder"
        obj.tank_shape = var_tank_shape
        # real
        var_tank_perimeter = 0.0
        obj.tank_perimeter = var_tank_perimeter
        # real
        var_maximum_temperature_limit = 7.7
        obj.maximum_temperature_limit = var_maximum_temperature_limit
        # alpha
        var_heater_priority_control = "MasterSlave"
        obj.heater_priority_control = var_heater_priority_control
        # object-list
        var_heater_1_setpoint_temperature_schedule_name = "object-list|Heater 1 Setpoint Temperature Schedule Name"
        obj.heater_1_setpoint_temperature_schedule_name = var_heater_1_setpoint_temperature_schedule_name
        # real
        var_heater_1_deadband_temperature_difference = 0.0
        obj.heater_1_deadband_temperature_difference = var_heater_1_deadband_temperature_difference
        # real
        var_heater_1_capacity = 0.0
        obj.heater_1_capacity = var_heater_1_capacity
        # real
        var_heater_1_height = 0.0
        obj.heater_1_height = var_heater_1_height
        # object-list
        var_heater_2_setpoint_temperature_schedule_name = "object-list|Heater 2 Setpoint Temperature Schedule Name"
        obj.heater_2_setpoint_temperature_schedule_name = var_heater_2_setpoint_temperature_schedule_name
        # real
        var_heater_2_deadband_temperature_difference = 0.0
        obj.heater_2_deadband_temperature_difference = var_heater_2_deadband_temperature_difference
        # real
        var_heater_2_capacity = 0.0
        obj.heater_2_capacity = var_heater_2_capacity
        # real
        var_heater_2_height = 0.0
        obj.heater_2_height = var_heater_2_height
        # alpha
        var_heater_fuel_type = "Electricity"
        obj.heater_fuel_type = var_heater_fuel_type
        # real
        var_heater_thermal_efficiency = 0.50005
        obj.heater_thermal_efficiency = var_heater_thermal_efficiency
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
        var_off_cycle_parasitic_height = 0.0
        obj.off_cycle_parasitic_height = var_off_cycle_parasitic_height
        # real
        var_on_cycle_parasitic_fuel_consumption_rate = 0.0
        obj.on_cycle_parasitic_fuel_consumption_rate = var_on_cycle_parasitic_fuel_consumption_rate
        # alpha
        var_on_cycle_parasitic_fuel_type = "Electricity"
        obj.on_cycle_parasitic_fuel_type = var_on_cycle_parasitic_fuel_type
        # real
        var_on_cycle_parasitic_heat_fraction_to_tank = 0.5
        obj.on_cycle_parasitic_heat_fraction_to_tank = var_on_cycle_parasitic_heat_fraction_to_tank
        # real
        var_on_cycle_parasitic_height = 0.0
        obj.on_cycle_parasitic_height = var_on_cycle_parasitic_height
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
        var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = 0.0
        obj.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature
        # real
        var_skin_loss_fraction_to_zone = 0.5
        obj.skin_loss_fraction_to_zone = var_skin_loss_fraction_to_zone
        # real
        var_off_cycle_flue_loss_coefficient_to_ambient_temperature = 0.0
        obj.off_cycle_flue_loss_coefficient_to_ambient_temperature = var_off_cycle_flue_loss_coefficient_to_ambient_temperature
        # real
        var_off_cycle_flue_loss_fraction_to_zone = 0.5
        obj.off_cycle_flue_loss_fraction_to_zone = var_off_cycle_flue_loss_fraction_to_zone
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
        # real
        var_use_side_inlet_height = 0.0
        obj.use_side_inlet_height = var_use_side_inlet_height
        # real
        var_use_side_outlet_height = 0.0
        obj.use_side_outlet_height = var_use_side_outlet_height
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
        var_source_side_inlet_height = 0.0
        obj.source_side_inlet_height = var_source_side_inlet_height
        # real
        var_source_side_outlet_height = 0.0
        obj.source_side_outlet_height = var_source_side_outlet_height
        # alpha
        var_inlet_mode = "Fixed"
        obj.inlet_mode = var_inlet_mode
        # real
        var_use_side_design_flow_rate = 0.0
        obj.use_side_design_flow_rate = var_use_side_design_flow_rate
        # real
        var_source_side_design_flow_rate = 0.0
        obj.source_side_design_flow_rate = var_source_side_design_flow_rate
        # real
        var_indirect_water_heating_recovery_time = 0.0001
        obj.indirect_water_heating_recovery_time = var_indirect_water_heating_recovery_time
        # integer
        var_number_of_nodes = 5
        obj.number_of_nodes = var_number_of_nodes
        # real
        var_additional_destratification_conductivity = 0.0
        obj.additional_destratification_conductivity = var_additional_destratification_conductivity
        # real
        var_node_1_additional_loss_coefficient = 54.54
        obj.node_1_additional_loss_coefficient = var_node_1_additional_loss_coefficient
        # real
        var_node_2_additional_loss_coefficient = 55.55
        obj.node_2_additional_loss_coefficient = var_node_2_additional_loss_coefficient
        # real
        var_node_3_additional_loss_coefficient = 56.56
        obj.node_3_additional_loss_coefficient = var_node_3_additional_loss_coefficient
        # real
        var_node_4_additional_loss_coefficient = 57.57
        obj.node_4_additional_loss_coefficient = var_node_4_additional_loss_coefficient
        # real
        var_node_5_additional_loss_coefficient = 58.58
        obj.node_5_additional_loss_coefficient = var_node_5_additional_loss_coefficient
        # real
        var_node_6_additional_loss_coefficient = 59.59
        obj.node_6_additional_loss_coefficient = var_node_6_additional_loss_coefficient
        # real
        var_node_7_additional_loss_coefficient = 60.6
        obj.node_7_additional_loss_coefficient = var_node_7_additional_loss_coefficient
        # real
        var_node_8_additional_loss_coefficient = 61.61
        obj.node_8_additional_loss_coefficient = var_node_8_additional_loss_coefficient
        # real
        var_node_9_additional_loss_coefficient = 62.62
        obj.node_9_additional_loss_coefficient = var_node_9_additional_loss_coefficient
        # real
        var_node_10_additional_loss_coefficient = 63.63
        obj.node_10_additional_loss_coefficient = var_node_10_additional_loss_coefficient
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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterheaterstratifieds[0].name, var_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].tank_volume, var_tank_volume)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].tank_height, var_tank_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].tank_shape, var_tank_shape)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].tank_perimeter, var_tank_perimeter)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].maximum_temperature_limit, var_maximum_temperature_limit)
        self.assertEqual(idf2.waterheaterstratifieds[0].heater_priority_control, var_heater_priority_control)
        self.assertEqual(idf2.waterheaterstratifieds[0].heater_1_setpoint_temperature_schedule_name, var_heater_1_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_1_deadband_temperature_difference, var_heater_1_deadband_temperature_difference)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_1_capacity, var_heater_1_capacity)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_1_height, var_heater_1_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].heater_2_setpoint_temperature_schedule_name, var_heater_2_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_2_deadband_temperature_difference, var_heater_2_deadband_temperature_difference)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_2_capacity, var_heater_2_capacity)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_2_height, var_heater_2_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].heater_fuel_type, var_heater_fuel_type)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].heater_thermal_efficiency, var_heater_thermal_efficiency)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].off_cycle_parasitic_fuel_consumption_rate, var_off_cycle_parasitic_fuel_consumption_rate)
        self.assertEqual(idf2.waterheaterstratifieds[0].off_cycle_parasitic_fuel_type, var_off_cycle_parasitic_fuel_type)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].off_cycle_parasitic_heat_fraction_to_tank, var_off_cycle_parasitic_heat_fraction_to_tank)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].off_cycle_parasitic_height, var_off_cycle_parasitic_height)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].on_cycle_parasitic_fuel_consumption_rate, var_on_cycle_parasitic_fuel_consumption_rate)
        self.assertEqual(idf2.waterheaterstratifieds[0].on_cycle_parasitic_fuel_type, var_on_cycle_parasitic_fuel_type)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].on_cycle_parasitic_heat_fraction_to_tank, var_on_cycle_parasitic_heat_fraction_to_tank)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].on_cycle_parasitic_height, var_on_cycle_parasitic_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].ambient_temperature_indicator, var_ambient_temperature_indicator)
        self.assertEqual(idf2.waterheaterstratifieds[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].ambient_temperature_zone_name, var_ambient_temperature_zone_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].ambient_temperature_outdoor_air_node_name, var_ambient_temperature_outdoor_air_node_name)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature, var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].skin_loss_fraction_to_zone, var_skin_loss_fraction_to_zone)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].off_cycle_flue_loss_coefficient_to_ambient_temperature, var_off_cycle_flue_loss_coefficient_to_ambient_temperature)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].off_cycle_flue_loss_fraction_to_zone, var_off_cycle_flue_loss_fraction_to_zone)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].peak_use_flow_rate, var_peak_use_flow_rate)
        self.assertEqual(idf2.waterheaterstratifieds[0].use_flow_rate_fraction_schedule_name, var_use_flow_rate_fraction_schedule_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].cold_water_supply_temperature_schedule_name, var_cold_water_supply_temperature_schedule_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].use_side_inlet_node_name, var_use_side_inlet_node_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].use_side_outlet_node_name, var_use_side_outlet_node_name)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].use_side_effectiveness, var_use_side_effectiveness)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].use_side_inlet_height, var_use_side_inlet_height)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].use_side_outlet_height, var_use_side_outlet_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.waterheaterstratifieds[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].source_side_effectiveness, var_source_side_effectiveness)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].source_side_inlet_height, var_source_side_inlet_height)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].source_side_outlet_height, var_source_side_outlet_height)
        self.assertEqual(idf2.waterheaterstratifieds[0].inlet_mode, var_inlet_mode)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].use_side_design_flow_rate, var_use_side_design_flow_rate)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].source_side_design_flow_rate, var_source_side_design_flow_rate)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].indirect_water_heating_recovery_time, var_indirect_water_heating_recovery_time)
        self.assertEqual(idf2.waterheaterstratifieds[0].number_of_nodes, var_number_of_nodes)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].additional_destratification_conductivity, var_additional_destratification_conductivity)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_1_additional_loss_coefficient, var_node_1_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_2_additional_loss_coefficient, var_node_2_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_3_additional_loss_coefficient, var_node_3_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_4_additional_loss_coefficient, var_node_4_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_5_additional_loss_coefficient, var_node_5_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_6_additional_loss_coefficient, var_node_6_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_7_additional_loss_coefficient, var_node_7_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_8_additional_loss_coefficient, var_node_8_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_9_additional_loss_coefficient, var_node_9_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.waterheaterstratifieds[0].node_10_additional_loss_coefficient, var_node_10_additional_loss_coefficient)
        self.assertEqual(idf2.waterheaterstratifieds[0].source_side_flow_control_mode, var_source_side_flow_control_mode)
        self.assertEqual(idf2.waterheaterstratifieds[0].indirect_alternate_setpoint_temperature_schedule_name, var_indirect_alternate_setpoint_temperature_schedule_name)