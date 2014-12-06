import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import ChillerElectric

log = logging.getLogger(__name__)

class TestChillerElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerElectric()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_nominal_capacity = 0.0
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_nominal_cop = 0.0001
        obj.nominal_cop = var_nominal_cop
        # node
        var_chilled_water_inlet_node_name = "node|Chilled Water Inlet Node Name"
        obj.chilled_water_inlet_node_name = var_chilled_water_inlet_node_name
        # node
        var_chilled_water_outlet_node_name = "node|Chilled Water Outlet Node Name"
        obj.chilled_water_outlet_node_name = var_chilled_water_outlet_node_name
        # node
        var_condenser_inlet_node_name = "node|Condenser Inlet Node Name"
        obj.condenser_inlet_node_name = var_condenser_inlet_node_name
        # node
        var_condenser_outlet_node_name = "node|Condenser Outlet Node Name"
        obj.condenser_outlet_node_name = var_condenser_outlet_node_name
        # real
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_design_condenser_inlet_temperature = 12.12
        obj.design_condenser_inlet_temperature = var_design_condenser_inlet_temperature
        # real
        var_temperature_rise_coefficient = 0.0001
        obj.temperature_rise_coefficient = var_temperature_rise_coefficient
        # real
        var_design_chilled_water_outlet_temperature = 14.14
        obj.design_chilled_water_outlet_temperature = var_design_chilled_water_outlet_temperature
        # real
        var_design_chilled_water_flow_rate = 0.0
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_fluid_flow_rate = 0.0
        obj.design_condenser_fluid_flow_rate = var_design_condenser_fluid_flow_rate
        # real
        var_coefficient_1_of_capacity_ratio_curve = 17.17
        obj.coefficient_1_of_capacity_ratio_curve = var_coefficient_1_of_capacity_ratio_curve
        # real
        var_coefficient_2_of_capacity_ratio_curve = 18.18
        obj.coefficient_2_of_capacity_ratio_curve = var_coefficient_2_of_capacity_ratio_curve
        # real
        var_coefficient_3_of_capacity_ratio_curve = 19.19
        obj.coefficient_3_of_capacity_ratio_curve = var_coefficient_3_of_capacity_ratio_curve
        # real
        var_coefficient_1_of_power_ratio_curve = 20.2
        obj.coefficient_1_of_power_ratio_curve = var_coefficient_1_of_power_ratio_curve
        # real
        var_coefficient_2_of_power_ratio_curve = 21.21
        obj.coefficient_2_of_power_ratio_curve = var_coefficient_2_of_power_ratio_curve
        # real
        var_coefficient_3_of_power_ratio_curve = 22.22
        obj.coefficient_3_of_power_ratio_curve = var_coefficient_3_of_power_ratio_curve
        # real
        var_coefficient_1_of_full_load_ratio_curve = 23.23
        obj.coefficient_1_of_full_load_ratio_curve = var_coefficient_1_of_full_load_ratio_curve
        # real
        var_coefficient_2_of_full_load_ratio_curve = 24.24
        obj.coefficient_2_of_full_load_ratio_curve = var_coefficient_2_of_full_load_ratio_curve
        # real
        var_coefficient_3_of_full_load_ratio_curve = 25.25
        obj.coefficient_3_of_full_load_ratio_curve = var_coefficient_3_of_full_load_ratio_curve
        # real
        var_chilled_water_outlet_temperature_lower_limit = 26.26
        obj.chilled_water_outlet_temperature_lower_limit = var_chilled_water_outlet_temperature_lower_limit
        # alpha
        var_chiller_flow_mode = "ConstantFlow"
        obj.chiller_flow_mode = var_chiller_flow_mode
        # real
        var_design_heat_recovery_water_flow_rate = 0.0
        obj.design_heat_recovery_water_flow_rate = var_design_heat_recovery_water_flow_rate
        # node
        var_heat_recovery_inlet_node_name = "node|Heat Recovery Inlet Node Name"
        obj.heat_recovery_inlet_node_name = var_heat_recovery_inlet_node_name
        # node
        var_heat_recovery_outlet_node_name = "node|Heat Recovery Outlet Node Name"
        obj.heat_recovery_outlet_node_name = var_heat_recovery_outlet_node_name
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_operating_schedule_name = "object-list|Basin Heater Operating Schedule Name"
        obj.basin_heater_operating_schedule_name = var_basin_heater_operating_schedule_name
        # real
        var_condenser_heat_recovery_relative_capacity_fraction = 0.5
        obj.condenser_heat_recovery_relative_capacity_fraction = var_condenser_heat_recovery_relative_capacity_fraction
        # object-list
        var_heat_recovery_inlet_high_temperature_limit_schedule_name = "object-list|Heat Recovery Inlet High Temperature Limit Schedule Name"
        obj.heat_recovery_inlet_high_temperature_limit_schedule_name = var_heat_recovery_inlet_high_temperature_limit_schedule_name
        # node
        var_heat_recovery_leaving_temperature_setpoint_node_name = "node|Heat Recovery Leaving Temperature Setpoint Node Name"
        obj.heat_recovery_leaving_temperature_setpoint_node_name = var_heat_recovery_leaving_temperature_setpoint_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerelectrics[0].name, var_name)
        self.assertEqual(idf2.chillerelectrics[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.chillerelectrics[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.chillerelectrics[0].nominal_cop, var_nominal_cop)
        self.assertEqual(idf2.chillerelectrics[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerelectrics[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerelectrics[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerelectrics[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerelectrics[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectrics[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectrics[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerelectrics[0].design_condenser_inlet_temperature, var_design_condenser_inlet_temperature)
        self.assertAlmostEqual(idf2.chillerelectrics[0].temperature_rise_coefficient, var_temperature_rise_coefficient)
        self.assertAlmostEqual(idf2.chillerelectrics[0].design_chilled_water_outlet_temperature, var_design_chilled_water_outlet_temperature)
        self.assertAlmostEqual(idf2.chillerelectrics[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerelectrics[0].design_condenser_fluid_flow_rate, var_design_condenser_fluid_flow_rate)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_1_of_capacity_ratio_curve, var_coefficient_1_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_2_of_capacity_ratio_curve, var_coefficient_2_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_3_of_capacity_ratio_curve, var_coefficient_3_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_1_of_power_ratio_curve, var_coefficient_1_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_2_of_power_ratio_curve, var_coefficient_2_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_3_of_power_ratio_curve, var_coefficient_3_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_1_of_full_load_ratio_curve, var_coefficient_1_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_2_of_full_load_ratio_curve, var_coefficient_2_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].coefficient_3_of_full_load_ratio_curve, var_coefficient_3_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerelectrics[0].chilled_water_outlet_temperature_lower_limit, var_chilled_water_outlet_temperature_lower_limit)
        self.assertEqual(idf2.chillerelectrics[0].chiller_flow_mode, var_chiller_flow_mode)
        self.assertAlmostEqual(idf2.chillerelectrics[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.chillerelectrics[0].heat_recovery_inlet_node_name, var_heat_recovery_inlet_node_name)
        self.assertEqual(idf2.chillerelectrics[0].heat_recovery_outlet_node_name, var_heat_recovery_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerelectrics[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.chillerelectrics[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.chillerelectrics[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.chillerelectrics[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)
        self.assertAlmostEqual(idf2.chillerelectrics[0].condenser_heat_recovery_relative_capacity_fraction, var_condenser_heat_recovery_relative_capacity_fraction)
        self.assertEqual(idf2.chillerelectrics[0].heat_recovery_inlet_high_temperature_limit_schedule_name, var_heat_recovery_inlet_high_temperature_limit_schedule_name)
        self.assertEqual(idf2.chillerelectrics[0].heat_recovery_leaving_temperature_setpoint_node_name, var_heat_recovery_leaving_temperature_setpoint_node_name)