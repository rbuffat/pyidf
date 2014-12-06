import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationCondenserEvaporativeCooled
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationCondenserEvaporativeCooled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcondenserevaporativecooled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCondenserEvaporativeCooled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_rated_effective_total_heat_rejection_rate = 0.0
        obj.rated_effective_total_heat_rejection_rate = var_rated_effective_total_heat_rejection_rate
        # real
        var_rated_subcooling_temperature_difference = 0.0
        obj.rated_subcooling_temperature_difference = var_rated_subcooling_temperature_difference
        # alpha
        var_fan_speed_control_type = "Fixed"
        obj.fan_speed_control_type = var_fan_speed_control_type
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_minimum_fan_air_flow_ratio = 0.0
        obj.minimum_fan_air_flow_ratio = var_minimum_fan_air_flow_ratio
        # real
        var_approach_temperature_constant_term = 10.0
        obj.approach_temperature_constant_term = var_approach_temperature_constant_term
        # real
        var_approach_temperature_coefficient_2 = 10.0
        obj.approach_temperature_coefficient_2 = var_approach_temperature_coefficient_2
        # real
        var_approach_temperature_coefficient_3 = 15.0
        obj.approach_temperature_coefficient_3 = var_approach_temperature_coefficient_3
        # real
        var_approach_temperature_coefficient_4 = 0.0
        obj.approach_temperature_coefficient_4 = var_approach_temperature_coefficient_4
        # real
        var_minimum_capacity_factor = 11.11
        obj.minimum_capacity_factor = var_minimum_capacity_factor
        # real
        var_maximum_capacity_factor = 12.12
        obj.maximum_capacity_factor = var_maximum_capacity_factor
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # real
        var_rated_air_flow_rate = 14.14
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # real
        var_rated_water_pump_power = 17.17
        obj.rated_water_pump_power = var_rated_water_pump_power
        # object-list
        var_evaporative_water_supply_tank_name = "object-list|Evaporative Water Supply Tank Name"
        obj.evaporative_water_supply_tank_name = var_evaporative_water_supply_tank_name
        # object-list
        var_evaporative_condenser_availability_schedule_name = "object-list|Evaporative Condenser Availability Schedule Name"
        obj.evaporative_condenser_availability_schedule_name = var_evaporative_condenser_availability_schedule_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_condenser_refrigerant_operating_charge_inventory = 21.21
        obj.condenser_refrigerant_operating_charge_inventory = var_condenser_refrigerant_operating_charge_inventory
        # real
        var_condensate_receiver_refrigerant_inventory = 22.22
        obj.condensate_receiver_refrigerant_inventory = var_condensate_receiver_refrigerant_inventory
        # real
        var_condensate_piping_refrigerant_inventory = 23.23
        obj.condensate_piping_refrigerant_inventory = var_condensate_piping_refrigerant_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].name, var_name)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].rated_effective_total_heat_rejection_rate, var_rated_effective_total_heat_rejection_rate)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].rated_subcooling_temperature_difference, var_rated_subcooling_temperature_difference)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].fan_speed_control_type, var_fan_speed_control_type)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].minimum_fan_air_flow_ratio, var_minimum_fan_air_flow_ratio)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].approach_temperature_constant_term, var_approach_temperature_constant_term)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].approach_temperature_coefficient_2, var_approach_temperature_coefficient_2)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].approach_temperature_coefficient_3, var_approach_temperature_coefficient_3)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].approach_temperature_coefficient_4, var_approach_temperature_coefficient_4)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].minimum_capacity_factor, var_minimum_capacity_factor)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].maximum_capacity_factor, var_maximum_capacity_factor)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].rated_water_pump_power, var_rated_water_pump_power)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].evaporative_water_supply_tank_name, var_evaporative_water_supply_tank_name)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].evaporative_condenser_availability_schedule_name, var_evaporative_condenser_availability_schedule_name)
        self.assertEqual(idf2.refrigerationcondenserevaporativecooleds[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].condenser_refrigerant_operating_charge_inventory, var_condenser_refrigerant_operating_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].condensate_receiver_refrigerant_inventory, var_condensate_receiver_refrigerant_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenserevaporativecooleds[0].condensate_piping_refrigerant_inventory, var_condensate_piping_refrigerant_inventory)