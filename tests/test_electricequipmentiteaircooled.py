import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.internal_gains import ElectricEquipmentIteAirCooled

log = logging.getLogger(__name__)

class TestElectricEquipmentIteAirCooled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricequipmentiteaircooled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricEquipmentIteAirCooled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # alpha
        var_design_power_input_calculation_method = "Watts/Unit"
        obj.design_power_input_calculation_method = var_design_power_input_calculation_method
        # real
        var_watts_per_unit = 0.0
        obj.watts_per_unit = var_watts_per_unit
        # real
        var_number_of_units = 0.0
        obj.number_of_units = var_number_of_units
        # real
        var_watts_per_zone_floor_area = 0.0
        obj.watts_per_zone_floor_area = var_watts_per_zone_floor_area
        # object-list
        var_design_power_input_schedule_name = "object-list|Design Power Input Schedule Name"
        obj.design_power_input_schedule_name = var_design_power_input_schedule_name
        # object-list
        var_cpu_loading_schedule_name = "object-list|CPU Loading  Schedule Name"
        obj.cpu_loading_schedule_name = var_cpu_loading_schedule_name
        # object-list
        var_cpu_power_input_function_of_loading_and_air_temperature_curve_name = "object-list|CPU Power Input Function of Loading and Air Temperature Curve Name"
        obj.cpu_power_input_function_of_loading_and_air_temperature_curve_name = var_cpu_power_input_function_of_loading_and_air_temperature_curve_name
        # real
        var_design_fan_power_input_fraction = 0.5
        obj.design_fan_power_input_fraction = var_design_fan_power_input_fraction
        # real
        var_design_fan_air_flow_rate_per_power_input = 0.0
        obj.design_fan_air_flow_rate_per_power_input = var_design_fan_air_flow_rate_per_power_input
        # object-list
        var_air_flow_function_of_loading_and_air_temperature_curve_name = "object-list|Air Flow Function of Loading and Air Temperature Curve Name"
        obj.air_flow_function_of_loading_and_air_temperature_curve_name = var_air_flow_function_of_loading_and_air_temperature_curve_name
        # object-list
        var_fan_power_input_function_of_flow_curve_name = "object-list|Fan Power Input Function of Flow Curve Name"
        obj.fan_power_input_function_of_flow_curve_name = var_fan_power_input_function_of_flow_curve_name
        # real
        var_design_entering_air_temperature = 14.14
        obj.design_entering_air_temperature = var_design_entering_air_temperature
        # alpha
        var_environmental_class = "None"
        obj.environmental_class = var_environmental_class
        # alpha
        var_air_inlet_connection_type = "AdjustedSupply"
        obj.air_inlet_connection_type = var_air_inlet_connection_type
        # object-list
        var_air_inlet_room_air_model_node_name = "object-list|Air Inlet Room Air Model Node Name"
        obj.air_inlet_room_air_model_node_name = var_air_inlet_room_air_model_node_name
        # object-list
        var_air_outlet_room_air_model_node_name = "object-list|Air Outlet Room Air Model Node Name"
        obj.air_outlet_room_air_model_node_name = var_air_outlet_room_air_model_node_name
        # node
        var_supply_air_node_name = "node|Supply Air Node Name"
        obj.supply_air_node_name = var_supply_air_node_name
        # real
        var_design_recirculation_fraction = 0.25
        obj.design_recirculation_fraction = var_design_recirculation_fraction
        # object-list
        var_recirculation_function_of_loading_and_supply_temperature_curve_name = "object-list|Recirculation Function of Loading and Supply Temperature Curve Name"
        obj.recirculation_function_of_loading_and_supply_temperature_curve_name = var_recirculation_function_of_loading_and_supply_temperature_curve_name
        # real
        var_design_electric_power_supply_efficiency = 0.50005
        obj.design_electric_power_supply_efficiency = var_design_electric_power_supply_efficiency
        # object-list
        var_electric_power_supply_efficiency_function_of_part_load_ratio_curve_name = "object-list|Electric Power Supply Efficiency Function of Part Load Ratio Curve Name"
        obj.electric_power_supply_efficiency_function_of_part_load_ratio_curve_name = var_electric_power_supply_efficiency_function_of_part_load_ratio_curve_name
        # real
        var_fraction_of_electric_power_supply_losses_to_zone = 0.5
        obj.fraction_of_electric_power_supply_losses_to_zone = var_fraction_of_electric_power_supply_losses_to_zone
        # alpha
        var_cpu_enduse_subcategory = "CPU End-Use Subcategory"
        obj.cpu_enduse_subcategory = var_cpu_enduse_subcategory
        # alpha
        var_fan_enduse_subcategory = "Fan End-Use Subcategory"
        obj.fan_enduse_subcategory = var_fan_enduse_subcategory
        # alpha
        var_electric_power_supply_enduse_subcategory = "Electric Power Supply End-Use Subcategory"
        obj.electric_power_supply_enduse_subcategory = var_electric_power_supply_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].name, var_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].zone_name, var_zone_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].design_power_input_calculation_method, var_design_power_input_calculation_method)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].watts_per_unit, var_watts_per_unit)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].number_of_units, var_number_of_units)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].watts_per_zone_floor_area, var_watts_per_zone_floor_area)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].design_power_input_schedule_name, var_design_power_input_schedule_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].cpu_loading_schedule_name, var_cpu_loading_schedule_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].cpu_power_input_function_of_loading_and_air_temperature_curve_name, var_cpu_power_input_function_of_loading_and_air_temperature_curve_name)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].design_fan_power_input_fraction, var_design_fan_power_input_fraction)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].design_fan_air_flow_rate_per_power_input, var_design_fan_air_flow_rate_per_power_input)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].air_flow_function_of_loading_and_air_temperature_curve_name, var_air_flow_function_of_loading_and_air_temperature_curve_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].fan_power_input_function_of_flow_curve_name, var_fan_power_input_function_of_flow_curve_name)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].design_entering_air_temperature, var_design_entering_air_temperature)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].environmental_class, var_environmental_class)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].air_inlet_connection_type, var_air_inlet_connection_type)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].air_inlet_room_air_model_node_name, var_air_inlet_room_air_model_node_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].air_outlet_room_air_model_node_name, var_air_outlet_room_air_model_node_name)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].supply_air_node_name, var_supply_air_node_name)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].design_recirculation_fraction, var_design_recirculation_fraction)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].recirculation_function_of_loading_and_supply_temperature_curve_name, var_recirculation_function_of_loading_and_supply_temperature_curve_name)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].design_electric_power_supply_efficiency, var_design_electric_power_supply_efficiency)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].electric_power_supply_efficiency_function_of_part_load_ratio_curve_name, var_electric_power_supply_efficiency_function_of_part_load_ratio_curve_name)
        self.assertAlmostEqual(idf2.electricequipmentiteaircooleds[0].fraction_of_electric_power_supply_losses_to_zone, var_fraction_of_electric_power_supply_losses_to_zone)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].cpu_enduse_subcategory, var_cpu_enduse_subcategory)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].fan_enduse_subcategory, var_fan_enduse_subcategory)
        self.assertEqual(idf2.electricequipmentiteaircooleds[0].electric_power_supply_enduse_subcategory, var_electric_power_supply_enduse_subcategory)