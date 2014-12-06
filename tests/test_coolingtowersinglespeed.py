import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import CoolingTowerSingleSpeed

log = logging.getLogger(__name__)

class TestCoolingTowerSingleSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coolingtowersinglespeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoolingTowerSingleSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # real
        var_design_water_flow_rate = 0.0001
        obj.design_water_flow_rate = var_design_water_flow_rate
        # real
        var_design_air_flow_rate = 0.0001
        obj.design_air_flow_rate = var_design_air_flow_rate
        # real
        var_design_fan_power = 0.0001
        obj.design_fan_power = var_design_fan_power
        # real
        var_design_ufactor_times_area_value = 1050000.00005
        obj.design_ufactor_times_area_value = var_design_ufactor_times_area_value
        # real
        var_free_convection_air_flow_rate = 0.0
        obj.free_convection_air_flow_rate = var_free_convection_air_flow_rate
        # real
        var_free_convection_air_flow_rate_sizing_factor = 0.5
        obj.free_convection_air_flow_rate_sizing_factor = var_free_convection_air_flow_rate_sizing_factor
        # real
        var_free_convection_ufactor_times_area_value = 150000.0
        obj.free_convection_ufactor_times_area_value = var_free_convection_ufactor_times_area_value
        # real
        var_free_convection_ufactor_times_area_value_sizing_factor = 0.5
        obj.free_convection_ufactor_times_area_value_sizing_factor = var_free_convection_ufactor_times_area_value_sizing_factor
        # alpha
        var_performance_input_method = "UFactorTimesAreaAndDesignWaterFlowRate"
        obj.performance_input_method = var_performance_input_method
        # real
        var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio = 13.13
        obj.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio
        # real
        var_nominal_capacity = 0.0001
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_free_convection_capacity = 0.0
        obj.free_convection_capacity = var_free_convection_capacity
        # real
        var_free_convection_nominal_capacity_sizing_factor = 0.5
        obj.free_convection_nominal_capacity_sizing_factor = var_free_convection_nominal_capacity_sizing_factor
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
        var_evaporation_loss_factor = 21.21
        obj.evaporation_loss_factor = var_evaporation_loss_factor
        # real
        var_drift_loss_percent = 22.22
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
        # alpha
        var_capacity_control = "FanCycling"
        obj.capacity_control = var_capacity_control
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
        self.assertEqual(idf2.coolingtowersinglespeeds[0].name, var_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].design_water_flow_rate, var_design_water_flow_rate)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].design_air_flow_rate, var_design_air_flow_rate)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].design_fan_power, var_design_fan_power)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].design_ufactor_times_area_value, var_design_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_air_flow_rate, var_free_convection_air_flow_rate)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_air_flow_rate_sizing_factor, var_free_convection_air_flow_rate_sizing_factor)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_ufactor_times_area_value, var_free_convection_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_ufactor_times_area_value_sizing_factor, var_free_convection_ufactor_times_area_value_sizing_factor)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].performance_input_method, var_performance_input_method)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].heat_rejection_capacity_and_nominal_capacity_sizing_ratio, var_heat_rejection_capacity_and_nominal_capacity_sizing_ratio)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_capacity, var_free_convection_capacity)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].free_convection_nominal_capacity_sizing_factor, var_free_convection_nominal_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].evaporation_loss_mode, var_evaporation_loss_mode)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].evaporation_loss_factor, var_evaporation_loss_factor)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].drift_loss_percent, var_drift_loss_percent)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].blowdown_calculation_mode, var_blowdown_calculation_mode)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].blowdown_makeup_water_usage_schedule_name, var_blowdown_makeup_water_usage_schedule_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].capacity_control, var_capacity_control)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].number_of_cells, var_number_of_cells)
        self.assertEqual(idf2.coolingtowersinglespeeds[0].cell_control, var_cell_control)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].cell_minimum_water_flow_rate_fraction, var_cell_minimum_water_flow_rate_fraction)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].cell_maximum_water_flow_rate_fraction, var_cell_maximum_water_flow_rate_fraction)
        self.assertAlmostEqual(idf2.coolingtowersinglespeeds[0].sizing_factor, var_sizing_factor)