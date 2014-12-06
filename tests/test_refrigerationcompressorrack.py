import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationCompressorRack

log = logging.getLogger(__name__)

class TestRefrigerationCompressorRack(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcompressorrack(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCompressorRack()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_heat_rejection_location = "Outdoors"
        obj.heat_rejection_location = var_heat_rejection_location
        # real
        var_design_compressor_rack_cop = 0.0001
        obj.design_compressor_rack_cop = var_design_compressor_rack_cop
        # object-list
        var_compressor_rack_cop_function_of_temperature_curve_name = "object-list|Compressor Rack COP Function of Temperature Curve Name"
        obj.compressor_rack_cop_function_of_temperature_curve_name = var_compressor_rack_cop_function_of_temperature_curve_name
        # real
        var_design_condenser_fan_power = 0.0
        obj.design_condenser_fan_power = var_design_condenser_fan_power
        # object-list
        var_condenser_fan_power_function_of_temperature_curve_name = "object-list|Condenser Fan Power Function of Temperature Curve Name"
        obj.condenser_fan_power_function_of_temperature_curve_name = var_condenser_fan_power_function_of_temperature_curve_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # node
        var_watercooled_condenser_inlet_node_name = "node|Water-Cooled Condenser Inlet Node Name"
        obj.watercooled_condenser_inlet_node_name = var_watercooled_condenser_inlet_node_name
        # node
        var_watercooled_condenser_outlet_node_name = "node|Water-Cooled Condenser Outlet Node Name"
        obj.watercooled_condenser_outlet_node_name = var_watercooled_condenser_outlet_node_name
        # alpha
        var_watercooled_loop_flow_type = "VariableFlow"
        obj.watercooled_loop_flow_type = var_watercooled_loop_flow_type
        # object-list
        var_watercooled_condenser_outlet_temperature_schedule_name = "object-list|Water-Cooled Condenser Outlet Temperature Schedule Name"
        obj.watercooled_condenser_outlet_temperature_schedule_name = var_watercooled_condenser_outlet_temperature_schedule_name
        # real
        var_watercooled_condenser_design_flow_rate = 0.0001
        obj.watercooled_condenser_design_flow_rate = var_watercooled_condenser_design_flow_rate
        # real
        var_watercooled_condenser_maximum_flow_rate = 0.0001
        obj.watercooled_condenser_maximum_flow_rate = var_watercooled_condenser_maximum_flow_rate
        # real
        var_watercooled_condenser_maximum_water_outlet_temperature = 35.0
        obj.watercooled_condenser_maximum_water_outlet_temperature = var_watercooled_condenser_maximum_water_outlet_temperature
        # real
        var_watercooled_condenser_minimum_water_inlet_temperature = 20.0
        obj.watercooled_condenser_minimum_water_inlet_temperature = var_watercooled_condenser_minimum_water_inlet_temperature
        # object-list
        var_evaporative_condenser_availability_schedule_name = "object-list|Evaporative Condenser Availability Schedule Name"
        obj.evaporative_condenser_availability_schedule_name = var_evaporative_condenser_availability_schedule_name
        # real
        var_evaporative_condenser_effectiveness = 0.5
        obj.evaporative_condenser_effectiveness = var_evaporative_condenser_effectiveness
        # real
        var_evaporative_condenser_air_flow_rate = 0.0001
        obj.evaporative_condenser_air_flow_rate = var_evaporative_condenser_air_flow_rate
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # real
        var_design_evaporative_condenser_water_pump_power = 0.0
        obj.design_evaporative_condenser_water_pump_power = var_design_evaporative_condenser_water_pump_power
        # object-list
        var_evaporative_water_supply_tank_name = "object-list|Evaporative Water Supply Tank Name"
        obj.evaporative_water_supply_tank_name = var_evaporative_water_supply_tank_name
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # object-list
        var_refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name = "object-list|Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"
        obj.refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name = var_refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name
        # object-list
        var_heat_rejection_zone_name = "object-list|Heat Rejection Zone Name"
        obj.heat_rejection_zone_name = var_heat_rejection_zone_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcompressorracks[0].name, var_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].heat_rejection_location, var_heat_rejection_location)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].design_compressor_rack_cop, var_design_compressor_rack_cop)
        self.assertEqual(idf2.refrigerationcompressorracks[0].compressor_rack_cop_function_of_temperature_curve_name, var_compressor_rack_cop_function_of_temperature_curve_name)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].design_condenser_fan_power, var_design_condenser_fan_power)
        self.assertEqual(idf2.refrigerationcompressorracks[0].condenser_fan_power_function_of_temperature_curve_name, var_condenser_fan_power_function_of_temperature_curve_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_inlet_node_name, var_watercooled_condenser_inlet_node_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_outlet_node_name, var_watercooled_condenser_outlet_node_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].watercooled_loop_flow_type, var_watercooled_loop_flow_type)
        self.assertEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_outlet_temperature_schedule_name, var_watercooled_condenser_outlet_temperature_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_design_flow_rate, var_watercooled_condenser_design_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_maximum_flow_rate, var_watercooled_condenser_maximum_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_maximum_water_outlet_temperature, var_watercooled_condenser_maximum_water_outlet_temperature)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].watercooled_condenser_minimum_water_inlet_temperature, var_watercooled_condenser_minimum_water_inlet_temperature)
        self.assertEqual(idf2.refrigerationcompressorracks[0].evaporative_condenser_availability_schedule_name, var_evaporative_condenser_availability_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].evaporative_condenser_air_flow_rate, var_evaporative_condenser_air_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertAlmostEqual(idf2.refrigerationcompressorracks[0].design_evaporative_condenser_water_pump_power, var_design_evaporative_condenser_water_pump_power)
        self.assertEqual(idf2.refrigerationcompressorracks[0].evaporative_water_supply_tank_name, var_evaporative_water_supply_tank_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.refrigerationcompressorracks[0].refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name, var_refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name)
        self.assertEqual(idf2.refrigerationcompressorracks[0].heat_rejection_zone_name, var_heat_rejection_zone_name)