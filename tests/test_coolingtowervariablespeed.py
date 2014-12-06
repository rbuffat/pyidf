import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import CoolingTowerVariableSpeed

log = logging.getLogger(__name__)

class TestCoolingTowerVariableSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coolingtowervariablespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoolingTowerVariableSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # alpha
        var_model_type = "CoolToolsCrossFlow"
        obj.model_type = var_model_type
        # object-list
        var_model_coefficient_name = "object-list|Model Coefficient Name"
        obj.model_coefficient_name = var_model_coefficient_name
        # real
        var_design_inlet_air_wetbulb_temperature = 20.0
        obj.design_inlet_air_wetbulb_temperature = var_design_inlet_air_wetbulb_temperature
        # real
        var_design_approach_temperature = 0.0001
        obj.design_approach_temperature = var_design_approach_temperature
        # real
        var_design_range_temperature = 0.0001
        obj.design_range_temperature = var_design_range_temperature
        # real
        var_design_water_flow_rate = 0.0001
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_design_air_flow_rate = 0.0001
        obj.design_air_flow_rate = var_design_air_flow_rate
        # real
        var_design_fan_power = 0.0001
        obj.design_fan_power = var_design_fan_power
        # object-list
        var_fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = "object-list|Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"
        obj.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = var_fan_power_ratio_function_of_air_flow_rate_ratio_curve_name
        # real
        var_minimum_air_flow_rate_ratio = 0.35
        obj.minimum_air_flow_rate_ratio = var_minimum_air_flow_rate_ratio
        # real
        var_fraction_of_tower_capacity_in_free_convection_regime = 0.1
        obj.fraction_of_tower_capacity_in_free_convection_regime = var_fraction_of_tower_capacity_in_free_convection_regime
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_operating_schedule_name = "object-list|Basin Heater Operating Schedule Name"
        obj.basin_heater_operating_schedule_name = var_basin_heater_operating_schedule_name
        # alpha
        var_evaporation_loss_mode = "LossFactor"
        obj.evaporation_loss_mode = var_evaporation_loss_mode
        # real
        var_evaporation_loss_factor = 19.19
        obj.evaporation_loss_factor = var_evaporation_loss_factor
        # real
        var_drift_loss_percent = 20.2
        obj.drift_loss_percent = var_drift_loss_percent
        # alpha
        var_blowdown_calculation_mode = "ConcentrationRatio"
        obj.blowdown_calculation_mode = var_blowdown_calculation_mode
        # real
        var_blowdown_concentration_ratio = 2.0
        obj.blowdown_concentration_ratio = var_blowdown_concentration_ratio
        # object-list
        var_blowdown_makeup_water_usage_schedule_name = "object-list|Blowdown Makeup Water Usage Schedule Name"
        obj.blowdown_makeup_water_usage_schedule_name = var_blowdown_makeup_water_usage_schedule_name
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name
        # integer
        var_number_of_cells = 1
        obj.number_of_cells = var_number_of_cells
        # alpha
        var_cell_control = "MinimalCell"
        obj.cell_control = var_cell_control
        # real
        var_cell_minimum_water_flow_rate_fraction = 0.50005
        obj.cell_minimum_water_flow_rate_fraction = var_cell_minimum_water_flow_rate_fraction
        # real
        var_cell_maximum_water_flow_rate_fraction = 1.0
        obj.cell_maximum_water_flow_rate_fraction = var_cell_maximum_water_flow_rate_fraction
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].name, var_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].model_type, var_model_type)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].model_coefficient_name, var_model_coefficient_name)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_inlet_air_wetbulb_temperature, var_design_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_approach_temperature, var_design_approach_temperature)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_range_temperature, var_design_range_temperature)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_air_flow_rate, var_design_air_flow_rate)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].design_fan_power, var_design_fan_power)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].fan_power_ratio_function_of_air_flow_rate_ratio_curve_name, var_fan_power_ratio_function_of_air_flow_rate_ratio_curve_name)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].minimum_air_flow_rate_ratio, var_minimum_air_flow_rate_ratio)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].fraction_of_tower_capacity_in_free_convection_regime, var_fraction_of_tower_capacity_in_free_convection_regime)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].evaporation_loss_mode, var_evaporation_loss_mode)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].evaporation_loss_factor, var_evaporation_loss_factor)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].drift_loss_percent, var_drift_loss_percent)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].blowdown_calculation_mode, var_blowdown_calculation_mode)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].blowdown_makeup_water_usage_schedule_name, var_blowdown_makeup_water_usage_schedule_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].number_of_cells, var_number_of_cells)
        self.assertEqual(idf2.coolingtowervariablespeeds[0].cell_control, var_cell_control)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].cell_minimum_water_flow_rate_fraction, var_cell_minimum_water_flow_rate_fraction)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].cell_maximum_water_flow_rate_fraction, var_cell_maximum_water_flow_rate_fraction)
        self.assertAlmostEqual(idf2.coolingtowervariablespeeds[0].sizing_factor, var_sizing_factor)